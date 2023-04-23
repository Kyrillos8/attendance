from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


# Create your views here.

class OsraApiView(APIView):
    #for the serializer
    serializer_class=OsraSerializers
    #for the model
    def get(self, request):
        allOsra = Osra.objects.all().values()
        return Response({"message":"List of Osra","Osra List":allOsra})
    
    def post(self,request):
        print('request data is: ',request.data)
        serializer_obj=OsraSerializers(data=request.data)
        if(serializer_obj.is_valid()):
            Osra.objects.create(osra_number=serializer_obj.data.get("osra_number"),
                                osra_name=serializer_obj.data.get("osra_name")
                                )
            

        osra=Osra.objects.all().filter(id=request.data["id"]).values()

        return Response({"message":"New Osra created","Osra":osra})
    
class shamasApiView(APIView):
    #for the serializer
    serializer_class=ShamasSerializers
    #for the model
    def get(self, request):
        shamamsa = Shamas.objects.all().values()
        return Response({"message":"List of shamamsa","Shamas List":shamamsa})
    
    def post(self,request):
        print('request data is: ',request.data)
        serializerr_obj=ShamasSerializers(data=request.data)
        if(serializerr_obj.is_valid()):
            Shamas.objects.create(
                                osra_id=serializerr_obj.data.get("osra_id"),
                                shamas_name=serializerr_obj.data.get("shamas_name"),
                                # osra=serializerr_obj.data.get("osra.osra_number")
                                )

        shamas=Shamas.objects.all().filter(id=request.data["id"]).values()

        return Response({"message":"New Shamas is created","Shamas":shamas})
    
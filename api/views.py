from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

# Create your views here.

class OsraApiView(APIView):
    def get(self, request):
        allOsra = Osra.objects.all().values()
        return Response({"message":"List of Osra","Osra List":allOsra})
    
    def post(self,request):
        
        Osra.objects.create(osra_id=request.data["osra_id"],
                            osra_name=request.data["osra_name"]
                            )

        osra=Osra.objects.all().filter(id=request.data["id"]).values()

        return Response({"message":"New Osra created","Osra":osra})
    
class shamasApiView(APIView):
    def get(self, request):
        shamamsa = Shamas.objects.all().values()
        return Response({"message":"List of shamamsa","Shamas List":shamamsa})
    
    def post(self,request):
        
        Shamas.objects.create(
                              shamas_name=request.data["shamas_name"],
                              osra=request.data["osra_name"]
                              )

        shamas=Shamas.objects.all().filter(id=request.data["id"]).values()

        return Response({"message":"New Shamas is created","Shamas":shamas})
    
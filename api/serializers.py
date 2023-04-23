from rest_framework import serializers

# Create your models here.
class OsraSerializers(serializers.Serializer):
    osra_number = serializers.IntegerField(label="enter osra number")
    osra_name = serializers.CharField(label="enter osra name")
    

class ShamasSerializers(serializers.Serializer):
    shamas_name = serializers.CharField(label="enter shamas name")
    osra_id = serializers.IntegerField(label="enter osra number for the shamas")
    
    
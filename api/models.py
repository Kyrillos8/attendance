from django.db import models

# Create your models here.
class Osra(models.Model):
    id = models.AutoField(primary_key=True)
    osra_id = models.IntegerField(null=False)
    osra_name = models.CharField(max_length=500,null=False)
    
    def __str__ (self):
        return self.osra_name


class Shamas(models.Model):
    shamas_name = models.CharField(max_length=500)
    osra = models.ForeignKey(Osra,on_delete=models.CASCADE)
    def __str__ (self):
        return self.shamas_name
    
    
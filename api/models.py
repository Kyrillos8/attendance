from django.db import models

# Create your models here.
class Osra(models.Model):
    osra_number = models.IntegerField(null=False,unique=True)
    osra_name = models.CharField(max_length=500,null=False)
    
    def __str__ (self):
        return self.osra_name


class Shamas(models.Model):
    shamas_name = models.CharField(max_length=500)
    osra = models.ForeignKey(Osra,on_delete=models.CASCADE,name='osra') #it's name in the database is osara_id *"CAN'T BE CHANGED"*
    def __str__ (self):
        return self.shamas_name#osra.osra_number 
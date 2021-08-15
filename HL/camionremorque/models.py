from django.db import models

# Create your models here.
class Remorque(models.Model):
    id = models.AutoField(primary_key=True)
    matriculation = models.CharField(max_length=255)

class Camion(models.Model):
    id = models.AutoField(primary_key=True)
    matriculation = models.CharField(max_length=255)
    remorque = models.ForeignKey(Remorque, on_delete=models.CASCADE,blank=True,null=True)
    matriculation = models.CharField(max_length=255)
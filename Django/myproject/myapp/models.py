from django.db import models

# Create your models here.
class Feature(models.Model): 
    # id is default here so no need to include
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=500)
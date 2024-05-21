from django.db import models

# Create your models here.
class RegistrationModel(models.Model):
    username=models.CharField(max_length=30)
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    age=models.IntegerField()
    email=models.EmailField()
    

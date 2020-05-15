from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profiles(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    
    
    
    

    #Metadata
    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
       return self.last_name


class File(models.Model):
    name = models.CharField(max_length=150)
    file = models.FileField(upload_to="files/", max_length=100)
    

    class Meta:
        verbose_name = ("File")
        verbose_name_plural = ("Files")

    def __str__(self):
        return self.name

    
from django.db import models
from profiles.models import *
# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100, help_text='Enter title')
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Profiles, related_name='posts', on_delete=models.CASCADE)

   #Metadata
    class Meta :
        ordering = ['-date']
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

   #Methods
   

    def __str__(self):
        return self.title
    


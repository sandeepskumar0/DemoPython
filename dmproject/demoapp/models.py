from django.db import models


# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    inform=models.TextField()

    def __str__(self):
       return self.name

class Team(models.Model):

    image=models.ImageField(upload_to='pics')
    cname = models.CharField(max_length=250)
    desc=models.TextField()

    def __str__(self):
       return self.cname
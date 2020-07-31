from django.db import models

# Create your models here.
class Destinations(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='pics/')
    descr = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

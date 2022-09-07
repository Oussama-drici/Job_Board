from django.db import models

# Create your models here.


class Infos(models.Model):
    place = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=25)

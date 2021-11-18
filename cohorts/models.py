from django.db import models

# Create your models here.
from django.db.models import JSONField


class Cohort(models.Model):
    name= models.CharField(max_length=30, unique=True)
    priest= models.EmailField()
    priestess= models.EmailField()
    natives_list= JSONField(default=list)
    date_created = models.DateTimeField(auto_now_add=True)


class Native(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    native_id = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=225)
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images')
    date_created = models.DateTimeField(auto_now_add=True)



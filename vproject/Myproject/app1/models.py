from django.db import models

# Create your models here.
class Games(models.Model):
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='pages/')
    cover = models.FileField(upload_to='pic/')
class Private(models.Model):
    user=models.CharField(max_length=45)
    password=models.CharField(max_length=45)
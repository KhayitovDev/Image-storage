from django.db import models

# Create your models here.
class ImageFiles(models.Model):
    file=models.FileField(upload_to='images/')
    

class AudioFiles(models.Model):
    file=models.FileField(upload_to='audios/')
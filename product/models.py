from django.db import models

# Create your models here.
import cloudinary
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete

# @receiver(pre_delete, sender=Photo)
# def photo_delete(sender, instance, **kwargs):
#     cloudinary.uploader.destroy(instance.image.public_id)

class Photo(models.Model):
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    
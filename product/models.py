from django.db import models

# Create your models here.
import cloudinary
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete

@receiver(pre_delete, sender=Photo)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)

class Photo(models.Model):
    image = CloudinaryField('image')
    caption = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.caption if self.caption != "" else "No caption"
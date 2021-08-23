from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    image = CloudinaryField('image')
    link = models.URLField()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

#class Services(models.Model)


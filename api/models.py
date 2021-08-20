from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to = "project_images")
    link = models.URLField()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

#class Services(models.Model)


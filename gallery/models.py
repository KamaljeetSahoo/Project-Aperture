from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=100)

class Picture(models.Model):
    image = models.ImageField(upload_to = 'image_repository')
    tag = models.ManyToManyField(Tag, blank=True)
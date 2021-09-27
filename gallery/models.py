from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.tag_name)

class Picture(models.Model):
    image = models.ImageField(upload_to = 'image_repository')
    tag = models.ManyToManyField(Tag, blank=True)
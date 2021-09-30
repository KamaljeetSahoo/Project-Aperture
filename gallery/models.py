from django.db import models
from PIL import Image

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.tag_name)

class Picture(models.Model):
    image = models.ImageField(upload_to = 'image_repository')
    tag = models.ManyToManyField(Tag, blank=True)

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            size = (500, 500)
            img.thumbnail(size=size)
            img.save(self.image.path)
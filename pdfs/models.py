from django.db import models

# Create your models here.
class PDF_Caption(models.Model):
    description = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return str(self.description)

class PDF_Tag(models.Model):
    tag_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.tag_name)

class ExtractedImage(models.Model):
    image = models.ImageField(upload_to = "extracted_images/")
    caption = models.ManyToManyField(PDF_Caption, blank=True)
    tag = models.ManyToManyField(PDF_Tag, blank=True)

class PDF_File(models.Model):
    pdf = models.FileField(upload_to='pdf_repository/')
    image = models.ManyToManyField(ExtractedImage, blank=True)

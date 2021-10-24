from django.db import models

# Create your models here.
class FrameTag(models.Model):
    tag_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.tag_name)

class FrameCaption(models.Model):
    description = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return str(self.description)

class ExtractedFrame(models.Model):
    image = models.ImageField(upload_to = "extracted_video_frames/")
    tag = models.ManyToManyField(FrameTag, blank=True)
    caption = models.ManyToManyField(FrameCaption, blank=True)

class Video(models.Model):
    video = models.FileField(upload_to = "video_repository/")
    extracted_image = models.ManyToManyField(ExtractedFrame, blank=True)
from django.contrib import admin
from .models import Video, ExtractedFrame, FrameTag, FrameCaption

# Register your models here.
admin.site.register(Video)
admin.site.register(ExtractedFrame)
admin.site.register(FrameTag)
admin.site.register(FrameCaption)
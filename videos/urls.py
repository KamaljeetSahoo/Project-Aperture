from django.urls import path
from .views import browse_videos, video_upload

urlpatterns = [
    path('videos/', browse_videos, name="browse_videos"),
    path('upload_video/', video_upload, name="video_upload")
]
from django.urls import path
from .views import browse_videos, video_upload, handle_upload_video, view_single_video_content, edit_video_frame_view

urlpatterns = [
    path('videos/', browse_videos, name="browse_videos"),
    path('upload_video/', video_upload, name="video_upload"),
    path('handle_upload/', handle_upload_video),
    path('video_view/<int:video_id>/', view_single_video_content),
    path('edit_video_frame/<int:image_id>/', edit_video_frame_view, name="edit_video_frame")
]
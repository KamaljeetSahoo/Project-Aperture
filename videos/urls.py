from django.urls import path
from .views import browse_videos, video_upload, handle_upload_video, view_single_video_content, edit_video_frame_view
from .views import add_tag_video_frame, delete_tag_video_frame, update_caption_video_frame, video_search_view

urlpatterns = [
    path('videos/', browse_videos, name="browse_videos"),
    path('upload_video/', video_upload, name="video_upload"),
    path('handle_upload/', handle_upload_video),
    path('video_view/<int:video_id>/', view_single_video_content),
    path('edit_video_frame/<int:image_id>/',
         edit_video_frame_view, name="edit_video_frame"),
    path('add_tag_video_frame/<int:image_id>/', add_tag_video_frame),
    path('delete_tag_video_frame/<int:tag_id>/<int:image_id>/',
         delete_tag_video_frame),
    path('update_caption_video_frame/<int:image_id>/', update_caption_video_frame),
    path('video_search/', video_search_view, name='video_search')
]

from django.urls import path
from .views import contributeImageView, homepage, single_image_view, after_upload_view, delete_tag_from_image

urlpatterns = [
    path('contribute/', contributeImageView, name="ImageContribute"),
    path('', homepage, name="home"),
    path('image/<int:image_id>/', single_image_view),
    path('edit_image/<int:image_id>/', after_upload_view, name="edit_image"),
    path('delete_tag/<int:tag_id>/<int:image_id>/', delete_tag_from_image)
]
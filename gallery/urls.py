from django.urls import path
from .views import contributeImageView, homepage, single_image_view

urlpatterns = [
    path('contribute/', contributeImageView, name="ImageContribute"),
    path('', homepage, name="home"),
    path('image/<int:image_id>/', single_image_view)
]
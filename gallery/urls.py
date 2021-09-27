from django.urls import path
from .views import contributeImageView, landig_view, single_image_view

urlpatterns = [
    path('contribute/', contributeImageView, name="ImageContribute"),
    path('landing/', landig_view, name="landing"),
    path('image/<int:image_id>/', single_image_view)
]
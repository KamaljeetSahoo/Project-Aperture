from django.urls import path
from .views import contributeImageView, landig_view

urlpatterns = [
    path('contribute/', contributeImageView, name="ImageContribute"),
    path('landing/', landig_view, name="landing")
]
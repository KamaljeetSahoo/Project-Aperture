from django.urls import path
from .views import contributeImageView

urlpatterns = [
    path('contribute/', contributeImageView, name="ImageContribute")
]
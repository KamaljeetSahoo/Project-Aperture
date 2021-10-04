from django.urls import path
from .views import contributeImageView, homepage, single_image_view, after_upload_view, delete_tag_from_image
from .views import add_tag_to_image, tag_based_image_search, tag_click_search, reverse_image_search

urlpatterns = [
    path('contribute/', contributeImageView, name="ImageContribute"),
    path('', homepage, name="home"),
    path('image/<int:image_id>/', single_image_view),
    path('edit_image/<int:image_id>/', after_upload_view, name="edit_image"),
    path('delete_tag/<int:tag_id>/<int:image_id>/', delete_tag_from_image),
    path('add_tag_to_image/<int:image_id>/', add_tag_to_image, name="add_tag_image"),
    path('image_tag_search/', tag_based_image_search, name="search_tag"),
    path('tag_click_search/<int:tag_id>/', tag_click_search, name="tag_click_search"),
    path('reverse_image_search/', reverse_image_search, name="ReverseImageSearch")
]
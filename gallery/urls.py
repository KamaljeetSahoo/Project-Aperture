from django.urls import path
from .views import contributeImageView, homepage, single_image_view, after_upload_view, delete_tag_from_image
from .views import add_tag_to_image, tag_based_image_search, tag_click_search, reverse_image_search, recently_uploaded_view
from .views import trending_image_view, tag_analytics_dashboard, multiple_image_upload
from .views import delete_tag_multiple, add_tag_multiple, multi_edit_page_view, update_caption

urlpatterns = [
    path('contribute/', contributeImageView, name="ImageContribute"),
    path('multiple_upload/', multiple_image_upload),
    path('', homepage, name="home"),
    path('recently_uploaded', recently_uploaded_view, name="recently_uploaded"),
    path('image/<int:image_id>/', single_image_view),
    path('edit_image/<int:image_id>/', after_upload_view, name="edit_image"),
    path('delete_tag/<int:tag_id>/<int:image_id>/', delete_tag_from_image),
    path('edit_caption/<int:image_id>/', update_caption),
    path('add_tag_to_image/<int:image_id>/', add_tag_to_image, name="add_tag_image"),
    path('image_tag_search/', tag_based_image_search, name="search_tag"),
    path('tag_click_search/<int:tag_id>/', tag_click_search, name="tag_click_search"),
    path('reverse_image_search/', reverse_image_search, name="ReverseImageSearch"),
    path('most_viewed/', trending_image_view, name="trending_images"),
    path('tag_analytics/', tag_analytics_dashboard, name="tag_dashboard"),
    path('multi_delete_tag/<slug:slug>/<int:tag_id>/<int:image_id>/', delete_tag_multiple),
    path('multi_add_tag/<slug:slug>/<int:image_id>/', add_tag_multiple),
    path('muti_edit/<slug:slug>/', multi_edit_page_view, name="multi-edit-page")
]
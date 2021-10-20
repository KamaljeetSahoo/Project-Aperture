from django.urls import path
from .views import pdf_upload_view, pdf_upload, pdf_explore, single_pdf_view
from .views import delete_tag_from_image, edit_page_view, add_tag_to_image, update_caption_pdf_image

urlpatterns = [
    path('pdf_upload_view/', pdf_upload_view, name="upload_pdf_view"),
    path('browse_pdfs/', pdf_explore, name='explore_pdfs'),
    path('upload_pdf/', pdf_upload, name="pdf_upload"),
    path('single_view_pdf/<int:pdf_id>/', single_pdf_view),
    path('edit_image_pdf/<int:image_id>/', edit_page_view, name="edit_pdf_image_view"),
    path('delete_tag_pdf_image/<int:tag_id>/<int:image_id>/',delete_tag_from_image),
    path('add_tag_image_pdf/<int:image_id>/', add_tag_to_image),
    path('update_caption_image_pdf/<int:image_id>/', update_caption_pdf_image)
]
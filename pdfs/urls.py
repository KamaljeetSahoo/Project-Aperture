from django.urls import path
from .views import pdf_upload_view, pdf_upload, pdf_explore, single_pdf_view

urlpatterns = [
    path('pdf_upload_view/', pdf_upload_view, name="upload_pdf_view"),
    path('browse_pdfs/', pdf_explore, name='explore_pdfs'),
    path('upload_pdf/', pdf_upload, name="pdf_upload"),
    path('single_view_pdf/<int:pdf_id>/', single_pdf_view)
]
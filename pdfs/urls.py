from django.urls import path
from .views import pdf_upload_view, pdf_upload, pdf_explore

urlpatterns = [
    path('pdf_upload_view/', pdf_upload_view, name="upload_pdf_view"),
    path('browse_pdfs/', pdf_explore, name='explore_pdfs'),
    path('upload_pdf/', pdf_upload, name="pdf_upload"),
]
from django.urls import path
from .views import pdf_upload_view, pdf_upload

urlpatterns = [
    path('pdf_upload_view/', pdf_upload_view, name="upload_pdf_view"),
    path('upload_pdf/', pdf_upload, name="pdf_upload")
]
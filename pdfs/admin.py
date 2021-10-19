from django.contrib import admin
from .models import PDF_File, PDF_Caption, PDF_Tag, ExtractedImage

# Register your models here.
admin.site.register(PDF_File)
admin.site.register(PDF_Caption)
admin.site.register(PDF_Tag)
admin.site.register(ExtractedImage)

from django.contrib import admin
from .models import Tag, Picture, Caption

# Register your models here.
admin.site.register(Tag)
admin.site.register(Picture)
admin.site.register(Caption)
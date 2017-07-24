from django.contrib import admin
from .models import Photo
from shop.models import Photo, Tag
from django.utils.safestring import mark_safe




class PhotoAdmin(admin.ModelAdmin):
    list_display=['id', 'title']
admin.site.register(Photo, PhotoAdmin)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['name']

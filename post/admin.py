from django.contrib import admin
from .models import Post, Media

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'body']

@admin.register(Media)
class Media(admin.ModelAdmin):
    list_display = ['post', 'image_tag']
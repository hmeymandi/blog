from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class Postadmin(admin.ModelAdmin):

    list_display = ['title','date_created','author','status']
    ordering = ['status']



from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'datetime_modified']

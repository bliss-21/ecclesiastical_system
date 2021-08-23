from django.contrib import admin

# Register your models here.
from.models import Category, Song
admin.site.register(Category)
admin.site.register(Song)

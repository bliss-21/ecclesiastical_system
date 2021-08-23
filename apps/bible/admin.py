from django.contrib import admin

# Register your models here.

from.models import Book, Testament, Verse


admin.site.register(Book)
admin.site.register(Verse)
admin.site.register(Testament)

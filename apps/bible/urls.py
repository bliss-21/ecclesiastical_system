from django.urls import path
from .views import bible_test
urlpatterns = [
    path('home', bible_test, name='bible'),
]
from django.db.models.query_utils import FilteredRelation
from django.urls import path
from .views import listado, cancion

urlpatterns = [
    path('listado/', listado, name="listado"),
    path('listado/<id>/', listado, name="listado"),
    path('cancion/<id>/', cancion, name="cancion"),
]
from django.shortcuts import render
from .models import Category, Song
# Create your views here.
def listado(request, id=-1):
    if id==-1:
        canciones = Song.objects.all()
    else:
        canciones = Song.objects.filter(category_id=id)

    tipos = Category.objects.all()
    variables = {
        'tipos':tipos,
        'canciones':canciones,
    }

    return render(request, 'song_book/listado.html', variables)

def cancion(request, id):

    cancion = Song.objects.filter(id=id)

    tipos = Category.objects.all()
    variables = {
        'tipos':tipos,
        'cancion':cancion,
    }

    return render(request, 'song_book/cancion.html', variables)

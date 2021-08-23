from django.shortcuts import render
from .models import Book, Verse, Testament
# Create your views here.

def tupla_versiculos(desde, hasta=0):
    rango = []

    if hasta<=desde:
        rango.append(desde)
    else:
        for x in range(desde,hasta+1):
            rango.append(x)
    return rango

def bible_test(request):
    libros = Book.objects.all()
    data = {
        'libros':libros,
    }
    #preguntar Versiculo

    if request.POST:

            
        libro = request.POST.get('cboLibro')

        capitulo = request.POST.get('cap')
        desde = int(request.POST.get('des'))
        hasta =request.POST.get('hasta')
        
        direccion_versiculo = Book.objects.get(id=libro).name+' '+str(capitulo)+' : '+str(desde)
        
        
        if len(hasta)==0 or int(hasta)<=int(desde):
            hasta = 0
        else:
            hasta = int(hasta)
            direccion_versiculo = direccion_versiculo +' - '+str(hasta)
            data['hasta'] = hasta

        versiculos = Verse.objects.filter(book_id=libro, chapter=capitulo, verse__in=tupla_versiculos(desde,hasta) )
        print(versiculos)
        try:
            if versiculos.exists():
                data['versiculos'] = versiculos
            else:
                data['no_encontrado'] = 'Ups!!, el versiculo no se encuentra'      
        except:
            pass
        data['direccion_versiculo'] = direccion_versiculo

        #le mandamos los valores que recojemos del POST para que se mantengan en el formulario
        data['capitulo'] = capitulo
        data['desde'] = desde
        data['libro'] = Book.objects.get(id=libro).name
        

    return render(request, 'bible/home.html', data)
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import estudiante

def lista_estudiantes(request):
    """Lista todos los estudiantes."""
    estudiante_list = estudiante.objects.all()
    return render(request, 'lista.html', {'Estudiantes': estudiante_list})


def crear_estudiante(request):
    """Crea un nuevo alumno"""
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        carrera = request.POST.get('carrera')
        
        if nombre and apellido and edad and carrera:
            estudiante.objects.create(
                nombre=nombre,
                apellido=apellido,
                edad=int(edad),
                carrera=carrera
            )
            messages.success(request, 'Estudiante creado exitosamente.')
            return redirect('lista_estudiantes')
        else:
            messages.error(request, 'Todos los campos son obligatorios.')
    
    return render(request, 'crear.html')
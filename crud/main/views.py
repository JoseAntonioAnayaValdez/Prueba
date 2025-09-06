# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import estudiante

def lista_estudiantes(request):
    """Lista todos los estudiantes."""
    estudiante_list = estudiante.objects.all()
    return render(request, 'lista.html', {'Estudiantes': estudiante_list})

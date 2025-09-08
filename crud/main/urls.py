from django.urls import path
from . import views

urlpatterns = [
    # path('', views.inicio, name='inicio'),
    # path('', views.about, name='about'),
    path('', views.lista_estudiantes, name='lista_estudiantes'),
    path('crear/', views.crear_estudiante, name='crear_estudiante'),
]
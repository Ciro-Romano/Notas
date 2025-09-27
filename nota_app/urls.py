from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.lista_notas, name='lista_notas'), 
    path('crear_nota/', views.crear_notas, name='crear_nota'),
    path('eliminar/<int:id>/', views.eliminar_notas, name='eliminar_nota'),
] 
from django.urls import path

from . import views

urlpatterns = [
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/<int:id>', views.client_by_id, name='client_by_id'),
    path('clientes/editar/<int:id>', views.editar, name='editar')
]
from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, update, delete

urlpatterns = [
    path('', home),
    path('salvar/', salvar, name="salvar"),
    path('editar/<int:task_id>', editar, name="editar"),
    path('update/<int:task_id>', update, name="update"),
    path('delete/<int:task_id>', delete, name="delete")
]

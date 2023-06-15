from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('recipe/<int:id_recipe>/', views.recipe)
]

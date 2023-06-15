from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('recipes/<int:id_recipe>/', views.recipe)
]

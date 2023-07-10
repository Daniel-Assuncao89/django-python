from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/category/<int:id_category>/',
         views.category, name="category"),
    path('recipes/<slug:slug>/', views.recipe, name="recipe"),
]

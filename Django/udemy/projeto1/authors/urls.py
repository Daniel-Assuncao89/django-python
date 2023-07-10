from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('register/create/', views.register_create, name='register_create'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/recipe_create', views.dashboard_recipe_create,
         name='dashboard_recipe_create'),
    path('dashboard/recipe_edit/<int:recipe_id>', views.dashboard_recipe_edit,
         name='dashboard_recipe_edit'),
]

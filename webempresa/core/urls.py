from django.urls import path
from . import views             # Importamos las vistas de Core

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="store"),
]

from django.urls import path
from . import views             # Importamos las vistas de Services

urlpatterns = [
    path('', views.services, name="services"),
]


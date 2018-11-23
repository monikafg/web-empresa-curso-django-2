from django.urls import path
from . import views             # Importamos las vistas de Contact

urlpatterns = [
    path('', views.contact, name="contact"),
]

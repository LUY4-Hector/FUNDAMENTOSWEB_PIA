# Urls para la pagina

from django.urls import path
from . import views

urlpatterns = [
		    path('estatica/', views.estatica, name="estatica"),
		    path('dinamica/', views.dinamica, name="dinamica"),
        ]
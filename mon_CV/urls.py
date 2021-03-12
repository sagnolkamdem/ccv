from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='accueil'), # La vue pour l'accueil    
    path('techno', views.techno, name='techno'), # La vue pour l'accueil
    path('contact', views.contact, name='contact'),  # La vue pour contacter par email
]
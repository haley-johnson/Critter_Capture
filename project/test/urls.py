from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('critters/', views.critters, name='critters'),  # Critter page
    path('endangerment/', views.conservation, name='endangerment')
]
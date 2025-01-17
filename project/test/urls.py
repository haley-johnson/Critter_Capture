from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('critters/', views.critters, name='critters'),  # Critter page
    path('conservation/', views.conservation, name='conservation'),
    path('upload_image/', views.upload_image, name='upload_image')
]
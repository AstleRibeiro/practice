from django.urls import path
from . import views

app_name='firsthello'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contactus/', views.contact, name='contactus'),
    path('', views.index),



]

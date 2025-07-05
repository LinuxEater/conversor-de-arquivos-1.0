from django.urls import path
from . import views

urlpatterns = [
    path('', views.converter, name='converter'),
    path('about/', views.converter, name='about'),
]
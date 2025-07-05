from django.urls import path
from . import views

urlpatterns = [
    path('', views.converter, name='converter'),
    path('about/', views.about, name='about'),
    path('price/', views.price, name='price'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.converter_txt_pdf, name='converter'),
]
from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.formpage),
    path('process', views.process),
    path('result', views.result)
]
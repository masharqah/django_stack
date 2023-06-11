from django.urls import path     
from . import views

urlpatterns = [ 
    path('', views.index),
    path('enterform', views.setparameters),
    path('proccess_money',views.proccess_money),
    path('reset',views.reset)
  ]
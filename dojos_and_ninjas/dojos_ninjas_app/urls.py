from django.urls import path     
from . import views

urlpatterns = [ 
    path('', views.index),
    path('add_entries', views.add_entries),
    path('del_dojo', views.del_dojo)

  ]
from django.urls import path     
from . import views

urlpatterns = [ 
    path('', views.index),
    path('login', views.login),
    path('reg', views.reg),
    path('welcome', views.welcome),
    path ('success', views.success),
    path('logout', views.logout) 
  ]
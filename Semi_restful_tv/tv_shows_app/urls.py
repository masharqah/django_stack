from django.urls import path     
from . import views

urlpatterns = [ 
    path('shows', views.shows),
    path('shows/new', views.add_show_form),
    path('add_show', views.add_show),
    path('delete_show/<int:id>', views.delete_show),
    path('shows/<int:id>', views.show_info),
    path('shows/edit/<int:id>', views.edit_show_form),
    path('shows/edit/edit_show/<str:id>', views.edit_show),
  ]
from django.urls import path     
from . import views

urlpatterns = [ 
    path('', views.index),
    path('add_course', views.add_course),
    path('comments/<int:id>', views.comments),
    path('comments/<int:id>/add_comment', views.add_comment),
    path('remove_course/<int:id>', views.remove_course )
  ]
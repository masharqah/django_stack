from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root),	
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:blogNumber>', views.ShowBlogNumber),
    path('blogs/<int:blogNumber>/edit', views.edit),
    path('blogs/<int:blogNumber>/delete', views.destroy),
    path('blogs/json', views.json)

]
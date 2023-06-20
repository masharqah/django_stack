from django.urls import path     
from . import views

urlpatterns = [ 
    path('', views.index),
    path('add_book', views.add_book),
    path('books/<str:id>',views.book_info),
    path('authors/<str:id>',views.author_info),
    path('author_to_book',views.author_to_book),
    path('authors', views.authors),
    path('book_to_author', views.book_to_author),
    path('authors/<str:id>', views.author_info),
    path('add_author', views.add_author)
  ]
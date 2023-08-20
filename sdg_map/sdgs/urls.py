from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name ='home'),
    path('add', views.add, name = 'add'),
    path('delete/<int:point_id>/', views.delete_point, name='delete_point'),
    path('download-csv/', views.download_csv, name='download_csv')
]
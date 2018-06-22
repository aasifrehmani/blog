from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('view/<postid>', views.view, name='view'),
    path('edit/<postid>', views.edit, name='edit'),
    path('delete/<postid>', views.delete, name='delete')
]
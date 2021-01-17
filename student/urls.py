from django.urls import path, include
from student import views

path('users/', views.UserList.as_view()),
path('users/<int:pk>/', views.UserDetail.as_view()),
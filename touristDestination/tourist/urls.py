from django.contrib import admin
from django.urls import path
from .views import *




urlpatterns = [

    path('api/create/',CreateView.as_view(),name='create'),
    path('api/retrieve/<int:pk>/',RetrieveView.as_view(), name='retrieve'),
    path('api/update/<int:pk>/',RetrieveUpdateView.as_view(), name='update'),
    path('api/delete/<int:pk>/',DeleteView.as_view(), name='delete'),
    path('api/search/<str:search>/',Search.as_view(), name='Search'),
    path('index/',index, name='index'),
    path('createDestination/',createDestination, name='createDestination'),
    path('editDestination/<int:pk>/',editDestination, name='editDestination'),
]

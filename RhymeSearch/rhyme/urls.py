# coding=utf-8
from django.urls import path
from . import views

app_name = 'rhyme'
urlpatterns = [
    path('', views.rhyme, name='rhyme'),
    path('getRhyme/', views.get_rhyme, name='getRhyme'),
    path('getRhyme/<int:pnum>/', views.get_rhyme, name='getRhyme'),
]

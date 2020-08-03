from django.urls import path
from core import views

urlpatterns = [
    path('', views.starting, name='starting'),
    path('create_user/', views.create_user, name='create_user'),
    path('quiz/<int:pk>/', views.quiz, name='quiz'),
    path('check/<int:pk>/', views.check, name='check'),
    path('score/<int:pk>/', views.score, name='score'),
    path('quiz/<int:pk>/result/', views.result, name='result')
]

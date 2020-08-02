from django.urls import path
from core import views

urlpatterns = [
    path('', views.starting, name='starting'),
    # path('greeting/', views.greeting, name='greeting'),
    path('quiz/', views.quiz, name='quiz'),
]

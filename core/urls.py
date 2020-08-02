from django.urls import path
from core import views

urlpatterns = [
    path('', views.starting, name='starting'),
    path('create_user/', views.create_user, name='create_user'),
    path('create_user/quiz/<int:pk>', views.quiz, name='quiz'),
    path('check/<int:pk>', views.check, name='check')
]

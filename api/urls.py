from aiquest.views import index, student, Login, RegisterAPI, LoginAPI
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('student/', student),
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
]
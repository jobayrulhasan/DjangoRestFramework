from aiquest.views import index, student
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('student/', student),
]
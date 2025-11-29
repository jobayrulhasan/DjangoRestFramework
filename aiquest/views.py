from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student1
from .serializers import StudentSerializar

# Create your views here.

@api_view(['GET', 'POST', 'PUT'])
def index(request):
    course = {
        'coursename': 'Django',
        'topics': ['django', 'api', 'asp']
    }
    if request.method == 'GET':
        return Response(course)
    elif request.method == 'POST':
        return Response(course)
    elif request.method == 'PUT':
        return Response(course)
    
    
@api_view(['GET', 'POST'])
def student(request):
    if request.method == 'GET':
        objs = Student1.objects.all()
        serializer = StudentSerializar(objs, many=True)
        return Response(serializer.data)
    else:
        data = request.data
        serializer = StudentSerializar(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
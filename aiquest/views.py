from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student1
from .serializers import StudentSerializar, LoginSerializer, RegisterSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

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
    
    
@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def student(request):
    if request.method == 'GET':
        objs = Student1.objects.all()
        serializer = StudentSerializar(objs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = StudentSerializar(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        objs = Student1.objects.get(id=data['id'])
        serializer = StudentSerializar(objs, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        objs = Student1.objects.get(id=data['id'])
        serializer = StudentSerializar(objs, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data = request.data
        objs = Student1.objects.get(id=data['id'])
        objs.delete()
        return Response({'message': 'Deleted successfully!'})

# for login
@api_view(['POST'])  
def Login(request):
    data = request.data
    serializer = LoginSerializer(data = data)
    if serializer.is_valid():
        data = serializer.validated_data
        return Response({'message':'Login success!'})
    return Response(serializer.errors)

# for user registration
class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        
        if not serializer.is_valid():
            return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({
            'status': True,
            'message': 'user created'
        }, status=status.HTTP_200_OK)
        
# Login for token
class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({"status": False, "message": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"status": False, "message": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                "status": True,
                "message": "Login success",
                "token": token.key
            }
        )
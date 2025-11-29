from rest_framework import serializers
from .models import Student1
from django.contrib.auth.models import User



class StudentSerializar(serializers.ModelSerializer):
    class Meta:
        model = Student1
        fields = '__all__'
        

# login 
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    
# user registration
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self, data):
        if User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError("Username already taken")
        if User.objects.filter(email = data['email']).exists():
            raise serializers.ValidationError("Email already taken")
        return data
    
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
    
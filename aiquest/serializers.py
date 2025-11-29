from rest_framework import serializers
from .models import Student1



class StudentSerializar(serializers.ModelSerializer):
    class Meta:
        model = Student1
        fields = '__all__'
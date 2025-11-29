from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    
    
class Student1(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
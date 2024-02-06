from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','task_name','task_desc','image','completed']

class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password']
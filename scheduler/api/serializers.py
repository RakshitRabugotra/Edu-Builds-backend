from rest_framework import serializers
from .models import Course, MyUser

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'url', 'duration', 'user_id')


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'user_email', 'passwd')

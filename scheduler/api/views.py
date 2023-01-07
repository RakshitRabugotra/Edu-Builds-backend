from django.shortcuts import render
from rest_framework import generics
from .serializers import CourseSerializer, MyUserSerializer
from .models import Course, MyUser

class CourseView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class MyUserView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

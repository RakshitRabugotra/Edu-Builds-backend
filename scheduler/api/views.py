from django.shortcuts import render
from rest_framework import generics
from .serializers import CourseSerializer, MyUserSerializer
from .models import Course, MyUser
from django.contrib.auth import authenticate, login

class CourseView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class MyUserView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


# To authenticate the user on login
def user_auth(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        # Redirect to a successful page
        ...
    else:
        # Return an 'invalid login' error message
        ...

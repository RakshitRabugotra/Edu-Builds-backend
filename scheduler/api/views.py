from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def base_view(request):
    return HttpResponse("<h1>HEllloo</h1>")
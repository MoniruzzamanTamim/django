from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def about(request):
    return HttpResponse("hello I am Tamim")
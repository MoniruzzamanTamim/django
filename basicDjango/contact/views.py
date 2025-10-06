from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def phone(request):
    return HttpResponse("My Contact Number is: 01739820399")
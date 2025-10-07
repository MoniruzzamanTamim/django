from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    context = {
        'name': 'Tamim'
    }
    return render(request, 'home.html', context)
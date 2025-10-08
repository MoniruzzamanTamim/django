from django.shortcuts import render
from datetime import  datetime

# Create your views here.


# def test(request):
#     name = 'tamim'
#     id = 23105036
#     institute = 'Canadian University of bangladeh'
#     return render(request, 'veriable/veriable.html', {'name': name})
   
def test(request):
   context = {
        'name': 'Md Moniruzzaman Tamim',
        'page_title': 'আমার ওয়েবসাইট',
        'welcome_message': 'স্বাগতম!',
        'users': ['রহিম', 'করিম', 'সুমন']
    }
   return render(request, 'veriable/veriable.html', context)
   
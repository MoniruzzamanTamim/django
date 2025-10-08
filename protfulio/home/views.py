from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'homePage/home.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # You can save this to database or send email here
        return HttpResponse(f"Thank you {name},  Your Mail {email} we received your message.")
    return render(request, 'contactPage/contact.html')

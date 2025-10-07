from django.urls import path
from . import views

urlpatterns = [
    path('', views.phone),          # ← এখানে ফাঁকা string '' ব্যবহার করা হয়েছে
]
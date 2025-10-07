from django.urls import path
from . import views

urlpatterns = [
    path('', views.about),          # ← এখানে ফাঁকা string '' ব্যবহার করা হয়েছে
]
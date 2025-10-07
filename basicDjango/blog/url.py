from django.urls import path
from . import views

urlpatterns = [
    path('', views.tamim),          # ← এখানে ফাঁকা string '' ব্যবহার করা হয়েছে
    path('userinfo/', views.userinfo),
]

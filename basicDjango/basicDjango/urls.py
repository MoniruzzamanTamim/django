"""
URL configuration for basicDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Option One 
# from blog import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('tamim/',views.tamim ),
#     path('userinfo/', views.userinfo),
# ]


# # OPTION-2: RENAME VIEW NAME
# from blog import views as blogView
# from tamim import views as aboutview
# from contact import views as contactView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('tamim/',blogView.tamim ),
#     path('userinfo/', blogView.userinfo),
#     path('contactView/', aboutview.about),
#     path('contact/', contactView.phone),
# ]

# # OPTION-3: Import DirecT Function to USe Link 
# from blog.views import tamim
# from blog.views import userinfo
# from tamim.views import about
# from contact.views import phone


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('tamim/', tamim ),
#     path('userinfo', userinfo),
#     path('about/', about),
#     path('contact', phone),
# ]

# Option-4: Include Function
from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.url')),
    path('about/', include('tamim.url')),
    path('contact/', include('contact.url')),
]
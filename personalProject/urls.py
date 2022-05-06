"""personalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
º
from petclub.views import HelloWorld
from petclub.views import PetAPIView
from petclub.views import PetListAPIView
from petclub.views import PersonView
from petclub.views import PetView

urlpatterns = [
    path('hi', HelloWorld.as_view(), name="helloworld"),
    path('api-auth/', include('rest_framework.urls')),
    path('pet-l', PetListAPIView.as_view(), name="pet-list"),
    path('pet-r', PetAPIView.as_view(), name="pet"),
    path('persons', PersonView.as_view(), name="person"),
    path('pets', PetView.as_view(), name='pet'),
]

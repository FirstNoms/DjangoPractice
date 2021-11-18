"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from django.urls import path, include


# def register(self):
#     print("Something hooooooge!")
#     return HttpResponse("Something hooooooge!")
#
#
#
# def login(request):
#     return render(request, "home.html")
#
#
#
# def home(request):
#     return render(request, "home.html")



#CRUD OPERATION(FUNCTIONS) FOR NATIVES
# def create_native(request):
#     return render(request, "create_native.html")
#
#
# def get_natives(request):
#     return render(request, "get_natives.html")
#
#
# def get_native(request):
#     return render(request, "get_native.html")
#
#
# def update_native(request):
#     return render(request, "update_native.html")
#
#
# def delete_native(request):
#     return render(request, "delete_native.html")



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home),
    path('cohorts', include("cohorts.urls")),

   ]

from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "user"

urlpatterns = [
    path('login/',views.loginauth,name="login"),
    path('logout/',views.logout,name="logout"),
  
]
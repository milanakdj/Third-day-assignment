from django.contrib import admin
from django.urls import path,include
from qna_app import views

urlpatterns = [
  path('view/',views.questions),
  path('popular/',views.popular),
]
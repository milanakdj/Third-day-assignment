from django.contrib import admin
from django.urls import path,include
from qna_app import views
app_name='qna'


urlpatterns = [
  path('read/',views.questions,name="read"),
  path('view/',views.questions),
  path('popular/',views.popular),
]
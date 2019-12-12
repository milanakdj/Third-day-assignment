from django.contrib import admin
from django.urls import path,include
from qna_app import views
app_name='qna'


urlpatterns = [
  path('read/',views.question,name="read"),
  path('update/<int:id>',views.update_question,name="update"),
  path('vote/<int:id>',views.vote_question,name="vote"),
  path('delete/<int:id>',views.delete_question,name="delete"),
  path('add/',views.addquestion,name="add"),
  path('view/',views.questions),
  path('popular/',views.popular),
  path('answer/<int:id>/',views.answer, name="ans"),
  path('listview/',views.QuestionListView.as_view(),name="listview"),
]
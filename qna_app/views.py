from django.shortcuts import render

from .models import QuestionModel,AnswerModel,CategoryModel
# Create your views here.


def questions(request):
    Question=QuestionModel.objects.all()
    return render(request,'question.html',{'question':Question})


def popular(request):
    Category=CategoryModel.objects.all()
    Question=QuestionModel.objects.all()
    Answer = AnswerModel.objects.all()

    return render(request,'popular.html',{'category':Category,'question':Question,'answer':Answer})
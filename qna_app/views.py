from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView,ListView

from .models import QuestionModel,AnswerModel,CategoryModel
# Create your views here.
from .forms import QuestionForm, AnswerForm


def popular(request):
    Category=CategoryModel.objects.all()
    Question=QuestionModel.objects.all()
    Answer = AnswerModel.objects.all()

    return render(request,'popular.html',{'category':Category,'question':Question,'answer':Answer})


def detail(request, id):
    question = QuestionModel.objects.filter(id=id).first()

    if request.method=="POST":
        #THIS MEANS THE USER SUBMITTED THE ANSWER   
        
        answer = AnswerModel(answer_desc=request.POST['answer'], question=question)
        answer.save(force_insert=True) #this makes so that the attributes that are needed but not sent still gets those to store the default


    answers = AnswerModel.objects.filter(question=id)
    d={
        'question':question,
        'answers':answers
    }
    return render(request, 'detail.html',d)


def questions(request):
    Question=QuestionModel.objects.all()
    return render(request,'questionmodel_list.html',{'question':Question})



def question(request):
    if 'id' in request.session:
        question=QuestionModel.objects.all()
        return render(request,'questionmodel_list.html',{'question':question})
    else:
        return redirect ('user:login')


def addquestion(request):
    if request.method=="POST":
        forms = QuestionForm(request.POST, request.FILES)
        if forms.is_valid():
            try:
                forms.save()
                return redirect ('qna:read')
            except:
                return HttpResponse('Failed')
        else:
            print(forms.errors)
            return HttpResponse('For not Valid!')
    else:
        # forms=QuestionForm
        category = CategoryModel.objects.all()
        return render(request,'questionmodel_create.html',{'category':category})


def update_question(request, id):
    question = QuestionModel.objects.get(id=id)
    form = QuestionForm(instance=question)
    if request.method=="POST":
        forms = QuestionForm(request.POST, request.FILES, instance=question)
        if forms.is_valid():
            try:
                forms.save()
                return redirect ('qna:read')
            except:
                return HttpResponse('Failed')
        else:
            print(forms.errors)
            return HttpResponse('For not Valid!')
    else:
        return render (request,'questionmodel_update.html',{'form':form})
        return HttpResponse('updated')

def delete_question(request, id):
    question = QuestionModel.objects.get(id=id)
    questions.delete()
    return HttpResponse('deleted')

def vote_question(request, id):
    questions = QuestionModel.objects.get(id=id)
    vote = questions.question_votes + 1
    questions.question_votes=vote
    questions.save()
    return redirect('qna:read')

def comment(request, id):
    questions = QuestionModel.objects.get(id=id)



def answer(request, id):
    if request.method=="POST":
        by = request.POST.get('answer_by')
        desc = request.POST.get('answer_desc')
        answer_img = request.POST.get('question_img')
        question = QuestionModel.objects.get(id=id)
        Comment = AnswerModel(answer_by=by,answer_desc=desc,question_img=answer_img, question=question)
        
        Comment.save()
        return HttpResponse('success')
    else:
        form = AnswerForm()
        a={'form':form}
        b={'id':id}
        c={**a,**b}
        return render(request,'answermodel.html',c)
#     answers = AnswerModel.objects.all()
#     return render(request,'answermodel.html',{'answer':answers})



class QuestionListView(ListView):
    queryset = QuestionModel.objects.all()





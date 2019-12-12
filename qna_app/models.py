from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    title=models.CharField(max_length=255)
    category_desc = models.CharField(max_length=120)


class QuestionModel(models.Model):
    title=models.CharField(max_length=255)
    posted_by = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    question_desc = models.TextField()
    question_votes=models.IntegerField(default=0)
    question_img=models.ImageField(upload_to='QuestionImg',blank=True,null=True)
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return(self.title)


class AnswerModel(models.Model):
    answer_by = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_accepted=models.BooleanField(default=False)
    answer_desc = models.TextField()
    question=models.ForeignKey(QuestionModel,on_delete=models.CASCADE)
    answer_votes=models.IntegerField(default=0)
    question_img=models.ImageField(upload_to='QuestionImg',blank=True,null=True)
    def __str__(self):
        return self.answer_desc[:49] +'...'

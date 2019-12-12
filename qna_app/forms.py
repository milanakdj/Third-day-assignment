from django import forms
from .models import QuestionModel

class QuestionModel(forms.ModelForm):
    class Meta:
        models = QuestionModel
        fields = '__all__'
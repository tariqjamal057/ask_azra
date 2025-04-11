from django import forms

from .models import Answer, Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "content"]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]

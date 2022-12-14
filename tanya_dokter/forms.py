# from dataclasses import fields
from django import forms
from .models import Answer, Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'detail', 'tags')


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('detail', )

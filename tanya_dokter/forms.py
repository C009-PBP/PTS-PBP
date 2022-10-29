# from dataclasses import fields
from django import forms
from .models import Forum


class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ('specialization', 'title', 'question')

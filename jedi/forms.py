from django import forms
from django.db import IntegrityError

from .models import Candidate, Answer, Question
from django.core.exceptions import ValidationError, PermissionDenied


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'planet', 'age', 'email']


class QuestionForm(forms.ModelForm):
    text = forms.BooleanField(required=False)
    answer = forms.BooleanField(initial=False, required=False)

    class Meta:
        model = Question
        fields = '__all__'
        widgets = {'text': forms.HiddenInput()}
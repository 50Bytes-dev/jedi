from django import forms
from django.db.models import Prefetch
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.forms import formset_factory, modelformset_factory, BaseModelFormSet

from jedi.models import Candidate, Question, Answer, Jedi
from .forms import CandidateForm, QuestionForm


def login(request):
    return render(request, 'login.html', {})


class CandidateCreate(View):

    def get(self, request):
        form = CandidateForm()
        return render(request, 'index.html', context={'form': form})

    def post(self, request):
        bound_form = CandidateForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect('question', new_post.id)
        return render(request, 'list_task.html', context={'form': bound_form})


class JediList(View):

    def get(self, request):
        jedis = Jedi.objects.select_related('planet').all()
        return render(request, 'list_jedi.html', context={'jedis': jedis})


class JediSetPadavan(View):

    def get(self, request, jedi_id, candidate_id):
        Candidate.objects.filter(pk=candidate_id).update(jedi_id=jedi_id)
        return redirect('candidatelist', jedi_id)


class CandidateList(View):

    def get(self, request, jedi_id):
        jedi = Jedi.objects.get(pk=jedi_id)
        candidates = Candidate.objects.prefetch_related(
            Prefetch(
                'answers_table',
                to_attr='answers',
                queryset=Answer.objects.select_related('question')
            )
        ).filter(jedi=None, planet=jedi.planet)
        return render(request, 'list_candidate.html', context={'candidates': candidates, 'jedi_id': jedi_id})


class QuestionView(View):
    template_name = 'list_task.html'
    QuestionFormSet = modelformset_factory(Question, fields=('id', 'text'), form=QuestionForm, extra=0)

    def get(self, request, candidate_id):
        candidate = Candidate.objects.get(pk=candidate_id)
        questions = Question.objects.filter(order=candidate.planet)
        formset = self.QuestionFormSet(queryset=questions)
        return render(request, self.template_name, {
            'formset': formset,
            'candidate_id': candidate_id
        })

    def post(self, request, candidate_id):
        candidate = Candidate.objects.get(pk=candidate_id)
        formset = self.QuestionFormSet(request.POST)
        for form in formset.forms:
            if form.is_valid():
                data = form.cleaned_data
                Answer(candidate=candidate, answer=data['answer'], question=data['id']).save()
        return redirect('/')
from django.urls import path

from jedi.views import CandidateCreate, login, QuestionView, JediList, CandidateList, JediSetPadavan
from . import views


urlpatterns = [
    path('',  views.login, name='login'),
    path('jedi/',  JediList.as_view(), name='jedilist'),
    path('<int:jedi_id>/candidate_list/',  CandidateList.as_view(), name='candidatelist'),
    path('<int:jedi_id>/candidate_list/<int:candidate_id>',  JediSetPadavan.as_view(), name='setpadavan'),
    path('candidate/',  CandidateCreate.as_view(), name='candidatecreate'),
    path('candidate/list_task/<int:candidate_id>/',  QuestionView.as_view(), name='question'),
]
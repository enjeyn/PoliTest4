from django.views.generic import DetailView, ListView, RedirectView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect

from ptest.models import Choice, Question, Vote


class QuestionListView(ListView):
    model = Question


class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['question'].votable = self.object.can_vote(self.request.user)
        return context


class QuestionVoteView(RedirectView):
    def post(self, request, *args, **kwargs):
        question = Question.objects.get(id=kwargs['pk'])
        user = request.user
        choice = Choice.objects.get(id=request.POST['choice_pk'])
        Vote.objects.create(question=question, user=user, choice=choice)
        return super(QuestionVoteView, self).post(request, *args, **kwargs)

    def get_redirect_url(self, **kwargs):
        return reverse_lazy('ptest:detail', args=[kwargs['pk']])


class ResultsView(ListView):
    model = Vote

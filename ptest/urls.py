from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from ptest import views
from ptest.views import QuestionDetailView, QuestionListView, QuestionVoteView, ResultsView

app_name = 'ptest'

urlpatterns = [
    url(r'^$', QuestionListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', QuestionDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/vote/$', login_required(QuestionVoteView.as_view()), name='vote'),
    url(r'^result/$', ResultsView.as_view(), name='result'),
]
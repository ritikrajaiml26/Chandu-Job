from django.urls import path
from . import views

app_name = 'answerkeys'

urlpatterns = [
    path('', views.AnswerKeyListView.as_view(), name='answerkey_list'),
]

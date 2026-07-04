from django.views.generic import ListView, DetailView
from .models import AnswerKey

class AnswerKeyListView(ListView):
    model = AnswerKey
    template_name = 'answerkeys/answerkey_list.html'
    context_object_name = 'answerkeys'
    paginate_by = 20

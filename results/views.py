from django.views.generic import ListView, DetailView
from .models import Result

class ResultListView(ListView):
    model = Result
    template_name = 'results/result_list.html'
    context_object_name = 'results'
    paginate_by = 20

class ResultDetailView(DetailView):
    model = Result
    template_name = 'results/result_detail.html'
    context_object_name = 'result'

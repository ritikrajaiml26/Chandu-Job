from django.views.generic import ListView, DetailView
from .models import AdmitCard

class AdmitCardListView(ListView):
    model = AdmitCard
    template_name = 'admitcards/admitcard_list.html'
    context_object_name = 'admitcards'
    paginate_by = 20

class AdmitCardDetailView(DetailView):
    model = AdmitCard
    template_name = 'admitcards/admitcard_detail.html'
    context_object_name = 'admitcard'

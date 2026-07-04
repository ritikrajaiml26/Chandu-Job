from django.views.generic import ListView, DetailView
from .models import Admission

class AdmissionListView(ListView):
    model = Admission
    template_name = 'admissions/admission_list.html'
    context_object_name = 'admissions'
    paginate_by = 20

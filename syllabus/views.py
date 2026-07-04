from django.views.generic import ListView, DetailView
from .models import Syllabus

class SyllabusListView(ListView):
    model = Syllabus
    template_name = 'syllabus/syllabus_list.html'
    context_object_name = 'syllabus_list'
    paginate_by = 20

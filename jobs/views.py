from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Job
from results.models import Result
from admitcards.models import AdmitCard
from answerkeys.models import AnswerKey
from syllabus.models import Syllabus
from admissions.models import Admission

def home(request):
    latest_jobs = Job.objects.filter(status='published').order_by('-created_at')[:10]
    trending_jobs = Job.objects.filter(status='published', is_trending=True).order_by('-created_at')[:8]
    latest_results = Result.objects.all()[:10]
    latest_admit_cards = AdmitCard.objects.all()[:10]
    latest_answer_keys = AnswerKey.objects.all()[:5]
    latest_syllabus = Syllabus.objects.all()[:5]
    latest_admissions = Admission.objects.all()[:5]
    
    context = {
        'latest_jobs': latest_jobs,
        'trending_jobs': trending_jobs,
        'latest_results': latest_results,
        'latest_admit_cards': latest_admit_cards,
        'latest_answer_keys': latest_answer_keys,
        'latest_syllabus': latest_syllabus,
        'latest_admissions': latest_admissions,
    }
    return render(request, 'jobs/home.html', context)

class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 12

    def get_queryset(self):
        return Job.objects.filter(status='published').order_by('-created_at')

class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views_count += 1
        obj.save()
        return obj

def job_search(request):
    query = request.GET.get('q')
    results = Job.objects.filter(status='published')
    if query:
        results = results.filter(
            Q(title__icontains=query) | 
            Q(organization_name__icontains=query) |
            Q(short_description__icontains=query)
        )
    return render(request, 'jobs/search_results.html', {'jobs': results, 'query': query})

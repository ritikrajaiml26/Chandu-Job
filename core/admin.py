from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Category

class CustomAdminSite(AdminSite):
    site_header = "Chandu Job Portal Admin Panel"
    site_title = "Chandu Job Portal Admin"
    index_title = "Dashboard Statistics & Content Management"

    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        
        # Import models inside to avoid circular dependencies
        from jobs.models import Job
        from results.models import Result
        from admitcards.models import AdmitCard
        from answerkeys.models import AnswerKey
        from syllabus.models import Syllabus
        from admissions.models import Admission
        from django.db.models import Sum
        
        extra_context['stats'] = {
            'total_jobs': Job.objects.count(),
            'published_jobs': Job.objects.filter(status='published').count(),
            'draft_jobs': Job.objects.filter(status='draft').count(),
            'total_results': Result.objects.count(),
            'total_admitcards': AdmitCard.objects.count(),
            'total_answerkeys': AnswerKey.objects.count(),
            'total_syllabus': Syllabus.objects.count(),
            'total_admissions': Admission.objects.count(),
            'total_categories': Category.objects.count(),
            'total_job_views': Job.objects.aggregate(total_views=Sum('views_count'))['total_views'] or 0,
        }
        
        return super().index(request, extra_context)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from jobs.models import Job
from results.models import Result
from admitcards.models import AdmitCard

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['jobs:home', 'jobs:job_list', 'results:result_list', 'admitcards:admitcard_list', 'pages:about', 'pages:contact']

    def location(self, item):
        return reverse(item)

class JobSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Job.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('jobs:job_detail', args=[obj.slug])

class ResultSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Result.objects.all()

    def location(self, obj):
        return reverse('results:result_detail', args=[obj.slug])

class AdmitCardSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return AdmitCard.objects.all()

    def location(self, obj):
        return reverse('admitcards:admitcard_detail', args=[obj.slug])

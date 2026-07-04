from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap, JobSitemap, ResultSitemap, AdmitCardSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'jobs': JobSitemap,
    'results': ResultSitemap,
    'admitcards': AdmitCardSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
    path('', include('jobs.urls')),
    path('results/', include('results.urls')),
    path('admit-cards/', include('admitcards.urls')),
    path('answer-keys/', include('answerkeys.urls')),
    path('syllabus/', include('syllabus.urls')),
    path('admissions/', include('admissions.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

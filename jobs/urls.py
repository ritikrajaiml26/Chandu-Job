from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.JobListView.as_view(), name='job_list'),
    path('jobs/<slug:slug>/', views.JobDetailView.as_view(), name='job_detail'),
    path('search/', views.job_search, name='job_search'),
]

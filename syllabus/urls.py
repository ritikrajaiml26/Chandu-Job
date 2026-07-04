from django.urls import path
from . import views

app_name = 'syllabus'

urlpatterns = [
    path('', views.SyllabusListView.as_view(), name='syllabus_list'),
]

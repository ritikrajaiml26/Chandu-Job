from django.urls import path
from . import views

app_name = 'results'

urlpatterns = [
    path('', views.ResultListView.as_view(), name='result_list'),
    path('<slug:slug>/', views.ResultDetailView.as_view(), name='result_detail'),
]

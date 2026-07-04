from django.urls import path
from . import views

app_name = 'admitcards'

urlpatterns = [
    path('', views.AdmitCardListView.as_view(), name='admitcard_list'),
    path('<slug:slug>/', views.AdmitCardDetailView.as_view(), name='admitcard_detail'),
]

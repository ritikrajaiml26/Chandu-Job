from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms/', views.terms, name='terms'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
]

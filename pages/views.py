from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from django.http import HttpResponse

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        f"Sitemap: {request.scheme}://{request.get_host()}/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('pages:contact')
    return render(request, 'pages/contact.html')

def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')

def terms(request):
    return render(request, 'pages/terms.html')

def disclaimer(request):
    return render(request, 'pages/disclaimer.html')

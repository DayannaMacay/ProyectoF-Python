from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def service(request):
    return render(request, "core/service.html")

def contact(request):
    return render(request, "core/contact.html")


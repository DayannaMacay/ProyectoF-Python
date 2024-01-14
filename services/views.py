from django.shortcuts import render
from .models import Service, Testimony

# Create your views here.
def service(request):
    services = Service.objects.all()
    testimonials = Testimony.objects.all()
    return render(request, "services/service.html", {'services': services, 'testimonials': testimonials})

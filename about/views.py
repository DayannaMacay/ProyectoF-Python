from django.shortcuts import render
from .models import About, Schedule

def about(request):
    barbers = About.objects.all()
    schedules = Schedule.objects.all()
    return render(request, 'about/about.html', {'barbers': barbers, 'schedules': schedules})

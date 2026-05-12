
from django.shortcuts import render
from .models import Driver

def driver_list(request):
    drivers = Driver.objects.all().order_by('last_name', 'first_name')
    return render(request, 'drivers/list.html', {'drivers': drivers})

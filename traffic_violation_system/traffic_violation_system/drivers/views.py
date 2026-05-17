
from django.db.models import Count
from django.shortcuts import render
from .models import Driver

def driver_list(request):
    drivers = Driver.objects.annotate(violation_count=Count('violation')).order_by('-violation_count', 'last_name', 'first_name')
    return render(request, 'drivers/list.html', {'drivers': drivers})

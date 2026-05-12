
from django.shortcuts import render
from .models import Vehicle

def vehicle_list(request):
    vehicles = Vehicle.objects.select_related('driver').order_by('plate_number')
    return render(request, 'vehicles/list.html', {'vehicles': vehicles})

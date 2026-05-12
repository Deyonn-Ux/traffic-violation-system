
from django.shortcuts import render
from .models import Violation

def violation_list(request):
    plate = request.GET.get('plate', '').strip()
    license_number = request.GET.get('license', '').strip()
    violations = Violation.objects.select_related('driver', 'vehicle')

    if plate:
        violations = violations.filter(vehicle__plate_number__icontains=plate)

    if license_number:
        violations = violations.filter(driver__license_number__icontains=license_number)

    context = {
        'violations': violations.order_by('status', 'violation_type'),
        'plate_query': plate,
        'license_query': license_number,
    }
    return render(request, 'violations/list.html', context)

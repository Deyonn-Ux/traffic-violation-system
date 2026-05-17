from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from django.shortcuts import redirect, render

from drivers.models import Driver
from payments.models import Payment
from vehicles.models import Vehicle
from violations.models import Violation


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('payment_list')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


@login_required
def account_settings(request):
    return render(request, 'accounts/settings.html')


@login_required
@user_passes_test(lambda u: u.is_staff)
def staff_portal(request):
    repeat_offenders = (
        Driver.objects.annotate(violation_count=Count('violation'))
        .filter(violation_count__gte=2)
        .order_by('-violation_count', 'last_name', 'first_name')
    )
    context = {
        'total_drivers': Driver.objects.count(),
        'total_vehicles': Vehicle.objects.count(),
        'total_violations': Violation.objects.count(),
        'total_payments': Payment.objects.count(),
        'pending_payments': Payment.objects.filter(status='pending').count(),
        'paid_payments': Payment.objects.filter(status='paid').count(),
        'repeat_offenders': repeat_offenders,
    }
    return render(request, 'accounts/staff_portal.html', context)

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count
from django.shortcuts import redirect, render

from drivers.models import Driver
from payments.models import Payment
from vehicles.models import Vehicle
from violations.models import Violation
from .forms import SignUpForm, UpdateEmailForm, UpdateMobileForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('payment_list')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


@login_required
def account_settings(request):
    mobile_number = request.session.get('mobile_number')
    return render(request, 'accounts/settings.html', {'mobile_number': mobile_number})


@login_required
def update_email(request):
    if request.method == 'POST':
        form = UpdateEmailForm(request.POST)
        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.save()
            messages.success(request, 'Email address updated successfully.')
            return redirect('account_settings')
    else:
        form = UpdateEmailForm(initial={'email': request.user.email})

    return render(request, 'accounts/update_email.html', {'form': form})


@login_required
def update_mobile(request):
    if request.method == 'POST':
        form = UpdateMobileForm(request.POST)
        if form.is_valid():
            request.session['mobile_number'] = form.cleaned_data['mobile_number']
            messages.success(request, 'Mobile number saved for this browser session.')
            return redirect('account_settings')
    else:
        form = UpdateMobileForm(initial={'mobile_number': request.session.get('mobile_number', '')})

    return render(request, 'accounts/update_mobile.html', {'form': form})


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

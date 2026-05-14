
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from .models import Payment

def payment_list(request):
    payments = Payment.objects.select_related('violation', 'user').order_by('-created_at')
    return render(request, 'payments/list.html', {'payments': payments})


@login_required
def payment_checkout(request):
    receipt = None

    if request.method == 'POST':
        timestamp = timezone.now().strftime('%Y%m%d%H%M%S%f')[:-3]
        receipt = Payment.objects.create(
            user=request.user,
            ticket_number=request.POST.get('ticket_number', '').strip(),
            plate_number=request.POST.get('plate_number', '').strip(),
            violation_type=request.POST.get('violation_type', '').strip(),
            payment_method=request.POST.get('payment_method', 'GCash'),
            amount_paid=request.POST.get('amount_paid') or 0,
            receipt_number=f'TVS-{timestamp}',
            status='pending',
        )
        messages.success(request, 'Temporary receipt created. Your payment is pending admin verification.')

    return render(request, 'payments/checkout.html', {'receipt': receipt})

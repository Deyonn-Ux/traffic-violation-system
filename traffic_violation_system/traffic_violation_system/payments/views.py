
from django.shortcuts import render
from .models import Payment

def payment_list(request):
    payments = Payment.objects.select_related('violation').order_by('payment_method')
    return render(request, 'payments/list.html', {'payments': payments})

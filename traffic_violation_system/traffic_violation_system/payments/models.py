
from django.db import models
from django.conf import settings
from django.utils import timezone
from violations.models import Violation

class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Verification'),
        ('paid', 'Paid'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    violation = models.ForeignKey(Violation, on_delete=models.SET_NULL, null=True, blank=True)
    ticket_number = models.CharField(max_length=100, blank=True)
    plate_number = models.CharField(max_length=50, blank=True)
    violation_type = models.CharField(max_length=200, blank=True)
    payment_method = models.CharField(max_length=50)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    receipt_number = models.CharField(max_length=100, blank=True, db_index=True)
    created_at = models.DateTimeField(default=timezone.now)
    verified_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.receipt_number or f"{self.payment_method} payment"

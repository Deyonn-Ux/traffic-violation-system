
from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'receipt_number',
        'ticket_number',
        'plate_number',
        'payment_method',
        'amount_paid',
        'status',
        'user',
        'created_at',
    )
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = ('receipt_number', 'ticket_number', 'plate_number', 'user__username')
    readonly_fields = ('receipt_number', 'created_at')
    ordering = ('-created_at',)

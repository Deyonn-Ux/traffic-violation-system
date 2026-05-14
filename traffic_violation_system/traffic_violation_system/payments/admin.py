
from django.contrib import admin
from django.utils import timezone
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
    list_editable = ('status',)
    actions = ('mark_as_paid', 'mark_as_pending', 'mark_as_rejected')

    @admin.action(description='Mark selected payments as Paid')
    def mark_as_paid(self, request, queryset):
        updated = queryset.update(status='paid', verified_at=timezone.now())
        self.message_user(request, f'{updated} payment(s) marked as Paid.')

    @admin.action(description='Mark selected payments as Pending Verification')
    def mark_as_pending(self, request, queryset):
        updated = queryset.update(status='pending', verified_at=None)
        self.message_user(request, f'{updated} payment(s) marked as Pending Verification.')

    @admin.action(description='Mark selected payments as Rejected')
    def mark_as_rejected(self, request, queryset):
        updated = queryset.update(status='rejected', verified_at=timezone.now())
        self.message_user(request, f'{updated} payment(s) marked as Rejected.')

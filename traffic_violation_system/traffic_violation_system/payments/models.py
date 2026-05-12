
from django.db import models
from violations.models import Violation

class Payment(models.Model):
    violation = models.ForeignKey(Violation, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.payment_method

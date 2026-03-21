from django.db import models
from django.conf import settings

class Transaction(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    amount = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, default='PENDING') # PENDING, SUCCESS, FAILURE
    txn_id = models.CharField(max_length=100, null=True, blank=True)
    bank_txn_id = models.CharField(max_length=100, null=True, blank=True)
    txn_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.status}"

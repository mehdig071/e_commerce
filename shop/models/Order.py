from django.db import models
from accounts.models.Customer import Customer

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ]
    client_name = models.CharField(max_length=255)
    billing_address = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    quantity = models.IntegerField()
    taxe = models.FloatField()
    author = models.ForeignKey(Customer, on_delete=models.PROTECT)
    order_cost = models.FloatField()
    order_cost_ttc = models.FloatField()
    is_paid = models.BooleanField(default=False)
    carrier_name = models.CharField(max_length=255)
    carrier_price = models.FloatField()
    payment_method = models.CharField(max_length=255)
    stripe_payment_intent = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.client_name}"
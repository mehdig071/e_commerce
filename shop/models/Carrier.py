from django.db import models
from django.utils.text import slugify

class Carrier(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    description = models.CharField(max_length=120, blank=False, null=False)
    details = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="carrier_images/%Y/%m/%d/", blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Carrier'
        verbose_name_plural = 'Carriers'
        
    def __str__(self):
        return f"{self.name} ( {self.price} € )" 

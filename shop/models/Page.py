from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Page(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    is_head = models.BooleanField(blank=False, null=False)
    is_foot = models.BooleanField(blank=False, null=False)
    is_checkout = models.BooleanField(blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs) 

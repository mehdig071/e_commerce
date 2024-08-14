from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    agree_terms = models.BooleanField(default=False)
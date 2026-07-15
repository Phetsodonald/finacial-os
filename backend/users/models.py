from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pay_day = models.PositiveSmallIntegerField(default=25)
    currency = models.CharField(max_length=5, default="ZAR")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
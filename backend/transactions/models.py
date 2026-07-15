from django.db import models
from django.conf import settings

class Transactions(models.Model):
    class TransactionType(models.TextChoices):
        INCOME = "income", "Income"
        EXPENSE = "expense", "Expense"

    class Category(models.TextChoices):
        SALARY = "salary", "Salary"
        FREELANCE = "freelance", "Freelance"
        FOOD = "food", "Food"
        FUEL = "fuel", "Fuel"
        RENT = "rent", "Rent"
        SHOPPING = "shopping", "Shopping"
        INTERNET = "internet",  "Internet"
        ENTERTAINMENT = "entertainment", "Entertainment"
        INVESTMENT = "investment", "Investment"
        SAVINGS = "savings", "Savings"
        OTHER = "other", "Other"
    
    class PaymentMethod(models.TextChoices):
        CASH = "cash", "Cash"
        CARD = "card", "Card"
        EFT = "eft", "EFT"
        MOBILE = "mobile", "Mobile"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transactions")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TransactionType.choices)
    category = models.CharField(max_length=30, choices=Category.choices)
    payment_method = models.CharField(max_length=30, choices=PaymentMethod.choices)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.title} - R{self.amount}"
from django.db import models
from django.conf import settings

class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user}'s Wallet"

class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions')
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    is_credit = models.BooleanField(default=True)

    def __str__(self):
        return f"Transaction on {self.date.strftime('%Y-%m-%d %H:%M:%S')}"
    
    def deposit(self, amount, description="Deposit"):
        self.balance += amount
        self.save()
        Transaction.objects.create(wallet=self, amount=amount, description=description, is_credit=True)

    def withdraw(self, amount, description="Withdrawal"):
        if self.balance >= amount:
            self.balance -= amount
            self.save()
            Transaction.objects.create(wallet=self, amount=amount, description=description, is_credit=False)
            return True
        return False

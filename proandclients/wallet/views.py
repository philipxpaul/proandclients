from django.shortcuts import redirect
from wallet.models import Wallet

def deposit_to_wallet(request, amount):
    wallet, created = Wallet.objects.get_or_create(user=request.user)
    wallet.deposit(amount, description="Top-up Wallet")
    return redirect('consultant')  # Redirect to a confirmation page or back to the wallet page

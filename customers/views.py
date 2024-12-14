from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomerRegistrationForm, CustomerProfileForm
from .models import Customer

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Registration successful. Please complete your profile.')
            return redirect('customers:profile')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'customers/register.html', {'form': form})

@login_required
def profile(request):
    customer = request.user.customer
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('customers:profile')
    else:
        form = CustomerProfileForm(instance=customer)
    return render(request, 'customers/profile.html', {'form': form})
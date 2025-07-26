from django.shortcuts import render, redirect
from .forms import CustomerSignUpForm, SellerSignUpForm

def customer_signup(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace with your login page or home
    else:
        form = CustomerSignUpForm()
    return render(request, 'accounts/signup_customer.html', {'form': form})


def seller_signup(request):
    if request.method == 'POST':
        form = SellerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SellerSignUpForm()
    return render(request, 'accounts/signup_seller.html', {'form': form})






# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomerLoginForm, SellerLoginForm

def customer_login_view(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # or redirect to customer dashboard
    else:
        form = CustomerLoginForm()
    return render(request, 'accounts/customer_login.html', {'form': form})


def seller_login_view(request):
    if request.method == 'POST':
        form = SellerLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # or redirect to seller dashboard
    else:
        form = SellerLoginForm()
    return render(request, 'accounts/seller_login.html', {'form': form})

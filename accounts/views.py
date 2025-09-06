from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.models import Product


User = get_user_model()

# ===============================
# Customer Signup
# ===============================
def signup_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup_customer')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('signup_customer')

        user = User.objects.create_user(
            username=email, email=email, password=password, first_name=name, user_type='customer'
        )
        user.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login_customer')

    return render(request, 'accounts/signup.html', {'user_type': 'Customer'})


# ===============================
# Seller Signup
# ===============================
def signup_seller(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup_seller')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('signup_seller')

        user = User.objects.create_user(
            username=email, email=email, password=password, first_name=name, user_type='seller'
        )
        user.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login_seller')

    return render(request, 'accounts/signup.html', {'user_type': 'Seller'})


# ===============================
# Customer Login
# ===============================
def login_customer(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user and user.user_type == 'customer':  
            login(request, user)
            return redirect('customer_dashboard')  
        else:
            messages.error(request, "Invalid credentials for customer")
            return redirect('login_customer')
    return render(request, 'accounts/login.html', {'user_type': 'Customer'})




# ===============================
# Seller Login
# ===============================
def login_seller(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user and user.user_type == 'seller':
            login(request, user)
            return redirect('seller_dashboard')
        else:
            messages.error(request, "Invalid credentials for seller")
            return redirect('login_seller')
    return render(request, 'accounts/login.html', {'user_type': 'Seller'})


# ===============================
# Dashboard redirect
# ===============================
@login_required
def dashboard(request):
    """
    Login করার পরে user কে redirect করবে তাদের type অনুযায়ী
    """
    if request.user.user_type == 'seller':
        return redirect('seller_home')
    elif request.user.user_type == 'customer':
        return redirect('customer_home')
    else:
        return redirect('home')


# ===============================
# Seller & Customer Home Pages
# ===============================



# ===============================
# Seller Dashboard
# ===============================
@login_required
def seller_home(request):
    my_products = Product.objects.filter(seller=request.user)
    top_deals = Product.objects.filter(is_top_deal=True)
    total_orders_count = Order.objects.filter(product__seller=request.user).count()
    total_earnings = sum([o.total_price for o in Order.objects.filter(product__seller=request.user)])
    
    context = {
        'my_products': my_products,
        'top_deals': top_deals,
        'my_products_count': my_products.count(),
        'total_orders_count': total_orders_count,
        'total_earnings': total_earnings,
    }
    return render(request, 'accounts/seller_home.html', context)





@login_required
def customer_home(request):
    return render(request, 'accounts/customer_home.html')


# ===============================
# Forgot Password (Optional / Future)
# ===============================
# def forgot_password(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         try:
#             user = User.objects.get(email=email)
#             return redirect('reset_password', email=email)
#         except User.DoesNotExist:
#             messages.error(request, "Email not registered")
#             return redirect('forgot_password')
#     return render(request, 'accounts/forgot_password.html')


# def reset_password(request, email):
#     try:
#         user = User.objects.get(email=email)
#     except User.DoesNotExist:
#         messages.error(request, "Invalid request")
#         return redirect('forgot_password')
#
#     if request.method == 'POST':
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirmPassword')
#
#         if password != confirm_password:
#             messages.error(request, "Passwords do not match")
#             return redirect('reset_password', email=email)
#
#         user.set_password(password)
#         user.save()
#         messages.success(request, "Password updated successfully! Please log in.")
#         if user.user_type == 'customer':
#             return redirect('login_customer')
#         else:
#             return redirect('login_seller')
#
#     return render(request, 'accounts/reset_password.html', {'email': email})
def seller_home(request):
    return render(request, "accounts/seller_home.html")

def create_post(request):
    return render(request, "accounts/create_post.html")

def manage_posts(request):
    return render(request, "accounts/manage_posts.html")

def orders(request):
    return render(request, "accounts/orders.html")




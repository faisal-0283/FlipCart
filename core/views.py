from django.shortcuts import render
from .models import Banner, Category, Product

def index(request):
    banners = Banner.objects.filter(is_active=True)  # get all active banners
    popular_categories = Category.objects.filter(is_popular=True)
    top_deals = Product.objects.filter(is_top_deal=True)
    
    return render(request, 'core/index.html', {
        'banners': banners,
        'popular_categories': popular_categories,
        'top_deals': top_deals,
    })




def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def faq(request):
    return render(request, 'core/faq.html')

def terms(request):
    return render(request, 'core/terms.html')









from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Username or Password wrong')

    return render(request, 'core/login.html')




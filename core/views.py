from django.shortcuts import render, redirect
from .models import Banner, Category, Product
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import get_object_or_404

def home(request):   
    banners = Banner.objects.filter(is_active=True)
    popular_categories = Category.objects.filter(is_popular=True)
    top_deals = Product.objects.filter(is_top_deal=True)
    
    return render(request, 'core/index.html', {
        'banners': banners,
        'popular_categories': popular_categories,
        'top_deals': top_deals,
    })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:home')  
        else:
            messages.error(request, 'Username or Password wrong')

    return render(request, 'core/login.html')


def search_products(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Product.objects.filter(
            Q(name__icontains=query) | Q(category__name__icontains=query)
        )

    return render(request, 'core/search_results.html', {'results': results, 'query': query})



def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'core/product_detail.html', {'product': product})






# from django.shortcuts import render
# from .models import Banner, Category, Product
# from django.db.models import Q

# def index(request):
#     banners = Banner.objects.filter(is_active=True)  # get all active banners
#     popular_categories = Category.objects.filter(is_popular=True)
#     top_deals = Product.objects.filter(is_top_deal=True)
    
#     return render(request, 'core/index.html', {
#         'banners': banners,
#         'popular_categories': popular_categories,
#         'top_deals': top_deals,
#     })




# def home(request):
#     return render(request, 'core/index.html')


# # def index(request):
# #     return render(request, 'core/index.html')

# # def about(request):
# #     return render(request, 'core/about.html')

# # def contact(request):
# #     return render(request, 'core/contact.html')

# # def faq(request):
# #     return render(request, 'core/faq.html')

# # def terms(request):
# #     return render(request, 'core/terms.html')









# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from django.contrib import messages

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home') 
#         else:
#             messages.error(request, 'Username or Password wrong')

#     return render(request, 'core/login.html')






# def search_products(request):
#     query = request.GET.get('q')
#     results = []

#     if query:
#         results = Product.objects.filter(
#             Q(name__icontains=query) | Q(category__name__icontains=query)
#         )

#     return render(request, 'core/search_results.html', {'results': results, 'query': query})
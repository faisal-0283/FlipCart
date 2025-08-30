from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/customer/', views.signup_customer, name='signup_customer'),
    path('signup/seller/', views.signup_seller, name='signup_seller'),
    path('login/customer/', views.login_customer, name='login_customer'),
    path('login/seller/', views.login_seller, name='login_seller'),
   

    # Dashboard URLs
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/customer/', views.customer_home, name='customer_dashboard'),
    path('dashboard/seller/', views.seller_home, name='seller_dashboard'),
    
    
    # Logout for customer
    path('logout/', auth_views.LogoutView.as_view(next_page='login_customer'), name='logout'),

    # Logout for seller (optional)
    path('logout/seller/', auth_views.LogoutView.as_view(next_page='login_seller'), name='seller_logout'),


    
    # # Forgot password URLs
    # path('forgot-password/', views.forgot_password, name='forgot_password'),
    # path('reset-password/<str:email>/', views.reset_password, name='reset_password'),
]

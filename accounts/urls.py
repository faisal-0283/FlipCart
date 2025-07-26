from django.urls import path
from . import views

# app_name = 'accounts'

urlpatterns = [
    path('signup/customer/', views.customer_signup, name='signup_customer'),
    path('signup/seller/', views.seller_signup, name='signup_seller'),

    path('login/customer/', views.customer_login_view, name='customer_login'),
    path('login/seller/', views.seller_login_view, name='seller_login'),

    
]

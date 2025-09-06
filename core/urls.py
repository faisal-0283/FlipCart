from django.urls import path
from . import views
from core import views

app_name = 'core'

urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.home, name='home'), 
    path('search/', views.search_products, name='search'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('faq/', views.faq, name='faq'),
    # path('terms/', views.terms, name='terms'),
    # path('login/', views.user_login, name='login'),
     
]



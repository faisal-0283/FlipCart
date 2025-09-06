from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Product
from .models import CartItem
from django.contrib import messages

# Add to Cart
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f"{product.name} added to cart")
    return redirect('core:product_detail', product_id=product.id)


# View Cart
@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum([item.total_price() for item in cart_items])
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total': total})


# Remove item
@login_required
def remove_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    messages.success(request, "Item removed from cart")
    return redirect('cart:view_cart')


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('core:product_detail', product_id=product.id)















# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     if request.user.is_authenticated:
#         cart_item, created = CartItem.objects.get_or_create(
#             user=request.user,
#             product=product
#         )
#     else:
#         session_key = request.session.session_key
#         if not session_key:
#             request.session.create()
#             session_key = request.session.session_key
#         cart_item, created = CartItem.objects.get_or_create(
#             session_key=session_key,
#             product=product
#         )
#     if not created:
#         cart_item.quantity += 1
#     cart_item.save()
#     return redirect('cart:view_cart')




# def view_cart(request):
#     if request.user.is_authenticated:
#         cart_items = CartItem.objects.filter(user=request.user)
#     else:
#         session_key = request.session.session_key
#         if not session_key:
#             cart_items = []
#         else:
#             cart_items = CartItem.objects.filter(session_key=session_key)
#     total = sum([item.total_price() for item in cart_items])
#     return render(request, 'cart/view_cart.html', {'cart_items': cart_items, 'total': total})
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from cart.models import CartItem
# from .models import Order

# def checkout(request):
#     # যদি user login না থাকে
#     if not request.user.is_authenticated:
#         return redirect('login_customer')  # এখানে name='login_customer' ঠিক দিতে হবে

#     cart_items = CartItem.objects.filter(user=request.user)
#     if not cart_items:
#         messages.info(request, "Your cart is empty")
#         return redirect('cart:view_cart')

#     if request.method == 'POST':
#         for item in cart_items:
#             Order.objects.create(
#                 user=request.user,
#                 product=item.product,
#                 quantity=item.quantity,
#                 total_price=item.total_price()
#             )
#         cart_items.delete()
#         messages.success(request, "Order placed successfully!")
#         return redirect('login_customer')

#     total = sum([item.total_price() for item in cart_items])
#     return render(request, 'orders/checkout.html', {'cart_items': cart_items, 'total': total})



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Order
from django.contrib import messages

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        messages.info(request, "Your cart is empty")
        return redirect('cart:view_cart')

    if request.method == 'POST':
        for item in cart_items:
            Order.objects.create(
                user=request.user,
                product=item.product,
                quantity=item.quantity,
                total_price=item.total_price()
            )
        cart_items.delete()
        messages.success(request, "Order placed successfully!")
        return redirect('login_customer')

    total = sum([item.total_price() for item in cart_items])
    return render(request, 'orders/checkout.html', {'cart_items': cart_items, 'total': total})

from django.db import models
from django.contrib.auth import get_user_model
from core.models import Product

User = get_user_model()

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price

    # def __str__(self):
    #     return f"{self.user.username} - {self.product.name}"


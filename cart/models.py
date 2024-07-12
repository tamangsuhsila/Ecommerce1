from django.db import models
from account.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from product.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)
    
    def __str__(self):
        return self.user.username +" "+ str(self.total_price)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, blank=True, null=True)
    
    def __str__(self):
        return self.user.username +" "+ self.product.product_name
    
@receiver(pre_save, sender=CartItem)
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_product = Product.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
    total_cart_items = CartItem.objects.filter(user =cart_items.user)
    
    cart = Cart.objects.get(id=cart_items.cart.id)
    cart.total_price = cart.total_price + cart_items.price
    cart.save()
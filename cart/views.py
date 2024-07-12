from rest_framework.response import Response
from rest_framework import viewsets
from product.models import Product
from .models import Cart, CartItem
from  .serializers import CartSerializer, CartItemSerializer
from rest_framework.permissions import IsAuthenticated

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        user= request.user
        cart = Cart.objects.filter(user=user, order=False).first()
        queryset = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        cart, created= Cart.objects.get_or_create(user=user, order=False)
        product = Product.objects.get(id=data.get('product'))
        price = product.price
        quantity = data.get('quantity')
        cart_items= CartItem(cart=cart, user=user, product=product, price=price, quantity=quantity)
        cart_items.save()
        return Response({'message': 'Item added to cart'})
    
    def delete(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        cart_item = CartItem.objects.get(id=data.get('id'))
        cart_item.delete()
        cart = Cart.objects.filter(user=user, order=False).first()
        return Response({'message': 'Item removed from cart'})
    
    def put(self, request, *args, **kwargs):
        data= request.data
        cart_item = CartItem.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        return Response({'message': 'Item quantity updated'})
    
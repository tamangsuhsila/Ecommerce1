from rest_framework.response import Response
from rest_framework import viewsets
from product.models import Product
from .models import Cart, CartItem
from  .serializers import CartSerializer, CartItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status   

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
    
    def post(self, request, *args, **kwargs):
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user, order=False)
        
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        user = request.user
        cart = Cart.objects.filter(user=user, order=False).first()
        
        if cart:
            cart.delete()
            return Response({'message': 'Cart deleted successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No cart found'}, status=status.HTTP_404_NOT_FOUND)

    

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user, order=False).first()
        
        if not cart:
            return Response({"error": "No active cart found for user"}, status=status.HTTP_400_BAD_REQUEST)
        
        product_id = request.data.get('product')
        quantity = request.data.get('quantity')

        if not product_id or not quantity:
            return Response({"error": "Product and quantity are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            quantity = int(quantity)
        except ValueError:
            return Response({"error": "Quantity must be an integer"}, status=status.HTTP_400_BAD_REQUEST)

        cart_item = CartItem.objects.create(cart=cart, user=user, product=product, quantity=quantity)
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
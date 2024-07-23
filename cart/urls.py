from django.urls import path,include
from rest_framework import routers
from .views import CartViewSet, CartItemViewSet

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'cartitem', CartItemViewSet, basename='cartitem')

urlpatterns = [
    path('', include(router.urls))
]


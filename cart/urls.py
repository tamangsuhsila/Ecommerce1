from django.urls import path,include
from rest_framework import routers
from .views import CartViewSet

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'cartitem', CartViewSet, basename='cartitem')

urlpatterns = [
    path('', include(router.urls))
]


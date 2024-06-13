from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'posts', PostViewSet)
# router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
}), name='post'),

]


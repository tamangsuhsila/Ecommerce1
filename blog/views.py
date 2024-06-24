
from .models import Post
from .serializers import  PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.

# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    
    
class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
    
    
    def delete(self, request, pk= None):
        pk = request.data.get('id')
        Posts = get_object_or_404(Post, pk=pk)
        Posts.delete()
        return Response({ 'message':'Post deleted successfully'})
    
    def post(self, request, pk=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


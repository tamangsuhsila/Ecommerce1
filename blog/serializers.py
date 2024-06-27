
from rest_framework import serializers
from blog.models import  Post
from django.utils import timezone


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'
        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
        
        
    def validate(self, data):
        image = data.get('image')
        publish = data.get('publish')
        
        if image:
            # if image.size> 2*1024*1024:
            #     raise serializers.ValidationError("Image is too large.Maximum size is 2MB")
            if not image.name.endswith(('png','jpg','jpeg')):
                raise serializers.ValidationError("Image is not in correct format")
        
        if publish and publish.date() != timezone.now().date():
            raise serializers.ValidationError("Publish date must be today.")
        return data
        


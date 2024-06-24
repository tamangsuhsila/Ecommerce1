from rest_framework import serializers
from  branch.models import Branch, Review

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields='__all__'
        
        
    def validate(self, data):
        image = data.get('image')
        phone_number = data.get('phone_number')
        if image:
            if image.size> 2*1024*1024:
                raise serializers.ValidationError("Image is too large.Maximum size is 2MB")
            if not image.name.endswith(('png','jpg','jpeg')):
                raise serializers.ValidationError("Image is not in correct format")
    
        if len(str(phone_number)) != 10:
            raise serializers.ValidationError("Phone number must be 10 digits")
        return data
    
    
        
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'
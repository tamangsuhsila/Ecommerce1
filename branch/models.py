from django.db import models
# from django.contrib.auth.models import User


class Branch(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='static/branch', blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Review(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField() 
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rating
        # return  f"Review for {self.branch.name} - Rating: {self.rating}"
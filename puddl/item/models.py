from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)

    class Meta: 
        # ordering = ('name',)
        verbose_name_plural= 'Categories'
        
    
    def __str__(self):#to know the name in admin
        return self.name
    
class Item(models.Model):
    category= models.ForeignKey(Category, related_name='items',on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    description= models.TextField(blank=True, null=True)
    price= models.CharField(max_length=10)
    image=models.ImageField(upload_to='item_image',blank=True,null=True)
    is_sold=models.BooleanField(default=False)
    created_by=models.ForeignKey(User ,related_name='items',on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        # ordering = ('name',)
        verbose_name_plural= 'Item'
        
    def __str__(self):
            return f'Name::{self.name}, Category::{self.category}'
            
    
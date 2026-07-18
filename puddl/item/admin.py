from django.contrib import admin
from .models import Category,Item #importing categroy from models

# Register your models here.
admin.site.register(Category) 
admin.site.register(Item)

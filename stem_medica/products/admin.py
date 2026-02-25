from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Product, Category, Image

class ProductAdmin(ModelAdmin):
    list_filter = ('category', 'status')
    search_fields = ('model', 'brand')
    ordering = ('category',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Image)

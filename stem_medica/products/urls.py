from django.urls import path
from .views import publish_product, product_view, products_view, publish_category, category_view

urlpatterns = [
    path('publish/', publish_product, name='publish-product-page'),
    path('products/<int:pk>',product_view, name='product-page'),
    path('products/',products_view, name='products-page'),
    path('categories/',category_view, name='categories-page'),
    path('categories/<str:pk>',category_view, name='category-page'),
    path('publish-category/', publish_category, name='publish-category-page'),
    
]

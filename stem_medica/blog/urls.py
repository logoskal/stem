from django.urls import path
from .views import publish_blog, blog_view, blogs_view
urlpatterns = [
    path('publish/', publish_blog, name='publish-blog-page'),
    path('blogs/', blogs_view, name='blogs-page'),
    path('blogs/<int:pk>', blog_view, name='blog-page'),
    
]

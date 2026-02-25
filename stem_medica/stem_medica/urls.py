from .admin import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('config/', admin.site.urls, name='admin-page'),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('', include('users.urls')),
    path('', include('products.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
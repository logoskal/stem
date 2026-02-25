from django.urls import path
from django.contrib.auth.views import LoginView
from .views import logout

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login-page'),
    path('logout/', logout, name='logout-page')
]

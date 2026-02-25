from django.urls import path
from django.contrib.auth.views import LoginView
from .views import home, contact_us, about_us, download, download_link, latest_section

urlpatterns = [
    path('', home, name='home-page'),
    path('home/', home, name='home-page-redirect'),
    path('home/latest', latest_section, name='home-latest-page'),
    path('contact-us/', contact_us, name='contact-us-page'),
    path('about-us/', about_us, name='about-us-page'),
    path('download/', download, name='download-page'),
    path('download/<str:file_name>/', download_link, name='download-link')
]

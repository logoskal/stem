from django.shortcuts import render
from django.http import FileResponse, Http404
from products.models import Product, Category

import os
from django.conf import settings

product_list = Product.objects.all()
product_list_listed = list(product_list)
product_list_reverse = product_list.order_by('-id')


def home(request, ):
    return render(request, 'home/home.html',{'page_title':'Home','products':product_list.order_by('?'), 'categories': list(Category.objects.all()),'categories_active': Category.objects.all()[0:3],'categories_rest': Category.objects.all()[3:] })

def latest_section(request, ):
    return render(request, 'home/latest.html',{'page_title':'Home', 'products':product_list.order_by('-id'), 'categories': Category.objects.all(),'categories_active': Category.objects.all()[0:3],'categories_rest': Category.objects.all()[3:] })

def contact_us(request, ):
    return render(request, 'home/contact-us.html', {'page_title':'Contact Us'})

def about_us(request):
    return render(request, 'home/about-us.html', {'page_title':'About Us'})

def download(request):
        return render(request, 'home/download.html', {'page_title':'Download', 'products':product_list_listed, 'half':product_list_listed.__len__()//2})

def download_link(request, file_name):
    file_path = file_name
    
    if not os.path.exists(file_path):
        raise Http404('Requested File Not Found')
    
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'  # Optional: to force download
    return response


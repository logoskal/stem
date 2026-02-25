from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import ProductForm, ImageForm, CategoryForm
from .models import Image, Product, Category
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def publish_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        image_form = request.FILES.getlist('image') # Manually Processing the images

        if form.is_valid():
            form.save()

            for image in image_form:
                print('image')  
                Image.objects.create(product=form.instance,image=image)
        messages.success(request, 'Product Published', extra_tags='success')
        return redirect('products-page')
    else:
        return render(request, 'products/publish_product.html', {'page_title':'Publish','form': ProductForm, 'images': ImageForm()})

def products_view(request):
    query = request.GET.get('q', '')
    products = Product.objects.all()
    results = list(products)
    results.reverse()
    query = query.lower().strip(' /$\\=')   
    if query == '':
        pass
    else:
        results = []
        for product in products:
            if (product.status) and ((query in str(product.name).lower())) or (query in str(product.model).lower()) or (query in str(product.brand).lower()) or (query in str(product.description).lower()):
                results.append(product)
    return render(request, 'products/products.html', {'page_title':'Products','results': results})

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    category = product.category
    return render(request, 'products/product.html', context={'full_title':(str(product.brand) +' '+ str(product.model)[:15] + ' - Stem Medica'),'product':product, 'category': category})

def category_view(request, pk=''):
    query = pk.lower().strip(' /$\\=')   
    if query == '':
        return render(request, 'products/categories.html', {'results': Category.objects.all()})
    else:
        category = get_object_or_404(Category, pk=query)
        return render(request, 'products/category.html', {'full_title':category.name,'category': category})

@login_required
def publish_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        print(request.POST)
        print('\n CATEGORY FORM: \n')
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Published', extra_tags='success')
        return redirect('categories-page')
    
    else:
        return render(request, 'products/publish_category.html', {'page_title':'Add Category','form': CategoryForm})

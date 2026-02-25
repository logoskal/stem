from django.shortcuts import render
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import BlogForm
from .models import Blog
from django.contrib import messages
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required

@login_required
def publish_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        messages.success(request, 'Blog Published', extra_tags='success')
        return redirect('blogs-page')
    else:
        return render(request, 'blog/publish_blog.html', {'form': BlogForm, 'blog':Blog.objects.first()})
    
def blog_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.intro = (blog.intro).strip().replace('\n', '</p><p>')
    blog.content_1 = (blog.content_1).strip().replace('\n', '</p><p>')
    blog.content_2 = (blog.content_2).strip().replace('\n', '</p><p>')
    return render(request, 'blog/blog.html', {'blog' : blog})

def blogs_view(request):
    blogs = (Blog.objects.all()).reverse()
    return render(request, 'blog/blogs.html', {'blogs' : blogs, 'last':Blog.objects.last()})



def download_link(request, file_name):
    file_path = file_name
    
    if not os.path.exists(file_path):
        raise Http404('Requested File Not Found')
    
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'  # Optional: to force download
    return response


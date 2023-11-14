from django.shortcuts import render
from blog.models import Post
#not the same folder, can't use .models
# Create your views here.

def frontpage(request):
    posts = Post.objects.all()
    return render(request,"core/frontpage.html", {'posts':posts})

def about(request):
    return render(request,"core/about.html")

def cssgrid(request):
    return render(request,"core/cssgrid.html")

def bootstrap(request):
    return render (request,"core/bootstrap.html")
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from django.core.paginator import Paginator
from faker import Faker

# Create your views here.

def home(request):
    blogs = Blog.objects

    blog_lists = Blog.objects.all()
    paginator = Paginator(blog_lists, 3)
    pages = request.GET.get('page')
    page = paginator.get_page(pages)

    return render(request,'blog/home.html', { 'blogs' : blogs , 'page' : page })

def about(request):
    return render(request, 'blog/about.html')

def search(request):
    search_word = request.GET['searching']
    return render(request, 'blog/search.html', {'searching_W' : search_word})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog' : blog_detail})

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['content']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def new_faker(request) :
    blog = Blog()
    myfaker = Faker()
    blog.title = myfaker.word()
    blog.body = myfaker.sentence()
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

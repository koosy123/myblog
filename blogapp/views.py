from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog

def home(request):
    blogs = Blog.objects #쿼리셋
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html',{'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request,'detail.html',{'details':details})

def new(request): # new.html 띄워주는 함수
    return render(request,'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

from django.shortcuts import render
from blog.models import Post, Category
from django.http import HttpResponse
from django.db.models import Q, Count

def index(request):
    return render(request, 'cyberkernel/index.html', {'posts': Post.objects.all()[:4], 'categories': Category.objects.all()[:4], 'trendings': Post.objects.order_by('-view')[:4]})

def trending(request):
    return render(request, 'cyberkernel/trending.html', {'blogs': Post.objects.order_by('-view')[:20]})

def category(request):
    a = Post.objects.values('auther').annotate(num_blogs=Count('category'))
    print(a)
    return render(request, 'category/category.html', {'categories': Category.objects.all()})

def category_title(request, title):
    category = Category.objects.get(title=title)
    blogs = Post.objects.filter(category=category.id)
    return render(request, 'category/category_title.html', {'category': category, 'blogs': blogs})

def search(request):
    query = request.GET['query']
    objs = Post.objects.filter(Q(title__icontains=query) | 
                            Q(description__icontains=query) | 
                            Q(content__icontains=query)).distinct()
    return render(request, 'cyberkernel/search.html', {'objs': objs, 'query': query})
    

def about(request):
	return HttpResponse('about page')
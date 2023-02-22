from django.shortcuts import render, redirect
from blog.models import Post, Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import  messages
from blog.forms import PostForm
from django.http import Http404

import logging
from cyberkernel.settings import DEBUG

logger = logging.getLogger('CyberKernel')
logger.setLevel(logging.DEBUG) if DEBUG else logger.setLevel(logging.WARNING)
fh = logging.FileHandler('logs/cyberkernel.log')
formatter = logging.Formatter(
	'[*] {asctime} :: {name} :: {filename} :: {funcName} :: {lineno} :: {levelname:<8} {message}', style='{'
	)
fh.setFormatter(formatter)
logger.addHandler(fh)


def index(request):
    return render(
    	request,
    	'cyberkernel/index.html',
    	{
    	'posts':Post.objects.all()[:4],
    	'categories':Category.objects.all()[:4],
    	'trendings': Post.objects.order_by('-view')[:4]
    	}
    )

def trending(request):
    return render(request, 'cyberkernel/trending.html', {'blogs': Post.objects.order_by('-view')[:20]})

def category(request):
    return render(request, 'category/category.html', {'categories': Category.objects.all()})

def category_title(request, title):
    try:
    	category = Category.objects.get(title=title)
    	blogs = Post.objects.filter(category=category.id)
    	return render(request, 'category/category_title.html', {'category': category, 'blogs': blogs})
    except Exception as e:
    	logger.error(f'Exceptiom occur IP:{request.META.get("REMOTE_ADDR")} {e}')
    	raise Http404()

def search(request):
    query = request.GET['query']
    objs = Post.objects.filter(Q(title__icontains=query) | 
                            Q(description__icontains=query) | 
                            Q(content__icontains=query)).distinct()
    return render(request, 'cyberkernel/search.html', {'objs': objs, 'query': query})
    



@login_required	
def post(request):
	if not request.user.is_auther:
		logger.warning(f'Non auther user trying to access post route IP:{request.META.get("REMOTE_ADDR")} USER:{request.user}')
		messages.info(request,
			'Only authers can post'
		)
		return redirect('index')
	if request.method == 'POST':
		data = PostForm(request.POST, request.FILES)
		if data.is_valid():
			data.save(commit=False)
			data.auther = request.user
			data.save()
			messages.success(request, 
			'Blog added successfuly')
		else:
			messages.warning(request,
			'Data is not valid')
	return render(request, 'cyberkernel/post.html',{
		'form': PostForm()
	})


'''
	All errors zone
'''	
def error_404(request, exception):
	return render(request, '404.html')
from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.db.models import F

import logging
from cyberkernel.settings import DEBUG

logger = logging.getLogger('Blog')
logger.setLevel(logging.DEBUG) if DEBUG else logger.setLevel(logging.WARNING)
fh = logging.FileHandler('logs/blog.log')
formatter = logging.Formatter(
	'[*] {asctime} :: {name} :: {filename} :: {funcName} :: {lineno} :: {levelname:<8} {message}', style='{'
	)
fh.setFormatter(formatter)
logger.addHandler(fh)


# Create your views here.
def blog_index(request):
    return render(request, 'blog/blog_index.html', {'blogs': Post.objects.all().order_by('-upload_date')[:20]})

def blog(request, slug):
    obj = Post.objects.filter(slug=slug)[0]
    if obj is not None:
        obj.view = F('view') + 1
        obj.save()
        return render(request, 'blog/blog.html', {'post': obj, 'blogs': Post.objects.all()[:5]})
    else:
        logger.warning(f'Blog not exists IP:{request.META.get("REMOTE_ADDR")} for SLUG:{obj}')
        raise Http404()
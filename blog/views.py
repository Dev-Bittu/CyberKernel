from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.db.models import F

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
        raise Http404()
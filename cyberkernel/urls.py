"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from about import views as about_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('blog/', include('blog.urls')),
    path('account/', include('account.urls')),
    path('trending/', views.trending, name='trending'),
    path('category/', views.category, name='category'),
    path('category/<slug:title>', views.category_title, name='category_title'),
    path('search/', views.search, name='search'),
    path('about/', about_views.about, name='about'),
    path('terms-and-conditions', about_views.terms_and_conditions, name='terms&conditions'),
    path('help-and-feedback', about_views.help_and_feedback, name='help&feedback'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'cyberkernel.views.error_404'
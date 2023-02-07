from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('setting/', views.setting, name='setting'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/', views.profile, name='profile'),
]
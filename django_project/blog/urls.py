from django.urls import path  # importing path from urls (copied this from urls of main project)
from . import views   # importing views 

urlpatterns = [
    path('', views.home, name='blog-home'),  # defining the path for this app ('' means "home page"  and this will direct to views.home(home function of views) which has given name = blog-home)
    path('about/', views.about, name='blog-about'),
]
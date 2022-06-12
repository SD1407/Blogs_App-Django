"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include  # here we are importing include which is imp for including that 'blogs/path'
 # here we could have created urls for that users app specifically and could have called it like other apps(blog, home page) but her we are importing its views and redirecting it through a different method
from users import views as user_views  # importing views of users as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),  # here redirecting it to view section and using the register function there
    path('', include('blog.urls')),  # here we are giving the path as 'blog/' if we enter blog thne this will redirect to that "blog/urls" and there "" means home will be called
    
]

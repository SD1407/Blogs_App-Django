from django.contrib import admin
from .models import post

# Register your models here.
# we need to register our models in admin site to access that from admin page for that we need to import 'post' from models and also register it
admin.site.register(post)  # now admin page wil have 'post' table 

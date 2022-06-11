from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# here in models section we can use django build in model class to create models for to store and use for our database
class post(models.model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)



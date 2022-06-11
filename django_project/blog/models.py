from email.policy import default
from django.db import models
from django.utils import timezone  # this will import the timezone
from django.contrib.auth.models import User # this will import the user(author here)


# remember we need to run makemigrations cmd to create files in mirations folder and need to use migrate cmd to create the models in database
# this the date base structure
# here in models section we can use django build in model class to create models for to store and use for our database
class post(models.Model):  # here we are using django inbuilt models and we can create tables which will crearte fields where we can store data from admin page and can use them
    title = models.CharField(max_length=100)  # models.CharField (this is ig predefined django class)
    content = models.TextField()  # test field is for long texts
    date_posted = models.DateTimeField(default=timezone.now)  # date and time field (here wehave pass an argument which will let us fill the date and time and also if we forget to pass then that will fill the space automatically also)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # we imported that user table which we are passing as an argument (on_delete=models.CASCADE  this implies that id we dlt the author then it will dlt that post also)
    # as the author is unique for each post but an author can have multiple posts (for this in django we have this ForeignKey)

    def __str__(self):
        return self.title  # here we use double underscore(_) method (which we use in OOP python, can check this out later) this makes sure that the posts will be displayed by their title only(as we have modified here we need to exit() 'pyhton shell' then we can use this change)



from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model) :
    title = models.CharField(max_length=100)
    content = models.TextField()
    # There are couple options to store date_posted in the database
    #   - (auto_now=True) stores current time whenever the post is created and updated.
    #   - (auto_now_add=True) stores current time when the post object is constructed.
    #   - (default=timezone.now): the 'default' takes a function, not the function value.
    #        So not attach (). 
    date_posted = models.DateTimeField(default=timezone.now)
    # on_delete tells Django to delete the posts once the User is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # this will be called when printing the post
    def __str__(self) :
        return self.title

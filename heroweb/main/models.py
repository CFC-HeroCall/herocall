from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# This is a model for the posts
# Every post has a title, a text, an author and it can be a reply to a tab from a specific post
class Post(models.Model):
    title = models.CharField(max_length=120)
    text = models.CharField(max_length=2000)

    # The author is a model from the User models (It is a default from Django)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    # A post doesnt have to be a reply, so these two fields can be null
    reply_post = models.IntegerField(null=True)
    reply_tab = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.author.username} --> {self.title}'

# Every tab has a title, a text, and it is conatined within a specific post
class Tab(models.Model):
    title = models.CharField(max_length=120)
    text = models.CharField(max_length=2000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title} --> {self.title}'
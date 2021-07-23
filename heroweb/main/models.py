from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    text = models.CharField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    reply_post = models.IntegerField(null=True)
    reply_tab = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.author.username} --> {self.title}'

class Tab(models.Model):
    title = models.CharField(max_length=120)
    text = models.CharField(max_length=2000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title} --> {self.title}'
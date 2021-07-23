from django.shortcuts import render
from main.models import Post, Tab

# Create your views here.
def home(request):
    return render(request, 'index.html')

def explore(request):
    post = Post.objects.all()[0]
    tabs = Tab.objects.all().filter(post=post)
    content = {
        'post':post,
        'tabs':tabs
    }
    return render(request, 'explore.html', content)
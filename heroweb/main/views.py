from django.shortcuts import render
from main.models import Post, Tab

# Create your views here.
def home(request):
    return render(request, 'index.html')

def explore(request):
    post = Post.objects.all()[0]
    replies_raw = Post.objects.all().filter(reply=post.id)
    views = []
    i = 0
    for reply in replies_raw:
        if i % 2 == 0:
            views.append([reply])
        else:
            views[len(views)-1].append(reply)
        i += 1

    print(views)
    tabs = Tab.objects.all().filter(post=post)
    content = {
        'post':post,
        'tabs':tabs,
        'views':views
    }
    return render(request, 'explore.html', content)
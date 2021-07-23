from django.shortcuts import render, redirect
from django.contrib import messages
from main.models import Post, Tab
from main.forms import PostCreationForm

# Create your views here.
def home(request):
    # Access the posts that aren't replies to another post
    posts = Post.objects.all().filter(reply_post=None)
    content = {
        'posts':posts,
    }
    return render(request, 'index.html', content)

def explore(request):
    # Access the first post for showing purposes
    post = Post.objects.all()[0]
    # Let's create a list of all the posts that have a as a reply the one that we are looking at
    replies_raw = Post.objects.all().filter(reply_post=post.id)
    views = []
    i = 0

    # For creates a view of 2 posts to show. So it is a list of lists of 2 posts each
    for reply in replies_raw:
        if i % 2 == 0:
            views.append([reply])
        else:
            views[len(views)-1].append(reply)
        i += 1

    # Access all the tabs for that post
    tabs = Tab.objects.all().filter(post=post)
    content = {
        'post':post,
        'tabs':tabs,
        'views':views
    }
    return render(request, 'explore.html', content)

def post(request, id):
    #Same as explore, but getting the id of the post that the user is looking at.
    # This id is obtained from the url (the id variable)
    post = Post.objects.all().get(id=id)
    posts = Post.objects.all()
    replies_raw = Post.objects.all().filter(reply_post=post.id)
    views = []
    i = 0
    for reply in replies_raw:
        if i % 2 == 0:
            views.append([reply])
        else:
            views[len(views)-1].append(reply)
        i += 1

    tabs = Tab.objects.all().filter(post=post)
    content = {
        'post':post,
        'posts':posts,
        'tabs':tabs,
        'views':views
    }
    return render(request, 'post.html', content)

def make_post(request):
    if request.method == "POST":
        #Access the form through the request object
        form = PostCreationForm(request.POST)
        #If valid, save
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            #Tell the user that the registration was succesful. This will be functional later on
            messages.success(request, f"Post created succesfully")
            #Redirect to the login page
            return redirect("home")
    
    #If not, we only show the form to the user
    else:
        form = PostCreationForm()

    return render(request, 'make_post.html', {'form':form})
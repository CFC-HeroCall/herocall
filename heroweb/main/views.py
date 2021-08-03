from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.models import Post, Tab
from main.forms import PostCreationForm

# Create your views here.
def home(request):
    # Access the posts that aren't replies to another post
    posts = Post.objects.all().filter(reply_tab=None)
    content = {
        'posts':posts,
    }
    return render(request, 'index.html', content)

def test(request):
    return render(request, 'test.html')

def explore(request):
    posts_raw = Post.objects.all().filter(reply_tab=None)
    indeces = list(range(len(posts_raw)))
    indeces.reverse()
    posts = []

    for index in indeces:
        posts.append(posts_raw[index])

    return render(request, 'explore.html', {'posts':posts})

def post(request, id):
    # Same as explore, but getting the id of the post that the user is looking at.
    # This id is obtained from the url (the id variable)
    main_post = Post.objects.all().get(id=id)
    posts = Post.objects.all()

    tabs = Tab.objects.all().filter(post=main_post)
    content = {
        'main_post':main_post,
        'posts':posts,
        'tabs':tabs,
    }
    return render(request, 'post.html', content)

def delete_post(request):
    main_post = Post.objects.all().get(id=request.GET['post_id'])
    main_post.delete()

    messages.success(request, f"Post deleted succesfully")
    return redirect(request.GET['location'])

@login_required
def make_post(request):
    if request.method == "POST":
        #Access the form through the request object
        form = PostCreationForm(request.POST)
        ntabs = int(request.POST['indicator'])
        try:
            reply_tab = request.POST['reply']
        except:
            reply_tab = None

        tabs = []
        for tab in range(ntabs):
            print(f'Tab {tab}:')
            if tab == 0:
                tab = ''
            title = request.POST[f'tab_title{tab}']
            content = request.POST[f'tab_text{tab}']
            print(title)
            print(content)
            tabs.append({
                'title':title,
                'content':content
            })

        #If valid, save
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.reply_tab = reply_tab
            post.save()
            for tab in tabs:
                new_tab = Tab(title=tab['title'], text=tab['content'], post=post)
                new_tab.save()

            #Tell the user that the registration was succesful. This will be functional later on
            messages.success(request, f"Post created succesfully")
            #Redirect to the login page
            if reply_tab != None:
                return_post = Tab.objects.all().get(id=reply_tab).post.id
                print(return_post)
                print(Tab.objects.all().get(id=reply_tab))
                return redirect("post", return_post)
            else:
                return redirect("home")
    
    #If not, we only show the form to the user
    else:
        form = PostCreationForm()
        try:
            reply = request.GET['reply']
            contents = {
                'form':form,
                'reply':reply
            }
        except:
            contents = {
                'form':form,
            }


        

    return render(request, 'make_post.html', contents)
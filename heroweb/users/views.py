from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm

# Create your views here.

#Registration response
def register(request):
    #If it was accesed through POST method then we have to check the information and store
    if request.method == "POST":
        #Access the form through the request object
        form = UserRegisterForm(request.POST)
        #If valid, save
        if form.is_valid():
            form.save()
            #Tell the user that the registration was succesful. This will be functional later on
            messages.success(request, f"Account created. Now you can login")
            #Redirect to the login page
            return redirect("login")
    
    #If not, we only show the form to the user
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form':form})

#If the user is not logged in, Django will redirect the user to the login page and then get back here.
# The @ is a decorator. Pretty complex stuff, not even sure how they work. I think that
# allows to add a function to whatever is next to the @. So in this case we are adding profile to login_required, which
# is defined by Django
# But don't worry too much about it, it is an advanced topic
@login_required
def profile(request):
    #If it was accesed through POST method then we have to check the information and store
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        # If valid, save it
        if form.is_valid():
            form.save()
            #Tell the user that the update was succesful. This will be functional later on
            messages.success(request, "Account updated")
            # Redirect to the profile page again so the post method gets back to a get method. This fixes the typicalerror when
            # subitting a form and refreshing the page "Are you sure you want to submit the information again?"
            return redirect("profile")

    # We just show the form
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        "form": form,
    }

    return render(request, "profile.html", context)

def mock_home(request):
    return render(request, 'mock_home.html')
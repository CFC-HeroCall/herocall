from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

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
"""heroweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from users.views import register, mock_home, profile
from main.views import home, explore, post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    #The url for the example to show
    path('explore/', explore, name="explore"),

    # The view for any post. It accepts an argument in the url: the post id
    # This allows to show the specific post that the user clicked on
    path('post/<int:id>/', post, name="post"),


    #This is just a mock version of a home page for me to test the redirection functionalities
    path('create_account/', register, name="create_account"),

    #That is an automatic view done by Django. I'm only defining the file that it has to redirect to
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),

    # Same as login but for loggin out
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('profile/', profile, name="profile"),
    
    # PASSWORD RESET
    # Automatic view for password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='pass_reset/password_reset.html'),
        name="password_reset"),
    # Automatic view for password done sending the email
    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='pass_reset/password_reset_done.html'),
        name="password_reset_done"),
    #Confirmation of password reset. This is the page that the link emailed takes to
    # The <> things are placeholders. They are the key and the token that Django provides for security. It's
    # automatically done by the view
    path('password_reset_confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='pass_reset/password_reset_confirm.html'),
        name="password_reset_confirm"),
    # Reset completed page
    path('password_reset_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='pass_reset/password_reset_complete.html'),
        name="password_reset_complete"),
]

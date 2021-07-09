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

urlpatterns = [
    path('admin/', admin.site.urls),
    #This is just a mock version of a home page for me to test the redirection functionalities
    path('mock_home/', mock_home, name="home"),
    path('create_account/', register, name="create_account"),
    #That is an automatic view done by Django. I'm only defining the file that it has to redirect to
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    # Same as login but for loggin out
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('profile/', profile, name="profile"),
]

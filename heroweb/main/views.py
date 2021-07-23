from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def explore(request):
    return render(request, 'explore.html')
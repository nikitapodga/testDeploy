from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def error404(request):
    return render(request, '404.html')

def about(request):
    return render(request, 'about.html')

def addtocart(request):
    return render(request, 'add-to-cart.html')

def men(request):
    return render(request, 'men.html')

def single(request):
    return render(request, 'single.html')

def women(request):
    return render(request, 'women.html')

def reglogin(request):
    return render(request, 'login.html')

def reglogout(request):
    return render(request, 'logged_out.html')
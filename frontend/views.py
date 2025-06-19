from django.shortcuts import render

# Create your views here.

def register_user(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request,"register.html")
        User.objects.create_user(username=username,password=password)
    return render(request,"register.html")
from django.contrib.auth.models import User    

def index(request):
    return render(request,"index.html")
from backend.models import productTable
def products(request):
    data=productTable.objects.all()
    return render(request,"products.html",{"data":data})
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
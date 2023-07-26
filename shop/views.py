from django.shortcuts import render
from shop.models import Category
from shop.models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q

def allProdCat(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})
def allproducts(request,cslug):
    c   =Category.objects.get(slug=cslug)
    p=Product.objects.filter(category__slug=cslug)
    return render(request, 'products.html', {'p': p,'c':c})
def prodetail(request,pslug):
    p = Product.objects.get(slug=pslug)
    return render(request, 'detail.html', {'p': p})
def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return allProdCat(request)
        else:
            messages.error(request,"invalid Credentials")
    return render(request,'login.html')
def user_logout(request):
    logout(request)
    return allProdCat(request)
def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        p = request.POST['p']
        cp = request.POST['cp']
        if p==cp:
            user = User.objects.create_user(username=u,first_name=f, last_name=l, email=e, password=p)
            user.save()
            return allProdCat(request)
    return render(request,'register.html')


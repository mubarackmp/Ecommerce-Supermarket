
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import MainCatogory, ProdCatogory, Products, CartItem
from .form import *



def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        if password1 == password2:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'username alreadt exists!!!')
                print("already have")
                return redirect('SuperMarket1:user_signup')
            else:
                new_user=User.objects.create_user(username,email,password1)
                new_user.save()
                return redirect('SuperMarket1:user_login')
        else:
            print('wrong password')
    return render(request,'signup.html')

def user_logine(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass1')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('SuperMarket1:all_products')
        else:
            messages.info(request,'user not exist')
            print('user not exist')
            return redirect('SuperMarket1:user_login')
    return render(request,'login.html')  

def user_logout(request):
    logout(request)
    return redirect('SuperMarket1:user_login')


def all_products(request):
	catogory = MainCatogory.objects.all()
	products = Products.objects.all()
	return render(request, 'index.html', {'products': products, 'catogory':catogory})

def Main_catogory_product_list(request, mc_id):
    catogory = MainCatogory.objects.all()
    mcatogorye = MainCatogory.objects.get(id=mc_id)
    pcatogorye = ProdCatogory.objects.filter(maincatogory=mcatogorye)
    productse = []
    for item in pcatogorye:
        products = Products.objects.filter(prodcatogory=item)
        productse += products
    return render(request, 'mainitemse.html', {'products': productse,'cate':mcatogorye, 'catogory':catogory, 'pcatogory':pcatogorye})


def Prod_catogory_product_list(request, pc_id):
    catogory = MainCatogory.objects.all()
    catogorye = ProdCatogory.objects.all()
    pcatogorye = ProdCatogory.objects.get(id=pc_id)
    products = Products.objects.filter(prodcatogory=pcatogorye)
    print(products)
    return render(request, 'proditemse.html', {'products': products,'cate':pcatogorye, 'catogory':catogory, 'pcatogory':catogorye})   

def itempage(request, p):
	prod = Products.objects.get(id=p)
	return render (request,'itempage.html',{'products':prod})

def view_cart(request):
    catogory = MainCatogory.objects.all()
    catogorye = ProdCatogory.objects.all()
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'catogory':catogory, 'pcatogory':catogorye})

def add_to_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity +=1
    cart_item.save()
    return redirect('SuperMarket1:view_cart')

def remove_from_cart(request, item_id):
	cart_item = CartItem.objects.get(id=item_id)
	cart_item.delete()
	return redirect('SuperMarket1:view_cart')

def remove_one_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.quantity -= 1
    cart_item.save()
    return redirect('SuperMarket1:view_cart')


def addMainCat(request):
    a=MainCatForm()
    if request.method == 'POST':
        a=MainCatForm(request.POST)
        if a.is_valid():
            a.save()
    return render(request,'cmcat.html',{'f1':a})

def addProdCat(request):
    b = ProdCatForm()
    if request.method == 'POST':
        b=ProdCatForm(request.POST)
        if b.is_valid():
            b.save()
    return render(request,'cpcat.html',{'f2':b})

def addProducts(request):
    c=ProductForm()
    if request.method == 'POST':
        c=ProductForm(request.POST,request.FILES)
        if c.is_valid():
            c.save()
    return render(request,'cpd.html',{'f3':c})

def storeroom(request):
    users =User.objects.all()
    MaCat = MainCatogory.objects.all()
    PrCat = ProdCatogory.objects.all()
    products = Products.objects.all()

    return render(request,'storeroom.html',{'u':users, 'm':MaCat, 'p':PrCat, 'pro':products})

def search(request):
    if request.method == 'POST':
        s=request.POST.get('search')
        if Products.objects.filter(ptype=s).exists():
           a = Products.objects.get(ptype=s)
           return render(request,'itempage.html',{'products':a})
        elif ProdCatogory.objects.filter(name=s).exists():
            a = Products.objects.filter(prodcatogory=s)
            return render(request,'itempage.html',{'prod':a})
        elif MainCatogory.objects.filter(name=s).exists():
            aa = MainCatogory.objects.get(name=s)
            pcatogorye = ProdCatogory.objects.filter(maincatogory=aa)
            for item in pcatogorye:
                c = Products.objects.filter(prodcatogory=item)
            return render(request,'itempage.html',{'prod':c})
        else:
            return redirect('SuperMarket1:all_products')      
    else:
         return redirect('SuperMarket1:all_products')



def Prodsearch(request):
    if request.method == 'POST':
        s=request.POST.get('search')
        if Products.objects.filter(ptype=s).exists():
           a = Products.objects.get(ptype=s)
           return render(request,'searchprodect.html',{'products':a})
        elif ProdCatogory.objects.filter(name=s).exists():
            a = Products.objects.filter(prodcatogory=s)
            return render(request,'searchprodect.html',{'products':a})
        elif MainCatogory.objects.filter(name=s).exists():
            aa = MainCatogory.objects.get(name=s)
            pcatogorye = ProdCatogory.objects.filter(maincatogory=aa)
            for item in pcatogorye:
                c = Products.objects.filter(prodcatogory=item)
            return render(request,'searchprodect.html',{'products':c})
        else:
            return redirect('SuperMarket1:storeroom')      
    else:
         return redirect('SuperMarket1:storeroom')

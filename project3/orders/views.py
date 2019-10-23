import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q
from .models import Product, Type

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request,"login.html",{"message": None})
    else:
    
        context = {
            "user": request.user,
            "regular_pizzas_small": Product.objects.filter(Q(detailproducttype__type__name='Regular Pizza') & Q(detailproducttype__size='small')).values('id','name','detailproducttype__price'),
            "regular_pizzas_large": Product.objects.filter(Q(detailproducttype__type__name='Regular Pizza') & Q(detailproducttype__size='large')).values('id','name','detailproducttype__price'),
            "sicilian_pizzas_small": Product.objects.filter(Q(detailproducttype__type__name='Sicilian Pizza') & Q(detailproducttype__size='small')).values('id','name','detailproducttype__price'),
            "sicilian_pizzas_large": Product.objects.filter(Q(detailproducttype__type__name='Sicilian Pizza') & Q(detailproducttype__size='large')).values('id','name','detailproducttype__price'),
            "toppings": Product.objects.filter(detailproducttype__type__name='Toppings'),
            "subs_small": Product.objects.filter(Q(detailproducttype__type__name='Subs') & Q(detailproducttype__size='small')).values('id','name','detailproducttype__price'),
            "subs_large": Product.objects.filter(Q(detailproducttype__type__name='Subs') & Q(detailproducttype__size='large')).values('id','name','detailproducttype__price'),
            "pastas": Product.objects.filter(detailproducttype__type__name='Pasta').values('id','name','detailproducttype__price'),
            "salads": Product.objects.filter(detailproducttype__type__name='Salads').values('id','name','detailproducttype__price'),
            "dinner_platters_small": Product.objects.filter(Q(detailproducttype__type__name='Dinner Platters') & Q(detailproducttype__size='small')).values('id','name','detailproducttype__price'),
            "dinner_platters_large": Product.objects.filter(Q(detailproducttype__type__name='Dinner Platters') & Q(detailproducttype__size='large')).values('id','name','detailproducttype__price')
        }
        

        return render(request,"menu.html", context)




def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "login.html", {"message": "Invalid credentials"})

def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logget out"})


def register_view(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password_again = request.POST["password_again"]
        if not password == password_again:
            return render(request, "register.html", {"message": "Password don't match"})
        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        return render(request, "login.html", {"message": "Account created succesfully"})
    else:
        return render(request, "register.html")


def my_orders(request):
    if request.is_ajax() and request.POST:
        #get_value = request.body
        #print(get_value)
        #print(type(get_value))
        #n.loads(request.POST.get('data', ''))
        #print(data)
        data = json.loads(request.POST.get('data'))
        print(data)
        print(type(data))
        return JsonResponse({"success":True},status=200)
    else:
        if request.method == "GET":
            return render(request,"my_orders.html")
    
        

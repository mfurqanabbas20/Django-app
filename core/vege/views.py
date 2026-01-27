from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# login maintains the session while authenticate user

# Create your views here.

@login_required(login_url="/login/")
def receipes(request):
    if request.method == "POST":
        data = request.POST
        # print("Name", data["receipe_name"])
        file = request.FILES["receipe_image"]
        # print(file,"*"*5)
        # or 
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")
        print("Receipe_image", receipe_image)

        print("Description", data["receipe_description"])
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )
        return redirect('/vege/')
    
    return render(request, 'receipes.html')


# vege = Receipe.objects.all().order_by('receipe_view_count') asc
# vege = Receipe.objects.all().order_by('-receipe_view_count') minus for desc
# vege = Receipe.objects.all().order_by('-receipe_view_count')[0:10] for limit

# vege = Receipe.objects.filter(receipe_view_count = 55) for filtering

# double underscore special string hota 

# gte, lte,

# vege = Receipe.objects.filter(receipe_view_count__gte = 55) for filtering greater

# vege = Receipe.objects.filter(receipe_view_count__lte = 55) for filtering less

# queryset = Student.objects.filter(student_name__startswith = "fur")

# queryset = Student.objects.filter(student_name__endswith = "qan")

# queryset = Student.objects.filter(student_name__icontains = "a")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("user_name")
        password = request.POST.get("password")


    if not User.objects.filter(username=username).exists():
        messages.info(request, 'Username not exists')
        return redirect("/login/")
    
    user = authenticate(username=username, password=password)

    if user is None:
        messages.info(request, 'Invalid login credentials')
        return redirect("/login/")
    
    else:
        login(request, user)

    return render(request, "login.html")

def logout_page(request):
    logout()
    return redirect("/login/")

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("user_name")
        password = request.POST.get("password")
    
    user = User.objects.filter(username = username)

    if user.exists():
        messages.info(request, 'Username already taken')
        return redirect("/register/")

    user = User.objects.create(
        first_name,
        last_name,
        username,
    )
    # this is to encrypt the password
    user.set_password(password)

    user.save()


    return render(request, "login.html")
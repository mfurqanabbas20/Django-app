from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


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


def login_page(request):
    return render(request, "login.html")

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
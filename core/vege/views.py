from django.shortcuts import render, redirect
from .models import *

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
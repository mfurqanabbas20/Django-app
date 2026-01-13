from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
       <h1 style="color: red">Hey, I am a Django Server</h1>
    """)

def success_page(request):
    # data hm context k zariya phonchaiyein gaye template mei 
    peoples = [
        {"name": "Furqan", "age": 22},
        {"name": "Furqan", "age": 21},
        {"name": "Furqan", "age": 20},
    ]
    return render(request, "index.html", context={"peoples": peoples})

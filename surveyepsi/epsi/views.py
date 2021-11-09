from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def home(request):
    print("select.html")



    return render(request, "survey/select1.html")

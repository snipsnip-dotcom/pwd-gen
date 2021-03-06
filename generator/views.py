from django.shortcuts import render
#render from django allows to import templates
from django.http import HttpResponse
import random
# create your views here.

def home(request):
    return render (request,'generator/home.html')

def password(request):
    
    characters=list("abcdefghijklmnopqrstuvwxyz")
    thepassword=""
    length= int((request.GET.get("length",12)))
    # 12 is the default value

    if request.GET.get("uppercase"):
       characters.extend(list("abcdefghijklmnopqrstuvwxyz"))

    if request.GET.get("spl characters"):
        characters.extend(list("!@#$%^&*()"))

    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))
    
    for x in range(length):
        thepassword += random.choice(characters)


    return render(request,'generator/password.html',{"password":thepassword})

def about(request):
    return render(request, "generator/about.html")

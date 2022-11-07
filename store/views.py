from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import *
from django.contrib.auth import authenticate, login as logina, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    template = loader.get_template('index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('login.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def carro(request):
    template = loader.get_template('carro.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def platerak(request):
    template = loader.get_template('platerak.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def mariscadas(request):
    template = loader.get_template('mariscadas.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def bebidas(request):
    template = loader.get_template('bebidas.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def platerak(request):
  myprodu = Produktua.objects.all().values()
  template = loader.get_template('platerak.html')
  context = {
    'myprodu': myprodu,
  }
  return HttpResponse(template.render(context, request))

def bebidas(request):
  myprodu = Produktua.objects.all().values()
  template = loader.get_template('bebidas.html')
  context = {
    'myprodu': myprodu,
  }
  return HttpResponse(template.render(context, request))

def mariscadas(request):
  myprodu = Produktua.objects.all().values()
  template = loader.get_template('mariscadas.html')
  context = {
    'myprodu': myprodu,
  }
  return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template('register.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def createuser(request):
    if request.method == 'POST':
        izena= request.POST["izena"]
        email = request.POST["email"]
        passw = request.POST["pass"]
        confpass = request.POST["confpass"]
        if passw == confpass:
            hasha = make_password(passw)
            user = User(username=izena, email=email, password=hasha)
            user.save()
            erab = Erabiltzailea(izena=izena,erabitlzailea_id=user)
            erab.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return redirect("/register")
          
@csrf_exempt
def hasisaioa(request):
  if request.method == 'POST':
    username = request.POST['izena']
    password = request.POST['pass']
    user = authenticate(request, username = username, password = password)
    if user is not None:
        logina(request, user)
        messages.info(request, f"You are now logged in as {username}")
        return redirect('/')
    else:
        messages.error(request, "Invalid username or password.")
        return redirect('/')
     

def amaitusaioa(request):
  logout(request)
  return redirect("index")
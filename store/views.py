from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def carro(request):
    template = loader.get_template('carro.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())


@csrf_exempt
def createuser(request):
    if request.method == 'POST':
        izena= request.POST["izena"]
        email = request.POST["email"]
        passw = request.POST["pass"]
        confpass = request.POST["confpass"]
        if passw == confpass:
            hasha = make_password(passw)
            user = User.objects.create_user(username=izena, email=email, password=hasha)
            erab = Erabiltzailea(izena=izena,erabitlzailea_id=user)
            erab.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return redirect("/register")


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

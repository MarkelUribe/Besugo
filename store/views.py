from django.http import HttpResponse
from django.template import loader
from .models import Produktua

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def carro(request):
    template = loader.get_template('carro.html')
    return HttpResponse(template.render())

def platerak(request):
    template = loader.get_template('platerak.html')
    return HttpResponse(template.render())

def mariscadas(request):
    template = loader.get_template('mariscadas.html')
    return HttpResponse(template.render())

def bebidas(request):
    template = loader.get_template('bebidas.html')
    return HttpResponse(template.render())


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



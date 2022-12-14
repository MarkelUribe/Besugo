from datetime import timezone
import json
from datetime import date
import this
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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
from datetime import datetime


def index(request):
    if request.method == 'GET' and 'mez' in request.GET:
        mez = request.GET['mez']
    else:
        mez = ""
    template = loader.get_template('index.html')
    context = {
        'mez': mez
    }
    return HttpResponse(template.render(context, request))


def login(request):
    if request.method == 'GET' and 'mez' in request.GET:
        mez = request.GET['mez']
    else:
        mez = ""
    template = loader.get_template('login.html')
    context = {
        'mez': mez
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
    if request.method == 'GET' and 'mez' in request.GET:
        mez = request.GET['mez']
    else:
        mez = ""
    template = loader.get_template('register.html')
    context = {
        'mez': mez
    }
    return HttpResponse(template.render(context, request))


@csrf_exempt
def createuser(request):
    if request.method == 'POST':
        izena = request.POST["izena"]
        email = request.POST["email"]
        passw = request.POST["pass"]
        confpass = request.POST["confpass"]
        if passw == confpass:
            hasha = make_password(passw)
            user = User(username=izena, email=email, password=hasha)
            user.save()
            erab = Erabiltzailea(izena=izena, erabitlzailea_id=user)
            erab.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return redirect("/register?mez=Pasahitzak ez dira berdinak")


@csrf_exempt
def hasisaioa(request):
    if request.method == 'POST':
        username = request.POST['izena']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            logina(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('/login?mez=erabiltzailea edo pasahitza okerrak dira')


def amaitusaioa(request):
    logout(request)
    return redirect("index")


def mariscadascarro(request):

    myerabiltzaile = Erabiltzailea.objects.get(erabitlzailea_id=request.user)
    myprodu = Produktua.objects.all().values()

    if Eskaera.objects.filter(erabiltzailea=myerabiltzaile, egoera=0).count() <= 0:
        now = datetime.now()
        dia = str(now.day)
        mes = str(now.month)
        anio = str(now.year)
        x = anio + "-" + mes + "-" + dia
        y = 0
        j = myerabiltzaile

        eskaera = Eskaera(data=x, egoera=y, erabiltzailea=j)
        eskaera.save()
        template = loader.get_template('mariscadas.html')
        context = {
            'erabiltzailea': myerabiltzaile,
            'mykarroa': eskaera,
            'myprodu': myprodu,
        }
        return HttpResponse(template.render(context, request))
    else:
        myprodu = Produktua.objects.all().values()
        template = loader.get_template('mariscadas.html')
        context = {
            'myprodu': myprodu,
        }
        return HttpResponse(template.render(context, request))


def platoscarro(request):
      
  myerabiltzaile = Erabiltzailea.objects.get(erabitlzailea_id=request.user)
  myprodu = Produktua.objects.all().values()

  if Eskaera.objects.filter(erabiltzailea=myerabiltzaile, egoera=0).count() <= 0:
      now = datetime.now()
      dia = str(now.day)
      mes = str(now.month)
      anio = str(now.year)
      x = anio + "-" + mes + "-" + dia
      y = 0
      j = myerabiltzaile

      eskaera = Eskaera(data=x, egoera=y, erabiltzailea=j)
      eskaera.save()
      template = loader.get_template('platerak.html')
      context = {
            'mykarroa': eskaera,
            'myprodu': myprodu,
        }
      return HttpResponse(template.render(context, request))
  else:
      myprodu = Produktua.objects.all().values()
      template = loader.get_template('platerak.html')
      context = {
            'myprodu': myprodu,
        }
      return HttpResponse(template.render(context, request))


def bebidascarro(request):
      
  myerabiltzaile = Erabiltzailea.objects.get(erabitlzailea_id=request.user)
  myprodu = Produktua.objects.all().values()

  if Eskaera.objects.filter(erabiltzailea=myerabiltzaile, egoera=0).count() <= 0:
      now = datetime.now()
      dia = str(now.day)
      mes = str(now.month)
      anio = str(now.year)
      x = anio + "-" + mes + "-" + dia
      y = 0
      j = myerabiltzaile

      eskaera = Eskaera(data=x, egoera=y, erabiltzailea=j)
      eskaera.save()
      template = loader.get_template('bebidas.html')
      context = {
            'mykarroa': eskaera,
            'myprodu': myprodu,
        }
      return HttpResponse(template.render(context, request))
  else:
      myprodu = Produktua.objects.all().values()
      template = loader.get_template('bebidas.html')
      context = {
            'myprodu': myprodu,
        }
      return HttpResponse(template.render(context, request))
 
@csrf_exempt
def updatecarro(request):
    idProd = int(request.POST.get('id'))
    cont = int(request.POST.get('cont'))
    funtz = request.POST.get('funtz')
    myerabiltzaile = Erabiltzailea.objects.get(erabitlzailea_id=request.user)
    myeskaera = Eskaera.objects.get(erabiltzailea=myerabiltzaile, egoera=0)
    myprodu = Produktua.objects.get(id=idProd)

        
    if funtz == 'gei':
        if EskaeraLerroa.objects.filter(eskaera=myeskaera,produktua=myprodu).count() == 0:
            eskaeralerroa = EskaeraLerroa(eskaera=myeskaera,produktua=myprodu, kopurua=1)
            eskaeralerroa.save()
            #return totalaitzuli(request, myeskaera, myprodu, "EskaeraLerroa sortu da")
        
        if cont<=myprodu.stock:    
            myeskaeralerroa = EskaeraLerroa.objects.get(eskaera=myeskaera,produktua=myprodu)
            myeskaeralerroa.kopurua=cont
            myeskaeralerroa.save()
            return totalaitzuli(request, myeskaera, myprodu, "EskaeraLerroa eguneratu da")

        else:
            myeskaeralerroa = EskaeraLerroa.objects.get(eskaera=myeskaera,produktua=myprodu)
            myeskaeralerroa.kopurua=myeskaeralerroa.produktua.stock
            myeskaeralerroa.save()
            return totalaitzuli(request, myeskaera, myprodu, "Ez dago stock-ik")

    elif funtz == 'ken':
        if EskaeraLerroa.objects.filter(eskaera=myeskaera,produktua=myprodu).count() == 0:
            myeskaeralerroa = EskaeraLerroa(eskaera=myeskaera,produktua=myprodu, kopurua=1)
            myeskaeralerroa.save()
            #return totalaitzuli(request, myeskaera, myprodu, "EskaeraLerroa sortu da")
            
        if cont<=myprodu.stock:
            myeskaeralerroa = EskaeraLerroa.objects.get(eskaera=myeskaera,produktua=myprodu)
            myeskaeralerroa.kopurua=cont
            myeskaeralerroa.save()
            return totalaitzuli(request, myeskaera, myprodu, "EskaeraLerroa eguneratu da")
        else:
            myeskaeralerroa = EskaeraLerroa.objects.get(eskaera=myeskaera,produktua=myprodu)
            myeskaeralerroa.kopurua=myeskaeralerroa.produktua.stock
            myeskaeralerroa.save()
            return totalaitzuli(request, myeskaera, myprodu, "Ez dago stock-ik")
    elif funtz == 'hasi':
        return totalaitzuli(request, myeskaera, myprodu, "hasiera")
  
def totalaitzuli(request, myeskaera, myprodu, msg):
    total = 0
    gureeskaerak = EskaeraLerroa.objects.filter(eskaera= myeskaera)
    
    lista=[]
    for e in gureeskaerak:
        lista.append({'produktuaid':e.produktua.id, 'kopurua':e.kopurua})
        total += (float(e.produktua.prezioa) * float(e.kopurua))
        
    
    return JsonResponse([{'stock':myprodu.stock, 'total': total, 'mezua': msg, 'eskaerak': lista}], safe=False)


def mariscadascarro(request):

    myerabiltzaile = Erabiltzailea.objects.get(erabitlzailea_id=request.user)
    myprodu = Produktua.objects.all().values()

    if Eskaera.objects.filter(erabiltzailea=myerabiltzaile, egoera=0).count() <= 0:
        now = datetime.now()
        dia = str(now.day)
        mes = str(now.month)
        anio = str(now.year)
        x = anio + "-" + mes + "-" + dia
        y = 0
        j = myerabiltzaile

        eskaera = Eskaera(data=x, egoera=y, erabiltzailea=j)
        eskaera.save()
        template = loader.get_template('mariscadas.html')
        context = {
            'mykarroa': eskaera,
            'myprodu': myprodu,
        }
        return HttpResponse(template.render(context, request))
    else:
        myprodu = Produktua.objects.all().values()
        template = loader.get_template('mariscadas.html')
        context = {
            'myprodu': myprodu,
        }
        return HttpResponse(template.render(context, request))
    
def carro(request):
    myerabiltzaile = Erabiltzailea.objects.get(erabitlzailea_id=request.user)
    
    if Eskaera.objects.filter(erabiltzailea=myerabiltzaile, egoera=0).count() <= 0:
      now = datetime.now()
      dia = str(now.day)
      mes = str(now.month)
      anio = str(now.year)
      x = anio + "-" + mes + "-" + dia
      y = 0
      j = myerabiltzaile

      eskaera = Eskaera(data=x, egoera=y, erabiltzailea=j)
      eskaera.save()
      
        
    myeskaera = Eskaera.objects.get(erabiltzailea=myerabiltzaile, egoera=0)
    eskaeralerroak = EskaeraLerroa.objects.filter(eskaera=myeskaera)
    
    itzuli = []
    for i in eskaeralerroak:
        if i.kopurua == 0:
            i.delete()
        else:
            
            produktua = Produktua.objects.get(id = i.produktua.id)
            
            itzuli.append({'izena': produktua.izena, 'mota': produktua.mota,'kopurua': i.kopurua, 'prezioa': produktua.prezioa, 'id': produktua.id,})
    
    
    context = {
            'myprodu': itzuli,
            'helbidea': myerabiltzaile.helbidea,
            'ordainketa': myerabiltzaile.ordainketaMota,
        }
    
    template = loader.get_template('carro.html')
    
    return HttpResponse(template.render(context, request))

@csrf_exempt
def eskaeraezabatu(request):
    idProd = int(request.POST.get('id'))
    prod = Produktua.objects.get(id=idProd)
    erab = Erabiltzailea.objects.get(erabitlzailea_id = request.user)
    eskaera = Eskaera.objects.get(erabiltzailea=erab, egoera=0)
    
    eskaeralerroa = EskaeraLerroa.objects.get(eskaera=eskaera, produktua=prod)
    eskaeralerroa.delete()
    
    return JsonResponse([{'mezua':prod.izena+'ren eskaera arazorik gabe ezabatu da'}], safe=False)

@csrf_exempt
def totalajaso(request):
    total = 0
    erab = Erabiltzailea.objects.get(erabitlzailea_id = request.user)
    myeskaera =  Eskaera.objects.get(erabiltzailea=erab, egoera=0)
    gureeskaerak = EskaeraLerroa.objects.filter(eskaera= myeskaera)
    
    lista=[]
    for e in gureeskaerak:
        lista.append({'produktuaid':e.produktua.id, 'kopurua':e.kopurua})
        total += (float(e.produktua.prezioa) * float(e.kopurua))
        
    return JsonResponse([{'total':round(total, 2)}], safe=False)
   
   

def pago(request):
    template = loader.get_template('pago.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def envio(request):
    template = loader.get_template('envio.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def carroenvio(request):
    herria = request.POST['herria']
    helbidea = request.POST['helbidea']
    erab = Erabiltzailea.objects.get(erabitlzailea_id = request.user)
    
    erab.helbidea = helbidea +", "+ herria
    erab.save()
        
    return carro(request)
@csrf_exempt
def ordainketaegin(request):
    erab = Erabiltzailea.objects.get(erabitlzailea_id = request.user)
    myeskaera =  Eskaera.objects.get(erabiltzailea=erab, egoera=0)
    gureeskaerak = EskaeraLerroa.objects.filter(eskaera= myeskaera)
    
    
    if erab.ordainketaMota == None or erab.helbidea == None:
        return JsonResponse([{ 'mez':'Ordainketa mota edo helbidea ez dituzu zehaztu.'}], safe=False)
    
    
    
    total = 0
    lista=[]
    for e in gureeskaerak:
        lista.append({'produktua':e.produktua.izena, 'kopurua':e.kopurua, 'prezioa':round((float(e.produktua.prezioa) * float(e.kopurua)), 2) })
        total += (float(e.produktua.prezioa) * float(e.kopurua))
        
        
    if total >= 80:
        print("erosi")
        myeskaera.egoera = 2
        myeskaera.save()
        for e in gureeskaerak:
            print('stock '+ str(e.produktua.stock - e.kopurua))
            Produktua.objects.filter(id = e.produktua.id).update(stock = e.produktua.stock - e.kopurua)
            
        return JsonResponse([{'mez':'', 'izena':erab.izena, 'total':total,'eguna':date.today(), 'lista':lista}], safe=False)
    else:
        return JsonResponse([{ 'mez':'Prezio minimoa 80???-koa da'}], safe=False)

@csrf_exempt
def ordainketamota(request):
    mota = request.POST['mota']
    erab = Erabiltzailea.objects.get(erabitlzailea_id = request.user)
    erab.ordainketaMota = mota
    erab.save()
    return JsonResponse([{'mez':'ondo'}], safe=False)
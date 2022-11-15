from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('carro/', views.carro, name='carro'),
    path('platerak/', views.platerak, name='platerak'),
    path('mariscadas/', views.mariscadas, name='mariscadas'),
    path('bebidas/', views.bebidas, name='bebidas'),
    path('register/', views.register, name='register'),
    path('register/createuser/', views.createuser, name='createuser'),
    path('hasisaioa/', views.hasisaioa, name='hasisaioa'),
    path('amaitusaioa/', views.amaitusaioa, name='amaitusaioa'),
    path('mariscadascarro/', views.mariscadascarro, name='mariscadascarro'),
    path('platoscarro/', views.platoscarro, name='platoscarro'),
    path('bebidascarro/', views.bebidascarro, name='bebidascarro'),
    path('updatecarro/', views.updatecarro, name='updatecarro'),
    path('carro/', views.carro, name='carro'),
    path('eskaeraezabatu/', views.eskaeraezabatu, name='eskaeraezabatu'),
    path('totalajaso/', views.totalajaso, name='totalajaso'),
    path('pago/', views.pago, name='pago'),
    path('ordainketaegin/', views.ordainketaegin, name='ordainketaegin'),
]
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
]
from django.db import models
from django.forms import DateField



class Erabiltzailea(models.Model):

    ERABILTZAILE_MOTA = (
        (0, 'Admin'),
        (1, 'Bezeroa'),
        (2, 'Banatzailea'),
    )

    izena = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    pasahitza = models.CharField(max_length=30)
    mota = models.IntegerField(choices = ERABILTZAILE_MOTA)

class Produktua(models.Model):

    PRODUKTU_MOTA = (
        (0, 'Osagaia'),
        (1, 'Platera'),
        (2, 'Edaria'),
    )

    izena = models.CharField(max_length=255)
    deskribapena = models.CharField(max_length=255)
    prezioa = models.FloatField()
    stock = models.FloatField()
    mota = models.IntegerField(choices = PRODUKTU_MOTA)

class Eskaera(models.Model):

    EGOERA = (
        (0, 'Karrito'),
        (1, 'Bidean'),
        (2, 'Faktura'),
    )

    data = models.DateField()
    egoera = models.IntegerField(choices = EGOERA)
    erabiltzailea = models.ForeignKey( Erabiltzailea, on_delete=models.CASCADE)

class EskaeraLerroa(models.Model):
    eskaera = models.ForeignKey( Eskaera, on_delete=models.CASCADE)
    produktua = models.ForeignKey( Produktua, on_delete=models.CASCADE)
    #constraint_eskaera = models.UniqueConstraint(fields = ['eskaera', 'produktua'], name = 'constraint_eskaera')
    kopurua = models.IntegerField()
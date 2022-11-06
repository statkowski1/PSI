from django.db import models

# Create your models here.
class klient(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    adres_zamieszkania = models.CharField(max_length=45)
    data_urodzenia = models.DateTimeField()
    mail = models.CharField(max_length=45)
    numer_telefonu = models.CharField(max_length=45)

class sklep_elektroniczny(models.Model):
    kraj = models.CharField(max_length=45)
    miasto = models.CharField(max_length=45)
    ulica = models.CharField(max_length=45)

class produkt(models.Model):
    nazwa = models.CharField(max_length=45)
    cena = models.DecimalField(max_digits=10, decimal_places=10)
    producent = models.CharField(max_length=45)

class magazyn(models.Model):
    kraj = models.CharField(max_length=45)
    miasto = models.CharField(max_length=45)
    ulica = models.CharField(max_length=45)

class tranzakcja(models.Model):
    data_tranzakcji = models.DateTimeField()
    koszt_tranzakcji = models.DecimalField(max_digits=10, decimal_places=10)
    klient_id_klienta = models.ForeignKey(klient, on_delete=models.CASCADE)
    sklep_elektroniczny_id_sklepu = models.ForeignKey(sklep_elektroniczny, on_delete=models.CASCADE)

class dostepnosc(models.Model):
    class yes_or_not(models.TextChoices):
        YES = 'T'
        NOT = 'N'
    class sklep_lub_magazyn(models.TextChoices):
        SKLEP = 'S'
        MAGAZYN = 'M'
    dostepnosc = models.CharField(max_length=1, choices=yes_or_not.choices, default=yes_or_not.NOT)
    ilosc = models.IntegerField()
    sklep_czy_magazyn = models.CharField(max_length=1, choices=sklep_lub_magazyn.choices, default=sklep_lub_magazyn.SKLEP)
    magazyn_id_magazynu = models.ForeignKey(magazyn, on_delete=models.CASCADE)
    produkt_id_produktu = models.ForeignKey(produkt, on_delete=models.CASCADE)
    sklep_elektroniczny_id_sklepu = models.ForeignKey(sklep_elektroniczny, on_delete=models.CASCADE)

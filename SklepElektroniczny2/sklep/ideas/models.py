from django.db import models

# Create your models here.
class klient(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    adres_zamieszkania = models.CharField(max_length=45)
    data_urodzenia = models.DateTimeField()
    mail = models.CharField(max_length=45)
    numer_telefonu = models.CharField(max_length=45)
    pesel = models.CharField(max_length=11)
    class Meta:
        ordering = ('nazwisko',)
    def __str__(self):
        return self.imie + ' ' + self.nazwisko

class produkt(models.Model):
    nazwa = models.CharField(max_length=45)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    producent = models.CharField(max_length=45)
    rodzaj = models.CharField(max_length=45)
    class Meta:
        ordering = ('nazwa',)
    def __str__(self):
        return self.nazwa

class sklep_elektroniczny(models.Model):
    kraj = models.CharField(max_length=45)
    miasto = models.CharField(max_length=45)
    ulica = models.CharField(max_length=45)
    class Meta:
        ordering = ('ulica',)
    def __str__(self):
        return self.miasto+' '+self.ulica

class magazyn(models.Model):
    kraj = models.CharField(max_length=45)
    miasto = models.CharField(max_length=45)
    ulica = models.CharField(max_length=45)
    class Meta:
        ordering = ('ulica',)
    def __str__(self):
        return self.miasto+' '+self.ulica

class tranzakcja(models.Model):
    kod_tranzakcji = models.CharField(max_length=90)
    data_tranzakcji = models.DateTimeField()
    koszt_tranzakcji = models.DecimalField(max_digits=10, decimal_places=10)
    nazwisko_klienta = models.ForeignKey(klient, related_name='tranzakcje', on_delete=models.CASCADE)
    ulica_sklepu = models.ForeignKey(sklep_elektroniczny, related_name='tranzakcje', on_delete=models.CASCADE)
    class Meta:
        ordering = ('kod_tranzakcji',)
    def __str__(self):
        return self.kod_tranzakcji

class dostepnosc(models.Model):
    class yes_or_not(models.TextChoices):
        YES = 'YES'
        NOT = 'NOT'
    class sklep_lub_magazyn(models.TextChoices):
        SKLEP = 'S'
        MAGAZYN = 'M'
    dostepnosc = models.CharField(max_length=3, choices=yes_or_not.choices, default=yes_or_not.NOT)
    ilosc = models.IntegerField()
    sklep_czy_magazyn = models.CharField(max_length=1, choices=sklep_lub_magazyn.choices, default=sklep_lub_magazyn.SKLEP)
    magazyn_ulica = models.ForeignKey(magazyn, related_name='dostepnosci', on_delete=models.CASCADE, blank=True, null=True)
    nazwa_produktu = models.ForeignKey(produkt, related_name='dostepnosci', on_delete=models.CASCADE)
    sklep_elektroniczny_ulica = models.ForeignKey(sklep_elektroniczny, related_name='dostepnosci', on_delete=models.CASCADE, blank=True, null=True)

class produkt_has_tranzakcja(models.Model):
    nazwa_produktu = models.ForeignKey(produkt, related_name='produktHasTranzakcja', on_delete=models.CASCADE)
    kod_tranzakcji = models.ForeignKey(tranzakcja, related_name='produktHasTranzakcja', on_delete=models.CASCADE)


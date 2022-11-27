from django.db import models

# Create your models here.
class klient(models.Model):
    id_klienta = models.IntegerField()
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
    id_produktu = models.IntegerField()
    nazwa = models.CharField(max_length=45)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    producent = models.CharField(max_length=45)
    rodzaj = models.CharField(max_length=45)
    class Meta:
        ordering = ('nazwa',)
    def __str__(self):
        return self.nazwa

class sklep_elektroniczny(models.Model):
    id_sklepu_elektronicznego = models.IntegerField()
    kraj = models.CharField(max_length=45)
    miasto = models.CharField(max_length=45)
    ulica = models.CharField(max_length=45)
    class Meta:
        ordering = ('ulica',)
    def __str__(self):
        return self.miasto+' '+self.ulica

class magazyn(models.Model):
    id_magazynu = models.IntegerField()
    kraj = models.CharField(max_length=45)
    miasto = models.CharField(max_length=45)
    ulica = models.CharField(max_length=45)
    class Meta:
        ordering = ('ulica',)
    def __str__(self):
        return self.miasto+' '+self.ulica

class tranzakcja(models.Model):
    id_tranzakcji = models.IntegerField()
    data_tranzakcji = models.DateTimeField()
    koszt_tranzakcji = models.DecimalField(max_digits=10, decimal_places=10)
    id_klienta = models.ForeignKey(klient, related_name='tranzakcje', on_delete=models.CASCADE)
    id_sklepu_elektronicznego = models.ForeignKey(sklep_elektroniczny, related_name='tranzakcje', on_delete=models.CASCADE)

class dostepnosc(models.Model):
    # class yes_or_not(models.TextChoices):
    #     YES = 'YES'
    #     NOT = 'NOT'
    # class sklep_lub_magazyn(models.TextChoices):
    #     SKLEP = 'SKLEP'
    #     MAGAZYN = 'MAGAZYN'
    YES = 'Y'
    NOT = 'N'
    yes_or_not = ((YES, 'YES'), (NOT, 'NOT'),)
    SKLEP = 'S'
    MAGAZYN = 'M'
    sklep_lub_magazyn = ((SKLEP, 'SKLEP'), (MAGAZYN, 'MAGAZYN'),)
    dostepnosc = models.CharField(max_length=3, choices=yes_or_not, default=NOT)
    ilosc = models.IntegerField()
    sklep_czy_magazyn = models.CharField(max_length=7, choices=sklep_lub_magazyn, default=SKLEP)
    id_magazynu = models.ForeignKey(magazyn, related_name='dostepnosci', on_delete=models.CASCADE, blank=True, null=True)
    id_produktu = models.ForeignKey(produkt, related_name='dostepnosci', on_delete=models.CASCADE)
    id_sklepu_elektronicznego = models.ForeignKey(sklep_elektroniczny, related_name='dostepnosci', on_delete=models.CASCADE, blank=True, null=True)

class produkt_has_tranzakcja(models.Model):
    id_produktu = models.ForeignKey(produkt, related_name='produktHasTranzakcja', on_delete=models.CASCADE)
    id_tranzakcji = models.ForeignKey(tranzakcja, related_name='produktHasTranzakcja', on_delete=models.CASCADE)


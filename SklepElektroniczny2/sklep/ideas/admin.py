from django.contrib import admin
from .models import klient, produkt, sklep_elektroniczny, magazyn, tranzakcja, dostepnosc, produkt_has_tranzakcja
# Register your models here.
admin.site.register(klient)
admin.site.register(produkt)
admin.site.register(sklep_elektroniczny)
admin.site.register(magazyn)
admin.site.register(tranzakcja)
admin.site.register(dostepnosc)
admin.site.register(produkt_has_tranzakcja)

from .models import klient, sklep_elektroniczny, produkt, magazyn, tranzakcja, dostepnosc, produkt_has_tranzakcja
from rest_framework import serializers

class klientSerializer(serializers.ModelSerializer):
    class Meta:
        model = klient
        fields = ['id', 'imie', 'nazwisko', 'adres_zamieszkania', 'data_urodzenia', 'mail', 'numer_telefonu']

class sklep_elektronicznySerializer(serializers.ModelSerializer):
    class Meta:
        model = sklep_elektroniczny
        fields = ['kraj', 'miasto', 'ulica']

class produktSerializer(serializers.ModelSerializer):
    class Meta:
        model = produkt
        fields = ['id', 'nazwa', 'cena', 'producent']

class magazynSerializer(serializers.ModelSerializer):
    class Meta:
        model = magazyn
        fields = ['id', 'kraj', 'miasto', 'ulica']

class tranzakcjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tranzakcja
        fields = ['id', 'data_tranzakcji', 'koszt_tranzakcji', 'klient_id_klienta', 'sklep_elektroniczny_id_sklepu']

class dostepnoscSerializer(serializers.ModelSerializer):
    class Meta:
        model = dostepnosc
        fields = ['dostepnosc', 'ilosc', 'sklep_czy_magazyn', 'magazyn_id_magazynu', 'produkt_id_produktu', 'sklep_elektroniczny_id_sklepu']

    def validate(self, ilosc):
        if ilosc['ilosc'] < 0:
            raise serializers.ValidationError(
                {'Ilość nie może być mniejsza od 0!'})
        return ilosc

class produkt_has_tranzakcjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = produkt_has_tranzakcja
        fields = ['tranzakcja_id_tranzakcji', 'produkt_id_produktu']

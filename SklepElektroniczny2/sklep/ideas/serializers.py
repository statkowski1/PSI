from .models import klient, sklep_elektroniczny, produkt, magazyn, tranzakcja, dostepnosc, produkt_has_tranzakcja
from rest_framework import serializers

class klientSerializer(serializers.ModelSerializer):
    class Meta:
        model = klient
        fields = ['pk', 'imie', 'nazwisko', 'adres_zamieszkania', 'data_urodzenia', 'mail', 'numer_telefonu']

class sklep_elektronicznySerializer(serializers.ModelSerializer):
    class Meta:
        model = sklep_elektroniczny
        fields = ['pk', 'kraj', 'miasto', 'ulica']

class produktSerializer(serializers.ModelSerializer):
    class Meta:
        model = produkt
        fields = ['pk', 'nazwa', 'cena', 'producent', 'rodzaj']
    def validate_cena(self, value):
        if value==0 and value<0:
            raise serializers.ValidationError("Cena nie może być mniejsza lub równa 0!")

class magazynSerializer(serializers.ModelSerializer):
    class Meta:
        model = magazyn
        fields = ['pk', 'kraj', 'miasto', 'ulica']

class tranzakcjaSerializer(serializers.ModelSerializer):
    nazwisko_klienta = serializers.SlugRelatedField(queryset=klient.objects.all(), slug_field='nazwisko')
    ulica_sklepu = serializers.SlugRelatedField(queryset=sklep_elektroniczny.objects.all(), slug_field='ulica')
    class Meta:
        model = tranzakcja
        fields = ['pk', 'kod_tranzakcji', 'data_tranzakcji', 'koszt_tranzakcji', 'nazwisko_klienta', 'ulica_sklepu']
    def validate_koszt_tranzakcji(self, value):
        if value==0 and value<0:
            raise serializers.ValidationError("Koszt tranzakcji nie może być mniejsza, bądź równa 0!")

class dostepnoscSerializer(serializers.ModelSerializer):
    magazyn_ulica = serializers.SlugRelatedField(queryset=magazyn.objects.all(), slug_field='ulica')
    sklep_ulica = serializers.SlugRelatedField(queryset=sklep_elektroniczny.objects.all(), slug_field='ulica')
    nazwa_produktu = serializers.SlugRelatedField(queryset=produkt.objects.all(), slug_field='nazwa')
    dostepnosc = serializers.ChoiceField(choices=dostepnosc.yes_or_not)
    #sklep_czy_magazyn = serializers.ChoiceField(choices=dostepnosc.sklep_lub_magazyn)
    class Meta:
        model = dostepnosc
        fields = ['pk', 'dostepnosc', 'ilosc', 'sklep_czy_magazyn', 'magazyn_ulica', 'nazwa_produktu', 'sklep_ulica']
    def validate_ilosc(self, value):
        if value<0:
            raise serializers.ValidationError("Ilość nie może być mniejsza od 0!",)
        return value

class produkt_has_tranzakcjaSerializer(serializers.ModelSerializer):
    nazwa_produktu = serializers.SlugRelatedField(queryset=produkt.objects.all(), slug_field='nazwa')
    kod_tranzakcji = serializers.SlugRelatedField(queryset=tranzakcja.objects.all(), slug_field='kod_tranzakcji')
    class Meta:
        model = produkt_has_tranzakcja
        fields = ['pk', 'nazwa_produktu', 'kod_tranzakcji']


from .models import klient, sklep_elektroniczny, produkt, magazyn, tranzakcja, dostepnosc, produkt_has_tranzakcja
from rest_framework import serializers

class klientSerializer(serializers.ModelSerializer):
    class Meta:
        model = klient
        fields = ['id_klienta', 'imie', 'nazwisko', 'adres_zamieszkania', 'data_urodzenia', 'mail', 'numer_telefonu']

class sklep_elektronicznySerializer(serializers.ModelSerializer):
    class Meta:
        model = sklep_elektroniczny
        fields = ['id_sklepu_elektronicznego', 'kraj', 'miasto', 'ulica']

class produktSerializer(serializers.ModelSerializer):
    class Meta:
        model = produkt
        fields = ['id_produktu', 'nazwa', 'cena', 'producent', 'rodzaj']
    def validate_cena(self, value):
        if value==0 and value<0:
            raise serializers.ValidationError("Cena nie może być mniejsza lub równa 0!")

class magazynSerializer(serializers.ModelSerializer):
    class Meta:
        model = magazyn
        fields = ['id_magazynu', 'kraj', 'miasto', 'ulica']

class tranzakcjaSerializer(serializers.ModelSerializer):
    id_klienta = serializers.SlugRelatedField(queryset=klient.objects.all(), slug_field='id_klienta')
    id_sklepu_elektronicznego = serializers.SlugRelatedField(queryset=sklep_elektroniczny.objects.all(), slug_field='id_sklepu_elektronicznego')
    class Meta:
        model = tranzakcja
        fields = ['id_tranzakcji', 'data_tranzakcji', 'koszt_tranzakcji', 'id_klienta', 'id_sklepu_elektronicznego']
    def validate_koszt_tranzakcji(self, value):
        if value==0 and value<0:
            raise serializers.ValidationError("Koszt tranzakcji nie może być mniejsza, bądź równa 0!")

class dostepnoscSerializer(serializers.ModelSerializer):
    id_magazynu = serializers.SlugRelatedField(queryset=magazyn.objects.all(), slug_field='id_magazynu')
    id_sklepu_elektronicznego = serializers.SlugRelatedField(queryset=sklep_elektroniczny.objects.all(), slug_field='id_sklepu_elektronicznego')
    id_produktu = serializers.SlugRelatedField(queryset=produkt.objects.all(), slug_field='id_produktu')
    dostepnosc = serializers.ChoiceField(choices=dostepnosc.yes_or_not)
    #sklep_czy_magazyn = serializers.ChoiceField(choices=dostepnosc.sklep_lub_magazyn)
    class Meta:
        model = dostepnosc
        fields = ['pk', 'dostepnosc', 'ilosc', 'sklep_czy_magazyn', 'id_magazynu', 'id_produktu', 'id_sklepu_elektronicznego']
    def validate_ilosc(self, value):
        if value<0:
            raise serializers.ValidationError("Ilość nie może być mniejsza od 0!",)
        return value

class produkt_has_tranzakcjaSerializer(serializers.ModelSerializer):
    id_produktu = serializers.SlugRelatedField(queryset=produkt.objects.all(), slug_field='id_produktu')
    id_tranzakcji = serializers.SlugRelatedField(queryset=tranzakcja.objects.all(), slug_field='id_tranzakcji')
    class Meta:
        model = produkt_has_tranzakcja
        fields = ['pk', 'id_produktu', 'id_tranzakcji']


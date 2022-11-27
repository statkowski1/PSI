from django.shortcuts import render
from .models import klient, sklep_elektroniczny, produkt, magazyn, tranzakcja, dostepnosc, produkt_has_tranzakcja
from rest_framework import viewsets
from .serializers import klientSerializer, sklep_elektronicznySerializer, produktSerializer, magazynSerializer, tranzakcjaSerializer, dostepnoscSerializer, produkt_has_tranzakcjaSerializer
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet

# Create your views here.

class klientFilter(FilterSet):
    from_birthdate = DateTimeFilter(field_name='data_urodzenia', lookup_expr='gte')
    to_birthdate = DateTimeFilter(field_name='data_urodzenia', lookup_expr='lte')
    class Meta:
        model = klient
        fields = ['from_birthdate', 'to_birthdate']

class klientList(generics.ListCreateAPIView):
    queryset = klient.objects.all()
    serializer_class = klientSerializer
    name = 'klient-list'
    filterset_class = klientFilter
    filterset_fields = ['nazwisko', 'mail', 'numer_telefonu']
    search_fields = ['nazwisko', '$mail', 'numer_telefonu']
    ordering_fields = ['mail', 'nazwisko', 'numer_telefonu']

class klientDetail(generics.RetrieveAPIView):
    queryset = klient.objects.all()
    serializer_class = klientSerializer
    name = 'klient-detail'

class sklep_elektronicznyList(generics.ListCreateAPIView):
    queryset = sklep_elektroniczny.objects.all()
    serializer_class = sklep_elektronicznySerializer
    name = 'sklep_elektroniczny-list'
    filterset_fields = ['kraj', 'miasto', 'ulica']
    search_fields = ['$miasto', 'ulica']
    ordering_fields = ['miasto']

class sklep_elektronicznyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = sklep_elektroniczny.objects.all()
    serializer_class = sklep_elektronicznySerializer
    name = 'sklep_elektroniczny-detail'

class produktFilter(FilterSet):
    min_cena = NumberFilter(field_name='cena', lookup_expr='gte')
    max_cena = NumberFilter(field_name='cena', lookup_expr='lte')
    class Meta:
        model = produkt
        fields = ['min_cena', 'max_cena']

class produktList(generics.ListCreateAPIView):
    queryset = produkt.objects.all()
    serializer_class = produktSerializer
    name = 'produkt-list'
    filterset_class = produktFilter
    filterset_fields = ['cena', 'producent', 'rodzaj']
    search_fields = ['cena', '$producent', '$rodzaj']
    ordering_fields = ['rodzaj', 'producent', 'cena']


class produktDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = produkt.objects.all()
    serializer_class = produktSerializer
    name = 'produkt-detail'

class magazynList(generics.ListCreateAPIView):
    queryset = magazyn.objects.all()
    serializer_class = magazynSerializer
    name = 'magazyn-list'
    filterset_fields = ['kraj', 'miasto', 'ulica']
    search_fields = ['$miasto', 'ulica']
    ordering_fields = ['miasto']

class magazynDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = magazyn.objects.all()
    serializer_class = magazynSerializer
    name = 'magazyn-detail'

class tranzakcjaList(generics.ListCreateAPIView):
    queryset = tranzakcja.objects.all()
    serializer_class = tranzakcjaSerializer
    name = 'tranzakcja-list'
    filterset_fields = ['data_tranzakcji', 'koszt_tranzakcji', 'id_klienta', 'id_sklepu_elektronicznego']
    search_fields = ['data_tranzakcji', 'koszt_tranzakcji']
    ordering_fields = ['id_sklepu_elektronicznego', 'data_tranzakcji', 'koszt_tranzakcji']

class tranzakcjaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = tranzakcja.objects.all()
    serializer_class = tranzakcjaSerializer
    name = 'tranzakcja-detail'

class dostepnoscList(generics.ListCreateAPIView):
    queryset = dostepnosc.objects.all()
    serializer_class = dostepnoscSerializer
    name = 'dostepnosc-list'
    filterset_fields = ['dostepnosc', 'id_produktu']
    search_fields = ['id_produktu', '$dostepnosc']
    ordering_fields = ['dostepnosc', 'id_produktu']

class dostepnoscDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = dostepnosc.objects.all()
    serializer_class = dostepnoscSerializer
    name = 'dostepnosc-detail'

class produkt_has_tranzakcjaList(generics.ListCreateAPIView):
    queryset = produkt_has_tranzakcja.objects.all()
    serializer_class = produkt_has_tranzakcjaSerializer
    name = 'produkt_has_tranzakcja-list'
    ordering_fields = ['id_tranzakcji']

class produkt_has_tranzakcjaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = produkt_has_tranzakcja.objects.all()
    serializer_class = produkt_has_tranzakcjaSerializer
    name = 'produkt_has_tranzakcja-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'klient': reverse(klientList.name, request=request),
                         'sklep_elektroniczny': reverse(sklep_elektronicznyList.name, request=request),
                         'produkt': reverse(produktList.name, request=request),
                         'magazyn': reverse(magazynList.name, request=request),
                         'tranzakcja': reverse(tranzakcjaList.name, request=request),
                         'dostepnosc': reverse(dostepnoscList.name, request=request),
                         'produkt_has_tranzakcja': reverse(produkt_has_tranzakcjaList.name, request=request)
        })
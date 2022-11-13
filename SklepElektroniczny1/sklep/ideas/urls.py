from rest_framework import routers
from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('klient', views.klientList.as_view(), name=views.klientList.name),
    path('klient/<int:id>', views.klientDetail.as_view(), name=views.klientDetail.name),
    path('sklep_elektroniczny', views.sklep_elektronicznyList.as_view(), name=views.sklep_elektronicznyList.name),
    path('sklep_elektroniczny/<int:id>', views.sklep_elektronicznyDetail.as_view(), name=views.sklep_elektronicznyDetail.name),
    path('produkt', views.produktList.as_view(), name=views.produktList.name),
    path('produkt/<int:id>', views.produktDetail.as_view(), name=views.klientDetail.name),
    path('magazyn', views.magazynList.as_view(), name=views.magazynList.name),
    path('magazyn/<int:id>', views.magazynDetail.as_view(), name=views.magazynDetail.name),
    path('tranzakcja', views.tranzakcjaList.as_view(), name=views.tranzakcjaList.name),
    path('tranzakcja/<int:id>', views.tranzakcjaDetail.as_view(), name=views.tranzakcjaDetail.name),
    path('dostepnosc', views.dostepnoscList.as_view(), name=views.dostepnoscList.name),
    path('dostepnosc/<int:id>', views.dostepnoscDetail.as_view(), name=views.dostepnoscDetail.name),
    path('produkt_has_tranzakcja', views.produkt_has_tranzakcjaList.as_view(), name=views.produkt_has_tranzakcjaList.name),
    path('produkt_has_tranzakcja', views.produkt_has_tranzakcjaDetail.as_view(), name=views.produkt_has_tranzakcjaDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]

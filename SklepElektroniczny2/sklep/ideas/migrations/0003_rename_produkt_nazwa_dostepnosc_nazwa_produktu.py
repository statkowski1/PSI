# Generated by Django 4.1.3 on 2022-11-19 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_magazyn_produkt_sklep_elektroniczny_tranzakcja_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dostepnosc',
            old_name='produkt_nazwa',
            new_name='nazwa_produktu',
        ),
    ]

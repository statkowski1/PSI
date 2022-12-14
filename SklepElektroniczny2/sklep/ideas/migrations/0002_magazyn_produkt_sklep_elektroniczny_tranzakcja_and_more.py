# Generated by Django 4.1.3 on 2022-11-19 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='magazyn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kraj', models.CharField(max_length=45)),
                ('miasto', models.CharField(max_length=45)),
                ('ulica', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ('ulica',),
            },
        ),
        migrations.CreateModel(
            name='produkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=45)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
                ('producent', models.CharField(max_length=45)),
                ('rodzaj', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ('nazwa',),
            },
        ),
        migrations.CreateModel(
            name='sklep_elektroniczny',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kraj', models.CharField(max_length=45)),
                ('miasto', models.CharField(max_length=45)),
                ('ulica', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ('ulica',),
            },
        ),
        migrations.CreateModel(
            name='tranzakcja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod_tranzakcji', models.CharField(max_length=90)),
                ('data_tranzakcji', models.DateTimeField()),
                ('koszt_tranzakcji', models.DecimalField(decimal_places=10, max_digits=10)),
                ('nazwisko_klienta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tranzakcje', to='ideas.klient')),
                ('ulica_sklepu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tranzakcje', to='ideas.sklep_elektroniczny')),
            ],
            options={
                'ordering': ('kod_tranzakcji',),
            },
        ),
        migrations.CreateModel(
            name='produkt_has_tranzakcja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod_tranzakcji', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produktHasTranzakcja', to='ideas.tranzakcja')),
                ('nazwa_produktu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produktHasTranzakcja', to='ideas.produkt')),
            ],
        ),
        migrations.CreateModel(
            name='dostepnosc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dostepnosc', models.CharField(choices=[('T', 'Yes'), ('N', 'Not')], default='N', max_length=1)),
                ('ilosc', models.IntegerField()),
                ('sklep_czy_magazyn', models.CharField(choices=[('S', 'Sklep'), ('M', 'Magazyn')], default='S', max_length=1)),
                ('magazyn_ulica', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dostepnosci', to='ideas.magazyn')),
                ('produkt_nazwa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dostepnosci', to='ideas.produkt')),
                ('sklep_elektroniczny_ulica', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dostepnosci', to='ideas.sklep_elektroniczny')),
            ],
        ),
    ]

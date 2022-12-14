# Generated by Django 4.1.3 on 2022-11-19 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='klient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=45)),
                ('nazwisko', models.CharField(max_length=45)),
                ('adres_zamieszkania', models.CharField(max_length=45)),
                ('data_urodzenia', models.DateTimeField()),
                ('mail', models.CharField(max_length=45)),
                ('numer_telefonu', models.CharField(max_length=45)),
                ('pesel', models.CharField(max_length=11)),
            ],
            options={
                'ordering': ('nazwisko',),
            },
        ),
    ]

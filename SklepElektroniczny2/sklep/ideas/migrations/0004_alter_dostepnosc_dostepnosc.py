# Generated by Django 4.1.3 on 2022-11-20 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_rename_produkt_nazwa_dostepnosc_nazwa_produktu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dostepnosc',
            name='dostepnosc',
            field=models.CharField(choices=[('YES', 'Yes'), ('NOT', 'Not')], default='NOT', max_length=3),
        ),
    ]

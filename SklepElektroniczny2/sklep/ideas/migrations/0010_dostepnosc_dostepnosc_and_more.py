# Generated by Django 4.1.3 on 2022-11-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0009_remove_dostepnosc_dostepnosc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dostepnosc',
            name='dostepnosc',
            field=models.CharField(choices=[('Y', 'YES'), ('N', 'NOT')], default='N', max_length=3),
        ),
        migrations.AlterField(
            model_name='dostepnosc',
            name='sklep_czy_magazyn',
            field=models.CharField(choices=[('S', 'SKLEP'), ('M', 'MAGAZYN')], default='S', max_length=7),
        ),
    ]

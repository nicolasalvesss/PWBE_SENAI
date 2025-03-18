# Generated by Django 5.1.7 on 2025-03-17 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('qtdRodas', models.PositiveIntegerField()),
                ('ano', models.PositiveIntegerField()),
                ('cor', models.CharField(max_length=255)),
                ('combustivel', models.CharField(choices=[('GASOLINA', 'Gasolina'), ('ETANOL', 'Etanol'), ('GNV', 'GNV'), ('ELETRICO', 'Eletrico'), ('ALCOOL', 'Alcool'), ('DIESEL', 'Diesel'), ('FB', 'FeedBack')], max_length=9)),
            ],
        ),
    ]

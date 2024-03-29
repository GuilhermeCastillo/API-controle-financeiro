# Generated by Django 5.0.3 on 2024-03-17 05:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=200, unique=True)),
                ('valor', models.FloatField()),
                ('data', models.DateField()),
                ('categoria', models.ForeignKey(blank=True, default=8, on_delete=django.db.models.deletion.PROTECT, related_name='despesas', to='despesas.categoria')),
            ],
        ),
    ]

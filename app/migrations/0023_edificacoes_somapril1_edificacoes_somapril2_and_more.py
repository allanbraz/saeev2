# Generated by Django 4.1.1 on 2023-02-22 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_edificacoes_calcnotail_edificacoes_potilumg'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificacoes',
            name='somapril1',
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='edificacoes',
            name='somapril2',
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='edificacoes',
            name='somapril3',
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
    ]
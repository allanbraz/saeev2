# Generated by Django 4.1.1 on 2023-02-21 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_edificacoes_notaic'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificacoes',
            name='notacondgeralcorrigida',
            field=models.CharField(blank=True, editable=False, max_length=1, null=True),
        ),
    ]

# Generated by Django 4.1.1 on 2023-02-26 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_ambientes_areaabertura_ambientes_led'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificacoes',
            name='nomepre',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='ambientes',
            name='areaabertura',
            field=models.FloatField(null=True),
        ),
    ]

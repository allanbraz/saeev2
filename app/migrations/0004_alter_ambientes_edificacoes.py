# Generated by Django 4.1.1 on 2023-02-19 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_ambientes_edificacao_ambientes_edificacoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambientes',
            name='edificacoes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ambiente_set', to='app.edificacoes'),
        ),
    ]

# Generated by Django 4.1.1 on 2023-02-20 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_ambientes_edificacoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambientes',
            name='edificacoes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ambientes', to='app.edificacoes'),
        ),
    ]

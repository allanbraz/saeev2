# Generated by Django 4.1.1 on 2023-02-19 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_ambientes_edificacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ambientes',
            name='edificacao',
        ),
        migrations.AddField(
            model_name='ambientes',
            name='edificacoes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.edificacoes'),
        ),
    ]

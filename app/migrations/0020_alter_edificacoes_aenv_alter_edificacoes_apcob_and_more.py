# Generated by Django 4.1.1 on 2023-02-22 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_ambientes_col1_ambientes_col2_ambientes_col3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edificacoes',
            name='aenv',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='edificacoes',
            name='apcob',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='edificacoes',
            name='atot',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='edificacoes',
            name='atotfachada',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='edificacoes',
            name='fsvidro',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='edificacoes',
            name='somaabertura',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='edificacoes',
            name='vtot',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
    ]
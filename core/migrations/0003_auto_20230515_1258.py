# Generated by Django 3.1.2 on 2023-05-15 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230503_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='vencimiento',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='vigente',
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
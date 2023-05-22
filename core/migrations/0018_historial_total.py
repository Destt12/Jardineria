# Generated by Django 3.1.2 on 2023-05-20 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_remove_historial_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='historial',
            name='total',
            field=models.DecimalField(decimal_places=2, default=2000, max_digits=10),
            preserve_default=False,
        ),
    ]

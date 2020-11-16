# Generated by Django 3.1.3 on 2020-11-15 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vessels', '0002_auto_20201115_1950'),
        ('equipments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='vessel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vessels.vessel'),
        ),
    ]

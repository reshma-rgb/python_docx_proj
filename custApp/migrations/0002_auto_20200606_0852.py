# Generated by Django 3.0.3 on 2020-06-06 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='account_bal',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='advance',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='bill',
            field=models.FloatField(default=0.0),
        ),
    ]

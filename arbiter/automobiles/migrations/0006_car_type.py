# Generated by Django 2.0.7 on 2018-07-18 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automobiles', '0005_auto_20180718_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='type',
            field=models.CharField(choices=[('audi', 'Audi'), ('bmw', 'BMW'), ('volvo', 'Volvo'), ('benz', 'Benz')], default=('audi', 'Audi'), max_length=16, unique=True),
        ),
    ]
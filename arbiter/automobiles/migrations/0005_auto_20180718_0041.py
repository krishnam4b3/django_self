# Generated by Django 2.0.7 on 2018-07-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automobiles', '0004_auto_20180717_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='carimage',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='company',
            name='companyimage',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='spare',
            name='spareimage',
            field=models.ImageField(upload_to=''),
        ),
    ]

# Generated by Django 2.0.7 on 2018-07-17 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automobiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='carimage',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='company',
            name='companyimage',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='spare',
            name='spareimage',
            field=models.ImageField(upload_to='images/'),
        ),
    ]

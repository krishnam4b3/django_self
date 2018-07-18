# Generated by Django 2.0.7 on 2018-07-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carname', models.CharField(max_length=16)),
                ('carimage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=16)),
                ('companyimage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Spare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sparename', models.CharField(max_length=16)),
                ('spareimage', models.ImageField(upload_to='')),
                ('available', models.BooleanField(default=False)),
            ],
        ),
    ]
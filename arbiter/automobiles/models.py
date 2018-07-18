from django.db import models

# Create your models here.
type_choices = (
    ('audi', 'audi'),
    ('bmw', 'BMW'),
    ('volvo', 'volvo'),
    ('benz', 'benz'),
)
class Company(models.Model):
    companyname = models.CharField(max_length=16)
    companyimage = models.ImageField()
    def __str__(self):
        return "{},{}".format(self.companyname,self.companyimage)

class Car(models.Model):
    carname = models.CharField(max_length=16)
    carimage = models.ImageField()
    type = models.CharField(max_length=16, choices=type_choices, unique=True,default=type_choices[0])
    def __str__(self):
        return "{},{}".format(self.carname,self.carimage)

class Spare(models.Model):
    sparename = models.CharField(max_length=16)
    spareimage = models.ImageField()
    available = models.BooleanField(default=False)
    def __str__(self):
        return "{},{},{}".format(self.sparename,self.spareimage,self.available)
   
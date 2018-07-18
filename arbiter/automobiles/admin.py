from django.contrib import admin
from .models import Company,Car,Spare
# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=['companyname','companyimage']
    list_filter=['companyname']
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display=['carname','carimage']
    list_filter=['carname','type']
@admin.register(Spare)
class SpareAdmin(admin.ModelAdmin):
    list_display=['sparename','spareimage','available']
    list_filter=['sparename','available']



from django.contrib import admin

from businessops_api import models

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.TransCategory)
admin.site.register(models.Company)
admin.site.register(models.Department)
admin.site.register(models.EmpDepartment)
admin.site.register(models.Employee)
admin.site.register(models.Product)
admin.site.register(models.Material)
admin.site.register(models.Revenue)
admin.site.register(models.Expense)

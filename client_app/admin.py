from django.contrib import admin

from client_app.models import Employee


# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
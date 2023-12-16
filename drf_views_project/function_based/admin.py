from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['first_name', 'last_name', 'email', 'salary', 'hire_date']

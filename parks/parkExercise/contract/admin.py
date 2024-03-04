from django.contrib import admin
from .models import Contract, Contract_rule

@admin.register(Contract)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'max_value')

@admin.register(Contract_rule)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'contract_id', 'until', 'value')

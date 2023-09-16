from django.contrib import admin
from .models import FiscalYear, FinancialEstimate

@admin.register(FiscalYear)
class FiscalYearAdmin(admin.ModelAdmin):
    list_display = ('year_in_bs', 'year_in_ad')

@admin.register(FinancialEstimate)
class FinancialEstimateAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'fiscal_year', 'total', 'federal', 'province', 'local_government', 'percentage_of_total_estimates')


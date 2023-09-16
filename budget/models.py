from django.db import models

# Create your models here.
class FiscalYear(models.Model):
    """ Fiscal Yaer """
    year_in_bs = models.CharField(max_length=10)
    year_in_ad = models.CharField(max_length=10)

    def __str__(self):
        return self.year_in_ad


class FinancialEstimate(models.Model):
    """ Financial Estimate """
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    federal = models.DecimalField(max_digits=10, decimal_places=2)
    province = models.DecimalField(max_digits=10, decimal_places=2)
    local_government = models.DecimalField(max_digits=10, decimal_places=2)
    percentage_of_total_estimates = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title

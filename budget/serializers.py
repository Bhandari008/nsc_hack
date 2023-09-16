from rest_framework import serializers
from .models import FiscalYear, FinancialEstimate

class FiscalYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiscalYear
        fields = '__all__'

class FinancialEstimateSerializer(serializers.ModelSerializer):
    fiscal_year_year_in_bs = serializers.SerializerMethodField()
    
    class Meta:
        model = FinancialEstimate
        fields = '__all__'
    
    def get_fiscal_year_year_in_bs(self, obj):
        return obj.fiscal_year.year_in_bs

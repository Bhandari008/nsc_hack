from rest_framework import viewsets, filters
from .models import FiscalYear, FinancialEstimate
from django.db.models import Q
from rest_framework import status
from .serializers import FiscalYearSerializer, FinancialEstimateSerializer
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, logout

class FiscalYearViewSet(viewsets.ModelViewSet):
    queryset = FiscalYear.objects.all()
    serializer_class = FiscalYearSerializer

class FinancialEstimateViewSet(viewsets.ModelViewSet):
    queryset = FinancialEstimate.objects.all()
    serializer_class = FinancialEstimateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'subtitle', 'fiscal_year__year_in_bs', 'fiscal_year__year_in_ad']

    def get_queryset(self):
        queryset = FinancialEstimate.objects.all()
        
        # Get query parameters
        title_param = self.request.query_params.get('title')
        subtitle_param = self.request.query_params.get('subtitle')
        fiscal_year_param = self.request.query_params.get('fiscal_year')

        # Apply filters based on parameters
        if title_param:
            queryset = queryset.filter(title__icontains=title_param)
        if subtitle_param:
            queryset = queryset.filter(subtitle__icontains=subtitle_param)
        if fiscal_year_param:
            queryset = queryset.filter(
                Q(fiscal_year__year_in_bs__icontains=fiscal_year_param) |
                Q(fiscal_year__year_in_ad__icontains=fiscal_year_param)
            )

        return queryset


class VerifyToken(APIView):
    def post(self, request):
        token = request.data.get('token')
        user =  authenticate(username="admin@admin.com", password="Admin123@")
        real_token, created = Token.objects.get_or_create(user=user)
        if token == real_token.key:
            return Response({"isVerified": True}, status=status.HTTP_200_OK)
        else:
            return Response({"isVerified": False}, status=status.HTTP_401_UNAUTHORIZED)

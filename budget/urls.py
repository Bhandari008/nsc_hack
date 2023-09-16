from django.urls import path, include
from rest_framework.routers import DefaultRouter
from budget import views

router = DefaultRouter()
router.register(r'fiscalyears', views.FiscalYearViewSet)
router.register(r'financialestimates', views.FinancialEstimateViewSet)

urlpatterns = [
    # Your other URL patterns
    path('api/', include(router.urls)),
    path('verify-token/', views.VerifyToken.as_view(), name='verify-token')
]

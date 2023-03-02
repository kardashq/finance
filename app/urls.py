from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

app_name = 'api'
router = DefaultRouter()

router.register('transaction', ActionViewSet, basename='transaction')

urlpatterns = [
    path('account/', AccountDetail.as_view(), name='account'),
    path('statistic/', TransactionsAPIView.as_view(), name='statistic'),
    path('statistic/period/', MonthlyStatsView.as_view(), name='period_statistic'),  # example http://127.0.0.1:8000/api/statistic/period/?month=2&year=2023&t=income
    path('statistic/period/download/', MonthlyExportTransactionsView.as_view(), name='period_download'),
    path('statistic/download/', ExportTransactionsView.as_view(), name='download'),
    path('', include(router.urls))
]
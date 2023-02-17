from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

app_name = 'api'
router = DefaultRouter()

router.register('action', ActionViewSet)

urlpatterns = [
    path('statistic/', TransactionsAPIView.as_view()),
    path('account/', AccountDetail.as_view()),
    path('download/', ExportTransactionsView.as_view()),
    path('statistic/period/', MonthlyStatsView.as_view()),  # example http://127.0.0.1:8000/api/stat/period/?month=2&year=2023&t=income
    path('', include(router.urls))
]

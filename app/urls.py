from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import AccountDetail, ActionViewSet, TransactionsAPIView

app_name = 'api'
router = DefaultRouter()

router.register('action', ActionViewSet)

urlpatterns = [
    path('stat/', TransactionsAPIView.as_view()),
    path('account/', AccountDetail.as_view()),
    path('', include(router.urls))
]
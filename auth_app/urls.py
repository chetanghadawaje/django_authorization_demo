from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

from auth_app.views import AddressViewSet, OrderViewSet

router = DefaultRouter()

router.register(r'v1/address', AddressViewSet, basename='address')
router.register(r'v1/order', OrderViewSet, basename='order')

urlpatterns = [
    re_path(r'^', include(router.urls)),
]

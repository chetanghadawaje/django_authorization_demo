from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import viewsets

from auth_app.models import Address, Order
from auth_app.serializer import AddressSerializer, OrderSerializer


class AddressViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):

    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_required = ("address.view_address",)


class OrderViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_required = ("order.view_order",)

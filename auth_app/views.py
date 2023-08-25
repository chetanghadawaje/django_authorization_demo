from rest_framework import viewsets

from auth_app.models import Address, Order
from auth_app.serializer import AddressSerializer, OrderSerializer


class AddressViewSet(viewsets.ModelViewSet):

    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class OrderViewSet(viewsets.ModelViewSet):

    serializer_class = AddressSerializer
    queryset = Order.objects.all()

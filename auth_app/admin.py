from django.contrib import admin
from auth_app.models import Address, Order


class AddressAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Address, AddressAdmin)
admin.site.register(Order, OrderAdmin)

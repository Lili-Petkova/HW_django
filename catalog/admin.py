from django.contrib import admin

from .models import City, Client, Product, Supplier


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


@admin.register(City)
class CityModelAdmin(admin.ModelAdmin):
    list_display = ["city"]


@admin.register(Client)
class ClientModelAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]


@admin.register(Supplier)
class SupplierModelAdmin(admin.ModelAdmin):
    list_display = ["name", "city"]

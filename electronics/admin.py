from django.contrib import admin
from electronics.models import Supplier, Contacts, Products, Arrears
from django.urls import reverse
from django.utils.safestring import mark_safe


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "supplier")
    list_filter = ("contacts__city",)  # фильтр по городам

    def supplier(self, obj):
        """
        ссылка на поставщика
        """
        app_label = obj._meta.app_label
        model_label = obj._meta.model_name
        url = reverse(f"admin:{app_label}_{model_label}_change", args=(obj.id,))
        return mark_safe(f'<a href="{url}">{obj.provider}</a>')

    supplier.short_description = "Поставщик"


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("id", "company", "email", "supplier")

    def supplier(self, obj):
        """
        ссылка на поставщика
        """
        app_label = obj._meta.app_label
        model_label = obj._meta.model_name
        url = reverse(f"admin:{app_label}_{model_label}_change", args=(obj.id,))
        return mark_safe(f'<a href="{url}">{obj.company}</a>')

    supplier.short_description = "Компания"


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "model", "provider")

    def provider(self, obj):
        """
        ссылка на поставщика
        """
        app_label = obj._meta.app_label
        model_label = obj._meta.model_name
        url = reverse(f"admin:{app_label}_{model_label}_change", args=(obj.id,))
        return mark_safe(f'<a href="{url}">{obj.supplier}</a>')

    provider.short_description = "Поставщик"


@admin.register(Arrears)
class ArrearsAdmin(admin.ModelAdmin):
    list_display = ("id", "supplier", "arrears", "provider")
    actions = ["сleaning_up_the_debt"]

    def provider(self, obj):
        """
        ссылка на поставщика
        """
        app_label = obj._meta.app_label
        model_label = obj._meta.model_name
        url = reverse(f"admin:{app_label}_{model_label}_change", args=(obj.id,))
        return mark_safe(f'<a href="{url}">{obj.supplier}</a>')

    provider.short_description = "Поставщик"

    @admin.action(description="Очистить задолженность")
    def сleaning_up_the_debt(modeladmin, request, queryset):
        queryset.update(arrears=0.0)

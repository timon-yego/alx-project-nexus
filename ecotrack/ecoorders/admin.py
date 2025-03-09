from django.contrib import admin
from .models import Order, OrderItem, Payment

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "status", "total_amount", "created_at")
    search_fields = ("user__username", "status")
    list_filter = ("status", "created_at")

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "subtotal")
    search_fields = ("order__id", "product__name")

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "payment_method", "transaction_id", "status", "paid_at")
    search_fields = ("transaction_id", "order__id")
    list_filter = ("payment_method", "status")

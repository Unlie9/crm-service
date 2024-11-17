from django.contrib import admin
from payment.models import Payment, Limit


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
     # Настройка отображения в админке
    list_filter = ('status',)  # Фильтрация по статусу
    search_fields = ('name', 'first_name', 'last_name')  # Поля поиска


@admin.register(Limit)
class LimitAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')  # Настройка отображения лимитов

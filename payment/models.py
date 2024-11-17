from django.db import models
from sitee.models import Site
from invoice.models import Invoice


class Limit(models.Model):
    LIMIT_CHOICES = [
        ("SINGLE_LIMIT", "Разовый лимит"),
        ("MONTHLY_LIMIT", "Месячный лимит"),
        ("MIN_BALANCE_LIMIT", "Минимальный балансовый лимит"),
        ("MAX_BALANCE_LIMIT", "Максимальный балансовый лимит"),
    ]

    name = models.CharField(max_length=64, choices=LIMIT_CHOICES, unique=True)
    value = models.IntegerField()  # Числовое значение для ограничения

    def __str__(self):
        return f"{self.get_name_display()}: {self.value}"


class Payment(models.Model):
    STATUS = [
        ("PENDING", "В ожидании"),
        ("PAID", "Оплачен"),
        ("CLOSED", "Закрыт"),
    ]

    name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    balance = models.IntegerField()
    limits = models.ManyToManyField(Limit, related_name="payments")  # Связь "многие ко многим" с лимитами
    status = models.CharField(max_length=64, choices=STATUS)
    site = models.ForeignKey(Site, null=True, blank=True, on_delete=models.SET_NULL)
    invoice = models.ForeignKey(Invoice, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} ({self.balance})"


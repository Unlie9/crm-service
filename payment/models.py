from django.db import models

from multiselectfield import MultiSelectField

from sitee.models import Site
from invoice.models import Invoice


class Payment(models.Model):
    LIMITS = [
        ("SINGLE_LIMIT", "Разовый лимит"),
        ("MONTHLY_LIMIT", "Месячный лимит"),
        ("MIN_BALANCE_LIMIT", "Минимальный балансовый лимит"),
        ("MAX_BALANCE_LIMIT", "Максимальный балансовый лимит"),
    ]

    STATUS = [
        ("PENDING", "В ожидании"),
        ("PAID", "Оплачен"),
        ("CLOSED", "Закрыт"),
    ]

    name       = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name  = models.CharField(max_length=64)
    balance    = models.IntegerField()
    limit      = MultiSelectField(max_length=64, choices=LIMITS)
    status     = models.CharField(max_length=64, choices=STATUS)
    site       = models.ForeignKey(Site, null=True, blank=True, on_delete=models.SET_NULL)
    invoice    = models.ForeignKey(Invoice, null=True, blank=True, on_delete=models.SET_NULL)

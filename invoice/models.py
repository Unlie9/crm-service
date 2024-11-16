import uuid
from django.db import models


class Invoice(models.Model):
    note   = models.TextField(null=True, blank=True)
    image  = models.ImageField(null=True, blank=True)
    number = models.AutoField(primary_key=True) 
    inv_amount = models.IntegerField(null=True, blank=True, help_text="Сумма за услуги компании")
    
    ord = models.CharField(
        max_length=36,
        unique=True,
        editable=False,
        default=uuid.uuid4
      )

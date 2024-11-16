from django.db import models


class Site(models.Model):
    name    = models.CharField(max_length=64)
    amount  = models.IntegerField()

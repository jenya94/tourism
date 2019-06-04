from django.db import models


class Currency(models.Model):
    currency_name = models.CharField(max_length=100)
    iso_4217_code = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.currency_name}({self.iso_4217_code})"

    @property
    def code(self):
        return self.iso_4217_code


class Price(models.Model):
    amount = models.PositiveIntegerField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

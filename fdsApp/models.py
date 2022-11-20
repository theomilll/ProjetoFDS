from django.db import models


class fdsApp(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    quantity_in_stock = models.IntegerField(null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class computers(models.Model):
    c_name = models.CharField(max_length=100, null=False, blank=False)
    c_quantity_in_stock = models.IntegerField(null=False, blank=False)

    def __str__(self) -> str:
        return self.c_name

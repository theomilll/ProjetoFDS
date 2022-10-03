from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    quantity_in_stock = models.IntegerField(null=False, blank=False)
    booked = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    book_date = models.DataField(auto_now_add=True)
    
    
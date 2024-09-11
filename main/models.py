from django.db import models

# Create your models here.
class ProductEntry(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    product_description = models.TextField(max_length=255)
    available_qty = models.IntegerField()

    @property
    def is_product_sold_out(self):
        return self.available_qty_1 > 0
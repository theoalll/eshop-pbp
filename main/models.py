from django.db import models

# Create your models here.
class ProductEntry(models.Model):
    product_name_1 = models.CharField(max_length=100)
    product_name_2 = models.CharField(max_length=100)
    product_name_3 = models.CharField(max_length=100)
    
    price_1 = models.IntegerField()
    price_2 = models.IntegerField()
    price_3 = models.IntegerField()

    product_description_1 = models.TextField(max_length=255)
    product_description_2 = models.TextField(max_length=255)
    product_description_3 = models.TextField(max_length=255)

    available_qty_1 = models.IntegerField()
    available_qty_2 = models.IntegerField()
    available_qty_3 = models.IntegerField()

    @property
    def is_product_1_sold_out(self):
        return self.available_qty_1 > 0

    @property
    def is_product_2_sold_out(self):
        return self.available_qty_2 > 0

    @property
    def is_product_3_sold_out(self):
        return self.available_qty_3 > 0


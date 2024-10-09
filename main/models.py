import uuid
from django.db import models

# Untuk Menghubungkan Model MoodEntry dengan User
from django.contrib.auth.models import User

# Create your models here.
class ProductEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # menghubungkan satu mood entry dengan satu user melalui sebuah relationship
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    product_description = models.TextField(max_length=255)
    available_qty = models.IntegerField()

    @property
    def is_product_sold_out(self):
        return self.available_qty_1 > 0
    
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    npm = models.IntegerField()
    kelas = models.CharField(max_length=1)
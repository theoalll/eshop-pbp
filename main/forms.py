from django.forms import ModelForm
from main.models import ProductEntry, User

# clean new data
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["product_name", "price", "product_description", "available_qty"]

    def clean_product_name(self):
        product_name = self.cleaned_data["product_name"]
        return strip_tags(product_name)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)

    def clean_product_description(self):
        product_description = self.cleaned_data["product_description"]
        return strip_tags(product_description)

    def clean_available_qty(self):
        available_qty = self.cleaned_data["available_qty"]
        return strip_tags(available_qty)
    

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["name", "npm", "kelas"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_npm(self):
        npm = self.cleaned_data["npm"]
        return strip_tags(npm)

    def clean_kelas(self):
        kelas = self.cleaned_data["kelas"]
        return strip_tags(kelas)
from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'product_name_1' : 'Product name 1',
        'product_name_2' : 'Product name 2',
        'product_name_3' : 'Product name 3',
        
        'price_1' : 1,
        'price_2' : 2,
        'price_3' : 3,

        'product_description_1' : 'Product description 1',
        'product_description_2' : 'Product description 2',
        'product_description_3' : 'Product description 3',

        'available_qty_1' : 1,
        'available_qty_2' : 2,
        'available_qty_3' : 3,
    }

    return render(request, "main.html", context)
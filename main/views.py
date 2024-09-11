from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'product_name' : 'Product name',
        'price' : 1,
        'product_description' : 'Product description',
        'available_qty' : 1,
        
        'nama_aplikasi' : 'PacilBay',
        'nama_aku' : 'Theo Ananda Lemuel',
        'kelas_aku' : 'PBP-A',
        'npm_aku' : '2306165660'
    }

    return render(request, "main.html", context)
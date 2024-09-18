from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import ProductEntry
from django.http import HttpResponse
from django.core import serializers


# formulir pendaftaran pengguna dalam aplikasi web
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# melakukan autentikasi dan login (jika autentikasi berhasil) + logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# mengharuskan pengguna masuk (login) terlebih dahulu sebelum dapat mengakses suatu halaman web.
from django.contrib.auth.decorators import login_required

# untuk Menggunakan Data Dari Cookies
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login')
def show_main(request):
    product_entries = ProductEntry.objects.all()

    context = {
        'product_name' : 'Product name',
        'price' : 1,
        'product_description' : 'Product description',
        'available_qty' : 1,
        'product_entries' : product_entries,
        
        'nama_aplikasi' : 'PacilBay',
        'nama_aku' : request.user.username,
        'kelas_aku' : 'PBP-A',
        'npm_aku' : '2306165660',

        'last_login': request.COOKIES['last_login'], # menambahkan informasi cookie last_login
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        
        product_entry = form.save(commit=False) #mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database
        product_entry.user = request.user
        product_entry.save()
        
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Fungsi ini berfungsi untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

# Fungsi ini berfungsi untuk mengautentikasi pengguna yang ingin login
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main")) # membuat response
        response.set_cookie('last_login', str(datetime.datetime.now())) #membuat cookie last_login dan menambahkannya ke dalam response
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

# Fungsi ini berfungsi untuk melakukan mekanisme logout
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login') # menghapus cookie last_login saat pengguna melakukan logout
    return response
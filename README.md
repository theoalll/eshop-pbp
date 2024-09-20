# README - PacilBay

## *Link* Aplikasi yang Sudah Dideploy
[Aplikasi PacilBay](http://theo-ananda-pacilbay.pbp.cs.ui.ac.id/) (http://theo-ananda-pacilbay.pbp.cs.ui.ac.id/)

<details>
  <summary><h2>Tugas 2: Implementasi *Model-View-Template* (MVT) pada Django (*Click to Expand*)</h2></summary>

### Langkah-langkah Implementasi Aplikasi Berbasis Django

1. **Menyiapkan *development environment*:**
   - Menginstal Python, Django, dan *dependencies* yang dibutuhkan.
   - Membuat *virtual environment* supaya aplikasi tidak bentrok dengan versi lain.

2. **Membuat Proyek Django:**
   - Menjalankan `django-admin startproject pacilbay` untuk membuat proyek baru.
   - Menyesuaikan pengaturan di `settings.py`, seperti konfigurasi *database*, `INSTALLED_APPS`, *allowed host* untuk mengizinkan `localhost` dan PWS mengakses aplikasi.

3. **Membuat Aplikasi Django:**
   - Menjalankan `python manage.py startapp *main*` untuk membuat aplikasi `main` di dalam proyek.
   - Menambahkan aplikasi *main* ke dalam `INSTALLED_APPS` di `settings.py`.

4. **Membuat *Template* HTML:**
   - Membuat *HTML file* di folder `templates` untuk mengatur *view frontend*.
   - Menggunakan *template variables* untuk menampilkan nilai dari variabel yang akan dibuat di `views.py`.

5. **Membuat Model (`models.py`):**
   - Merancang model data dengan membuat *field* pada model di `models.py`.
   - Menjalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk merefleksikan perubahan model ke *database*.

6. **Membuat Views (`views.py`):**
   - Mengimpor fungsi render dari `django.shortcuts` dan menambhakan fungsi `show_main` yang berisi *dictionary* data untuk dikirimkan ke *HTML file*.
   - Menghubungkan views dengan *template HTML* yang akan dirender.

7. **Mengatur *URL Routing* (`urls.py`):**
   - Mengatur *routing *URL** di `urls.py` untuk menambahkan *path* ke aplikasi *main*.
   - Memastikan setiap *view* memiliki *URL *pattern** yang sesuai.

8. **Melakukan *Deployment*:**
    - Membuat proyek baru di *Pacil Web services* (PWS).
    - Mengonfigurasi `settings.py` untuk menambahkan *URL deployment* PWS ke `ALLOWED_HOSTS`.
    - Melakukan *add, commit*, dan *push* ke PWS.

### Bagan *Request* *Client* ke Web Aplikasi Django

```mermaid
graph TD;
    Client -->|Request| *url*s.py;
    *url*s.py -->|Maps *URL*| views.*py*;
    views.py -->|Handles Logic| models.py;
    viewspy* -->|R*enders* *Template*| *template*s;
    models.py -->|Access *Data| *Database**;
    *Database* -->|Returns Data| models.py;
    models.py -->|Returns Data| views.py;
    *template*s -->|DisplaysResponse*| *Client*;
```
**Penjelasan Bagan:**
    - `urls.py`: Menghubungkan *URL* yang diminta ke aplikasi dan data yang tersedia di views.py.
   - `views.py`: Menampung *template variables* untuk menampilkan nilai dari variabel yang sudah dibuat dalam `context`, dan akan di-*render* di halaman HTML.
   - `models.py`: Berisi model data dan menghubungkan ke *database*. `models.py` digunakan oleh `views.py` untuk mengambil dan mengolah data dari variabel yang sudah dibuat.
   - *Template* (HTML): Mengatur tampilan halaman web. *HTML file* akan di-*render* oleh `views.py` dan dikirim sebagai respons ke *client*.

### Fungsi **Git** dalam Pengembangan Perangkat Lunak
Git adalah *control version software* untuk mengelola dan melacak perubahan dalam *source code* selama pengembangan *software*. Fungsi utama git:

1. sebagai ***control version*** yang melacak setiap perubahan yang dibuat di dalam *source code* sehingga *developer* bisa kembali ke versi sebelumnya;
2. sebagai **sarana kolaborasi** karena memungkinkan beberapa *developer* bekerja di berbagai fitur atau memperbaiki bug tanpa mengganggu pekerjaan *developer* lain melalui *branch*.
3. sebagai ***development environment*** melalui *branching* dan *merging* sehingga *developer* bisa membuat cabang untuk pengembangan fitur atau *bug fixing* kemudian menggabungkannya ke *main branch* setelah dites.
4. menjaga **keamanan dan *backup*** karena bisa menyimpan *history* di *remote repository* seperti GitHub, GitLab, dll sehingga mengurangi risiko kode hilang.

### Alasan Menggunakan Django sebagai *Framework* Awal dalam Pembelajaran
1. **Framework Lengkap**
      Django adalah *full-stack *framework** yang menyediakan semua yang dibutuhkan *developer* seperti *Object-Relational Mapping* (ORM), *template engine*, *form handling*, dan *routing*.
2. **Arsitektur MTV (Model-Template-View)**
      Arsitektur *Model-Template-View* (MTV) memudahkan *developer* memahami arsitektur aplikasi web.
3. **Keamanan Terjaga**
      Django menyediakan *middleware* yang otomatis melindungi aplikasi dari *Cross-Site *Request* Forgery* (CSRF) dan juga memiliki mekanisme untuk mencegah *Cross-Site Scripting* (XSS) dengan secara otomatis meng-*escape* output HTML.
4. **Community Support**
      Django memiliki *komunitas* yang besar dan dokumentasi yang lengkap sehingga *beginner friendly :D*

*###* Mengapa Model pada Django Disebut sebagai ORM?
Model pada *Django disebut sebagai* ORM (*Object-Relational Mapping*) karena terdapat *interface* antara model di Python (class) dengan *relational *database** (tabel). Denganprinsip* ini*,* *developer* bisa bekerja menggunakan *database* dengan konsep *object-oriented* tanpa harus membuat query SQL manual. Django ORM mengubah operasi *Create, Read, Update, Delete* (CRUD) di OOP Python ke *query SQL* yang bersifat *connected* dengan *database*, sehingga memudahkan interaksi aplikasi dengan data.
</details>

<details>
  <summary><h2>Tugas 3: Implementasi Form dan Data Delivery pada Django (*Click to Expand*)</h2></summary>

### Langkah-langkah Implementasi Form dan Data Delivery pada Django
1. **Membuat Kerangka *Views* dengan Skeleton**
   Saya membuat kerangka *views* (skeleton) supaya desain web konsisten dan mengurangi *redundant code*. 
   - Buat direktori `templates` di folder utama, buat file `base.html` sebagai kerangka yang akan dipakai untuk semua halaman web di aplikasi-aplikasi lain.
   - Isi `base.html` dengan sintaks HTML dan *Django *template* tags* `{% block meta %}` dan `{% block content %}` untuk bagian-bagian yang bisa diubah oleh *template* turunan di aplikasi-aplikasi lain.
   - Buka `settings.py`, tambahkan direktori `templates` (`'DIRS': [BASE_DIR / 'templates']`) ke dalam variabel `TEMPLATES` supaya *template* yg sudah dibuat dikenali Django.
2. **Mengubah *Primary Key* dari *Integer* Menjadi UUID**
   Untuk meningkatkan keamanan aplikasi, kita ubah *primary key* di model dari tipe data *integer* menjadi UUID (*Universally Unique Identifier*).
   - Pada `models.py` di aplikasi `main`, impor modul `uuid` dan ubah *primary key* menjadi UUIDField.
   - Menjalankan `makemigrations` dan `migrate` supaya perubahan yang kita lakukan disimpen di *database*.
3. **Membuat *Form Input Data***
   - Buat *file* `forms.py` di direktori *main*, dan buat `ModelForm` untuk model `ProductEntry`.
   - Buat *field* yang akan digunakan dalam *form* seperti `product_name`, `price`, `product_description`, dan `available_qty`.
   - Di `views.py`, buat fungsi `create_mood_entry` untuk menampilkan *form* dan menyimpan data baru saat *form* di-*submit* dan mereturn respons html ke *template* `create_product_entry`.
   - Validasi *form* menggunakan *function* `form.is_valid()` dan simpan data dengan *function* `form.save()`.
4. **Menampilkan Data di Halaman Web**
   - Ambil semua objek dari model `ProductEntry` dengan menambahkan *function* `ProductEntry.objects.all()` dan kirim ke *template* melalui *context* yang sudah dibuat sebelumnya. --> *function* ini akan di-*return* dengan html di *template* `main`.
   - Pada `main.html`, kita gunakan *looping* `{% for ... %}` untuk menampilkan data dalam bentuk tabel. 
   - Pada `main.html`, kita tambahkan juga tombol untuk mengakses halaman *form input* data baru.
5. **Mengembalikan Data dalam Bentuk XML dan JSON (dan berdasarkan ID)**
   - Di `views.py`, buat fungsi `show_xml` untuk mengambil semua data dari model `MoodEntry`
   - Gunakan *serializers* Django untuk mengubah data menjadi format XML.
   - Buat juga buat versi jsonnya :)
   - Buat fungsi `show_xml_by_id` dan `show_json_by_id` di views.py untuk *mereturn* data berdasarkan id yang sudah difilter sebagai parameter. --> variabel data diubah dari *all* menjadi `ProductEntry.objects.filter(pk=id)`
6. **Menambahkan *URL *Pattern*s***
   - Tambahkan *path* untuk setiap fungsi *view* baru di variabel `urlpatterns` supaya bisa diakses di browser.
   - Mengecek apakah data bisa diambil dengan benar menggunakan *postman* (screenshoot terlampir di bawah)
Setelah melalui 6 langkah ini, kita bisa membuat form, menyimpan data, menampilkan data, dan *mereturn* data dalam format XML atau JSON di Django

### Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah *platform*?
- Memungkinkan kita berinteraksi secara *real time* dengan *platform*
   Dengan menggunakan *data delivery*, kita bisa mengisi *form*, mengklik tombol, dan melakukan *search*. Data yang di-*input* dalam kegiatan-kegiatan tersebut harus dikirim ke *server* untuk diproses melalui peran *data delivery*. Melalui *data delivery* ini, kita bisa membuat interaksi menjadi lebih interaktif dan dinamis.

- Memunkinkan kita menerima data yang terbaru
   *Data delivery* memastikan bahwa data yang kita terima di *platform* selalu yang terbaru. Data yang realtime sangat dibutuhkan untuk aplikasi berita, cuaca, harga saham, dll yang membutuhkan data real time.

Contoh:
Saat *user* *login* ke *platform*, kredensial kita (misal *username* dan *password*) dikirim ke *server* untuk diverifikasi. Pengiriman tersebut membutuhkan *data delivery* pada *platform*. Tanpa *data delivery*, *user* tidak bisa melakukan *login* dan mengakses akun.

### mana yang lebih baik antara XML dan JSON?
JSON (*JavaScript Object Notation*) dan XML (*eXtensible Markup Language*) adalah format yang digunakan untuk pertukaran data antara *server* dan *client* dalam pengembangan aplikasi. Masing-masing memiliki kelebihan dan kekurangan, tapi JSON dianggap lebih baik daripada XML. Kenapa JSON lebih populer dibandingkan XML?

| Kriteria     | JSON     | XML |
|--------------|-----------|------------|
| Keterbacaan | JSON punya struktur yang lebih ringkas dan mudah dibaca manusia. JSON ditulis dalam format *key-value pairs* sehingga lebih mudah dipahami dan dikelola. | XML menggunakan *opening tag* dan *closing tag* untuk elemen datanya sehingga dokumennya lebih panjang dan lebih sulit dibaca. XML cenderung lebih *verbose* karena harus menggunakan banyak *markup* untuk menulis data.      |
| Ukuran data      | Karena JSON lebih ringkas, ukuran datanya juga lebih kecil dibanding XML. Karena lebih ringkas, lebih sedikit data yang harus dikirim melalui jaringan, sehingga dapat mengurangi waktu *loading* dan penggunaan *bandwidth*. | XML memiliki *overhead* yang lebih besar karena memerlukan *opening tag* dan *closing tag* untuk setiap elemen, yang dapat memperbesar ukuran *file*.        |
| *Compatibility* dengan JavaScript      | JSON adalah format yang berasal dari JavaScript, sehingga kompatibel dengan JavaScript. JSON dapat diubah menjadi objek JavaScript tanpa perlu *parser* lagi.   | XML membutuhkan *parser* untuk mengubah data menjadi objek JavaScript, sehingga lebih lambat dan kompleks.       |
| Keamanan      | JSON lebih aman terhadap serangan seperti *XML External Entity* (XXE) *attack* dibandingkan XML.   | XML lebih rentan terhadap berbagai jenis serangan karena kompleksitas dan fitur-fiturnya seperti DTD (*Document Type Definition*).        |

### Fungsi dari method is_valid() pada *form* Django
1. **Fungsi is_valid() pada Django Form**
   - Fungsi `is_valid()` memeriksa apakah data yang diterima dari *user* (melalui metode POST) memenuhi semua persyaratan yang sudah dibuat dalam form. Jika semua data valid, fungsi akan me-*return* nilai `True`. Jika ada data yang tidak valid, akan me-*return* `False`.
   - Fungsi `is_valid()` juga mengisi atribut `cleaned_data`. Ketika `is_valid()` bernilai `True`, Django akan membersihkan (*sanitize*) data *input* lalu me-*pass* ke dalam atribut `cleaned_data` pada objek *form*. 
   - Jika `is_valid()` mengembalikan `False`, Django akan mengisi atribut `errors` pada objek *form*. Atribut `errors` akan berisi informasi tentang kesalahan validasi yang terjadi pada setiap *field* di *form*.
2. **Mengapa Kita Membutuhkan *Method* is_valid()?**
   - `is_valid()` membantu kita menjaga integritas data karena sudah pasti semua semua data yang disimpan dalam sistem memenuhi persyaratan dan aturan validasi. --> ga mungkin ada data yang tidak lengkap atau formatnya salah.
   - `is_valid()` mencegah serangan keamanan seperti *SQL Injection* atau *Cross-Site Scripting* (XSS) dengan memastikan bahwa data *input* sudah disanitasi sebelum diproses atau disimpan dalam *database*.
   - Tanpa validasi `is_valid()`, data yang tidak valid bisa menyebabkan *error* di aplikasi. Misalnya *user* memasukkan *string* teks ke *field* yang seharusnya menerima *int*.

### Mengapa kita membutuhkan `csrf_token`?
`csrf_token` (*Cross-Site *Request* Forgery token*) adalah mekanisme keamanan saat ada *request form* dan HTTP POST *request*. Token ini melindungi aplikasi web dari serangan *Cross-Site *Request* Forgery* (CSRF) yaitu serangan di mana *attacker* memanipulasi **user** untuk mengirim *request* yang aneh-aneh tanpa diketahui *user*.
1 ***Mengapa *Kita* Membutuhkan `csrf_token` saat Membuat *Form* di *Django*?**
   **CSRF attack** terjadi ketika *attacker* mensabotase *session untuk* melakukan **action** yang tidak diinginkan atas nama *user* tersebut (misalnya *mengubah* *password**,** melakukan transaksi keuangan, dll). `csrf_token` dihasilkan secara *random* dan unik, ditambahkan ke setiap *form* yang memerlukanPOST* (seperti **form** *login*, registrasi, dan *update* data). Sehingga, *attacker* tidak bisa mensabotase *session* tsb. Jika token CSRF tidak valid atau tidak ada, *request* tersebut dianggap mencurigakan dan akan ditolak oleh Django.

2. **Apa yang Dapat Terjadi Jika Kita Tidak Menambahkan `csrf_token` pada *Form* Django?**
   - *Attacker* bisa mengirim *request* berbahaya yang mengirimkan POST *request* ke aplikasi web tanpa sepengetahuan *user*. Jika *user* telah masuk ke aplikasi tersebut, *session* akan digunakan untuk mengautentikasi *request* tersebut.
   - Dengan menggunakan sesi tersebut, *attacker* bisa memanipulasi data, melakukan transaksi, menghapus akun, atau melakukan tindakan lain yang berdampak pada *user* atau sistem.
   - CSRF *attack* dapat mengakibatkan hilangnya data *user*, membocorkan informasi sensitif, dll.
3. **Bagaimana hal tersebut dapat dimanfaatkan oleh *attacker*?**
   - *Attacker* bisa membuat web palsu/email *phishing* yang mengandung *form* HTML atau link berbahaya. Saat *user* masuk ke aplikasi atau mengklik *link* atau mengirim *form*, POST *request* akan dikirim ke *server* menggunakan sesi *user* tersebut.
   - Dengan menggunakan JavaScript atau *hidden element*, *attacker* bisa mengirim data secara otomatis ke aplikasi web target saat *user* reload *webpage* atau melakukan tindakan tertentu (seperti mengklik tombol).
   - Karena permintaan datang dari sesi *user* yang sah, *server* akan mempercayai permintaan tersebut dan menganggap bahwa itu berasal dari *user* yang sah.

### Mengakses keempat *URL* di poin 2 menggunakan Postman
![Screenshot 2024-09-11 193747](https://github.com/user-attachments/assets/ef05be18-d46f-4715-b180-16d83ea98389)
![Screenshot 2024-09-11 193831](https://github.com/user-attachments/assets/584b80e5-c78f-411d-9566-de859f4e3f06)
![Screenshot 2024-09-11 193842](https://github.com/user-attachments/assets/97965ca8-d866-4fd7-9b5d-95f071e0521b)
![Screenshot 2024-09-11 193851](https://github.com/user-attachments/assets/f339cb68-be38-4705-8390-a2217159ba9b)


</details>
<details>
  <summary><h2>Tugas 4: Implementasi Autentikasi, *Session*, dan *Cookies* pada Django (*Click to Expand*)</h2></summary>

### Langkah-Langkah Implementasi Autentikasi, *Session*, dan *Cookies* pada Django
Pada tugas ini, kita akan membangun sistem registrasi dan autentikasi *user* pada aplikasi Django yang telah dibuat. Dengan adanya sistem ini, *user* harus memiliki akun yang valid untuk mengakses halaman utama aplikasi dan hanya dapat melihat data yang terkait dengan akun mereka.

Dalam mengimplementasikan Autentikasi, *Session*, dan *Cookies* pada Django untuk memenuhi *checklist* Tugas 4, terdapat 6 langkah utama yang perlu dilakukan:

1. **Membuat Form untuk Registrasi dan Fungsi yang meng*handle* tugas tersebut**
   -  Pertama, kita akan mengimport modul `UserCreationForm` dan `messages` dari Django untuk membuat form registrasi dan menampilkan pesan notifikasi.
   - Kemudian, kita akan membuat fungsi `register` untuk meng*handle* *user* yang akan melakukan registrasi akun. Fungsi ini memiliki 6 fungsi utama:
      1. Menampilkan form registrasi saat pertama kali diakses.
      2. Memproses *data form* ketika *user* mengirimkan data.
      3. Memvalidasi data yang dimasukkan *user*.
      4. Menyimpan *data* *user* baru ke dalam *database*.
      5. Menampilkan pesan sukses jika pendaftaran berhasil.
      6. Mengarahkan *user* ke halaman *login*.
   - Setelah membuat fungsi `register`, kita akan membuat *template* `register.html` sebagai tampilan form registrasi. Pada *template* tersebut, kita menggunakan tag `{{ form.as_table }}` untuk menampilkan *field-field* form secara otomatis.
   - Terakhir, kita akan menambahkan *URL* *Pattern* di `urls.py` sehingga *user* bisa mengakses halaman `/register` dan melakukan registrasi dengan fungsi `register`.
2. **Membuat *Login Form***
   - Pertama, kita akan mengimpor modul `AuthenticationForm`, `authenticate`, dan `login` dari Django untuk meng*handle* proses autentikasi.
   - Setelah itu, kita akan membuat fungsi `login_user` untuk meng*handle* *user* yang akan melakukan *login* ke aplikasi. Fungsi ini memiliki 5 fungsi utama:
      1. Memproses data *login form*.
      2. Memvalidasi data *login*.
      3. Melakukan autentikasi *user*.
      4. Membuat *session* untuk *user* yang berhasil *login*.
      5. Mengarahkan *user* ke halaman utama (aplikasi *main*).
   - Setelah membuat fungsi `login_user`, kita akan membuat *template* `login.html` sebagai tampilan halaman *login*. 
   - Terakhir, kita akan menambahkan *URL* *Pattern* di `urls.py` sehingga *user* bisa mengakses halaman `/login` dan melakukan autentikasi dengan fungsi `login_user`.
3. **Membuat Fungsi *Logout***
   - Pertama, kita akan mengimpor modul `logout` dari Django untuk meng*handle* proses *logout*.
   - Setelah itu, kita akan membuat fungsi `logout_user` untuk meng*handle* *user* yang akan melakukan *logout*. Fungsi ini memiliki 3 fungsi utama:
      1. Menghapus *user* *session* yang sedang aktif.
      2. Mengarahkan *user* ke halaman *login*.
      3. Hapus *cookie* `last_login`.

   - Setelah membuat fungsi `logout_user`, kita akan membuat tombol *logout* pada halaman utama dan menghubungkannya dengan fungsi `logout_user`. 
   - Terakhir, kita akan menambahkan *URL* *Pattern* di `urls.py` sehingga *user* bisa mengakses halaman `/logout` dan mengakses fungsi `login_user`.

4. **Merestriksi Akses Halaman Utama**
   
   Kita hanya ingin halaman utama dapat diakses oleh *user* yang sudah melakukan *login*. Oleh sebab itu, kita perlu melakukan restriksi akses ke halaman utama terbatas kepada *user* yang sudah melakukan *login*. Kita akan menggunakan *decorator* `login_required` pada fungsi `show_main` yang sudah dibuat sebelumnya untuk memastikan hanya *user* yang sudah *login* yang dapat mengakses halaman utama.

5. **Menggunakan *Cookies* untuk Menyimpan Data *Login* Terakhir**
   - Kita akan menyimpan data *login* terakhir dengan menambahkan kode `response.set_cookie('last_login', str(datetime.datetime.now()))` di fungsi `login_user` untuk menyimpan waktu *login* terakhir dalam bentuk *cookie* saat *user* berhasil *login*.
   - Setelah menyimpan data *login* terakhir, kita akan menampilkannya pada halaman utama dengan cara menambahkan informasi *cookie* `last_login : *request*.COOKIES['last_login']` pada `context` di `views.py` lalu memanggil nilainya di halaman utama (`main.html`)
   - Kita juga akan menghapus *cookie* saat *user* *logout* dengan menambahkan kode `response.*delete_cookie*('last_login')` di fungsi `logout_user`

6 ***Menghubungkan *Model* `ProductEntry` dengan `User`**

   Kita ingin seorang **user* hanya* melihat *product* *entries* yang telah dibuat sendiri. Oleh karena itu, kita perlu menghubungkan model `ProductEntry` dengan `User dengan* cara*:*
   - Tambah *field* `user` yang bertipe `ForeignKey` pada model `ProductEntry`  untuk menghubungkan setiap entri *product* dengan *user* yang membuatnya.
   - Setelah membuat *field* `user`, kita akn mengubah fungsi `create_product_entry` untuk menyimpan *user* yang sedang *login* sebagai pemilik entri mood dengan meset variabel *user* di model `ProductEntry` dengan menambahkan kode `product_entry.user = *request*.user`
   - Selanjutnya, kita akan memfilter data `ProductEntry` supaya hanya menampilkan entri *product* yang dimiliki oleh *user* yang sedang *login* dengan mengubah variabel `product_entries` di fungsi `show_main` *yang* awalnya bernilai `MoodEntry.objects.all()` menjadi `MoodEntry.objectsfilter*(u*ser*=request.user)`
   - Setelah membuat perubahan pada model `ProductEntry*`, kita melakukan* migrasi untuk memperbarui struktur *database*.

### Perbedaan antara `HttpResponseRedirect()` dan `redirect()`
|Kriteria*     | `*HttpResponseRedirect*()`     | `redirect()` |
|--------------|-----------|------------|
| *Level of abstraction*|Merupakan *low level function* sehingga *developer* bisa memiliki kontrol yang lebih besar untuk pengaplikasian fungsi tersebut. `HttpResponseRedirect()` bisa mengatur atribut-atribut *HTTP respons* (misalnya *status code*, *header*, *cookie*, dll). | Merupakan *high level function* yang merupakan *shortcut* dari `HttpResponseRedirect()`. `redirect()` menyederhanakan proses pembuatan objek `HttpResponseRedirect` karena secara otomatis mengatur *status code* dan *header* yang biasanya digunakan untuk *redirect*.|
| Penggunaan | Biasanya digunakan dalam situasi yang memerlukan *HTTP response *custom*ization* yang lebih detail. Contoh: ketika mau mengatur *status code* yang berbeda (misal, 301 untuk *redirect permanen*) atau menambahkan *header *custom**. | Biasanya lebih sering dipakai karena lebih mudah digunakan dan cukup fleksibel untuk kebutuhan *redirect* (tanpa situasi khusus/*customization*). |
| Contoh Penggunaan | <pre lang="python">from django.http import HttpResponseRedirect<br># Menggunakan HttpResponseRedirect()<br>def my_view(request):<br>    response = HttpResponseRedirect('/success/')<br>    response['Location'] = 'https://example.com'  # Mengatur lokasi *redirect* secara manual<br>    return response</pre>| <pre lang="python">from django.shortcuts import redirect <br># Menggunakan redirect()<br>def my_view(request):<br>    return redirect('success')  # Menggunakan *URL* name</pre>|
| Kapan sebaiknya digunakan?| <li>Ketika perlu mengontrol secara detail *status code* atau *header response*</li><li>Ketika mau melakukan *redirect* ke *URL* yang tidak didefinisikan dalam `URLconf`. |  <li>Ketika mau melakukan *redirect* sederhana ke *URL* yang sudah didefinisikan di `URLconf`.</li><li>Ketika tidak melakukan *customization HTTP respons* yang kompleks</li>|

Secara garis besar, `redirect()` lebih banyak digunakan karena lebih mudah dibaca, lebih terintegrasi dengan Django, dan lebih fleksibel. Tapi, `HttpResponseRedirect()` tetap berguna ketika perlu melakukan *redirect* permanen (301), *header *custom*ization*, dan *redirect* ke *URL* eksternal.

### Cara kerja penghubungan model `ProductEntry` dengan `User`
Dalam Django, kita menghubungkan satu model dengan model lainnya untuk merepresentasikan hubungan antara data. Dalam kasus ini, kita mau menghubungkan model `ProductEntry` dan `User` karena kita ingin mengetahui siapa yang membuat entri *product* tersebut. Hubungan ini disebut **relasi** atau hubungan antar model.

Pada penghubungan model, kita menggunakan `ForeignKey`. `ForeignKey` adalah tipe *field* dalam Django yang digunakan untuk membuat hubungan *one-to-one* atau *one-to-many* antara dua model. Dalam kasus `ProductEntry` dan `User`, `ForeignKey` akan membuat sebuah kolom tambahan dalam tabel `ProductEntry` yang berisi ID dari *user* yang bersangkutan. Sehingga, setiap entri *product* akan menunjuk ke satu *user* tertentu (yang membuatnya).

**Cara Kerja Penghubungan `MoodEntry` dengan `User`**
1. Tambah *Field* `user` pada model `ProductEntry`
   
   Di file `models.py`, kita tambahkan *field* `user` dengan tipe `ForeignKey` ke model `MoodEntry`.
   <pre lang="python">
      from django.db import models
      from django.contrib.auth.models import *User*

      class MoodEntry(models.Model):
         *user* = models.ForeignKey(User, on_delete=models.CASCADE)
         # ... dst
   </pre>
   
2. Atur parameter `on_delete`
   Parameter `on_delete` berfungsi untuk mengatur apa yang terjadi pada data ketika objeknya dihapus. Kita akan assign nilai parameter dengan `models.CASCADE` berarti jika *user* dihapus, maka semua entri *product* yang terkait dengan *user* tersebut juga akan dihapus.
3. Simpan perubahan
   Setelah melakukan perubahan pada model, kita akan menjalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk membuat dan menerapkan perubahan pada *database*.

### Implementasi *authentication* dan *authorization* saat *user* *login* dalam Django
1. Perbedaan *authentication* dan *authorization*, apakah yang dilakukan saat *user* *login*

   | Kriteria | Authentication | Authorization |
   |--------------|-----------|------------|
   | Definisi| Proses verifikasi identitas *user*. Menjawab pertanyaan "**Siapa** kamu?" | Proses pemberian izin kepada *user* yang sudah terverifikasi untuk mengakses *resources* atau melakukan *request*. Menjawab pertanyaan "**Apa yang boleh** kamu lakukan?".|
   | Tujuan| Memastikan bahwa *user* adalah orang yang dia klaim (benar-benar dia)| Mengontrol akses ke bagian-bagian sistem yang berbeda berdasarkan *role* *user*|
   | Mekanisme | Biasanya menggunakan kredensial seperti *username* dan *password*, biometrik (sidik jari, wajah), token, atau OTP (*One-Time Password*)| Menggunakan kebijakan akses seperti *role-based access control* (RBAC) atau *attribute-based access control* (ABAC)|
   | Contoh| Memasukkan *username* dan *password* untuk masuk ke akun email, misalnya *login* ke SCELE | Jika *user* memasukkan *username* dan *password* yang terasosiasi dengan *role* dosen, maka ia bisa membuat course baru, sedangkan jika *user* memasukkan *username* dan *password* yang terasosiasi dengan *role* mahasiswa, maka ia tidak bisa membuat course baru|
   | Implementasi| Kebanyakan menggunakan *library* atau *framework* autentikasi yang sudah jadi| Biasanya diimplementasikan dengan menggunakan *role*, *permission*, atau kebijakan yang lebih *custom* |
   | Urutan Proses| Biasanya dilakukan duluan sebelum otorisasi| Dilakukan setelah autentikasi berhasil|
2. Bagaimana Django mengimplementasikan kedua konsep tersebut
   - Autentikasi di Django
      1. Model `User`: Django memiliki model `User` bawaan yang menyimpan informasi dasar seperti *username*, *password*, email, dll. Kita juga bisa meng-*custom* model tersebut.
      2. Form autentikasi: Django menyediakan form `AuthenticationForm` yang bisa digunakan untuk meng*handle* *login* *user*. Form ini memeriksa apakah *username* dan *password* yang dimasukkan cocok dengan data yang ada di *database*.
      3. *Middleware*: Berfungsi untuk memeriksa apakah *user* sudah melakukan *login* atau belum. Jika belum, *user* akan diarahkan ke halaman *login*.
      4. *Session*: Django menggunakan *session* untuk menyimpan informasi tentang *user* yang sedang *login*, sehingga sistem dapat mengetahui siapa yang sedang berinteraksi dengan aplikasi.

   - Otorisasi di Django
      1. *Permission*: Kita bisa membuat *permission* (izin) yang spesifik untuk setiap model atau *action*. Misal, kita bisa memberikan izin `delete_product` untuk menghapus produk bagi *role* admin.
      2. *Group*: Kita bisa mengelompokkan *permission* ke dalam *group*. Contoh: *group* "client" memiliki *permission* "add_to_cart", "buy_items",dan* "delete_from_cart".      
      3*. *Custom* *Permission*: Kita bisa membuat *permission* *custom* untuk kebutuhan spesifik.

### Peran *cookies* dalam mengingat* *user* yang telah *login*, keamanan *cookies*
1. Bagaimana Django mengingat* *user* yang telah *login*?
   Django menggunakan sistem *session* untuk mengingat *user* yang telah *login*. 
   
   - Pembuatan *Session*
      Ketika *user* berhasil *login*, Django akan membuat sebuah *session* yang unik untuk *user* tersebut. *Session* ini akan disimpan di server, bukan di browser pengguna. Setiap *session* memiliki *session* ID yang unik. *Session* ID tersebut akan dikirimkan ke browser *user* melalui *cookie*.
   - *Cookie* *Session* *ID*
      Browser *user* akan menyimpan *cookie* *session* *ID* yang sudah dibuat saat *user* *login*. Setiap kali *user* mengirim *request* ke server, *cookie* *session* *ID* ini akan ikut dikirim dalam *header* *request*.
   - Pencocokan *Session*
      Django akan memeriksa *cookie* *session* *ID* yang dikirim oleh browser. Jika *session* *ID* valid, Django akan mengambil data *session* dari server dan mengidentifikasi bahwa* *user** tersebut sudah *login*. Namun, jika *request* tidak mengandung *session ID* atau *session ID* tidak valid, django akan mengidentifikasi bahwa *user* tersebut belum *login* dan menolak *request* yang dikirim*.
*2*. Kegunaan lain dari *cookies* dan keamanan *cookies*
   - Meningkatkan *user* *experience*      
      Dengan menggunakan *cookies*, *website* bisa mengingat pengaturan *user* (misal: *font* *size, color* *theme*, atau *page layout*). 
   - Analisis Web
      *Cookies membantu* melacak perilaku *user* di website (misal: halaman yang* sering *dikunjungi*, durasi, pola *click*, dll)
   - Iklan
      *Cookies* dapat digunakan oleh perusahaan pengiklan untuk membuat *user profile* berdasarkan minatdan* perilaku *user* di berbagai website. *User profile* ini kemudian digunakan untuk menampilkan iklan yang relevan dengan minat pengguna.
3. Apakah semua *cookies* aman digunakan?
   Tidak semua *cookies* aman digunakan. Meskipun *cookies* memiliki banyak manfaat, terdapat beberapa risiko antara lain:
   - *Cookies* bisa dipakai untuk melacak aktivitas *user* sehingga memungkinkan pihak tertentu membuat profil rinci tentang minat dan kebiasaan pengguna. Hal ini bisa saja merupakan pelanggaran privasi.
   - Jika *cookies* tidak dikelola dengan aman, data yang tersimpan bisa dicuri. Hal ini menyebabkan informasi sensitif (misal kata sandi, informasi kartu kredit, dll) bisa bocor.
   - *Cross-Site Scripting* (XSS). *Cookies* bisa digunakan untuk melakukan XSS, di mana *attacker* menyuntikkan skrip ke dalam situs web yang kemudian dieksekusi di browser pengguna.
   - *Cookie* Poisoning untuk memodifikasi isi *cookie* untuk menipu server.
</details>
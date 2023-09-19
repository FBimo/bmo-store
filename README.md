# Tugas 2 PBP 2023

## Implementasi Checklist

### Membuat Proyek Django

1. Saya membuat sebuah folder khusus di komputer sebagai tempat proyek Django akan disimpan.

2. Di dalam folder tersebut, saya melakukan inisiasi awal untuk menyediakan repositori lokal yang kosong di dalam komputer dengan menjalankan perintah `git init`.

3. Setelah itu, saya melakukan konfigurasi awal _user_ dan _email_ dengan perintah,

    ```
    git config user.name <nama_user>
    git config user.email <nama_email>
    ```

4. Selanjutnya saya memeriksa terlebih dahulu bahwa konfigurasi yang dilakukan sudah terdaftar dengan perintah,

    ```
    git config --list --local
    ```

5. Apabila _user_ dan _email_ yang sudah dikonfigurasi sebelumnya muncul di keluaran perintah sebelumnya, saya dapat melanjutkan langkah berikutnya, yaitu membuat repositori baru di GitHub dengan nama repositori yang sama seperti repositori proyek lokal.

6. Berikutnya, di dalam repositori lokal proyek, saya menambahkan sebuah _file_ `README.md` dan menuliskan **Tugas 2 PBP 2023** sebagai judul.

7. Setelah itu, perlu dilakukan penghubungan antara repositori lokal di komputer dengan repositori di GitHub dengan cara menggunakan perintah,

    ```
    git branch -M main
    ```

    > Perintah di atas berguna untuk membuat cabang atau _branch_ utama baru yang bernama **main**

    Setelah itu, perlu dijalankan perintah,

    ```
    git remote add origin <URL_RepoGitHub>
    ```

    > Perintah di atas berguna untuk menghubungkan repositori di GitHub dengan repositori lokal.

8. Setelah kedua repositori terhubung, perlu dilakukan penyimpanan atas pembaruan yang sudah dilakukan di repositori lokal dengan perintah,

    ```
    git add .
    ```

    > Perintah di atas berguna untuk menandai semua file yang berubah di dalam repositori lokal yang nantinya akan dilakukan _commit_. 
    
    Setelah itu, dapat dijalankan,

    ```
    git status
    ```

    > Perintah di atas berguna untuk memeriksa status _file_ apa saja yang sudah dimodifikasi dan ditandai. 
    
    Setelah itu dapat dilakukan perintah,

    ```
    git commit -m <pesan_commit>
    ```

    Perintah di atas berguna untuk melakukan _commit_ atas perubahan yang terjadi di repositori lokal. Berikutnya dapat dilakukan,

    ```
    git push -u origin main
    ```

    > Perintah di atas berguna untuk menyimpan perubahan-perubahan yang terjadi di repositori lokal ke repositori GitHub, termasuk jika adanya penambahan _file_ baru.

9. Setelah penyimpanan berhasil, saya membuat _virtual environment_ dengan menjalankan perintah,

    ```
    python -m venv env
    ```

    > Perintah di atas berguna untuk membuat _virtual environment_. Hal ini berguna untuk mengisolasi _package_ serta _dependencies_ dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer lokal.

10. Setelah itu, saya perlu mengaktifkan _virtual environment_ dengan menjalankan,

    ```
    env\Scripts\activate.bat
    ```

11. Berikutnya saya menambahkan `requirements.txt` di dalam direktori proyek dengan isi sebagai berikut,

        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3

    Setelah itu, saya  melakukan perintah berikut,

    ```
    pip install -r requirements.txt
    ```

    > Perintah di atas berguna untuk memasang _dependencies_ di dalam direktori proyek

12. Selanjutnya, saya dapat membuat proyek Django baru dengan perintah,

    ```
    django-admin startproject <nama_proyek> .
    ```

### Membuat Aplikasi dengan Nama 'main'

1. Pertama, saya memastikan bahwa direktori pengerjaan di direktori proyek dan _virtual environtment_ telah diaktifkan.

2. Selanjutnya saya membuat aplikasi **main** dengan menjalankan perintah,

    ```
    python manage.py startapp main
    ```

    > Setelah perintah di atas dijalankan, di dalam direktori proyek akan ada sebuah direktori baru bernama **main**, direktori inilah yang berisi struktur dasar dari aplikasi **main**.

3. Sebelum menjalankan _routing_ agar aplikasi dapat berjalan, saya melakukan beberapa implementasi dasar terhadap struktur awal aplikasi, seperti

    - Mendaftarkan aplikasi **main** ke dalam proyek dengan menambahkan '**main**' ke dalam daftar aplikasi yang ada di bagian `INSTALLED_APPS` pada `settings.py` seperti kode di bawah ini,

        ```
        INSTALLED_APPS = [
            ...,
            'main',
            ...
        ]
        ```
        
    - Membuat dan mengisi _file_ `main.html` untuk membuat struktur dan tampilan dasar pada halaman _web_.

    - Menambah isi dari `models.py` di dalam direktori aplikasi `main` untuk mendefinisikan model baru. Di dalam model inilah kita dapat mengelola data dari aplikasi.

    - Membuat migrasi model agar Django dapat melacak pembaruan yang terjadi di `models.py` dengan perintah,

        ```
        python manage.py makemigrations
        ```
        
        > Perintah di atas berguna untuk menciptakan berkas migrasi berupa perubahan model. 
        
        Setelah itu perlu menjalankan perintah,

        ```
        python manage.py migrate
        ```
        
        > Perintah di atas berguna untuk mengaplikasikan perubahan yang terjadi pada model ke basis data.

    - Mengintegrasikan komponen `views.py` yang dapat menangani bagaimana data yang dikelola model ditampilkan kepada pengguna dengan menambahkan kode awal sebagai berikut,

        ```
        from django.shortcuts import render
        ```
        
        > Kode di atas berguna untuk mengimpor fungsi `render` yang berfungsi untuk melakukan _render_ tampilan HTML dengan menggunakan data yang diberikan.
    
### Melakukan _Routing_ pada Proyek

Untuk mengatur _routing_ tingkat proyek, saya perlu membuka `urls.py` di dalam direktori proyek, lalu menambahkan kode,

    from django.urls import path, include

        urlpatterns = [
            ...
        path('main/', include('main.urls')),
            ...
        ]

> Perlu diperhatikan bahwa fungsi `include` di atas berguna untuk mengimpor rute URL dari aplikasi lain ke dalam `urls.py` proyek dan _path_ `'main/'` nantinya akan diarahkan ke rute yang didefinisiakn dalam `urls.py` aplikasi `main`.
    
### Membuat Model pada Aplikasi 'main'
Berikut model yang saya tambahkan ke dalam `models.py`,

        from django.db import models
        class Item(models.Model):
            name = models.CharField(max_length=255)
            amount = models.IntegerField()
            date_added = models.DateField(auto_now_add=True)
            price = models.IntegerField()
            description = models.TextField()
            
Ada beberapa istilah penting yang perlu diperhatikan, seperti
- `Item` adalah nama model.
- `models.Model` merupakan kelas dasar yang digunakan untuk mendefinisikan model dalam Django.
- `name`, `amount`, `date_added`, `price`, dan `description` adalah atribut pada model dan setiap _field_ memiliki tipe data, seperti `Charfield`, `IntegerField`, `DateField`, dan `TextField`.

### Membuat Fungsi pada views.py

Berikut fungsi pada `views.py` untuk mengembalikan **nama aplikasi**, **nama**, dan **kelas** saya,

    from django.shortcuts import render
    
        def show_main(request):
            context = {
                'my_app': 'Bmo Store',
                'name': 'FBmo',
                'class': 'PBP C'
            }

            return render(request, "main.html", context)

Ada beberapa istilah penting yang perlu diperhatikan, seperti
- `def show_main(request)` adalah deklarasi fungsi `show_main` yang menerima parameter `request`. Fungsi ini mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai.
- `context` adalah _dictionary_ data yang akan dikirimkan ke tampilan.
- `return render(request, "main.html", context)` berguna untuk melakukan render tampilan `main.html`.

### Membuat _Routing_ pada urls.py Aplikasi main

Setelah membuat fungsi pada `views.py`, saya perlu membuat _routing_ pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat dengan kode sebagai berikut,

    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]

Ada beberapa istilah penting yang perlu diperhatikan, seperti
- Impor `path` dari `django.urls` untuk mendefinisikan pola URL.
- `app_name` merupakan variabel dari nama unik pada pola URL dalam aplikasi.
- Fungsi `show_main` dari `main.views` digunakan sebagai tampilan yang akan ditampilkan ketika URL terkait diakses.
    
### Melakukan _Deployment_ ke Adaptable

1. Saya _Login_ ke akun Adaptable menggunakan GitHub.
2. Saya memilih `New App` lalu `Connect an Existing Repository`.
3. Saya menghubungkan Adaptable dengan GitHub dengan memilih `All Repositories` pada proses instalasi.
4. Saya memilih repositori proyek dan memilih _branch_ untuk dijadikan _deployment branch_. 
5. Saya memilih `Python App Template` sebagai _template deployment_.
6. Saya memilih `PostgreSQL` sebagai tipe basis data yang akan digunakan.
7. Saya memilih versi Python yang sesuai dengan veris yang dimiliki.
8. Saya memasukkan perintah `python manage.py migrate && gunicorn <nama_proyek>.wsgi` pada bagian `Start Command`. 
9. Saya memasukkan nama aplikasi saya yang sekaligus akan menjadi nama _domain_ situs _web_ aplikasi.
10. Saya mencentang bagian `HTTP Listener on PORT` dan meng-klik `Deploy App` untuk memulai proses _deployment_.
11. Setelah proses _deployment_ selesai, saya mendapatkan tautan menuju aplikasi yang baru saja diluncurkan.

Tautan aplikasi: [Marpellus Cenep](https://marpellus-cenep.adaptable.app)
    

## Bagan _Request Client_
![django-request-flow](https://github.com/FBimo/marpellus-cenep/assets/119420957/9b1d3f76-0013-4b6f-a539-8974df6099a5)

- `urls.py`, sebagai tempat perkumpulan URL. Django akan mencari melewati _file_ ini untuk menemukan URL yang paling cocok sesuai dengan permintaan.
- `views.py`, sebagai jembatan penghubung dengan dua _file_ lainnya, yaitu `models.py` dan `template`. Setelah mendapat HttpRequest dari URL yang berkaitan, `views.py` dapat meminta data yang diperlukan melalui `models.py` dan dapat melakukan _render_ HTML menggunakan `template` agar dapat disajikan kepada pengguna.
- `models.py`, sebagai pengolah data dan penghubung antara _database_ dengan `views.py`. `models.py` dapat melakukan manipulasi struktur data aplikasi sesuai kebutuhan pengguna.
- `template`, struktur tampilan antarmuka pengguna yang akan membantu `views.py` dalam melakukan proses _render_ HTML.

## Alasan Penggunaan _Virtual Environment_
_Virtual Environment_ merupakan _tools_ untuk membuat lingkungan Python virtual yang terisolasi. Terisolasi di sini maksudnya versi-versi dependensi atau _packages_ yang ada di dalam lingkungan virtual tidak akan berpengaruh dengan versi dependensi yang ada di komputer lokal. Penggunaan virtual env cukup umum ketika ingin membuat proyek Django karena dengan adanya lingkungan isolasi, Python yang digunakan untuk menjalankan proyek Django tidak akan terganggu dengan pembaruan yang terjadi di komputer lokal (jika ada pembaruan) sehingga proyek dapat tetap berjalan walaupun adanya perubahan versi modul Python di komputer lokal. Sebuah proyek Django sebenarnya dapat tetap dijalankan jika tidak menggunakan virtual env, namun ada kemungkinan proyek akan mengalami gangguan karena adanya perubahan modul akibat perubahan versi modul di komputer lokal. Oleh karena itu, virtual env sangat disarankan apabila kita ingin membuat suatu proyek berbasis Django. 

## Penjelasan MVC, MVT, dan MVVM
### MVC
**Model View Controller** adalah salah satu pola arsitektur dalam pembuatan aplikasi dengan bagian-bagian seperti berikut,

- `Model`, betugas untuk menyiapkan, mengatur, memanipulasi, dan mengorganisasikan data yang ada di dalam _database_.

- `View`, bertugas untuk merepresentasikan informasi atau data yang telah dikelola oleh model agar dapat dilihat pengguna.

- `Controller`, bertugas untuk menghubungkan serta mengatur `model` dan `view` agar dapat saling terhubung.

Contoh _framework_ yang menggunakan MVC adalah Spring Boot.

### MVT
**Model View Template** merupakan pola arsitektur pengembangan aplikasi yang dapat dikatakan mirip dengan MVC, namun memiliki perbedaan di bagian `controller`. Pada MVT, `controller` diganti menjadi `template`. `Template` inilah yang akan menjadi representasi tampilan yang diperlihatkan kepada pengguna yang biasanya menggunakan HTML. 

- `Model`, bertugas untuk mengatur dan mengelola data dari aplikasi.

- `View`, bertugas untuk mengontrol bagaimana data yang dikelola oleh `model` akan ditampilkan kepada pengguna.

- `Template`, bertugas mengatur tampilan yang diperlihatkan kepada pengguna.

Contoh _framework_ yang menggunakan MVT adalah Django. 

### MVVM
**Model View ViewModel** merupakan gabungan dari MVC dan MVP.

- `Model`, terdiri dari data dasar yang digunakan untuk menjalankan aplikasi.

- `View`, sebagai antarmuka pengguna dan pola desain, mirip seperti yang digunakan oleh MVC.

- `ViewModel`, di satu sisi adalah abstraksi dari `View`, lalu sisi yang lain sebagai penyedia pembungkus model data yang akan ditautkan. `ViewModel` terdiri dari `Model` yang diubah menjadi `View` dan berisi perintah yang dapat digunakan oleh `View` untuk memengaruhi `Model`.

Contoh _framework_ yang menggunakan MVVM adalah WPF.

## Bonus
Berikut merupakan implementasi saya dalam melakukan _testing_ dasar lainnya,

    
    from django.test import TestCase, Client
    from main.models import Item

    #another test
    def setUp(self):
        Item.objects.create(name="sunspot", amount=1, price=5000, description='Gain atk power with unspent energy', atk_power=50)
        Item.objects.create(name="hawkeye", amount=1, price=5000, description='Gain 3 atk power if you play card here next turn', atk_power=45)
    
    def test_get_desc(self):
        sunspot = Item.objects.get(name="sunspot")
        hawkeye = Item.objects.get(name="hawkeye")
        self.assertEqual(sunspot.get_desc(), "Gain atk power with unspent energy")
        self.assertEqual(hawkeye.get_desc(), "Gain 3 atk power if you play card here next turn")
    

_Testing_ ini berguna untuk mengetahui bahwa program dapat membuat sebuah objek `Item` baru dan menjalankan suatu fungsi yang memanggil salah satu atributnya, dalam hal ini adalah atribut `description`. Di bawah ini merupakan hasil dari tesnya,

    
    (env) PS C:\Users\fzlbm\UI\Kuliah\Semester_3\PBP\github\marpellus-cenep> python manage.py test
    Found 3 test(s).
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 0.056s

    OK
    Destroying test database for alias 'default'...

# Tugas 3 PBP 2023

## Implementasi Checklist

### Membuat Form Input Data
1. Sebelum saya membuat sebuah _form_ untuk menginput data baru ke dalam aplikasi, saya perlu membuat kerangka views sebagai _template_ dari sebuah laman di situs agar dapat mengurangi menulis kode secara berulang.

2. Berikut merupakan kode `base.html` yang diletakkan pada folder `templates` di _root folder_,

    ```
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta
                name="viewport"
                content="width=device-width, initial-scale=1.0"
            />
            {% block meta %}
            {% endblock meta %}
        </head>

        <body>
            HEADER
            {% block content %}
            {% endblock content %}
            <br/><br/>
            FOOTER
        </body>
    </html>
    ```

3. Agar `base.html` terdeteksi sebagai _template_, saya perlu membuka `settings.py` pada subdirektori `marpellus_cenep` dan sedikit memodifikasi bagian `TEMPLATES` menjadi seperti ini,

    ```
    ...
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
            'APP_DIRS': True,
            ...
        }
    ]
    ...
    ```

4. Setelah itu, saya perlu mengunjungi subdirektori `templates` yang ada di di direktori `main` untuk mengubah sedikit `main.html`,

    ```
    {% extends 'base.html' %}

    {% block content %}
        <h1><b>{{my_app}}</b></h1>

        <h5>Name: </h5>
        <p>{{ name }}<p>
        <h5>Class: </h5>
        <p>{{ class }}<p>

        ...
    {% endblock content %}
    ```

    > dengan adanya `{% extends 'base.html' %}`, `main.html` sekarang sudah menggunakan `base.html` sebagai _template_.

5. Selanjutnya saya dapat langsung membuat `forms.py` pada direktori `main` sebagai struktur _form_ yang dapat menerima data produk baru dengan kode,

    ```
    from django.forms import ModelForm
    from main.models import Card

    class ProductForm(ModelForm):
        class Meta:
            model = Card
            fields = ["name", "amount", "price", "power", "energy_cost", "description"]
    ```

    Ada beberapa istilah penting yang perlu diperhatikan, seperti
    - `model = Card` berfungsi untuk menunjukkan model yang digunakan di _form_.
    - `fields = ["name", "amount", "price", "power", "energy_cost", "description"]` merupakan atribut-atribut yang dimiliki oleh model `Card`. 

### Modifikasi 'views' dan _Routing_ URL untuk Melihat Objek Model yang Sudah Ditambahkan

1. Pada _file_ `views.py` di foler `main`, perlu ditambahkan kode berikut,

    ```
    from django.http import HttpResponseRedirect
    from main.forms import ProductForm
    from main.models import Card
    from django.urls import reverse
    ```

2. Setelah itu saya membuat fungsi baru dengan nama `create_product` yang menerima parameter `request` untuk menghasilkan formulir yang dapat menambahkan data produk secara otomatis ketikad ata sudah di-_submit_ melalui _form_.

    ```
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_product.html", context)
    ```

    Ada beberapa istilah penting yang perlu diperhatikan, seperti
    - `form = ProductForm(request.POST or None)` berguna untuk membuat `ProductForm` baru dengan memasukkan QueryDict berdasarkan input _user_ pada `request.POST`.
    - `form.is_valid()` berguna untuk memvalidasi isi input dari _form_.
    - `form.save` berguna untuk membuat dan menyimpan data dari _form_.
    - `return HttpResponseRedirect(reverse('main:show_main'))` berguna untuk melakukan _redirect_ setelah data berhasil disimpan.

3. Selanjutnya saya memodifikasi fungsi `show_main` menjadi,

    ```
    def show_main(request):
        cards = Card.objects.all()

        ...

        context = {
            'my_app': 'Marpellus Cenep',
            'name': 'FBmo',
            'class': 'PBP C',
            'cards': cards,
            'total_cards': total_cards
        }

        return render(request, "main.html", context)
    ```

    > `Card.objects.all()` berfungsi untuk mengambil seluruh _object_ `Card` yang tersimpan di basis data.

4. Saya juga mengimpor fungsi `create_product` ke `urls.py` di folder `main`.

    ```
    from main.views import show_main, create_product
    ```

5. Setelah itu saya melakukan _routing_ fungsi sebelumnya ke dalam `urlspatterns` pada `urls.py` di `main` agar dapat mengakses fungsi yang sudah diimpor sebelumnya.

    ```
    path('create-product', create_product, name='create_product'),
    ```

6. Selanjutnya saya membuat `create_product.html` pada direktori `main/template` dengan kode,

    ```
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Card</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Card"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```

    Ada beberapa istilah penting yang perlu diperhatikan, seperti
    - `<form method="POST">` berguna untuk menandakan `block` untuk _form_ dengan metode POST.
    - `{% csrf_token %}` merupakan token sistem keamanan dari Django.
    - `{{ form.as_table }}` berguna untuk menampilkan _fields form_ yang sudah dibuat pada `forms.py` sebagai tabel.
    - `<input type="submit" value="Add` berguna sebagai tombol _submit_ untuk mengirim _request_ ke _view_ `create_product(request)`. 

7. Setelah itu saya memodifikasi kembali `main.html` untuk menambahkan kode berikut di dalam `{% block content %}` untuk menampilkan data produk dalam bentuk tabel.

    ```
    <table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Price</th>
            <th>Power</th>
            <th>Energy Cost</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>

        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

        {% for card in cards %}
            <tr>
                <td>{{ card.name }}</td>
                <td>{{ card.amount }}</td>
                <td>{{ card.price }}</td>
                <td>{{ card.power }}</td>
                <td>{{ card.energy_cost }}</td>
                <td>{{ card.description }}</td>
                <td>{{ card.date_added }}</td>
            </tr>
        {% endfor %}
    </table>

    <br />

    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Card
        </button>
    </a>
    ```

8. Setelah sudah melihat objek yang ditambahkan melalui **HTML**, saya mencoba agar dapat melihat juga dalam bentuk **XML** dan **JSON** baik dalam menggunakan ID objek maupun tidak dengan menambahkan impor berikut pada `views.py`,

    ```
    from django.http import HttpResponse
    from django.core import serializers
    ```

9. Mengambil data dalam bentuk **XML** dan **JSON**
    Saya membuat fungsi yang menerima parameter _request_ dan membuat variabel dalam fungsi tersebut yang menyimpan hasil _query_ dari seluruh data yang ada pada `Card`.

    #### XML
    ```
    def show_xml(request):
        data = Card.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    
    > `serializers` digunakan untuk menerjemahkan objek model menjadi format tertentu. 

    #### JSON

    ```
    def show_json(request):
        data = Card.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```    
    Setelah itu saya mengimpor fungsi yang baru saja dibuat dengan kode berikut pada `urls.py` di folder `main`,

        from main.views import show_main, create_product, show_xml, show_json


    dan menambahkan _path_ URL ke dalam `urlpatterns` untuk mengakses fungsi yangs udah diimpor tadi,

        ...
        path('xml/', show_xml, name='show_xml'), 
        path('json/', show_json, name='show_json'),
        ...

10. Mengambil data dalam bentuk **XML** dan **JSON** dengan ID objek dengan membuat fungsi yang menerima parameter _request_ dan id dengan nama `show_xml_by_id` dan `show_json_by_id`.

    #### XML
    ```
    def show_xml_by_id(request, id):
        data = Card.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```

    #### JSON
    ```
    def show_json_by_id(request, id):
        data = Card.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
            
    Setelah itu saya mengimpor fungsi yang baru saja dibuat dengan kode berikut pada `urls.py` di folder `main`,

        ```
        from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
        ```

    dan menambahkan _path_ URL ke dalam `urlpatterns` untuk mengakses fungsi yang udah diimpor tadi,

        ...
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
        ...

## Perbedaan antara _form_ POST dan GET dalam Django
### Penggunaan
POST digunakan untuk menginput data melalui _form_ dan mengirim data-data tersebut, biasanya sifat data yang dikirimkan oleh POST bersifat rahasia dan dapat memengaruhi _state_ pada suatu sistem, seperti pengubahan ataua modifikasi _database_. Sementara itu, GET digunakan untuk input _request_ data yang bersifat umum dan tidak memeiliki efek terhadap _state_ pada suatu sistem, seperti _form_ pencarian suatu situs. 

### Pengiriman Data
POST mengirimkan data atau nilai langsung ke _action_ untuk ditampung, tanpa menampilkan pada URL. Sementara GET menampilkan data atau nilai pada URL, kemudian akan ditampung oleh _action_.

### Pengambilan Variabel
`request.POST.get` dapat digunakan untuk mengambil variabel _form_ POST dan `request.GET.get` untuk _form_ GET

## Perbedaan XML, JSON, dan HTML dalam Pengiriman Data

### XML
Extensible Markup Language (XML) merupakan salah satu representasi data yang digunakan untuk pertukaran data aplikasi. XML menggunakan pola pohon, mirip seperti HTML dalam merepresentasikan data. Dalam pengunaannya, XML memiliki struktur yang lebih kompleks untuk ditulis dan dibaca sehingga menghasilkan _file_ yang memakan banyak ruang.

### JSON
Sama seperti XML, JavaScript Object Notation (JSON) juga merupakan representasi data dalam pertukaran data, tetapi JSON menggunakan struktur peta dengan pasangan kunci-nilai dalam penyusunannya. Dalam penggunaannya, JSON memiliki ukuran _file_ yang cenderung kecil sehingga transmisi datanya lebih cepat dibandingkan dengan XML.

### HTML
Jika sebelumnya XML dan JSON digunakan untuk menyimpan serta melakukan transmisi data, HyperText Markup Language (HTML) pada dasarnya digunakan untuk merepresentasikan bagaimana data tersebut ditampilkan pada suatu situs. HTML pada umumnya menjadi sebuah pondasi dari suatu laman di situs _web_ dan hampir tidak ada alternatif yang lebih praktikal lagi.

## Alasan JSON Sering Digunakan dalam Pertukaran Data
JSON memiliki format yang cukup sederhana dalam penulisan jika dibandingkan dengan XML. Hal itu membuat _file_ JSON dapat diproses lebih cepat sehingga waktu yang dibutuhkan untuk melakkukan transmisi data lebih sedikit. Selain itu, mayoritas bahasa pemrograman memiliki _library_ atau _built-in_ untuk melakukan _parsing string_ JSON menjadi objek atau kelas di bahasa pemrograman tersebut. Hal tersebut yang membuat JSON dapat dengan mudah diintegrasikan dengan banyak bahasa pemrograman.

## Hasil Akses URL untuk Melihat Objek Menggunakan Postman

### HTML
![SS_html](https://github.com/FBimo/marpellus-cenep/assets/119420957/dcd2894f-b3bd-451f-a4ed-40924c5ebdd9)
### XML
![SS_xml](https://github.com/FBimo/marpellus-cenep/assets/119420957/c6adb15b-c9f2-40ec-8cd3-93095521b906)
### JSON
![SS_json](https://github.com/FBimo/marpellus-cenep/assets/119420957/3d8bc82d-76e8-441c-832b-ecc5f8b5995c)
### XML by ID
![SS_xml_by_id](https://github.com/FBimo/marpellus-cenep/assets/119420957/939088de-0c10-4dab-a16a-5447e001402c)
### JSON by ID
![SS_json_by_id](https://github.com/FBimo/marpellus-cenep/assets/119420957/8a12e102-b059-47d7-b8c4-7835973842c9)

## Bonus

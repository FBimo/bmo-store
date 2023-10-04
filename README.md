<details>
<summary> 
Tugas 2
</summary>
<br>

# Tugas 2 PBP 2023
## A. Implementasi _Checklist_
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

### Membuat Aplikasi dengan Nama `main`

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
    
### Membuat Model pada Aplikasi `main`
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

### Membuat Fungsi pada `views.py`

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

### Membuat _Routing_ pada `urls.py` Aplikasi `main`

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
    

## B. Bagan _Request Client_
![django-request-flow](https://github.com/FBimo/marpellus-cenep/assets/119420957/9b1d3f76-0013-4b6f-a539-8974df6099a5)

- `urls.py`, sebagai tempat perkumpulan URL. Django akan mencari melewati _file_ ini untuk menemukan URL yang paling cocok sesuai dengan permintaan.
- `views.py`, sebagai jembatan penghubung dengan dua _file_ lainnya, yaitu `models.py` dan `template`. Setelah mendapat HttpRequest dari URL yang berkaitan, `views.py` dapat meminta data yang diperlukan melalui `models.py` dan dapat melakukan _render_ HTML menggunakan `template` agar dapat disajikan kepada pengguna.
- `models.py`, sebagai pengolah data dan penghubung antara _database_ dengan `views.py`. `models.py` dapat melakukan manipulasi struktur data aplikasi sesuai kebutuhan pengguna.
- `template`, struktur tampilan antarmuka pengguna yang akan membantu `views.py` dalam melakukan proses _render_ HTML.

## C. Alasan Penggunaan _Virtual Environment_
_Virtual Environment_ merupakan _tools_ untuk membuat lingkungan Python virtual yang terisolasi. Terisolasi di sini maksudnya versi-versi dependensi atau _packages_ yang ada di dalam lingkungan virtual tidak akan berpengaruh dengan versi dependensi yang ada di komputer lokal. Penggunaan virtual env cukup umum ketika ingin membuat proyek Django karena dengan adanya lingkungan isolasi, Python yang digunakan untuk menjalankan proyek Django tidak akan terganggu dengan pembaruan yang terjadi di komputer lokal (jika ada pembaruan) sehingga proyek dapat tetap berjalan walaupun adanya perubahan versi modul Python di komputer lokal. Sebuah proyek Django sebenarnya dapat tetap dijalankan jika tidak menggunakan virtual env, namun ada kemungkinan proyek akan mengalami gangguan karena adanya perubahan modul akibat perubahan versi modul di komputer lokal. Oleh karena itu, **virtual env sangat disarankan** apabila kita ingin membuat suatu proyek berbasis Django. 

## D. Penjelasan MVC, MVT, dan MVVM
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

## E. Bonus
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
</details>

<details>
<summary> 
Tugas 3
</summary>
<br>

# Tugas 3 PBP 2023
## A. Implementasi _Checklist_
### Membuat _Form_ Input Data

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

### Modifikasi _Views_ dan _Routing_ URL untuk Melihat Objek Model yang Sudah Ditambahkan

1. Pada _file_ `views.py` di folder `main`, perlu ditambahkan kode berikut,

    ```
    from django.http import HttpResponseRedirect
    from main.forms import ProductForm
    from main.models import Card
    from django.urls import reverse
    ```

2. Setelah itu saya membuat fungsi baru dengan nama `create_product` yang menerima parameter `request` untuk menghasilkan formulir yang dapat menambahkan data produk secara otomatis ketika data sudah di-_submit_ melalui _form_.

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
    urlpatterns = [
    ...
    path('create-product', create_product, name='create_product'),
    ...
    ]
    
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

9. Ketika ingin mengambil data dalam bentuk **XML** dan **JSON**, saya membuat fungsi yang menerima parameter _request_ dan membuat variabel dalam fungsi tersebut yang menyimpan hasil _query_ dari seluruh data yang ada pada `Card`.

    #### XML
    ```
    def show_xml(request):
        data = Card.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ``` 

    #### JSON

    ```
    def show_json(request):
        data = Card.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```    
    > `serializers` digunakan untuk menerjemahkan objek model menjadi format tertentu.

    Setelah itu saya mengimpor fungsi yang baru saja dibuat dengan kode berikut pada `urls.py` di folder `main`,

        from main.views import show_main, create_product, show_xml, show_json


    dan menambahkan _path_ URL ke dalam `urlpatterns` untuk mengakses fungsi yangs udah diimpor tadi,

        urlpatterns = [
            ...
            path('xml/', show_xml, name='show_xml'), 
            path('json/', show_json, name='show_json'),
            ...
        ]

10. Selanjutnya saya ingin mengambil data dalam bentuk **XML** dan **JSON** dengan ID objek dengan membuat fungsi yang menerima parameter _request_ dan id dengan nama `show_xml_by_id` dan `show_json_by_id`.

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

        from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id        

    dan menambahkan _path_ URL ke dalam `urlpatterns` untuk mengakses fungsi yang udah diimpor tadi,

        urlpatterns = [
            ...
            path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
            path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
            ...
        ]

## B. Perbedaan antara _form_ POST dan GET dalam Django
### Penggunaan
POST digunakan untuk menginput data melalui _form_ dan mengirim data-data tersebut, biasanya sifat data yang dikirimkan oleh POST bersifat rahasia dan dapat memengaruhi _state_ pada suatu sistem, seperti pengubahan atau modifikasi _database_. Sementara itu, GET digunakan untuk input _request_ data yang bersifat umum dan tidak memiliki efek terhadap _state_ pada suatu sistem, seperti _form_ pencarian suatu situs. 

### Pengiriman Data
POST mengirimkan data atau nilai langsung ke _action_ untuk ditampung, tanpa menampilkan pada URL. Sementara GET menampilkan data atau nilai pada URL, kemudian akan ditampung oleh _action_.

### Pengambilan Variabel
`request.POST.get` dapat digunakan untuk mengambil variabel _form_ POST dan `request.GET.get` untuk _form_ GET.

## C. Perbedaan XML, JSON, dan HTML dalam Pengiriman Data

### XML
Extensible Markup Language (XML) merupakan salah satu representasi data yang digunakan untuk pertukaran data aplikasi. XML menggunakan pola pohon, mirip seperti HTML dalam merepresentasikan data. Dalam pengunaannya, XML memiliki struktur yang lebih kompleks untuk ditulis dan dibaca sehingga menghasilkan _file_ yang memakan banyak ruang.

### JSON
Sama seperti XML, JavaScript Object Notation (JSON) juga merupakan representasi data dalam pertukaran data, tetapi JSON menggunakan struktur peta dengan pasangan kunci-nilai dalam penyusunannya. Dalam penggunaannya, JSON memiliki ukuran _file_ yang cenderung kecil sehingga transmisi datanya lebih cepat dibandingkan dengan XML.

### HTML
Jika sebelumnya XML dan JSON digunakan untuk menyimpan serta melakukan transmisi data, HyperText Markup Language (HTML) pada dasarnya digunakan untuk merepresentasikan bagaimana data tersebut ditampilkan pada suatu situs. HTML pada umumnya menjadi sebuah pondasi dari suatu laman di situs _web_ dan hampir tidak ada alternatif yang lebih praktikal lagi.

## D. Alasan JSON Sering Digunakan dalam Pertukaran Data
JSON memiliki format yang cukup sederhana dalam penulisan jika dibandingkan dengan XML. Hal itu membuat _file_ JSON dapat diproses lebih cepat sehingga waktu yang dibutuhkan untuk melakkukan transmisi data lebih sedikit. Selain itu, mayoritas bahasa pemrograman memiliki _library_ atau _built-in_ untuk melakukan _parsing string_ JSON menjadi objek atau kelas di bahasa pemrograman tersebut. Hal tersebut yang membuat JSON dapat dengan mudah diintegrasikan dengan banyak bahasa pemrograman.

## E. Hasil Akses URL untuk Melihat Objek Menggunakan Postman

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

## F. Bonus
Berikut merupakan tangkapan layar aplikasi yang terdapat petunjuk mengenai berapa banyak `Card` yang sudah ditambahkan ke dalam aplikasi.

```
def show_main(request):
    cards = Card.objects.all()

    total_cards = 0
    for card in cards:
        total_cards += 1

    context = {
        'my_app': 'Marpellus Cenep',
        'name': 'FBmo',
        'class': 'PBP C',
        'cards': cards,
        'total_cards': total_cards
    }

    return render(request, "main.html", context)
```

![bonus](https://github.com/FBimo/marpellus-cenep/assets/119420957/dcdf14d2-0ecf-472e-a10d-7cfeaa52f20b)
</details>

<details>
<summary> 
Tugas 4
</summary>
<br>

# Tugas 4 PBP 2023
## A. Implementasi _Checklist_
### Mengimplementasikan Fungsi Registrasi

1. Saya membuat fungsi dengan nama `register` yang menerima parameter `request` di `views.py` pada subdirektori `main`.

2. Setelah itu, saya perlu mengimpor beberapa hal sebagai berikut,

    ```
    ...
    from django.shortcuts import redirect
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages
    ...
    ```
    > `UserCreationForm` adalah impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna dalam suatu aplikasi _web_.

3. Selanjutnya, saya menambahkan isi dari fungsi `register` dengan kode berikut,

    ```
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
    ```

    Ada beberapa istilah yang harus diperhatikan,
    - `form = UserCreationForm(request.POST) ` digunakan untuk membuat `UserCreationForm`
    - `form.is_valid()` digunakan untuk memvalidasi isi input dari _form_ tersebut.
    - `form.save()` digunakan untuk membuat dan menyimpan data dari _form_ tersebut.
    - `messages.success(request, 'Your account has been successfully created!)` berguna untuk menampilkan pesan kepada pengguna. 
    - `return redirect('main:show_main')` digunakan untuk melakukan _redirect_ setelah data _form_ berhasil disimpan.

4. Setelah itu, saya membuat `register.html` pada folder `main/templates` dengan kode,

    ```
    {% extends 'base.html' %}

    {% block meta %}
        <title>Register</title>
    {% endblock meta %}

    {% block content %}  

    <div class = "login">
        
        <h1>Register</h1>  

            <form method="POST" >  
                {% csrf_token %}  
                <table>  
                    {{ form.as_table }}  
                    <tr>  
                        <td></td>
                        <td><input type="submit" name="submit" value="Daftar"/></td>  
                    </tr>  
                </table>  
            </form>

        {% if messages %}  
            <ul>   
                {% for message in messages %}  
                    <li>{{ message }}</li>  
                    {% endfor %}  
            </ul>   
        {% endif %}

    </div>  

    {% endblock content %}
    ```

5. Selanjutnya saya memperbarui `urls.py` pada `main` dengan menambahkan impor fungsi,

    ```
    ...
    from main.views import register
    ...
    ```

    dan menambahkan `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.

        ```
        urlpatterns = [
            ...
            path('register/', register, name='register'), 
            ...
        ]
        
        ```

### Mengimplementasikan Fungsi _Login_
1. Saya membuat fungsi dengan nama `login_user` yang menerima parameter `request` di `views.py` pada subdirektori `main`.

2. Setelah itu saya perlu mengimpor `authenticate` dan `login` pada bagian paling atas.

    ```
    ...
    from django.contrib.auth import authenticate, login
    ...
    ```
    > Pengimporan di atas berguna untuk melakukan autentikasi dan login jika autentikasi berhasil. 

3. Selanjutnya, saya menambahkan isi dari fungsi `login` dengan kode berikut,

    ```
    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:show_main')
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {}
        return render(request, 'login.html', context)
    ```
    
    > `authenticate(request, username=username, password=password` berguna untuk melakukan autentikasi pengguna berdasarkan _username_ dan _password_ ketika _login_.

4. Setelah itu, saya membuat `login.html` pada folder `main/templates` dengan kode,

    ```
    {% extends 'base.html' %}

    {% block meta %}
        <title>Login</title>
    {% endblock meta %}

    {% block content %}

    <div class = "login">

        <h1>Login</h1>

        <form method="POST" action="">
            {% csrf_token %}
            <table>
                <tr>
                    <td>Username: </td>
                    <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                </tr>
                        
                <tr>
                    <td>Password: </td>
                    <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                </tr>

                <tr>
                    <td></td>
                    <td><input class="btn login_btn" type="submit" value="Login"></td>
                </tr>
            </table>
        </form>

        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}     
            
        Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

    </div>

    {% endblock content %}
    ```

5. Selanjutnya saya memperbarui `urls.py` pada `main` dengan menambahkan impor fungsi,

    ```
    from main.views import login_user
    ```

    dan menambahkan `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.

        ```
        urlpatterns = [
            ...
            path('login/', login_user, name='login'),
            ...
        ]
        ```

### Mengimplementasikan Fungsi _Logout_
1. Saya membuat fungsi dengan nama `logout_user` yang menerima parameter `request` di `views.py` pada subdirektori `main`.

2. Setelah itu saya perlu mengimpor `logout`.

    ```
    ...
    from django.contrib.auth import logout
    ...
    ```

3. Selanjutnya, saya menambahkan isi dari fungsi `login` dengan kode berikut,

    ```
    def logout_user(request):
        logout(request)
        return redirect('main:login')
    ```

    Ada beberapa istilah yang harus diperhatikan,
    - `logout(request)` digunakan menghapus sesi pengguna yang saat ini masuk.
    - `return redirect('main:login')` berguna untuk mengarahkan pengguna ke halaman _login_ dalam aplikasi Django.

4. Setelah itu, saya menambahkan kode berikut ke dalam `main.html` setelah _hyperlink tag_ untuk _Add New Product_

    ```
    ...
    <a href="{% url 'main:logout' %}">
        <button>
            Logout
        </button>
    </a>
    ...
    ```

5. Selanjutnya saya memperbarui `urls.py` pada subdirektori `main` dengan menambahkan impor fungsi,

    ```
    ...
    from main.views import logout_user
    ...
    ```

    dan menambahkan `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.

        ```
        urlpatterns = [
            ...
            path('logout/', logout_user, name='logout'),
            ...
        ]
        
        ```

### Membuat Dua Akun dengan Setiap Akun Memiliki Tiga _Dummy Data_

Berikut merupakan bukti pembuatan dua akun dan masing-masing akun telah memiliki tiga _dummy data_,
#### Akun Pertama
![ss-main-privAcc1](https://github.com/FBimo/marpellus-cenep/assets/119420957/3f531768-5c77-4f35-b53d-3d1bd8f41817)
#### Akun Kedua
![ss-main-privAcc2](https://github.com/FBimo/marpellus-cenep/assets/119420957/9a641100-f25b-4df6-b4f0-8e2a76bbd3f2)

### Menghubungkan Model `Item` dengan `User`
> Perlu diketahui bahwa _term_ `Item` pada aplikasi saya adalah `Card`

1. Saya perlu mengimpor `user` dengan kode berikut di `models.py` pada subdirektori `main`.

    ```
    ...
    from django.contrib.auth.models import User
    ...
    ```

2. Setelah itu saya menambahkan kode berikut pada model `Card`.

    ```
    class Card(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
    ```
    > Kode di atas berguna untuk menghubungkan satu produk dengan satu _user_ melalui sebuah _relationship_ yang memastikan bahwa sebuah `Card` terasosiasikan dengan seorang _user_

3. Pada `views.py` di direktori `main`, saya mengubah fungsi `create_product` menjadi,

    ```
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        ...
    ```
    > Parameter `commit=False` yang berguna untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari _form_ langsung ke _database_. Hal tersebut membuat kita dapat memodifikasi objek tersebut sebelum dilakukan penyimpanan ke dalam _database_.

4. Selanjutnya saya mengubah fungsi `show_main` menjadi sebagai berikut.

    ```
    def show_main(request):
        cards = Card.objects.filter(user=request.user)

        ...

        context = {
            ...
            'name': request.user.username,
            ...
        }

        ...
    ```
    Ada beberapa hal yang harus diperhatikan,
    - `cards = Card.objects.filter(user=request.user)` berguna untuk menampilkan objek `Card` yang terasosiasikan dengan pengguna yang sedang _login_.
    - `'name': request.user.username` berguna untuk menampilkan _username_ pengguna yang _login_ pada halaman utama.

5. Setelah itu, saya menyimpan semua perubahan dan melakukan migrasi model dengan `python manage.py makemigrations`. Namun, akan terjadi error ketika membuat migrasi, oleh karena itu saya perlu,

    - Mengetik angka `1` untuk menetapkan _default value_ pada _field user_.
    - Mengetik angka `1` lagi untuk menetapkan _user_ dengan ID 1 sesuai dengan yang sudah dibuat pada model.

6. Selanjutnya saya dapat melakukan `python manage.py migrate` untuk mengaplikasikan migrasi yang dilakukan. 

### Menampilkan Rincian Informasi ketika Pengguna _logged in_ dan Menerapkan _Cookies_ Seperti `last_login` pada Halaman Utama Aplikasi

1. Sebelum melakukan implementasi _cookies_, saya perlu mengimpor beberapa hal berikut di `views.py` pada subdirektori `main`

    ```
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    ```

2. Setelah itu saya sedikit memodifikasi bagian `if user is not None` pada fungsi `login_user` dengan kode berikut.

    ```
    ...
    if user is not None:
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main")) 
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ...
    ```
    Ada beberapa istilah yang harus diperhatikan,
    - `login(request, user)` berguna untuk melakukan _login_.
    - `response = HttpResponseRedirect(reverse("main:show_main"))` berguna untuk membuat _response_.
    - `response.set_cookie('last_login', str(datetime.datetime.now()))` berguna untuk membuat _cookie_ `last_login` dan menambahkannya ke dalam _response_.

3. Selanjutnya saya menambahkan `'last_login': request.COOKIES['last_login']` pada fungsi `show_main` ke dalam variabel `context`.

    ```
    context = {
        'my_app': 'Marpellus Cenep',
        'name': request.user.username,
        'class': 'PBP C',
        'cards': cards,
        'total_cards': total_cards,
        'last_login': request.COOKIES['last_login']
    }
    ```

    > `'last_login': request.COOKIES['last_login']` berguna untuk menambahkan informasi _cookie_ `last_login` pada _response_ yang akan ditampilkan di halaman _web_.

4. Setelah itu saya mengubah fungsi `logput_user` dengan kode berikut.

    ```
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```
    
    > `response.delete_cookie('last_login')` berguna untuk menghapus _cookie_ `last_login` saat pengguna _logout_.

5. Selanjutnya saya dapat menambahkan kode berikut pada `main.html`.

    ```
    ...
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ...
    ```

6. Setelah itu, saya dapat melakukan `python manage.py runserver` dan melakukan _login_ untuk melihat data _cookie_ yang tersimpan dengan fitur _inspect element_.
   
   ![ss-main-cookies](https://github.com/FBimo/marpellus-cenep/assets/119420957/b51f006a-cc92-4ef5-8b5e-7fc5104bc46d)

## B. Django `UserCreationForm`
`UserCreationForm` merupakan suatu modul bawaan Django yang menyajikan sarana bagi penggunanya untuk melakukan sistem autentikasi. Sesuai dengan namanya, `UserCreationForm` dapat membuat _user_ baru yang dapat mengakses aplikasi _web_. `UserCreationForm` biasanya terdiri dari tiga _field_, yaitu `username`, `password1`, dan `password2`. _Field_ tersebut biasanya digunakan untuk melakukan konfirmasi _password_.

### Kelebihan `UserCreationForm`
Kelebihan dari `UserCreationForm` adalah memiliki sistem validasi. Penerapan validasi ini bermacam-macam, salah satunya ketika ada pengguna yang ternyata tidak mengisi semua kolom yang seharusnya diisi ketika melakukan pengisian _form_, sistem ini akan memberi peringatan kepada pengguna untuk melakukan pemeriksaan ulang terhadap isiannya. Sistem validasi ini juga dapat digunakan untuk berbagai macam entri dengan tipe data berbeda-beda sehingga dapat memberikan keleluasaan bagi admin untuk memverifikasi berbagai kolom yang memiliki tipe data yang khusus. Kelebihan `UserCreationForm` lainnya adalah memberikan kemudahan ketika kita ingin meletakkan data-data yang ada di _form_ ke tabel-tabel _database_ karena kita dapat menggunakan variabel data yang sama dari _form_ jika ingin dikirimkan ke _database_. 

### Kekurangan `UserCreationForm`
Kekurangan dari `UserCreationForm` adalah restriksi peraturan yang dimiliki oleh Django itu sendiri. Django mengharuskan kita untuk mengimpor modul secara keseluruhan dalam satu waktu karena _form_ yang kita buat itu merupakan _file_ .py yang terpisah. Dengan adanya restriksi dari Django, kita juga tidak bisa secara bebas memodifikasi bentuk dari _form_ yang diinginkan. 

## C. Perbedaan Autentikasi dan Otorisasi

### Autentikasi
Proses identifikasi awal ketika ingin melakukan akses ke sebuah sistem. Biasanya hal ini dapat kita sebut sebagai _login_ ke suatu sistem tertentu. Proses _login_ memeriksa apakah orang yang ingin mengakses sistem tersebut benar-benar adalah orang yang tepat. Misalnya jika ingin melakukan _login_ ketika ingin mengirim _email_ di perangkat yang belum memiliki akun orang yang ingin mengirim tersebut. Sistem akan memberikan suatu langkah-langkah untuk memverifikasi orang tersebut yang ingin mengakses akun miliknya sendiri, seperti memasukkan nama pengguna dan kata sandi. Hal ini mencegah sistem agar tetap aman dari ancaman intrusi oleh entitas asing.

### Otorisasi
Proses lanjutan dari autentikasi yang menitikberatkan terhadap otorisasi yang dimiliki oleh akun tersebut. Sistem akan melakukan filtrasi lagi terhadap kuasa yang dapat dipegang oleh akun-akun yang sudah berhasil _login_. Kuasa dalam konteks ini adalah kemampuan kebebasan baik dalam mengakses maupun memanipulasi data-data yang ada di dalam sistem tersebut. Contohnya adalah perbedaan akun admin dan _user_. Admin dapat dengan bebas dalam mengakses dan memanipulasi data-data yang ada di suatu sistem tersebut sementara _user_ biasanya hanya bisa mengakses data-data yang berhubungan dengan data personalnya.

> Kedua hal tersebut merupakan aspek yang cukup krusial untuk tetap menjaga sebuah integritas keamanan dari suatu aplikasi karena jika kedua aspek tersebut dihilangkan, aplikasi atau suatu sistem akan mudah dilakukan intrusi oleh oknum-oknum yang tidak bertanggung jawab. 

## D. Penjelasan _Cookies_ dalam Konteks Aplikasi _Web_
_Cookies_ merupakan suatu istilah untuk kumpulan informasi yang berisi rekam jejak pengguna ketika mengunjungi situs _web_ tertentu. _Cookies_ berguna untuk menyimpan beberapa data, seperti menyimpan pengaturan situs _web_, menyimpan data _login_ pengguna, menampilkan iklan, dan menyediakan konten yang lebih personal kepada pengguna. Dalam penggunaan _cookies_, khususnya di Django, data dari sesi tidak disimpan langsung di _browser_. Data tersebut disimpan pada server terlebih dahulu di server. Django akan membuat _string_ unik sepanjang 32 karakter (_session key_) dan mengaitkannya dengan data sesi. Server kemudian mengirim _cookie_ bernama `sessionid` yang berisi _session key_ sebagai _value_ ke browser. Pada _request_ selanjutnya, _browser_ mengirimkan _cookie_ `sessionid` ke server dan Django kemudian akan menggunakan _cookie_ ini untuk mengambil data sesi dan membuatnya dapat diakses. 

## E. Keamanan Penggunaan _Cookies_
Dalam kondisi _default_, _cookies_ tidak bisa melakukan transfer _malware_ karena data yang dibawa _cookies_ tidak berubah ketika berpindah dari komputer ke suatu situs _web_ dan sebaliknya. Perpindahan data _cookies_ ini sama sekali tidak berpengaruh kepada komputer lokal. Namun, pengguna disarankan untuk menghindari situs-situs yang mencurigakan dan membaca secara keseluruhan tentang data-data apa saja yang disimpan di dalam _cookies_ agar data di _cookies_ tidak dimanfaatkan oleh oknum-oknum tidak bertanggung jawab.

## F. Bonus
1. Berikut merupakan cuplikan kode dari `views.py`

    ```
    def increase_card(request, id):
        card = Card.objects.filter(user=request.user, pk=id).first()
        if card.amount > 0:
            card.amount += 1
        card.save()

        return HttpResponseRedirect(reverse('main:show_main'))


    def decrease_card(request, id):
        card = Card.objects.filter(user=request.user, pk=id).first()
        if card.amount > 0:
            card.amount -= 1
        card.save()

        return HttpResponseRedirect(reverse('main:show_main'))


    def remove_card(request, id):
        card = Card.objects.filter(user=request.user, pk=id).first()
        if card.amount > 0:
            card.delete()
        
        return HttpResponseRedirect(reverse('main:show_main'))
    ```

2. Berikut merupakan cuplikan dari kode `urls.py`

    ```
    ...
    from main.views import increase_card, decrease_card, remove_card

    ...

    urlpatterns = [
        ...
        path('increase-card/<int:id>', increase_card, name='increase_card'),
        path('decrease-card/<int:id>', decrease_card, name='decrease_card'),
        path('remove-card/<int:id>', remove_card, name='remove_card'),
    ]
    ```

3. Berikut merupakan cuplikan kode `main.html`

    ```
    {% for card in cards %}
        <tr>
            <td>{{ card.name }}</td>
            <td>
                <a href="{% url 'main:increase_card' card.id %}">
                    <button >
                        +
                    </button>
                </a>
                
                {{ card.amount }}

                <a href="{% url 'main:decrease_card' card.id %}">
                    <button >
                        -
                    </button>
                </a>
            </td>
            ...
            <td>
                <a href="{% url 'main:remove_card' card.id %}">
                    <button>
                        remove card
                    </button>
                </a>
            </td>
    ```

4. Berikut merupakan cuplikan proses implementasi

   #### Proses _Increament_
   
   ![bonus-inc-1](https://github.com/FBimo/marpellus-cenep/assets/119420957/1fa314cf-bc59-4817-a6a7-9e1ef6385f08)
   ![bonus-inc-2](https://github.com/FBimo/marpellus-cenep/assets/119420957/fbb84ad0-f04e-4bfc-a613-0496fb3af313)

   #### Proses _Decreament_

   ![bonus-dec-1](https://github.com/FBimo/marpellus-cenep/assets/119420957/921b3806-5665-4b22-9ae2-38c229c84c51)
   ![bonus-dec-2](https://github.com/FBimo/marpellus-cenep/assets/119420957/1bb8f701-88c4-41f6-9a71-a0fd1bb5e250)

   #### Proses _Remove_
   ![bonus-rm-1](https://github.com/FBimo/marpellus-cenep/assets/119420957/7437b45d-0316-435e-a85b-d5dd49cece50)
   ![bonus-rm-2](https://github.com/FBimo/marpellus-cenep/assets/119420957/cb3ea7b8-c492-4b53-9754-af8a80e936c6)
</details>

<details>
<summary> 
Tugas 5
</summary>
<br>

# Tugas 5 PBP 2023
## A. Implementasi _Checklist_
### Mengimplementasikan _Static Files_ pada Django

1. Saya melakukan kustomisasi pada halaman _web_ menggunakan _file_ CSS eksternal, oleh karena itu diperlukan pengaturan terhadap _file-file_ tersebut.
2. Pada `settings.py`, saya menambahkan kode berikut untuk menghubungkan _static files_ dengan aplikasi.

    ```
    ...
        STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]
    ...
    ```
3. Setelah itu, saya membuat direktori baru di _root_ dengan nama `static` yang akan berisi berbagai macam _static files_, salah satunya adalah _file_ CSS. Berikut merupakan potongan kode pada `login-style.css` yang berguna untuk melakukan  kustomisasi pada `login.html`.

    ```
    .global-container {
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #48e248;
    }

    .card-tittle,
    .card-text {
        color: #48e248;
    }

    .login-form {
        width: 380px;
        height: 450px;
        padding: 20px;
        background-color: #1a2226 !important;
        border-radius: 10px !important;
    }

    input[type="username"],
    input[type="password"] {
        background: #1a2226;
        color: #fff;
        border: 2px solid #00ff00;
        border-radius: 10px;
        margin-bottom: 25px;
    }
    ```
    > Kode di atas berada pada `static/css/`, pengklasifikasian dilakukan kembali karena _static files_ cukup beragam sehingga pemisahan ini akan sangat membantu untuk mengaturnya apabila ada jenis _static files_ baru yang ditambahkan. 

## B. Manfaat _Element Selector_
Dalam CSS, selector digunakan untuk memilih elemen HTML yang ingin kita beri style. Berikut adalah beberapa jenis selector dan manfaatnya:

1. **Type Selector**: Berguna untuk memilih semua elemen dengan jenis tertentu. Misalnya, `p { color: blue; }` akan menerapkan warna biru ke semua elemen paragraf. Kita dapat menggunakan ini jika ingin menerapkan gaya pada elemen yang memiliki jenis yang sama.

2. **Class Selector**: Berguna untuk memilih elemen berdasarkan kelasnya. Misalnya, `.myClass { color: red; }` akan menerapkan warna merah ke semua elemen dengan kelas "myClass". Kita dapat menggunakan ini ketika ingin menerapkan gaya ke sekelompok elemen yang memiliki kelas yang sama.

3. **ID Selector**: Berguna untuk memilih satu elemen berdasarkan ID-nya. Misalnya, `#myID { color: yellow; }` akan menerapkan warna kuning ke elemen dengan ID "myID". Kita dapat menggunakan ini ketika ingin menerapkan gaya ke satu elemen spesifik.

4. **Attribute Selector**: Berguna untuk memilih elemen berdasarkan atributnya. Misalnya, `[target='_blank'] { background-color: green; }` akan menerapkan warna latar belakang hijau ke semua elemen yang memiliki atribut target dengan nilai "_blank". Kita bisa menggunakan ini ketika ingin menerapkan gaya ke elemen berdasarkan atributnya.

5. **Pseudo-class Selector**: Berguna untuk memilih elemen berdasarkan status tertentu, seperti _hover_ atau _focus_. Misalnya, `a:hover { color: black; }` akan menerapkan warna hitam ke tautan saat _mouse_ diarahkan ke atasnya. Kita dapat menggunakan ini ketika ingin menerapkan gaya berdasarkan status atau kondisi tertentu dari elemen.

6. **Pseudo-element Selector**: Berguna untuk memilih bagian spesifik dari elemen, seperti `::first-line` atau `::before`. Misalnya, `p::first-line { font-weight: bold; }` akan menerapkan teks tebal ke baris pertama dari setiap paragraf. Kita dapat menggunakan ini ketika ingin menerapkan gaya ke bagian spesifik dari suatu elemen.

## C. HTML5 _Tag(s)_
| No. |       Tag        |                    Fungsi                         |
|:--- |:----------------:|:-------------------------------------------------:|
| 1.  | `<! DOCTYPE html>` |Deklarasi untuk mendefinisikan dokumen menjadi HTML|
| 2.  | `<html> `          |_Tag_ pembuka untuk membuat dokumen HTML           |
| 3.  | `<head>`           |Informasi meta tentang dokumen                     |
| 4.  | `<title> `         |Membuat judul halaman                              | 
| 5.  | `<body> `          |Menampung semua konten HTML                        |
| 6.  | `<h1> s/d <h6>`    |Membuat judul atau _heading_                       |
| 7.  | `<p> `             |Membuat paragraf                                   |
| 8.  | `<br> `            |Membuat garis baru                                 |
| 9.  | `<img>`            |Mendefinsikan gambar                               |
| 10. | `<input> `         |Membuat tipe input pada _form_ yang dibuat         |
| 11. | `<label> `         |Memberikan label pada elemen input                 |
| 12. | `<table>`          |Membuat tabel pada _web_                           |
| 13. | `<tr>  `           |Membuat baris pada tabel                           |
| 14. | `<td> `            |Membuat kolom pada tabel                           |
| 15. | `<th> `            |Membuat judul pada kolom.                          |

## D. Perbedaan _Margin_ dan _Padding_
### _Margin_
_Margin_ merupakan sisi terluar dari sebuah _element_. Dengan adanya _margin_, kita bisa mengatur jarak antar _element_ yang ada. Terdapat beberapa sisi luar _margin_, yaitu `margin-top`, `margin-bottom`, `margin-left`, dan `margin-right`.

### _Padding_
_Padding_ merupakan sisi dalam dari sebuah _element_. Dengan adanya _padding_ kita bisa mengatur jarak sisi dalam dari suatu _element_. Terdapat beberapa sisi dalam _padding_, yaitu `padding-top`, `padding-bottom`, `padding-left`, dan `padding-right`.

## E. Perbedaan _Framework_ CSS Tailwind dan Bootstrap
|           Boostrap          |          Tailwind           |
|:----------------------------|:----------------------------|
|Memiliki ukuran _file_ yang lebih besar karena menyediakan banyak fitur dan komponen yang sudah siap pakai.|Memiliki ukuran _file_ yang lebih ringan karena hanya memuat kelas-kelas utilitas yang ada.|
|Memiliki batasan dalam fleksibilitas desain yang unik. |Memiliki fleksibilitas yang lebih besar dengan pendekatan _utility first_ yang memungkinkan kita membangun desain yang sangat kustom.|
|Ramah bagi pemula karena komponen-komponennya sudah didefinisikan.|Butuh pembelajaran lebih lanjut karena memerlukan pemahaman mengenai kelas-kelas utilitas yang ada dan cara bagaimana menggabungkannya.|

Masing-masing _framework_ memiliki kelebihan dan kekurangannya masing-masing. Penggunaan kedua _framework_ ini sebenarnya dapat disesuaikan dengan kebutuhan pengembang. Apabila pengembang ingin memiliki desain yang lebih stabil, cepat dalam pengimplementasian, dan ramah bagi pemula, maka Bootstrap merupakan pilihan cocok. Namun apabila pengembang lebih ingin bebas dalam memodifikasi aplikasinya, memerlukan _file_ yang ringan, dan sudah cukup paham dengan CSS, maka Tailwind CSS merupakan pilihan yang tepat. 

</details>
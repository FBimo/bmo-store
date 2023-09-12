# Tugas 2 PBP 2023
1. Implementasi Checklist
    a. Membuat proyek Django
    - Saya membuat sebuah folder khusus di komputer sebagai tempat proyek Django akan disimpan

    - Di dalam folder tersebut, saya melakukan inisiasi awal untuk menyediakan repositori lokal yang kosong di dalam komputer dengan menjalankan perintah <git init>

    - Setelah itu, saya melakukan konfigurasi awal user dan email dengan perintah,

    <git config user.name [nama_user]>
    <git config user.email [nama_email]>

    - Selanjutnya saya memeriksa terlebih dahulu bahwa konfigurasi yang dilakukan sudah terdaftar dengan perintah,

    <git config --list --local>

    - Apabila user dan email yang sudah dikonfigurasi sebelumnya muncul di keluaran perintah sebelumnya, saya dapat melanjutkan langkah berikutnya, yaitu membuat repositori baru di GitHub dengan nama repositori yang sama seperti repositori proyek lokal

    -Berikutnya, di dalam repositori lokal proyek, saya menambahkan sebuah file <README.md> dan menuliskan "Tugas 2 PBP 2023" sebagai judul

    - Setelah itu, perlu dilakukan penghubungan antara repositori lokal di komputer dengan repositori di GitHub dengan cara menggunakan perintah,

    <git branch -M main>

    Perintah di atas berguna untuk membuat cabang atau branch utama baru yang bernama "main"

    Setelah itu, perlu dijalankan perintah,

    <git remote add origin [URL_RepoGitHub]>

    Perintah di atas berguna untuk menghubungkan repositori di GitHub dengan repositori lokal

    - Setelah kedua repositori terhubung, perlu dilakukan penyimpanan atas pembaruan yang sudah dilakukan di repositori lokal dengan perintah,

    <git add .>

    Perintah di atas berguna untuk menandai semua file yang berubah di dalam repositori lokal yang nantinya akan dilakukan commit. Setelah itu, dapat dijalankan,

    <git status>

    Perintah di atas berguna untuk memeriksa status file apa saja yang sudah dimodifikasi dan ditandai. Setelah itu dapat dilakukan perintah,

    <git commit -m [pesan_commit]>

    Perintah di atas berguna untuk melakukan commit atas perubahan yang terjadi di repositori lokal. Berikutnya dapat dilakukan,

    <git push -u origin main>

    Perintah di atas berguna untuk menyimpan perubahan-perubahan yang terjadi di repositori lokal ke repositori GitHub, termasuk jika adanya penambahan file baru

    - Setelah penyimpanan berhasil, saya membuat virtual environment dengan menjalankan perintah,

    <python -m venv env>

    Perintah di atas berguna untuk membuat virtual environment. Hal ini berguna untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer lokal.

    - Setelah itu, saya perlu mengaktifkan virtual environment dengan menjalankan,

    <env\Scripts\activate.bat>

    - Berikutnya saya menambahkan requirements.txt di dalam direktori proyek dengan isi sebagai berikut,

        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3

    Setelah itu, saya  melakukan perintah berikut,

    <pip install -r requirements.txt>

    Perintah di atas berguna untuk memasang dependencies di dalam direktori proyek

    - Selanjutnya, saya dapat membuat proyek Django baru dengan perintah,

    <django-admin startproject [nama_proyek] .>

    b. Membuat aplikasi dengan nama main
    - Pertama, saya memastikan bahwa direktori pengerjaan di direktori proyek dan virtual environtment telah diaktifkan

    - Selanjutnya saya membuat aplikasi main dengan menjalankan perintah,

    <python manage.py startapp main>

    Setelah perintah di atas dijalankan, di dalam direktori proyek akan ada sebuah direktori baru bernama main, direktori inilah yang berisi struktur dasar dari aplikasi main

    - Sebelum menjalankan routing agar aplikasi dapat berjalan, saya melakukan beberapa implementasi dasar terhadap struktur awal aplikasi, seperti

        - mendaftarkan aplikasi main ke dalam proyek dengan menambahkan 'main' ke dalam daftar aplikasi yang ada di bagian <INSTALLED_APPS> pada <settings.py> seperti kode di bawah ini

            INSTALLED_APPS = [
                ...,
                'main',
                ...,
            ]

        - membuat dan mengisi file <main.html> untuk membuat struktur dan tampilan dasar pada halaman web

        - menambah isi dari <models.py> di dalam direktori aplikasi <main> untuk mendefinisikan model baru. Di dalam model inilah kita dapat mengelola data dari aplikasi

        - setelah itu, perlu adanya migrasi model agar Django dapat melacak pembaruan yang terjadi di <models.py> dengan perintah,

        <python manage.py makemigrations>

        perintah di atas berguna untuk menciptakan berkas migrasi berupa perubahan model. Setelah itu perlu menjalankan perintah,

        <python manage.py migrate>

        perintah di atas berguna untuk mengaplikasikan perubahan yang terjadi pada model ke basis data

        - setelah dilakukan migrasi, saya perlu mengintegrasikan komponen <views.py> yang dapat menangani bagaimana data yang dikelola model ditampilkan kepada pengguna dengan menambahkan kode awal sebagai berikut

        <from django.shortcuts import render>

        kode di atas berguna untuk mengimpor fungsi render yang berfungsi untuk melakukan render tampilan HTML dengan menggunakan data yang diberikan

    c. Melakukan routing pada proyek
    - Untuk mengatur routing tingkat proyek, saya perlu membuka <urls.py> di dalam direktori proyek, lalu menambahkan kode

        from django.urls import path, include

            urlpatterns = [
                ...
            path('main/', include('main.urls')),
                ...
            ]

    Perlu diperhatikan bahwa fungsi include di atas berguna untuk mengimpor rute URL dari aplikasi lain ke dalam <urls.py> proyek dan path <'main/'> nantinya akan diarahkan ke rute yang didefinisiakn dalam <urls.py> aplikasi <main>

    d. Membuat model pada aplikasi <main>
    Berikut model yang saya tambahkan ke dalam <models.py>

        from django.db import models
        class Item(models.Model):
            name = models.CharField(max_length=255)
            amount = models.IntegerField()
            date_added = models.DateField(auto_now_add=True)
            price = models.IntegerField()
            description = models.TextField()
    
    Ada beberapa istilah penting yang perlu diperhatikan, seperti
    - <Item> adalah nama model
    - <models.Model> merupakan kelas dasar yang digunakan untuk mendefinisikan model dalam Django
    - <name>, <amount>, <date_added>, <price>, dan <description> adalah atribut pada model dan setiap field memiliki tipe data, seperti <Charfield>, <IntegerField>, <DateField>, dan <TextField>

    e. Membuat fungsi pada <views.py>
    Berikut fungsi pada <views.py> untuk mengembalikan nama aplikasi, nama, dan kelas saya

        from django.shortcuts import render

        def show_main(request):
            context = {
                'my_app': 'Bmo Store',
                'name': 'FBmo',
                'class': 'PBP C'
            }

            return render(request, "main.html", context)

    Ada beberapa istilah penting yang perlu diperhatikan, seperti
    - <def show_main(request)> adalah deklarasi fungsi <show_main> yang menerima parameter <request>. Fungsi ini mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai
    - <context> adalag dictionary data yang akan dikirimkan ke tampilan
    - return render(request, "main.html", context) berguna untuk melakukan render tampilan <main.html>

    f. Membuat routing pada <urls.py> aplikasi main
    - Setelah membuat fungsi pada <views.py>, saya perlu membuat routing pada <urls.py> aplikasi main untuk memetakan fungsi yang telah dibuat dengan kode sebagai berikut,

        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
    
    Ada beberapa istilah penting yang perlu diperhatikan, seperti
    - impor <path> dari <django.urls> untuk mendefinisikan pola URL
    - <app_name> merupakan variabel dari nama unik pada pola URL dalam aplikasi
    - fungsi <show_main> dari main.views digunakan sebagai tampilan yang akan ditampilkan ketika URL terkait diakses

    g. Melakukan deployment ke Adaptable
    


2. Bagan Request Client
![alt text](C:\Users\fzlbm\UI\Kuliah\Semester_3\PBP\Tugas\django-request-flow.png)

- <urls.py>, sebagai tempat perkumpulan URL.Django akan mencari melewati file ini untuk menemukan URL yang paling cocok sesuai dengan permintaan
- <views.py>, sebagai jembatan penghubung dengan dua file lainnya, yaitu <models.py> dan <template>. Setelah mendapat HttpRequest dari URL yang berkaitan, <views.py> dapat meminta data yang diperlukan melalui <models.py> dan dapat melakukan render HTML menggunakan <template> agar dapat disajikan kepada pengguna
- <models.py>, sebagai pengolah data dan penghubung antara database dengan <views.py>. <models.py> dapat melakukan manipulasi struktur data aplikasi sesuai kebutuhan pengguna
- <template>, struktur tampilan antarmuka pengguna yang akan membantu <views.py> dalam melakukan proses render HTML

3. Alasan Penggunaan Virtual Environment
Virtual Environment merupakan tools untuk membuat lingkungan python virtual yang terisolasi. Terisolasi di sini maksudnya versi-versi dependensi atau packages yang ada di dalam lingkungan virtual tidak akan berpengaruh dengan versi dependensi yang ada di komputer lokal. Penggunaan virtual env cukup umum ketika ingin membuat proyek Django karena dengan adanya lingkungan isolasi, python yang digunakan untuk menjalankan proyek Django tidak akan terganggu dengan pembaruan yang terjadi di komputer lokal (jika ada pembaruan) sehingga proyek dapat tetap berjalan walaupun adanya perubahan versi modul python di komputer lokal. Sebuah proyek Django sebenarnya dapat tetap dijalankan jika tidak menggunakan virtual env, namun ada kemungkinan proyek akan mengalami gangguan karena adanya perubahan modul akibat perubahan versi modul di komputer lokal. Oleh karena itu, virtual env sangat disarankan apabila kita ingin membuat suatu proyek berbasis Django. 

4. Penjelasan MVC, MVT, dan MVVM
    a. MVC
    Model View Controller adalah salah satu pola arsitektur dalam pembuatan aplikasi dengan bagian-bagian seperti berikut,

    - Model, betugas untuk menyiapkan, mengatur, memanipulasi, dan mengorganisasikan data yang ada di dalam database

    - View, bertugas untuk merepresentasikan informasi atau data yang telah dikelola oleh model agar dapat dilihat pengguna

    - Controller, bertugas untuk menghubungkan serta mengatur model dan view agar dapat saling terhubung.

    Contoh framework yang menggunakan MVC adalah Spring Boot
        
    b. MVT
    Model View Template merupakan pola arsitektur pengembangan aplikasi yang dapat dikatakan mirip dengan MVC, namun memiliki perbedaan di bagian controller. Pada MVT, controller diganti menjadi template. Template inilah yang akan menjadi representasi tampilan yang diperlihatkan kepada pengguna yang biasanya menggunakan HTML. 
    
    - Model, bertugas untuk mengatur dan mengelola data dari aplikasi

    - View, bertugas untuk mengontrol bagaimana data yang dikelola oleh model akan ditampilkan kepada pengguna

    - Template, bertugas mengatur tampilan yang diperlihatkan kepada pengguna

    Contoh framework yang menggunakan MVT adalah Django. 

    c. MVVM
    Model View ViewModel merupakan gabungan dari MVC dan MVP.

    - Model, terdiri dari data dasar yang digunakan untuk menjalankan aplikasi

    - View, sebagai antarmuka pengguna dan pola desain, mirip seperti yang digunakan oleh MVC

    - ViewModel, di satu sisi adalah abstraksi dari View, lalu sisi yang lain sebagai penyedia pembungkus model data yang akan ditautkan. ViewModel terdiri dari Model yang diubah menjadi View dan berisi perintah yang dapat digunakan oleh View untuk memengaruhi Model

    Contoh framework yang menggunakan MVVM adalah WPF.
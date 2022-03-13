# haddadblog

*haddadblog* merupakan personal blogging yang berisi profil dan artikel-artikel. Pengguna dapat melakukan register dan login untuk berinteraksi secara langsung di tiap artikel dengan memberikan komentar. Project dapat diakses melalui link berikut: https://haddadblog.herokuapp.com

## Daftar isi

- [haddadblog](#haddadblog)
  - [Daftar isi](#daftar-isi)
  - [Menjalankan Project](#menjalankan-project)
  - [Membuat Artikel](#membuat-artikel)
  - [Kontribusi](#kontribusi)
  - [Lisensi](#lisensi)

## Menjalankan Project 

1. Untuk menjalankan project pada laptop anda, pastikan anda telah menginstall python dan git, selanjutnya buka Command Prompt (cmd) atau terminal dan lakukan `clone` 
   ```shell
   git clone https://github.com/haddad9/haddadblog.git
   ```

2. lakukan `cd` pada direktori yang di-*clone*
   ```shell
   cd haddadblog
   ``` 


3. Buat Python *virtual environment* di dalamnya.

   ```shell
   python -m venv venv
   ```

   > Catatan: sesuaikan dengan *executable* `python` yang ada di komputer kamu,
   > karena terkadang (misal: di Ubuntu atau macOS) Python 3 hanya bisa
   > dipanggil dengan `python3`, bukan `python`.

4. Aktifkan *virtual environment* yang telah dibuat.\
   Di Windows:

   ```shell
   venv\Scripts\activate
   ```

   Di Linux/macOS:

   ```shell
   source venv/bin/activate
   ```

   Jika berhasil, akan muncul `(venv)` pada *prompt* cmd/terminal kamu.

5. Instal requirements Django pada *virtual environment* tersebut.

   ```shell
   python -m pip install - r requirements.txt
   ```

6. Lakukan migrasi database pada project Django

   ```shell
   python manage.py makemigrations
   ```

   ```shell
   python manage.py migrate
   ```


7. Jalankan project Django
   ```shell
   python manage.py runserver
   ```



## Membuat Artikel

Setelah menjalankan project Django, anda memerlukan `admin-privelege` untuk bisa menambahkan artikel baru pada blog.

1. Buat superuser

   ```shell
   python manage.py create superuser
   ```

   Isi username serta password sesuai dengan yang anda inginkan

2. Akun dengan username dan password yang abru dibuat memiliki akses `admin-privelge` sehingga akan muncul tombol untuk menambahkan artikel. Buatlah artikel dengan mengisi form yang telah disediakan pada aplikasi.

  

## Kontribusi

Saya terbuka terhadap hal-hal yang dapat diperbaiki, apabila ingin berkontribusi pada project saya, silakan buat *issue* atau kirim
*pull request* ke repositori untuk project  ini di [**GitHub**](https://github.com/haddad9/haddadblog).


## Lisensi
Project ini dibangun menggunakan [Django](https://www.djangoproject.com), [Bootsrap](https://getbootstrap.com), [Animate.css](https://getbootstrap.com)

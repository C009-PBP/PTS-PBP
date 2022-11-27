## Kelompok C09:
* Ardhito Nurhadyansah - 2106750206
* Aulia Fikri Al Khawariz - 2106701160
* Najmi Anasya Calyla - 2106639825
* Reza Taufiq Yahya - 2106654183
* Shafa Trivia Ezananda - 2206026971

## Tautan aplikasi Heroku: https://health-bud.herokuapp.com/


## Cerita aplikasi yang diajukan serta manfaatnya:

HealthBud merupakan aplikasi yang dibuat untuk mendukung pengadaan fasilitas kesehatan yang efektif dan efisien. Di bawah ini merupakan fitur-fitur yang terdapat pada aplikasi HealthBud:

- Homepage (Fikri)

HealthBud tentunya akan mempunyai tampilan utama, di mana  semua akses untuk menuju modul lainnya akan terdapat di homepage. Ketika user sudah selesai melakukan login, maka tampilan yang terlihat akan menuju homepage. Di homepage nantinya, selain ada tombol untuk mengakses modul yang lain, akan terdapat kolom untuk menulis review dari user tentang aplikasi HealthBud. Nantinya, semua reviews dari user akan bisa dilihat di homepage, tidak hanya review dari akun yang sedang login.

- Kalkulator BMI (Ardhito)

Untuk membantu user dalam memantau kesehatannya secara mandiri, HealthBud menyediakan fitur kalkulator BMI. Nantinya, user dapat memasukkan tinggi dan berat badannya ke input-field yang sesuai, lalu menekan tombol submit. Hasil perhitungan serta analisisnya akan muncul di halaman yang sama dan disimpan sebagai informasi riwayat kesehatan user berdasarkan BMI. Riwayat hasil analisis BMI dapat dilihat dengan menekan tombol riwayat BMI. Di dalam aplikasi ini, AJAX dapat diimplementasikan untuk melakukan load hasil BMI maupun hasil riwayat analisis BMI dari user secara asinkronus.

- Pengaturan akun (Nasya)

Di halaman pengaturan akun HealthBud, user dapat melengkapi data diri dan melakukan pengaturan akun miliknya. Salah satu fitur utama pada halaman ini adalah form riwayat kesehatan digital yang dapat diisi oleh user. Di halaman ini, akan disediakan form untuk mengisi informasi-informasi terkait kondisi kesehatan user. Setelah disimpan, data dapat diakses oleh user dan ditunjukkan saat berkonsultasi dengan dokter. Tujuan dari penyimpanan riwayat kesehatan digital adalah agar HealthBud dapat memudahkan user dalam menyimpan dan mengelola dokumen-dokumen atau informasi-informasi yang terkait dengan kondisi kesehatannya dengan aman. Fitur melihat dan memperbarui informasi pada profil dan pengaturan riwayat kesehatan hanya dapat diakses oleh pengguna yang sudah mendaftarkan akun dan login. Implementasi AJAX dilakukan ketika user memperbarui informasi-informasi utama profilnya (contoh nama dan foto profil) serta pada form riwayat kesehatan. 

- Jadwal praktek dokter + review dokter (Reza)

Salah satu tujuan dari aplikasi HealthBud ialah untuk mempermudah user mencari jadwal praktek dokter. Jadwal tersebut direpresentasikan dengan menggunakan tabel yang mengandung nama dokter, hari dan jam dokter tersebut praktik. Selain itu, user juga dapat mengirimkan review terhadap dokter.

- Tanya Dokter (Safa)

Healthbud dilengkapi fitur Tanya Dokter di mana orang umum dapat bertanya langsung pertanyaan-pertanyaan seputar kesehatan kepada dokter yang ahli di bidang tersebut. Ketika user masuk ke dalam app ini, akan diberikan opsi bertanya secara umum (berbentuk forum). Sebelum bertanya, tata cara akan ditampilkan dengan bentuk tampilan berupa card. 
Berikut tata caranya :
1. Pilih spesialisasi bidang dari pertanyaan yang ingin kamu ajukan. </br>
2. Isi formulir pertanyaan yang berisi judul dan pertanyaan yang ingin kamu tanyakan.  </br>
3. Apabila pertanyaanmu telah terverifikasi, tunggu dokter yang ahli pada bidang yang kamu pilih untuk menjawab pertanyaanmu. </br>
4. Setelah pertanyaanmu terjawab oleh dokter, pertanyaanmu akan berada pada halaman utama forum. </br>

Di dalam aplikasi ini, Implementasi AJAX dilakukan untuk mengambil input *form* berisi judul dan isi pertanyaan serta memuat pertanyaan dari user beserta jawaban dari dokter pada forum secara asinkronus.


## Daftar modul yang akan diimplementasikan:
* Authentication (untuk membedakan jenis user, melakukan register, dan login) --> Dhito
* Form pendaftaran client/pengaturan akun (riwayat kesehatan, dll) -> Nasya
* Kalkulator BMI -> Dhito
* Jadwal praktek dokter + review dokter -> Reza
* Tanya jawab dokter (Forum) -> Safa
* Homepage (mengandung review dari pasien menuju aplikasi)-> Fikri


## Role atau peran pengguna beserta deskripsinya (karena bisa saja lebih dari satu jenis pengguna yang mengakses aplikasi):

Pada implementasi aplikasi kami, jenis pengguna yang akan dapat menggunakan app ini adalah pasien dan dokter. Pasien harus login terlebih dahulu untuk dapat menggunakan app ini. Setelah berhasil masuk, Pasien akan ter-direct ke halaman homepage. Setelahnya, di homepage akan ditampilkan akses ke dalam modul yang lain, seperti Kalkulator BMI, Pengaturan Akun (isi profil), Info Dokter, serta Tanya Dokter.


Untuk dokter, login juga perlu dilakukan terlebih dahulu. Setelah berhasil masuk, Dokter akan ter-direct ke halaman homepage. Di homepage, akan ditampilkan akses ke dalam modul yang lain. Namun, user dengan tipe dokter tidak dapat mengakses aplikasi kalkulator BMI (diperuntukkan khusus untuk pasien). 

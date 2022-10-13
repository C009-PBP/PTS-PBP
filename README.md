## Kelompok C09:
Ardhito Nurhadyansah - 2106750206
Aulia Fikri Al Khawariz - 2106701160
Najmi Anasya Calyla - 2106639825
Reza Taufiq Yahya - 2106654183
Shafa Trivia Ezananda - 2206026971

## Tautan aplikasi Heroku: https://healthbud.herokuapp.com/

## Cerita aplikasi yang diajukan serta manfaatnya:

HealthBud merupakan aplikasi yang dibuat untuk mendukung pengadaan fasilitas kesehatan yang efektif dan efisien. Di bawah ini merupakan fitur-fitur yang terdapat pada aplikasi HealthBud:

- Homepage (Fikri)

HealthBud tentunya akan mempunyai tampilan utama, di mana  semua akses untuk menuju modul lainnya akan terdapat di homepage. Ketika user sudah selesai melakukan login, maka tampilan yang terlihat akan menuju homepage. Di homepage nantinya, selain ada tombol untuk mengakses modul yang lain, maka akan terdapat juga kolom untuk menulis review dari user tentang aplikasi HealthBud. Nantinya, semua reviews dari user akan bisa dilihat di homepage, tidak hanya review dari akun yang sedang login.

- Kalkulator BMI (Ardhito)

Untuk membantu user dalam memantau kesehatannya secara mandiri, HealthBud menyediakan fitur kalkulator BMI. Nantinya, user dapat memasukkan tinggi dan berat badannya ke input-field yang sesuai, lalu menekan tombol submit. Hasil perhitungan serta analisisnya akan muncul di halaman yang sama dan disimpan sebagai informasi riwayat kesehatan user berdasarkan BMI. Riwayat hasil analisis BMI dapat dilihat dengan menekan tombol riwayat BMI. Di dalam aplikasi ini, AJAX dapat diimplementasikan untuk melakukan load hasil BMI maupun hasil riwayat analisis BMI dari user secara asinkronus.

- Pengaturan akun (Nasya)

Di halaman pengaturan akun HealthBud, user dapat melengkapi data diri dan melakukan pengaturan akun miliknya. Salah satu fitur utama pada halaman ini adalah form riwayat kesehatan digital yang dapat diisi oleh user. Di halaman ini, akan disediakan form untuk mengisi informasi-informasi terkait kondisi kesehatan user. Setelah disimpan, data dapat diakses oleh user dan ditunjukkan saat berkonsultasi dengan dokter. Tujuan dari penyimpanan riwayat kesehatan digital adalah agar HealthBud dapat memudahkan user dalam menyimpan dan mengelola dokumen-dokumen atau informasi-informasi yang terkait dengan kondisi kesehatannya dengan aman. Fitur melihat dan memperbarui informasi pada profil dan pengaturan riwayat kesehatan hanya dapat diakses oleh pengguna yang sudah mendaftarkan akun dan login. Implementasi AJAX dilakukan ketika user memperbarui informasi-informasi utama profilnya (contoh nama dan foto profil) serta pada form riwayat kesehatan. 

- Jadwal praktek dokter + review dokter (Reza)

App HealthBud ini manfaatnya mempermudah user untuk mencari jadwal praktek dokter dan mencari informasi rumah sakit terdekat yang ada di jadwal praktek dokter. Di dalam app Healthbud ini nanti terdapat tabel. Isi tabel tersebut ada hari tanggal bulan tahun, kemudian nama dokter, jadwal praktek dokter hari tanggal bulan tahun serta jam praktek dan tempat dokter itu praktek yang terakhir ada review dokter yang isinya adalah review dari pasien setelah konsul ke dokter tersebut. Untuk implementasi ajax terdapat pada fitur review dokter untuk input form

- Tanya Dokter (Safa)

Healthbud dilengkapi fitur Tanya Dokter di mana orang umum dapat bertanya langsung pertanyaan-pertanyaan seputar kesehatan kepada dokter yang ahli di bidang tersebut. Ketika user masuk ke dalam app ini, akan diberikan opsi bertanya secara umum (berbentuk forum). Sebelum bertanya, tata cara akan ditampilkan dengan bentuk tampilan berupa card. 
Berikut tata caranya :
Pilih spesialisasi bidang dari pertanyaan yang ingin kamu ajukan.
Isi formulir pertanyaan yang berisi judul dan pertanyaan yang ingin kamu tanyakan.
Apabila pertanyaanmu telah terverifikasi, tunggu dokter yang ahli pada bidang yang kamu pilih untuk menjawab pertanyaanmu.
Setelah pertanyaanmu terjawab oleh dokter, pertanyaanmu akan berada pada halaman utama forum.


## Daftar modul yang akan diimplementasikan:
Login (username+pass) + register biasa
Form pendaftaran client/pengaturan akun (riwayat kesehatan, dll) -> Nasya
Kalkulator BMI -> Dhito
Jadwal praktek dokter + review dokter -> Reza
Tanya jawab dokter (Forum) -> Safa
Homepage (formnya → review dari pasien ke aplikasi kita), terus nanti bisa kayak ada tampilan reviews dari usernya -> Fikri


## Role atau peran pengguna beserta deskripsinya (karena bisa saja lebih dari satu jenis pengguna yang mengakses aplikasi):

Pada implementasi aplikasi kami, jenis pengguna yang akan dapat menggunakan app ini adalah pasien dan dokter. Pasien harus login terlebih dahulu untuk dapat menggunakan app ini. Setelah berhasil masuk, Pasien akan ter-direct ke halaman homepage. Setelahnya, di homepage akan ditampilkan akses ke dalam modul yang lain, seperti Kalkulator BMI, Pengaturan akun (Isi profil), jadwal praktik dan review dokter, serta Tanya Dokter.

Untuk dokter, login juga perlu dilakukan terlebih dahulu. Setelah berhasil masuk, Dokter akan ter-direct ke halaman homepage. Di homepage, akan ditampilkan akses ke dalam modul yang lain, seperti Pengaturan akun (Isi profil), jadwal praktik dan review dokter, serta Tanya Dokter.

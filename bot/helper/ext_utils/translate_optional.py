CLONE_HELP_MESSAGE = ["""<i>Kirim Gdrive | Gdtot | Tekan file | Filebee | Appdrive | Tautan Gdflix atau jalur RClone bersama dengan atau dengan membalas tautan/rc_path dengan perintah dengan Argumen.</i>

➲ <b><u>Argumen yang Tersedia</u></b>:

1. <b>-up atau -upload :</b> Unggah ke Drive atau RClone atau DDL Anda
2. <b>-i :</b> Unduh multi tautan dengan membalas
3. <b>-rcf :</b> RClone Bendera tambahan
4. <b>-id :</b> Id atau tautan Folder GDrive
5. <b>-index:</b> Url indeks untuk gdrive_arg
6. <b>-c atau -category :</b> Kategori Gdrive yang akan Diunggah, Nama Tertentu <tidak peka huruf besar-kecil>""",
"""<b><i> Tautan:</i></b>
Gdrive | Gdtot | Tekan file | Filebee | Appdrive | Tautan Gdflix atau jalur rclone

➲ <b><i>Multi Tautan <hanya dengan membalas gdlink atau rclone_path pertama>:</i></b>
<kode>/cmd</kode> -i 10<jumlah tautan/jalur>

➲ <b><i> Tautan Gdrive:</i></b>
<kode>/cmd</kode> gdrive_link

➲ <b><i>Jalur Klon RC dengan Bendera RC:</i></b> -rcf
<kode>/cmd</kode> <rcl atau rclone_path> -up <rcl atau rclone_path> -rcf flagkey:flagvalue|flagkey|flagkey:flagvalue

➲ <b><i>Unggah Drive Khusus:</i></b> -id & -index<Opsional>
<kode>/{cmd}</code> -id <kode>drive_folder_link</code> atau <kode>drive_id</code> -index <kode>https://example.com/0:</code>

➲ <b><i>Pilihan Kategori Khusus:</i></b> -c atau -kategori
<kode>/{cmd}</kode> -c <kode>nama_kategori</kode>

<b>CATATAN:</b>
1. Jika -up atau -upload tidak ditentukan maka tujuan rclone adalah RCLONE_PATH dari <code>config.env</code>.
2. Jika UserTD diaktifkan, maka hanya UserTD yang akan diunggah ke UserTD baik melalui tombol arg atau kategori langsung.
3. Untuk Multi Custom Upload selalu gunakan Arg di pesan masing-masing lalu balas dengan /cmd -i 10 <jumlah link>
"""]




PASSWORD_ERROR_MESSAGE = """
 < b>Tautan ini memerlukan kata sandi!< / b>
- Masukkan tanda<b>:: < /b> setelah tautan dan tulis kata sandi setelah tanda.
< b > Contoh: < / b> {}:: cinta kamu
Catatan: Tidak ada spasi di antara tanda <b>::< / b>
Untuk kata sandinya, Anda bisa menggunakan spasi! """
#!/usr/bin/env python3
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.ext_utils.TRANSLATE import default_desp , MIRROR_HELP_MESSAGE
from bot.helper.ext_utils.translate_optional import PASSWORD_ERROR_MESSAGE , CLONE_HELP_MESSAGE

YT_HELP_MESSAGE = ["""<i>Kirim tautan / file bersama dengan cmd atau balas cmd ke mirror atau leech yang didukung ytdl di Telegram atau GDrive atau DDLs dengan Mesin berbeda seperti RClone atau yt-dlp</i>

➲ <b><u>Available Args</u></b>:

1.  <b> - n atau-name: < / b> Ganti nama berkas.
2.  <b> - z atau-zip: < / b> Berkas zip atau Tautan
3.  <b>-naik atau-unggah: < / b> Unggah ke Drive Anda atau RClone atau DDL
4.  <b> - b atau-bulk: < / b> Unduh tautan massal.
5.  <b>-i: < /b> Unduh banyak tautan dengan balas
6.  <b> - m atau-sd atau-samedir: < / b> Unduh banyak tautan dalam direktori unggahan yang sama.
7.  <b>-opt or-options: < / b> Lampirkan opsi yt-dlp Khusus untuk ditautkan
8.  <b>-s atau-select: < / b> Pilih file dari tautan yt-dlp meskipun kualitas ditentukan
9.  <b>-rcf: < / b> RClone Bendera tambahan
10. <b>-id: < / b> Id atau tautan Folder GDrive
11. <b> - indeks: < / b> Url indeks untuk gdrive_arg
12. <b> - c or -category: < / b> Kategori Gdrive untuk Diunggah, Nama Spesifik (tidak peka huruf besar / kecil)
13. < b > -ud atau-dump: < / b> Buang kategori yang akan Diunggah, Nama Tertentu (tidak peka huruf besar / kecil) atau chat_id atau chat_username
14. <b> - ss atau-screenshots: < / b> Hasilkan Tangkapan Layar untuk File Leeched
15. <b> - t atau-thumb: < / b> Tumbnail Khusus untuk Hasil leech Tertentu
""", """
<blockquote>➲ <b><i>Kirim tautan bersama dengan baris perintah</i></b>:
<code>/cmd</code> link -s -n nama baru -opt x:y|x1:y1

➲ <b><i>Dengan membalas tautan</i></b>:
<code>/cmd</code> -n  nama baru -z password -opt x:y|x1:y1

➲ <b><i>Nama Baru</i></b>: -n or -name
<code>/cmd</code> link -n nama baru
<b> Catatan: </b> Jangan menambahkan ekstensi file

➲ <b><i>Pembuatan Tangkapan Layar</b>: -ss or -screenshots
<code>/cmd</code> link -ss number ,Screenshots untuk setiap File Video

➲ <b><i>Custom Thumbnail</b>: -t or -thumb
<code>/cmd</code> link -t tglink|dl_link
<b>Direct Link:</b> dl_link specifies download link, where it is Image url
<b>Tg Link:</b> Give Public/Private/Super Link to download Image from Tg

➲ <b><i>Quality Buttons</i></b>: -s or -select
Memetikan kualitas default ditambahkan dari opsi yt-dlp menggunakan opsi format dan Anda perlu memilih kualitas untuk tautan atau tautan tertentu dengan fitur multi tautan.
<code>/cmd</code> link -s

➲ <b<i>Zip files (dengan/tanpa pasword)</i></b>: -z or -zip password
<code>/cmd</code> link -z (zip)
<code>/cmd</code> link -z password (pasword zip)

➲ <b><i>Options</i></b>: -opt or -options
<code>/cmd</code> link -opt playliststart:^10|fragment_retries:^inf|matchtitle:S13|writesubtitles:true|live_from_start:true|postprocessor_args:{"ffmpeg": ["-threads", "4"]}|wait_for_video:(5, 100)
<b>Note:</b> Tambahkan `^` sebelum integer atau float, beberapa nilai harus berupa numerik dan beberapa string.
Seperti playlist_items:10 berfungsi dengan string, jadi tidak perlu menambahkan "^" sebelum angka tetapi playlistend hanya berfungsi dengan integer jadi Anda harus menambahkan "^" sebelum angka seperti contoh di atas.
Anda juga dapat menambahkan Tuple dan dict. Gunakan tanda kutip ganda di dalam dict.

➲ <b><i>Multi tautan hanya dengan membalas tautan pertama</i></b>: -i
<code>/cmd</code> -i 10(jumlah link)

➲ <b><i>Multi tautan dalam direktori unggahan yang sama hanya dengan membalas tautan pertama</i></b>: -m or -sd or -samedir
<code>/cmd</code> -i 10(jumlah link) -m nama folder

➲ <b><i>Upload Custom Drive:</i></b> -id & -index(Optional)
<code>/{cmd}</code> -id <code>drive_folder_link</code> or <code>drive_id</code> -index <code>https://example.com/0:</code>
Di sini, drive_id harus berupa id folder atau tautan folder dan indeks harus berupa url jika tidak maka tidak akan diterima.

➲ <b><i>Custom Category Select:</i></b> -c or -category
<code>/{cmd}</code> -c <code>category_name</code>
Ini berfungsi untuk Kategori Bot dan juga UserTDs (jika diaktifkan)
Anda juga dapat memilih Drive Upload dari Buttons jika memiliki lebih dari 1 dan argumen ini tidak ditentukan

➲ <b><i>Custom Dump Select:</i></b> -ud or -dump
<code>/{cmd}</code> -ud <code>dump_name</code> or <code>@username</code> or <code>-100xxxxxx chat_id</code> or all
Anda juga dapat memilih Buang Obrolan dari Tombol jika memiliki lebih dari 1 dan argumen ini tidak ditentukan
Anda -ud semua untuk Mengunggah di semua Dump Obrolan Anda
Pastikan Bot sudah menjadi Admin jika tidak, Bot tidak akan menerima.

➲ <b><i>Upload</i></b>: -up or -upload
<code>/cmd</code> link -up <code>rcl</code> (Untuk memilih konfigurasi rclone, remote dan path)
<code>/cmd</code> link -up <code>ddl</code>
Anda dapat langsung menambahkan jalur unggah: -up remote:dir/subdir

Jika DEFAULT_UPLOAD adalah rc maka Anda dapat meneruskan: gd untuk mengunggah menggunakan alat gdrive ke GDRIVE_ID.
Jika DEFAULT_UPLOAD adalah gd maka Anda dapat meneruskan: rc untuk mengunggah ke RCLONE_PATH.
Jika DEFAULT_UPLOAD adalah ddl maka Anda dapat melewatkan: rc atau gd untuk mengunggah ke RCLONE_PATH atau GDRIVE_ID
Jika Anda ingin menambahkan jalur secara manual dari konfigurasi Anda (diunggah dari usetting) tambahkan mrcc: sebelum jalur tanpa spasi
<code>/cmd</code> link -up <code>mrcc:</code>main:dump

➲ <b><i>RClone Flags</i></b>: -rcf
<code>/cmd</code> link -up path|rcl -rcf --buffer-size:8M|--drive-starred-only|key|key:value
This will override all other flags except --exclude
Check here all <a href='https://rclone.org/flags/'>RcloneFlags</a>.

➲ <b><i>Unduhan Massal</i></b>: -b or -bulk
Massal dapat digunakan melalui pesan teks dan dengan membalas file teks berisi tautan yang dipisahkan oleh baris baru.
Anda dapat menggunakannya hanya dengan membalas pesan (teks/file).
Semua opsi harus disertai tautan!
<b>Contoh:</b>
link1 -n nama baru -up remote1:path1 -rcf |key:value|key:value
link2 -z -n nama baru -up remote2:path2
link3 -z -n nama baru -opt ytdlpoptions

<b>Note:</b> Anda tidak dapat menambahkan -m arg hanya untuk beberapa tautan, lakukan untuk semua tautan atau gunakan multi tanpa massal!
tautan pswd: pass(zip) opt: ytdlpoptions up: remote2:path2
Balas contoh ini dengan cmd /cmd b(bulk) ini
Anda dapat mengatur awal dan akhir tautan dari massal dengan -b start:end atau hanya diakhiri dengan -b :end atau hanya dimulai dengan -b start. Awal defaultnya adalah dari nol (tautan pertama) hingga inf.

➲ <b>NOTES:</b>
Periksa semua opsi API yt-dlp dari <a href='https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184'>FILE</a> ini </blockquote>
"""]


RSS_HELP_MESSAGE = """
<blockquote expandable>➲ <b>Format to adding feed url(s):</b>
Title1 link (required)
Title2 link -c cmd -inf xx -exf xx
Title3 link -c cmd -d ratio:time -z password

➲ <b><i>Argument Details:</i></b>
-c command + any arg
-inf For included words filter.
-exf For excluded words filter.

<b>Example:</b> Title https://www.rss-url.com inf: 1080 or 720 or 144p|mkv or mp4|hevc exf: flv or web|xxx opt: up: mrcc:remote:path/subdir rcf: --buffer-size:8M|key|key:value
This filter will parse links that it's titles contains `(1080 or 720 or 144p) and (mkv or mp4) and hevc` and doesn't conyain (flv or web) and xxx` words. You can add whatever you want.

Another example: inf:  1080  or 720p|.web. or .webrip.|hvec or x264. This will parse titles that contains ( 1080  or 720p) and (.web. or .webrip.) and (hvec or x264). I have added space before and after 1080 to avoid wrong matching. If this `10805695` number in title it will match 1080 if added 1080 without spaces after it.

➲ <b><i>Filter Notes:</i></b>
1. | means and.
2. Add `or` between similar keys, you can add it between qualities or between extensions, so don't add filter like this f: 1080|mp4 or 720|web because this will parse 1080 and (mp4 or 720) and web ... not (1080 and mp4) or (720 and web)."
3. You can add `or` and `|` as much as you want."
4. Take look on title if it has static special character after or before the qualities or extensions or whatever and use them in filter to avoid wrong match.</blockquote>

<b>Timeout:</b> 60 sec.
"""


CATEGORY_HELP_MESSAGE = """id: Balas ke aktif /{cmd} yang digunakan untuk memulai pengunduhan atau tambahkan gid bersama dengan {cmd}
Perintah ini terutama untuk mengubah kategori jika Anda memutuskan untuk mengubah kategori dari unduhan yang sudah ditambahkan.
Tetapi Anda selalu dapat menggunakan-c atau -category with untuk memilih kategori sebelum pengunduhan dimulai.

<blockquote dapat diperluas>➲
<code> / {cmd}</code> - id <code>drive_folder_link<code> atau <code>drive_id</code> -indeks <code>https://example.com/0: </code> gid atau dengan membalas unduhan aktif

<b>CATATAN: </b> drive_id harus berupa id folder atau tautan folder dan indeks harus berupa url jika tidak maka tidak akan diterima
"""

help_string = [f'''⌬ <bold><i>Perintah Dasar!</i></bold>

<bold>Gunakan perintah Mirror untuk mengunduh link/file/rcl</bold>
• /{BotCommands.MirrorCommand[0]} or /{BotCommands.MirrorCommand[1]}: Unduh melalui file/url/media untuk Diunggah ke Cloud Drive.
• /{BotCommands.CategorySelect}: Pilih kategori Khusus untuk Diunggah ke Cloud Drive dari Kategori UserTds atau Bot.

<bold>Gunakan perintah qBit hanya untuk torrent:</bold>
• /{BotCommands.QbMirrorCommand[0]} or /{BotCommands.QbMirrorCommand[1]}: Unduh menggunakan qBittorrent dan Unggah ke Cloud Drive.
• /{BotCommands.BtSelectCommand}: Select files from torrents by btsel_gid or reply.

<bold>Gunakan perintah yt-dlp untuk YouTube atau situs apa pun yang didukung:</bold>
• /{BotCommands.YtdlCommand[0]} atau /{BotCommands.YtdlCommand[1]}: Mencerminkan tautan yang didukung yt-dlp.

<bold>Gunakan perintah Leech untuk mengunggah ke Telegram:</bold>
• /{BotCommands.LeechCommand[0]} atau /{BotCommands.LeechCommand[1]}: Unggah ke Telegram.
• /{BotCommands.QbLeechCommand[0]} atau /{BotCommands.QbLeechCommand[1]}: Unduh menggunakan qBittorrent dan unggah ke Telegram (Hanya untuk torrent).
• /{BotCommands.YtdlLeechCommand[0]} atau /{BotCommands.YtdlLeechCommand[1]}: Unduh menggunakan Yt-Dlp (tautan yang didukung) dan unggah ke telegram.

<bold>Perintah G-Drive:</bold>
• /{BotCommands.CloneCommand[0]}: Salin file/folder ke Cloud Drive.
• /{BotCommands.CountCommand} [drive_url]: Menghitung file/folder Google Drive.
• /{BotCommands.DeleteCommand} [drive_url]: Hapus file/folder dari Google Drive (Hanya Pemilik & Sudo).

<bold>Batalkan Tugas:</bold>
• /{BotCommands.CancelMirror}: Batalkan tugas dengan cancel_gid atau balas.''',

f'''⌬ <bold><i>Perintah Pengguna</i></bold>

<bold>Bot Settings:</bold>
• /{BotCommands.UserSetCommand[0]} or /{BotCommands.UserSetCommand[1]} [query]: Buka Bot Setting hanya di PM

<bold>Otentikasi:</bold>
• /login: Login ke Bot untuk Mengakses Bot tanpa Sistem Temp Pass (Pribadi)

<bold>Statistik Bot:</bold>
• /{BotCommands.StatusCommand[0]} atau /{BotCommands.StatusCommand[1]}: Menampilkan halaman status dari semua tugas aktif.
• /{BotCommands.StatsCommand[0]} atau /{BotCommands.StatsCommand[1]}: Menampilkan statistik detail Server.
• /{BotCommands.PingCommand[0]} atau /{BotCommands.PingCommand[1]}: Periksa berapa lama waktu yang dibutuhkan untuk melakukan Ping ke Bot.

<bold>RSS Feed:</bold>
• /{BotCommands.RssCommand}: Open RSS Menu (Sub/Unsub/Start/Pause)''',

f'''⌬ <bold><i>Perintah Admin</i></bold>

<bold>Bot Settings:</bold>
• /{BotCommands.BotSetCommand[0]} atau /{BotCommands.BotSetCommand[1]} [query]: Buka Pengaturan Bot (Hanya Pemilik & Sudo).
• /{BotCommands.UsersCommand}: Menampilkan Info Statistik Pengguna (Hanya Pemilik & Sudo).

<bold>Otentikasi:</bold>
• /{BotCommands.AuthorizeCommand[0]} atau /{BotCommands.AuthorizeCommand[1]}: Mengotorisasi obrolan atau pengguna untuk menggunakan bot (Hanya Pemilik & Sudo).
• /{BotCommands.UnAuthorizeCommand[0]} atau /{BotCommands.UnAuthorizeCommand[1]}: Membatalkan otorisasi chat atau pengguna untuk menggunakan bot (Hanya Pemilik & Sudo).
• /{BotCommands.AddSudoCommand}: Tambahkan pengguna sudo (Pemilik Saja).
• /{BotCommands.RmSudoCommand}: Hapus pengguna sudo (Pemilik Saja).
• /{BotCommands.AddBlackListCommand[0]} atau /{BotCommands.AddBlackListCommand[1]}: Menambahkan Pengguna di Daftar Hitam, sehingga pengguna tidak dapat menggunakan Bot lagi.
• /{BotCommands.RmBlackListCommand[0]} atau /{BotCommands.RmBlackListCommand[1]}: Menghapus Pengguna yang Masuk Daftar Hitam, sehingga pengguna dapat menggunakan Bot lagi.

<bold>Statistik Bot:</bold>
• /{BotCommands.BroadcastCommand[0]} atau /{BotCommands.BroadcastCommand[1]} [reply_msg]: Disiarkan ke pengguna PM yang telah memulai bot kapan saja.

<bold>Perintah G-Drive:</bold>
• /{BotCommands.GDCleanCommand[0]} atau /{BotCommands.GDCleanCommand[1]} [drive_id]: Hapus semua file dari folder tertentu di Google Drive.

<bold>Batalkan Tugas:</bold>
• /{BotCommands.CancelAllCommand[0]}: Membatalkan semua Tugas & /{BotCommands.CancelAllCommand[1]} untuk Beberapa Bot.

<bold>Pemeliharaan:</bold>
• /{BotCommands.RestartCommand[0]} atau /{BotCommands.RestartCommand[1]}: Mulai ulang dan Perbarui Bot (Hanya Pemilik & Sudo).
• /{BotCommands.RestartCommand[2]}: Mulai ulang dan Perbarui semua Bot (Hanya Pemilik & Sudo).
• /{BotCommands.LogCommand}: Dapatkan file log bot. Berguna untuk mendapatkan laporan kerusakan (Hanya Pemilik & Sudo).

<bold>Ececutors:</bold>
• /{BotCommands.ShellCommand}: Jalankan perintah shell (Hanya Pemilik).
• /{BotCommands.EvalCommand}: Jalankan Baris Kode Python | Garis (Hanya Pemilik).
• /{BotCommands.ExecCommand}: Jalankan Perintah Di Exec (Hanya Pemilik).
• /{BotCommands.ClearLocalsCommand}: Hapus {BotCommands.EvalCommand} atau {BotCommands.ExecCommand} penduduk lokal (Pemilik Saja).
• /exportsession: Menghasilkan User StringSession dari Versi Pyro yang Sama (Hanya Pemilik).

<bold>Umpan RSS:</bold>
• /{BotCommands.RssCommand}: Buka Menu RSS (Sub/Batal Sub/Mulai/Jeda)

<bold>Ekstra:</bold>
• /{BotCommands.AddImageCommand} [url/foto]: Tambahkan Gambar di Bot
• /{BotCommands.ImagesCommand}: Menghasilkan grid Gambar Tersimpan.''',

f'''⌬ <bold><i>Perintah lain-lain!</i></bold>

<bold>Ekstra:</bold>
• /{BotCommands.SpeedCommand[0]} atau /{BotCommands.SpeedCommand[1]}: Periksa Kecepatan di VPS/Server.
• /{BotCommands.MediaInfoCommand[0]} atau /{BotCommands.MediaInfoCommand[1]} [url/media]: Menghasilkan MediaInfo dari Media atau Url DL

<bold>Pencarian Torrent/Drive:</bold>
• /{BotCommands.ListCommand} [kueri]: Telusuri di Google Drive.
• /{BotCommands.SearchCommand} [query]: Mencari torrent dengan API.

<bold>Pencarian Film/Acara TV/Drama:</bold>
• /{BotCommands.IMDBCommand}: Cari di IMDB.
• /{BotCommands.AniListCommand}: Mencari anime di AniList.
• /{BotCommands.AnimeHelpCommand}: Panduan bantuan anime.
• /{BotCommands.MyDramaListCommand}: Cari di MyDramaList.
''']

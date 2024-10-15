#!/usr/bin/env python3
from bot.helper.telegram_helper.bot_commands import BotCommands

YT_HELP_MESSAGE = ["""<i>Kirim tautan / file bersama dengan cmd atau balas cmd ke mirror atau leech ste yang didukung ytdl di Telegram atau GDrive atau DDLs dengan Mesin berbeda seperti RClone atau yt-dlp</i>

➲ <b><u>Argumen yg tersedia</u></b>:

1. <b>-n atau -name :</b> Ubah nama berkas.
2. <b>-z atau -zip :</b> Berkas Zip atau Tautan
3. <b>-up atau -upload :</b> Unggah ke Drive atau RClone atau DDL Anda
4. <b>-b atau -bulk :</b> Unduh tautan massal.
5. <b>-i :</b> Unduh beberapa tautan dengan membalas
6. <b>-m atau -sd atau -samedir :</b> Unduh beberapa tautan dalam direktori unggah yang sama. 7. <b>-opt atau -options :</b> Lampirkan opsi yt-dlp Kustom ke tautan
8. <b>-s atau -select :</b> Pilih file dari tautan yt-dlp meskipun qual ditentukan
9. <b>-rcf :</b> Bendera tambahan RClone
10. <b>-id :</b> ID atau tautan Folder GDrive
11. <b>-index:</b> Url indeks untuk gdrive_arg
12. <b>-c atau -category :</b> Kategori Gdrive yang akan Diunggah, Nama Tertentu (tanpa memperhatikan huruf besar/kecil)
13. <b>-ud atau -dump :</b> Buang kategori yang akan Diunggah, Nama Tertentu (tanpa memperhatikan huruf besar/kecil) atau chat_id atau chat_username
14. <b>-ss atau -screenshots :</b> Hasilkan Tangkapan Layar untuk File yang Diambil Secara Lintah
15. <b>-t atau -thumb :</b> Thumb Kustom untuk Lintah Tertentu
""", """
➲ <b><i>Kirim tautan beserta baris perintah</i></b>:
<code>/cmd</code> link -s -n new name -opt x:y|x1:y1

➲ <b><i>Dengan membalas tautan</i></b>:
<code>/cmd</code> -n new name -z password -opt x:y|x1:y1

➲ <b><i>Nama Baru</i></b>: -n atau -name
<code>/cmd</code> link -n new name
<b>Catatan:</b> Jangan tambahkan ekstensi file

➲ <b><i>Pembuatan Cuplikan Layar</b>: -ss atau -screenshots
<code>/cmd</code> link -ss number, Cuplikan Layar untuk setiap File Video

➲ <b><i>Thumbnail Kustom</b>: -t atau -thumb
<code>/cmd</code> link -t tglink|dl_link
<b>Tautan Langsung:</b> dl_link menentukan tautan unduhan, di mana ia adalah URL Gambar
<b>Tautan Tg:</b> Berikan Tautan Publik/Pribadi/Super untuk mengunduh Gambar dari Tg

➲ <b><i>Tombol Kualitas</i></b>: -s atau -select
Jika kualitas default ditambahkan dari opsi yt-dlp menggunakan opsi format dan Anda perlu memilih kualitas untuk tautan tertentu atau tautan dengan fitur multitautan. <code>/cmd</code> link -s

➲ <b<i>File Zip (dengan/tanpa kata sandi)</i></b>: -z atau -zip password
<code>/cmd</code> link -z (zip)
<code>/cmd</code> link -z password (zip dilindungi kata sandi)

➲ <b><i>Opsi</i></b>: -opt atau -options
<code>/cmd</code> link -opt playliststart:^10|fragment_retries:^inf|matchtitle:S13|writesubtitles:true|live_from_start:true|postprocessor_args:{"ffmpeg": ["-threads", "4"]}|wait_for_video:(5, 100)
<b>Catatan:</b> Tambahkan `^` sebelum integer atau float, beberapa nilai harus berupa angka dan beberapa string. Seperti playlist_items:10 yang bekerja dengan string, jadi tidak perlu menambahkan `^` sebelum angka, tetapi playlistend hanya bekerja dengan integer, jadi Anda harus menambahkan `^` sebelum angka seperti contoh di atas.
Anda juga dapat menambahkan tuple dan dict. Gunakan tanda kutip ganda di dalam dict.

➲ <b><i>Multi tautan hanya dengan membalas tautan pertama</i></b>: -i
<code>/cmd</code> -i 10(jumlah tautan)

➲ <b><i>Multi tautan dalam direktori unggah yang sama hanya dengan membalas tautan pertama</i></b>: -m atau -sd atau -samedir
<code>/cmd</code> -i 10(jumlah tautan) -m nama folder

➲ <b><i>Unggah Drive Kustom:</i></b> -id & -index(Opsional)
<code>/{cmd}</code> -id <code>drive_folder_link</code> atau <code>drive_id</code> -index <code>https://example.com/0:</code>
Di sini, drive_id harus berupa id folder atau tautan folder dan index harus berupa url, jika tidak, drive_id tidak akan diterima.

➲ <b><i>Pilihan Kategori Kustom:</i></b> -c atau -kategori
<code>/{cmd}</code> -c <code>nama_kategori</code>
Ini berfungsi untuk Kategori Bot dan UserTD (jika diaktifkan)
Anda juga dapat memilih Unggah Drive dari Tombol jika memiliki lebih dari 1 dan argumen ini tidak ditentukan
➲ <b><i>Pilih Dump Kustom:</i></b> -ud atau -dump
<code>/{cmd}</code> -ud <code>dump_name</code> atau <code>@username</code> atau <code>-100xxxxxx chat_id</code> atau semua
Anda juga dapat memilih Dump Chat dari Tombol jika memiliki lebih dari 1 dan argumen ini tidak ditentukan
Anda -ud semua untuk Mengunggah di semua Dump Chat milik Anda
Pastikan Bot sudah menjadi Admin jika tidak, bot tidak akan menerimanya.

➲ <b><i>Unggah</i></b>: -up atau -upload
<code>/cmd</code> link -up <code>rcl</code> (Untuk memilih konfigurasi rclone, remote, dan jalur)
<code>/cmd</code> link -up <code>ddl</code>
Anda dapat langsung menambahkan jalur unggah: -up remote:dir/subdir

Jika DEFAULT_UPLOAD adalah `rc` maka Anda dapat meneruskan: `gd` untuk mengunggah menggunakan alat gdrive ke GDRIVE_ID.
Jika DEFAULT_UPLOAD adalah `gd` maka Anda dapat meneruskan: `rc` untuk mengunggah ke RCLONE_PATH.
Jika DEFAULT_UPLOAD adalah `ddl` maka Anda dapat meneruskan: `rc` atau `gd` untuk mengunggah ke RCLONE_PATH atau GDRIVE_ID
Jika Anda ingin menambahkan jalur secara manual dari konfigurasi Anda (diunggah dari pengaturan penggunaan) tambahkan <code>mrcc:</code> sebelum jalur tanpa spasi
<code>/cmd</code> link -up <code>mrcc:</code>main:dump

➲ <b><i>RClone Flags</i></b>: -rcf
<code>/cmd</code> link -up path|rcl -rcf --buffer-size:8M|--drive-starred-only|key|key:value
This will override all other flags except --exclude
Check here all <a href='https://rclone.org/flags/'>RcloneFlags</a>.

➲ <b><i>Bulk Download</i></b>: -b or -bulk
Bulk can be used by text message and by replying to text file contains links seperated by new line.
You can use it only by reply to message(text/file).
All options should be along with link!
<b>Example:</b>
link1 -n new name -up remote1:path1 -rcf |key:value|key:value
link2 -z -n new name -up remote2:path2
link3 -z -n new name -opt ytdlpoptions

<b>Note:</b> You can't add -m arg for some links only, do it for all links or use multi without bulk!
link pswd: pass(zip) opt: ytdlpoptions up: remote2:path2
Reply to this example by this cmd <code>/cmd</code> b(bulk)
You can set start and end of the links from the bulk with -b start:end or only end by -b :end or only start by -b start. The default start is from zero(first link) to inf.

➲ <b>NOTES:</b>
Check all yt-dlp API options from this <a href='https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184'>FILE</a>
"""]

MIRROR_HELP_MESSAGE = ["""<i>Send links/files along with cmd or reply to cmd to mirror or leech on Telegram or GDrive or DDLs with different Engines like RClone, Aria2 or qBit</i>

➲ <b><u>Argumen yang Tersedia</u></b>:

1. <b>-n atau -name :</b> Mengganti nama berkas.

2. <b>-z atau -zip :</b> Meng-zip berkas atau Tautan

3. <b>-e atau -extract atau -uz atau -unzip :</b> Mengekstrak/Mem-unzip berkas dari Arsip

4. <b>-up atau -upload :</b> Mengunggah ke Drive atau RClone atau DDL Anda

6. <b>-b atau -bulk :</b> Mengunduh tautan massal.

7. <b>-i :</b> Mengunduh beberapa tautan dengan membalas

9. <b>-m atau -sd atau -samedir :</b> Mengunduh beberapa tautan dalam direktori unggah yang sama.

10. <b>-d atau -seed :</b> Benih torrent Bittorrent. 11. <b>-s atau -select :</b> Pilih berkas dari torrent melalui Bittorrent
12. <b>-u atau -user :</b> Masukkan nama pengguna untuk Auth
13. <b>-p atau -pass :</b> Masukkan kata sandi untuk Auth
14. <b>-j atau -join :</b> Gabungkan Beberapa Berkas. 15. <b>-rcf :</b> Bendera tambahan RClone
16. <b>-id :</b> ID atau tautan Folder GDrive
17. <b>-index:</b> Url indeks untuk gdrive_arg
18. <b>-c atau -category :</b> Kategori Gdrive yang akan diunggah, Nama Tertentu (tanpa memperhatikan huruf besar/kecil)
19. <b>-ud atau -dump :</b> Kategori Dump yang akan diunggah, Nama Tertentu (tanpa memperhatikan huruf besar/kecil) atau chat_id atau chat_username
20. <b>-ss atau -screenshots :</b> Hasilkan Tangkapan Layar untuk File yang Diambil Secara Leech
21. <b>-t atau -thumb :</b> Thumb Kustom untuk Leech Tertentu
""", """
➲ <b><i>Dengan di sepanjang cmd</i></b>:
<code>/cmd</code> link -n nama baru

➲ <b><i>Dengan membalas link/file</i></b>:
<code>/cmd</code> -n new name -z -e -up upload_destination

➲ <b><i>Nama Baru Kustom</i></b>: -n atau -name
<code>/cmd</code> link -n new name
<b>CATATAN</b>: Tidak berfungsi dengan torrent.

➲ <b><i>Otorisasi Tautan Langsung</i></b>: -u -p atau -user -pass
<code>/cmd</code> link -u username -p password

➲ <b><i>Header kustom tautan langsung</i></b>: -h atau -headers
<code>/cmd</code> link -h key: value key1: value1

➲ <b><i>Pembuatan Cuplikan Layar</b>: -ss atau -screenshots
<code>/cmd</code> link -ss number, Cuplikan Layar untuk setiap File Video

➲ <b><i>Thumnail Kustom</b>: -t atau -thumb
<code>/cmd</code> link -t tglink|dl_link
<b>Tautan Langsung:</b> dl_link menentukan tautan unduhan, di mana ia adalah URL Gambar
<b>Tautan Tg:</b> Berikan Tautan Publik/Pribadi/Super untuk mengunduh Gambar dari Tg

➲ <b><i>Ekstrak / Zip</i></b>: -uz -z atau -zip -unzip atau -e -ekstrak
<code>/cmd</code> link -e password (ekstrak dilindungi kata sandi)
<code>/cmd</code> link -z password (zip dilindungi kata sandi)
<code>/cmd</code> link -z password -e (ekstrak dan zip dilindungi kata sandi)
<code>/cmd</code> link -e password -z password (ekstrak dilindungi kata sandi dan zip dilindungi kata sandi)
<b>CATATAN:</b> Ketika ekstrak dan zip ditambahkan dengan cmd, maka akan mengekstrak terlebih dahulu lalu zip, jadi selalu ekstrak terlebih dahulu

➲ <b><i>qPemilihan Bittorrent</i></b>: -s atau -select
<code>/cmd</code> link -s atau dengan membalas file/link

➲ <b><i>qBittorrent / Aria2 Seed</i></b>: -d atau -seed
<code>/cmd</code> link -d ratio:seed_time atau dengan membalas file/link
Untuk menentukan rasio dan waktu seed tambahkan -d ratio:time. Misalnya: -d 0.7:10 (rasio dan waktu) atau -d 0.7 (hanya rasio) atau -d :10 (hanya waktu) di mana waktu dalam menit.

➲ <b><i>Multi tautan hanya dengan membalas tautan/file pertama</i></b>: -i
<code>/cmd</code> -i 10(jumlah tautan/file)

➲ <b><i>Multi tautan dalam direktori unggah yang sama hanya dengan membalas tautan/file pertama</i></b>: -m atau -sd atau -samedir
<code>/cmd</code> -i 10(jumlah tautan/file) -m nama folder (multi pesan)
<code>/cmd</code> -b -m nama folder (pesan massal/file)

➲ <b><i>Unggah Drive Kustom:</i></b> -id & -indeks(Opsional)
<code>/{cmd}</code> -id <code>drive_folder_link</code> atau <code>drive_id</code> -indeks <code>https://example.com/0:</code>
Di sini, drive_id harus berupa folder id atau tautan folder dan indeks harus berupa url, jika tidak, maka tidak akan diterima.

➲ <b><i>Pilih Kategori Kustom:</i></b> -c atau -category
<code>/{cmd}</code> -c <code>category_name</code>
Ini berfungsi untuk Kategori Bot maupun UserTD (jika diaktifkan)
Anda juga dapat memilih Unggah Drive dari Tombol jika memiliki lebih dari 1 dan argumen ini tidak ditentukan

➲ <b><i>Pilih Dump Kustom:</i></b> -ud atau -dump
<code>/{cmd}</code> -ud <code>dump_name</code> atau <code>@username</code> atau <code>-100xxxxxx chat_id</code> atau semua
Anda juga dapat memilih Dump Chat dari Tombol jika memiliki lebih dari 1 dan argumen ini tidak ditentukan
Anda -ud semua untuk Mengunggah di semua Dump Chat milik Anda
Pastikan Bot sudah menjadi Admin, jika tidak, maka tidak akan diterima.

➲ <b><i>Unggahan Kustom</i></b>: -up atau -upload
<code>/cmd</code> link -up <code>rcl</code> (Untuk memilih konfigurasi rclone, remote, dan jalur)
<code>/cmd</code> link -up <code>ddl</code>
Anda dapat langsung menambahkan jalur unggah: -up remote:dir/subdir

Jika DEFAULT_UPLOAD adalah `rc` maka Anda dapat meneruskan: `gd` untuk mengunggah menggunakan alat gdrive ke GDRIVE_ID.
Jika DEFAULT_UPLOAD adalah `gd` maka Anda dapat meneruskan: `rc` untuk mengunggah ke RCLONE_PATH.
Jika DEFAULT_UPLOAD adalah `ddl` maka Anda dapat meneruskan: `rc` atau `gd` untuk mengunggah ke RCLONE_PATH atau GDRIVE_ID
Jika Anda ingin menambahkan jalur secara manual dari konfigurasi Anda (diunggah dari pengaturan), tambahkan <code>mrcc:</code> sebelum jalur tanpa spasi
<code>/cmd</code> link -up <code>mrcc:</code>main:dump

➲ <b><i>Bendera RClone</i></b>: -rcf
<code>/cmd</code> link|path|rcl -up path|rcl -rcf --buffer-size:8M|--drive-starred-only|key|key:value
Ini akan mengganti semua bendera lain kecuali --exclude
Centang di sini semua <a href='https://rclone.org/flags/'>RcloneFlags</a>.

➲ <b><i>Unduhan Massal</i></b>: -b atau -bulk
Bulk dapat digunakan melalui pesan teks dan dengan membalas file teks yang berisi tautan yang dipisahkan oleh baris baru.
Anda dapat menggunakannya hanya dengan membalas pesan (teks/file).
Semua opsi harus disertai tautan!
<b>Beberapa Contoh:</b>
link1 -n new name -up remote1:path1 -rcf |key:value|key:value
link2 -z -n new name -up remote2:path2
link3 -uz -n new name -up remote2:path2
<b>CATATAN:</b> Anda tidak dapat menambahkan argumen -m hanya untuk beberapa tautan, lakukan untuk semua tautan atau gunakan multi tanpa bulk!
Balas contoh ini dengan cmd <code>/cmd</code> ini -b(bulk)
Anda dapat mengatur awal dan akhir tautan dari bulk seperti seed, dengan -b start:end atau hanya diakhiri dengan -b :end atau hanya dimulai dengan -b start. Awal default adalah dari nol (tautan pertama) hingga inf.
➲ <b><i>Gabungkan File yang Dipisah</i></b>: -j atau -join
Opsi ini hanya akan berfungsi sebelum mengekstrak dan zip, jadi biasanya akan digunakan dengan argumen -m (samedir)
Opsi ini bukan Penggabungan Dua tautan/file. <b>Dengan Balasan:</b>
<code>/cmd</code> -i 3 -j -m nama folder
<code>/cmd</code> -b -j -m nama folder
Jika Anda memiliki tautan yang telah membagi file:
<code>/cmd</code> tautan -j

➲ <b><i>Unduhan RClone</i></b>:
Perlakukan jalur rclone persis seperti tautan
<code>/cmd</code> main:dump/ubuntu.iso atau <code>rcl</code>(Untuk memilih konfigurasi, jarak jauh, dan jalur)
Pengguna dapat menambahkan rclone mereka sendiri dari pengaturan pengguna

Jika Anda ingin menambahkan jalur secara manual dari konfigurasi Anda, tambahkan <code>mrcc:</code> sebelum jalur tanpa spasi
<code>/cmd</code> <code>mrcc:</code>main:dump/ubuntu.iso

➲ <b><i>Tautan TG</i></b>:
Perlakukan tautan tg seperti tautan langsung apa pun
Beberapa tautan memerlukan akses pengguna, jadi pastikan Anda menambahkan USER_SESSION_STRING untuknya.

<b><u>Jenis tautan:</u></b>
• <b>Publik:</b> <code>https://t.me/channel_name/message_id</code>
• <b>Pribadi:</b> <code>tg://openmessage?user_id=xxxxxx&message_id=xxxxx</code>
• <b>Super:</b> <code>https://t.me/c/channel_id/message_id</code>

➲ <b>CATATAN:</b>
1. Perintah yang dimulai dengan <b>qb</b> HANYA untuk torrent.

""]

RSS_HELP_MESSAGE = """
➲ <b>Format to adding feed url(s):</b>
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
4. Take look on title if it has static special character after or before the qualities or extensions or whatever and use them in filter to avoid wrong match.

<b>Timeout:</b> 60 sec.
"""

CLONE_HELP_MESSAGE = ["""<i>Send Gdrive | Gdtot | Filepress | Filebee | Appdrive | Gdflix link or RClone path along with or by replying to the link/rc_path by command with args.</i>

➲ <b><u>Available Args</u></b>:

1. <b>-up or -upload :</b> Upload to your Drive or RClone or DDL
2. <b>-i :</b> Download multi links by reply
3. <b>-rcf :</b> RClone additional Flags
4. <b>-id :</b> GDrive Folder id or link
5. <b>-index:</b> Index url for gdrive_arg
6. <b>-c or -category :</b> Gdrive category to Upload, Specific Name (case insensitive)""",
"""➲ <b><i>Links:</i></b>
Gdrive | Gdtot | Filepress | Filebee | Appdrive | Gdflix link or rclone path

➲ <b><i>Multi Links (only by replying to first gdlink or rclone_path):</i></b>
<code>/cmd</code> -i 10(number of links/paths)

➲ <b><i>Gdrive Link:</i></b>
<code>/cmd</code> gdrive_link

➲ <b><i>RClone Path with RC Flags:</i></b> -rcf
<code>/cmd</code> (rcl or rclone_path) -up (rcl or rclone_path) -rcf flagkey:flagvalue|flagkey|flagkey:flagvalue

➲ <b><i>Upload Custom Drive:</i></b> -id & -index(Optional)
<code>/{cmd}</code> -id <code>drive_folder_link</code> or <code>drive_id</code> -index <code>https://example.com/0:</code>

➲ <b><i>Custom Category Select:</i></b> -c or -category
<code>/{cmd}</code> -c <code>category_name</code>

<b>NOTES:</b>
1. If -up or -upload not specified then rclone destination will be the RCLONE_PATH from <code>config.env</code>.
2. If UserTD enabled, then only it will upload to UserTD either by direct arg or category buttons.
3. For Multi Custom Upload always use Arg in respective msgs and then reply with /cmd -i 10(number)
"""]

CATEGORY_HELP_MESSAGE = """Reply to an active /{cmd} which was used to start the download or add gid along with {cmd}
This command mainly for change category incase you decided to change category from already added download.
But you can always use -c or -category with to select category before download start.

➲ <b><i>Upload Custom Drive</i></b>
<code>/{cmd}</code> -id <code>drive_folder_link</code> or <code>drive_id</code> -index <code>https://example.com/0:</code> gid or by replying to active download

<b>NOTE:</b> drive_id must be folder id or folder link and index must be url else it will not accept.
"""

help_string = [f'''⌬ <b><i>Basic Commands!</i></b>

<b>Use Mirror commands to download your link/file/rcl</b>
┠ /{BotCommands.MirrorCommand[0]} or /{BotCommands.MirrorCommand[1]}: Download via file/url/media to Upload to Cloud Drive.
┖ /{BotCommands.CategorySelect}: Select Custom category to Upload to Cloud Drive from UserTds or Bot Categories.

<b>Use qBit commands for torrents only:</b>
┠ /{BotCommands.QbMirrorCommand[0]} or /{BotCommands.QbMirrorCommand[1]}: Download using qBittorrent and Upload to Cloud Drive.
┖ /{BotCommands.BtSelectCommand}: Select files from torrents by btsel_gid or reply.

<b>Use yt-dlp commands for YouTube or any supported sites:</b>
┖ /{BotCommands.YtdlCommand[0]} or /{BotCommands.YtdlCommand[1]}: Mirror yt-dlp supported link.

<b>Use Leech commands for upload to Telegram:</b>
┠ /{BotCommands.LeechCommand[0]} or /{BotCommands.LeechCommand[1]}: Upload to Telegram.
┠ /{BotCommands.QbLeechCommand[0]} or /{BotCommands.QbLeechCommand[1]}: Download using qBittorrent and upload to Telegram(For torrents only).
┖ /{BotCommands.YtdlLeechCommand[0]} or /{BotCommands.YtdlLeechCommand[1]}: Download using Yt-Dlp(supported link) and upload to telegram.

<b>G-Drive commands:</b>
┠ /{BotCommands.CloneCommand[0]}: Copy file/folder to Cloud Drive.
┠ /{BotCommands.CountCommand} [drive_url]: Count file/folder of Google Drive.
┖ /{BotCommands.DeleteCommand} [drive_url]: Delete file/folder from Google Drive (Only Owner & Sudo).

<b>Cancel Tasks:</b>
┖ /{BotCommands.CancelMirror}: Cancel task by cancel_gid or reply.''',

f'''⌬ <b><i>Users Commands!</i></b>

<b>Bot Settings:</b>
┖ /{BotCommands.UserSetCommand[0]} or /{BotCommands.UserSetCommand[1]} [query]: Open User Settings (PM also)

<b>Authentication:</b>
┖ /login: Login to Bot to Access Bot without Temp Pass System (Private)

<b>Bot Stats:</b>
┠ /{BotCommands.StatusCommand[0]} or /{BotCommands.StatusCommand[1]}: Shows a status page of all active tasks.
┠ /{BotCommands.StatsCommand[0]} or /{BotCommands.StatsCommand[1]}: Show Server detailed stats.
┖ /{BotCommands.PingCommand[0]} or /{BotCommands.PingCommand[1]}: Check how long it takes to Ping the Bot.

<b>RSS Feed:</b>
┖ /{BotCommands.RssCommand}: Open RSS Menu (Sub/Unsub/Start/Pause)''',

f'''⌬ <b><i>Owner or Sudos Commands!</i></b>

<b>Bot Settings:</b>
┠ /{BotCommands.BotSetCommand[0]} or /{BotCommands.BotSetCommand[1]} [query]: Open Bot Settings (Only Owner & Sudo).
┖ /{BotCommands.UsersCommand}: Show User Stats Info (Only Owner & Sudo).

<b>Authentication:</b>
┠ /{BotCommands.AuthorizeCommand[0]} or /{BotCommands.AuthorizeCommand[1]}: Authorize a chat or a user to use the bot (Only Owner & Sudo).
┠ /{BotCommands.UnAuthorizeCommand[0]} or /{BotCommands.UnAuthorizeCommand[1]}: Unauthorize a chat or a user to use the bot (Only Owner & Sudo).
┠ /{BotCommands.AddSudoCommand}: Add sudo user (Only Owner).
┠ /{BotCommands.RmSudoCommand}: Remove sudo users (Only Owner).
┠ /{BotCommands.AddBlackListCommand[0]} or /{BotCommands.AddBlackListCommand[1]}: Add User in BlackListed, so that user can't use the Bot anymore.
┖ /{BotCommands.RmBlackListCommand[0]} or /{BotCommands.RmBlackListCommand[1]}: Remove a BlackListed User, so that user can again use the Bot.

<b>Bot Stats:</b>
┖ /{BotCommands.BroadcastCommand[0]} or /{BotCommands.BroadcastCommand[1]} [reply_msg]: Broadcast to PM users who have started the bot anytime.

<b>G-Drive commands:</b>
┖ /{BotCommands.GDCleanCommand[0]} or /{BotCommands.GDCleanCommand[1]} [drive_id]: Delete all files from specific folder in Google Drive.

<b>Cancel Tasks:</b>
┖ /{BotCommands.CancelAllCommand[0]}: Cancel all Tasks & /{BotCommands.CancelAllCommand[1]} for Multiple Bots.

<b>Maintainance:</b>
┠ /{BotCommands.RestartCommand[0]} or /{BotCommands.RestartCommand[1]}: Restart and Update the Bot (Only Owner & Sudo).
┠ /{BotCommands.RestartCommand[2]}: Restart and Update all Bots (Only Owner & Sudo).
┖ /{BotCommands.LogCommand}: Get a log file of the bot. Handy for getting crash reports (Only Owner & Sudo).

<b>Executors:</b>
┠ /{BotCommands.ShellCommand}: Run shell commands (Only Owner).
┠ /{BotCommands.EvalCommand}: Run Python Code Line | Lines (Only Owner).
┠ /{BotCommands.ExecCommand}: Run Commands In Exec (Only Owner).
┠ /{BotCommands.ClearLocalsCommand}: Clear {BotCommands.EvalCommand} or {BotCommands.ExecCommand} locals (Only Owner).
┖ /exportsession: Generate User StringSession of Same Pyro Version (Only Owner).

<b>RSS Feed:</b>
┖ /{BotCommands.RssCommand}: Open RSS Menu (Sub/Unsub/Start/Pause)

<b>Extras:</b>
┠ /{BotCommands.AddImageCommand} [url/photo]: Add Images in Bot
┖ /{BotCommands.ImagesCommand}: Generate grid of Stored Images.''',

f'''⌬ <b><i>Miscellaneous Commands!</i></b>

<b>Extras:</b>
┠ /{BotCommands.SpeedCommand[0]} or /{BotCommands.SpeedCommand[1]}: Check Speed in VPS/Server.
┖ /{BotCommands.MediaInfoCommand[0]} or /{BotCommands.MediaInfoCommand[1]} [url/media]: Generate MediaInfo of Media or DL Urls

<b>Torrent/Drive Search:</b>
┠ /{BotCommands.ListCommand} [query]: Search in Google Drive(s).
┖ /{BotCommands.SearchCommand} [query]: Search for torrents with API.

<b>Movie/TV Shows/Drama Search:</b>
┠ /{BotCommands.IMDBCommand}: Search in IMDB.
┠ /{BotCommands.AniListCommand}: Search for anime in AniList.
┠ /{BotCommands.AnimeHelpCommand}: Anime help guide.
┖ /{BotCommands.MyDramaListCommand}: Search in MyDramaList.
''']


PASSWORD_ERROR_MESSAGE = """
<b>This link requires a password!</b>
- Insert sign <b>::</b> after the link and write the password after the sign.
<b>Example:</b> {}::love you
Note: No spaces between the signs <b>::</b>
For the password, you can use a space!
"""

default_desp = {'AS_DOCUMENT': 'Default type of Telegram file upload. Default is False mean as media.',
                'ANIME_TEMPLATE': 'Set template for AniList Template. HTML Tags supported',
                'AUTHORIZED_CHATS': 'Fill user_id and chat_id of groups/users you want to authorize. Separate them by space.',
                'AUTO_DELETE_MESSAGE_DURATION': "Interval of time (in seconds), after which the bot deletes it's message and command message which is expected to be viewed instantly.\n\n <b>NOTE:</b> Set to -1 to disable auto message deletion.",
                'BASE_URL': 'Valid BASE URL where the bot is deployed to use torrent web files selection. Format of URL should be http://myip, where myip is the IP/Domain(public) of your bot or if you have chosen port other than 80 so write it in this format http://myip:port (http and not https). Str',
                'BASE_URL_PORT': 'Which is the BASE_URL Port. Default is 80. Int',
                'BLACKLIST_USERS': 'Restrict User from Using the Bot. It will Display a BlackListed Msg. USER_ID separated by space. Str',
                'BOT_MAX_TASKS': 'Maximum number of Task Bot will Run parallel. (Queue Tasks Included). Int',
                'STORAGE_THRESHOLD': 'To leave specific storage free and any download will lead to leave free storage less than this value will be cancelled the default unit is GB. Int',
                'LEECH_LIMIT':  'To limit the Torrent/Direct/ytdlp leech size. the default unit is GB. Int',
                'CLONE_LIMIT': 'To limit the size of Google Drive folder/file which you can clone. the default unit is GB. Int',
                'MEGA_LIMIT': 'To limit the size of Mega download. the default unit is GB. Int',
                'TORRENT_LIMIT': 'To limit the size of torrent download. the default unit is GB. Int',
                'DIRECT_LIMIT': 'To limit the size of direct link download. the default unit is GB. Int',
                'YTDLP_LIMIT': 'To limit the size of ytdlp download. the default unit is GB. Int',
                'PLAYLIST_LIMIT': 'To limit Maximum Playlist Number. Int',
                'IMAGES': 'Add multiple telgraph(graph.org) image links that are seperated by spaces.',
                'IMG_SEARCH': 'Put Keyword to Download Images. Sperarte each name by , like anime, iron man, god of war',
                'IMG_PAGE': 'Set the page value for downloading a image. Each page have approx 70 images. Deafult is 1. Int',
                'IMDB_TEMPLATE': 'Set Bot Default IMDB Template. HTML Tags, Emojis supported. str',
                'AUTHOR_NAME': 'Author name for Telegraph pages, Shown in Telegraph Page as by AUTHOR_NAME',
                'AUTHOR_URL': 'Author URL for Telegraph page, Put Channel URL to Show Join Channel. Str',
                'COVER_IMAGE': 'Cover Image for Telegraph Page. Put Telegraph Photo Link',
                'TITLE_NAME': 'Title name for Telegraph pages (while using /list command)',
                'GD_INFO': 'Description of file uploaded to gdrive using bot',
                'DELETE_LINKS': 'Delete TgLink/Magnet/File on Start of Task to Auto Clean Group. Default is False',
                'EXCEP_CHATS': 'Exception Chats which will not use Logging, chat_id separated by space. Str',
                'SAFE_MODE': 'Hide Task Name, Source Link and Indexing of Leech Link for Safety Precautions. Default is False',
                'SOURCE_LINK': 'Add a Extra Button of Source Link whether it is Magnet Link or File Link or DL Link. Default is False',
                'SHOW_EXTRA_CMDS': 'Add Extra Commands beside Arg Format for -z or -e. \n\n<b>COMMANDS: </b> /unzipxxx or /zipxxx or /uzx or /zx',
                'BOT_THEME': 'Theme of the Bot to Switch. For now Deafault Theme Availabe is minimal. You can make your own Theme and Add in BSet. \n\n<b>Sample Format</b>: https://t.ly/9rVXq',
                'USER_MAX_TASKS': 'Limit the Maximum task for users of group at a time. use the Int',
                'DAILY_TASK_LIMIT': 'Maximum task a user can do in one day. use the Int',
                'DISABLE_DRIVE_LINK': 'Disable drive link button. Default is False. Bool',
                'DAILY_MIRROR_LIMIT': 'Total size upto which user can Mirror in one day. the default unit is GB. Int',
                'GDRIVE_LIMIT': 'To limit the size of Google Drive folder/file link for leech, Zip, Unzip. the default unit is GB. Int',
                'DAILY_LEECH_LIMIT': 'Total size upto which user can Leech in one day. the default unit is GB. Int',
                'USER_TASKS_LIMIT': 'The maximum limit on every users for all tasks. Int',
                'FSUB_IDS': 'Fill chat_id(-100xxxxxx) of groups/channel you want to force subscribe. Separate them by space. Int\n\nNote: Bot should be added in the filled chat_id as admin',
                'BOT_PM': 'File/links send to the BOT PM also. Default is False',
                'BOT_TOKEN': 'The Telegram Bot Token that you got from @BotFather',
                'CMD_SUFFIX': 'Telegram Bot Command Index number or Custom Text. This will added at the end all commands except Global Commands. Str',
                'DATABASE_URL': "Your Mongo Database URL (Connection string). Follow this Generate Database to generate database. Data will be saved in Database: auth and sudo users, users settings including thumbnails for each user, rss data and incomplete tasks.\n\n <b>NOTE:</b> You can always edit all settings that saved in database from the official site -> (Browse collections)",
                'DEFAULT_UPLOAD': 'Whether rc to upload to RCLONE_PATH or gd to upload to GDRIVE_ID or ddl to upload to DDLserver. Default is gd.',
                'DOWNLOAD_DIR': 'The path to the local folder where the downloads should be downloaded to. ',
                'MDL_TEMPLATE': 'Set Bot Custom Default MyDramaList Template. HTML Tags, Emojis Supported',
                'CLEAN_LOG_MSG': 'Clean Leech Log & Bot PM Task Start Message. Default is False',
                'LEECH_LOG_ID': "Chat ID to where leeched files would be uploaded. Int. NOTE: Only available for superGroup/channel. Add -100 before channel/superGroup id. In short don't add bot id or your id!",
                'MIRROR_LOG_ID': "Chat ID to where Mirror files would be Send. Int. NOTE: Only available for superGroup/channel. Add -100 before channel/superGroup id. In short don't add bot id or your id!. For Multiple id Separate them by space.",
                'EQUAL_SPLITS': 'Split files larger than LEECH_SPLIT_SIZE into equal parts size (Not working with zip cmd). Default is False.',
                'EXTENSION_FILTER': "File extensions that won't upload/clone. Separate them by space.",
                'GDRIVE_ID': 'This is the Folder/TeamDrive ID of the Google Drive OR root to which you want to upload all the mirrors using google-api-python-client.',
                'INCOMPLETE_TASK_NOTIFIER': 'Get incomplete task messages after restart. Require database and superGroup. Default is False',
                'INDEX_URL': 'Refer to https://gitlab.com/ParveenBhadooOfficial/Google-Drive-Index.',
                'IS_TEAM_DRIVE': 'Set True if uploading to TeamDrive using google-api-python-client. Default is False',
                'SHOW_MEDIAINFO': 'Add Button to Show MediaInfo in Leeched file. Bool',
                'SCREENSHOTS_MODE': 'Enable or Diable generating Screenshots via -ss arg. Default is False. Bool',
                'CAP_FONT': 'Add Custom Caption Font to Leeched Files, Available Values : b, i, u, s, code, spoiler. Reset Var to use Regular ( No Format )',
                'LEECH_FILENAME_PREFIX': 'Add custom word prefix to leeched file name. Str',
                'LEECH_FILENAME_SUFFIX': 'Add custom word suffix to leeched file name. Str',
                'LEECH_FILENAME_CAPTION': 'Add custom word caption to leeched file/vedios. Str',
                'LEECH_FILENAME_REMNAME': 'Remove custom word from the leeched file name. Str',
                'LOGIN_PASS': 'Permanent pass for user to skip the token system',
                'TOKEN_TIMEOUT': 'Token timeout for each group member in sec. Int',
                'DEBRID_LINK_API': 'Set debrid-link.com API for 172 Supported Hosters Leeching Support. Str',
                'REAL_DEBRID_API': 'Set real-debrid.com API for Torrent Cache & Few Supported Hosters (VPN Maybe). Str',
                'LEECH_SPLIT_SIZE': 'Size of split in bytes. Default is 2GB. Default is 4GB if your account is premium.',
                'MEDIA_GROUP': 'View Uploaded splitted file parts in media group. Default is False.',
                'MEGA_EMAIL': 'E-Mail used to sign-in on mega.nz for using premium account. Str',
                'MEGA_PASSWORD': 'Password for mega.nz account. Str',
                'OWNER_ID': 'The Telegram User ID (not username) of the Owner of the bot.',
                'QUEUE_ALL': 'Number of parallel tasks of downloads and uploads. For example if 20 task added and QUEUE_ALL is 8, then the summation of uploading and downloading tasks are 8 and the rest in queue. Int. NOTE: if you want to fill QUEUE_DOWNLOAD or QUEUE_UPLOAD, then QUEUE_ALL value must be greater than or equal to the greatest one and less than or equal to summation of QUEUE_UPLOAD and QUEUE_DOWNLOAD',
                'QUEUE_DOWNLOAD': 'Number of all parallel downloading tasks. Int',
                'QUEUE_UPLOAD': 'Number of all parallel uploading tasks. Int',
                'RCLONE_FLAGS': 'key:value|key|key|key:value . Check here all RcloneFlags.',
                'RCLONE_PATH': "Default rclone path to which you want to upload all the mirrors using rclone.",
                'RCLONE_SERVE_URL': 'Valid URL where the bot is deployed to use rclone serve. Format of URL should be http://myip, where myip is the IP/Domain(public) of your bot or if you have chosen port other than 80 so write it in this format http://myip:port (http and not https)',
                'RCLONE_SERVE_USER': 'Username for rclone serve authentication.',
                'RCLONE_SERVE_PASS': 'Password for rclone serve authentication.',
                'RCLONE_SERVE_PORT': 'Which is the RCLONE_SERVE_URL Port. Default is 8080.',
                'RSS_CHAT_ID': 'Chat ID where rss links will be sent. If you want message to be sent to the channel then add channel id. Add -100 before channel id. Int',
                'RSS_DELAY': 'Time in seconds for rss refresh interval. Recommended 900 second at least. Default is 900 in sec. Int',
                'SEARCH_API_LINK': 'Search api app link. Get your api from deploying this repository. Supported Sites: 1337x, Piratebay, Nyaasi, Torlock, Torrent Galaxy, Zooqle, Kickass, Bitsearch, MagnetDL, Libgen, YTS, Limetorrent, TorrentFunk, Glodls, TorrentProject and YourBittorrent',
                'SEARCH_LIMIT': 'Search limit for search api, limit for each site and not overall result limit. Default is zero (Default api limit for each site).',
                'SEARCH_PLUGINS': 'List of qBittorrent search plugins (github raw links). I have added some plugins, you can remove/add plugins as you want.',
                'STATUS_LIMIT': 'Limit the no. of tasks shown in status message with buttons. Default is 10. NOTE: Recommended limit is 4 tasks.',
                'STATUS_UPDATE_INTERVAL': 'Time in seconds after which the progress/status message will be updated. Recommended 10 seconds at least.',
                'STOP_DUPLICATE': "Bot will check file/folder name in Drive incase uploading to GDRIVE_ID. If it's present in Drive then downloading or cloning will be stopped. (NOTE: Item will be checked using name and not hash, so this feature is not perfect yet). Default is False",
                'SUDO_USERS': 'Fill user_id of users whom you want to give sudo permission. Separate them by space. Int',
                'TELEGRAM_API': 'This is to authenticate your Telegram account for downloading Telegram files. You can get this from https://my.telegram.org.',
                'TELEGRAM_HASH': 'This is to authenticate your Telegram account for downloading Telegram files. You can get this from https://my.telegram.org.',
                'TIMEZONE': 'Set your Preferred Time Zone for Restart Message. Get yours at <a href="http://www.timezoneconverter.com/cgi-bin/findzone.tzc">Here</a> Str',
                'TORRENT_TIMEOUT': 'Timeout of dead torrents downloading with qBittorrent and Aria2c in seconds. Int',
                'UPSTREAM_REPO': "Your github repository link, if your repo is private add https://username:{githubtoken}@github.com/{username}/{reponame} format. Get token from Github settings. So you can update your bot from filled repository on each restart.",
                'UPSTREAM_BRANCH': 'Upstream branch for update. Default is master.',
                'UPGRADE_PACKAGES': 'Install New Requirements File without thinking of Crash. Bool',
                'SAVE_MSG': 'Add button of save message. Bool',
                'SET_COMMANDS': 'Set bot command automatically. Bool',
                'JIODRIVE_TOKEN': 'Set token for the jiodrive.xyz to download the files. str',
                'USER_TD_MODE': 'Enable User GDrive TD to Use. Default is False',
                'USER_TD_SA': 'Add Global SA mail for User to give Permissions to Bot for UserTD Upload. Like wzmlx@googlegroups.com. Str',
                'USER_SESSION_STRING': "To download/upload from your telegram account and to send rss. To generate session string use this command <code>python3 generate_string_session.py</code> after mounting repo folder for sure.\n\n<b>NOTE:</b> You can't use bot with private message. Use it with superGroup.",
                'USE_SERVICE_ACCOUNTS': 'Whether to use Service Accounts or not, with google-api-python-client. For this to work see Using Service Accounts section below. Default is False',
                'WEB_PINCODE': ' Whether to ask for pincode before selecting files from torrent in web or not. Default is False. Bool.',
                'YT_DLP_OPTIONS': 'Default yt-dlp options. Check all possible options HERE or use this script to convert cli arguments to api options. Format: key:value|key:value|key:value. Add ^ before integer or float, some numbers must be numeric and some string. \nExample: "format:bv*+mergeall[vcodec=none]|nocheckcertificate:True"'
                }

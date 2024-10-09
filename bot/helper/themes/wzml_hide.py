#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = 'Original Repo'
    ST_BN1_URL = 'https://ouo.io/Sjev3s'
    ST_BN2_NAME = 'Repo This bot'
    ST_BN2_URL = 'https://ouo.io/r87GFB'
    ST_MSG = '''Dapat mengunggah file, tautan, torrents, dll. Untuk Telegram, Google Drive, server DDL dan situs yang didukung RCLone!\n\n'''
    ST_BOTPM = '''<b>🕵️ Bot PM berhasil dimulai! \n\nℹ️ Saya akan mengirim semua file dan tautan Anda di sini</b>.'''
    ST_UNAUTH = '''<b>⚠️ Akses ditolak!</b>'''
    LOG_DISPLAY_BT = '📑 Lihat Log'
    WEB_PASTE_BT = '📨 Wᴇʙ Pᴀsᴛᴇ (SB)'
    # ---------------------

    # async def stats(client, message):
    BOT_STATS = '''<b>🤖 <u>𝘽𝙤𝙩 𝙎𝙩𝙖𝙩𝙞𝙨𝙩𝙞𝙘𝙨</u></b>
    
<b>⏰ Bot Uptime :</b> {bot_uptime}

<b>💽 RAM</b>
➢{ram_bar} » ({ram}%)
➢<b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

<b>👒 SWAP</b>
➢{swap_bar} » ({swap}%)
➢<b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

<b>📦 DISK</b>
➢{disk_bar} » ({disk}%)
➢<b>Total Disk Read :</b> {disk_read}
➢<b>Total Disk Write :</b> {disk_write}
➢<b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}


    
    '''
    SYS_STATS = '''<b>🛠 <u>𝙎𝙮𝙨𝙩𝙚𝙢 𝙎𝙩𝙖𝙩𝙞𝙨𝙩𝙞𝙘𝙨</u></b>
    
<b>⏰ OS Uptime :</b> {os_uptime}
<b>☢️ OS Info :</b> {os_version}
➢<b>🔧 OS Arch :</b> {os_arch}

<b>🖥️ CPU</b>
➢{cpu_bar} » ({cpu}%)
➢<b>Frequency :</b> {cpu_freq}
➢<b>Average Load :</b> {sys_load}
➢<b>P-Cores :</b> {p_core} | <b>V-Cores :</b> {v_core}
➢<b>Total Cores :</b> {total_core}
➢<b>Usable CPUs :</b> {cpu_use}

<b>📶 Network Stats</b>
➢<b>Upload Data:</b> {up_data}
➢<b>Download Data:</b> {dl_data}
➢<b>Pkts Sent:</b> {pkt_sent}k
➢<b>Pkts Received:</b> {pkt_recv}k
➢<b>Total I/O Data:</b> {tl_data}


    '''
    REPO_STATS = '''<b>🧑‍💻 <u>𝙍𝙚𝙥𝙤 𝙎𝙩𝙖𝙩𝙞𝙨𝙩𝙞𝙘𝙨</u></b>
    
<b>♻️ Bot Terupdate :</b> {last_commit}
<b>🆔 Versi Saat ini :</b> {bot_version}
<b>🎈 Versi Terbaru :</b> {lat_version}
<b>📝 Log Perubahan :</b> {commit_details}

<b>💥 REMARKS :</b> <code>{remarks}</code>


    '''
    BOT_LIMITS = '''<b>❗<u>𝘽𝙤𝙩 𝙇𝙞𝙢𝙞𝙩𝙨</u></b>
    
<b>🎯 Direct :</b> <code>{DL} GB</code>
<b>🧲 Torrent :</b> <code>{TL} GB</code>
<b>☁️ GDrive :</b> <code>{GL} GB</code>
<b>📺 YT-DLP :</b> <code>{YL} GB</code>
<b>🎥 Playlist :</b> <code>{PL} Videos</code>
<b>Ⓜ️ Mega :</b> <code>{ML} GB</code>
<b>🎗️ Clone :</b> <code>{CL} GB</code>
<b>📂 Leech :</b> <code>{LL} GB</code>

<b>🔑 Token Validity :</b> {TV}
<b>🐢 Timeout :</b> {UTI}
<b>👤 User Tasks :</b> {UT}
<b>🚧 Total Tasks :</b> {BT}


    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>🔄 Menyalakan Ulang...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''<b>♻️ Bot berhasil di nyalakan! 🎉</b>

<b>📅 Tanggal:</b> {date}
<b>⏰ Waktu:</b> {time}
<b>🌍 ZonaWaktu:</b> {timz}
<b>🆔 Versi:</b> {version}

'''
    RESTARTED = '''<b>🔄 Bot Merestart otomatis!</b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<b>🙄 Starting Ping...</b>'
    PING_VALUE = '<b>🏓 Pong:</b> <code>{value}ms</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b>🚧 Tugas Dimulai</b>

<b>💠 Unggah:</b> {Mode}
<b>👤 Pengguna:</b> {Tag}\n\n"""
    LINKS_SOURCE = """<b>💡 Sumber:</b>
<b>⏰ Waktu:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    L_PM_START =            "🏁 <b><u>Leech Dimulai</u> :</b>\n\n<b>💡 sumber :</b> <a href='{msg_link}'>Klik Disini</a>"
    L_LOG_START =           "🏁 <b><u>Leech Dimulai</u> :</b>\n\n➢<b>👤 Pengguna :</b> {mention}\n➢<b>🆔 ID :</b> <code>{uid}</code>\n➢<b>💡 Sumber :</b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<code>{Name}</code>\n\n'
    SIZE =                  '<b>💾 Ukuran: </b>{Size}\n'
    ELAPSE =                '<b>⌛ Perkiraan: </b>{Time}\n'
    MODE =                  '<b>💠 Unggah: </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '<b>📂 Total Files: </b>{Files}\n'
    L_CORRUPTED_FILES =     '<b>💀 File Rusak: </b>{Corrupt}\n'
    L_CC =                  '<b>👤 Pengguna: </b>{Tag}\n\n'
    PM_BOT_MSG =            'ℹ️ <b><i>File telah dikirim!</i></b>'
    L_BOT_MSG =             'ℹ️ <b><i>File telah dikirim dalam bot PM!</i></b>'
    L_LL_MSG =              'ℹ️ <b><i>File telah dikirim.Akses melalui tautan!</i></b>'
    
    # ----- MIRROR -------
    M_TYPE =                '<b>📜 Jenis File: </b>{Mimetype}\n'
    M_SUBFOLD =             '<b>🗂️ SubFolders: </b>{Folder}\n'
    TOTAL_FILES =           '<b>📂 Files: </b>{Files}\n'
    RCPATH =                '<b>🚩 Path: </b><code>{RCpath}</code>\n'
    M_CC =                  '<b>👤 Pengguna: </b>{Tag}\n\n'
    M_BOT_MSG =             '🏁 <b><i>♻️Tautan telah dikirim dalam DM!!</i></b>\n♻️Segera amankan file anda sebelum dihapus atau ada pembersihan, pembersihan tidak ada konfirmasi ke pemilik file, sepenuhnya hak admin🙏🙏'
    
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Unduh Disini'
    SAVE_MSG =        '📩 Simpan'
    RCLONE_LINK =     '®️ RClone Link'
    DDL_LINK =        '🚀 {Serv} Link'
    SOURCE_URL =      '💡 Sumber'
    INDEX_LINK_F =    '🚀 Index Link'
    INDEX_LINK_D =    '🚀 Index Link'
    VIEW_LINK =       '🌐 Lihat Tautan'
    CHECK_PM =        '🕵️ Lihat di PM bot'
    CHECK_LL =        '📦 View in Dump'
    MEDIAINFO_LINK =  '📜 MediaInfo'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<blockquote><code>{Name}</code></blockquote>\n'

    #####---------PROGRESSIVE STATUS-------
    STATUS =            '\n{Status}'
    BAR =                            '{Bar}'
    PROCESSED =         '\n<b>🔄 Ukuran       :</b> <code>{Processed}</code>'
    
    ETA =                '\n<b>⏳ Perkiraan    :</b> <code>{Eta}</code>'
    SPEED =             '\n<b>📶 Kecepatan :</b> <code>{Speed}</code>'
    ELAPSED =          '\n<b>⏰ Berjalan      :</b> <code>{Elapsed}</code>'
    ENGINE =            '\n<b>⚙️ Mesin          :</b> <code>{Engine}</code>'
    STA_MODE =          '\n<b>💠 Unggah      :</b> {Mode}'
    SEEDERS =           '\n<b>🌱S/L               :</b> <code>{Seeders}</code> | '
    LEECHERS =                                           '<b></b> <code>{Leechers}</code>'

    ####--------SEEDING----------
    SEED_SIZE =      '\n<b>💾 Size:</b> <code>{Size}</code>'
    SEED_SPEED =     '\n<b>📶 Speed:</b> <code>{Speed}</code> | '
    UPLOADED =                                     '<b>Uploaded:</b> <code>{Upload}</code>'
    RATIO =          '\n<b>🌀 Ratio:</b> <code>{Ratio}</code> | '
    TIME =                                         '<b>Time:</b> <code>{Time}</code>'
    SEED_ENGINE =    '\n<b>⚙️ Engine:</b> <code>{Engine}</code>'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n<b>💾 Ukuran       :</b> <code>{Size}</code>'
    NON_ENGINE =     '\n<b>⚙️ Mesin          :</b> <code>{Engine}</code>'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n<b>👤 Pengguna   :</b> <code>Mode Aman👀</code>'
    ID =                                                        ' | <code>{Id}</code>'
    BTSEL =          '\n<b>✂️ Pilih:</b> {Btsel}'
    CANCEL =         '\n\n<b>🚫</b> {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '👑 <b><u>Bot Stats</u></b>\n'
    TASKS =  '➢<b>🚧 Tasks:</b> {Tasks}\n'
    BOT_TASKS = '➢<b>🚧 Tasks:</b> <code>{Tasks}/{Ttask}</code> | <b>👷 Available:</b> <code>{Free}</code>\n'
    Cpu = '➢<b>🖥️ CPU:</b> <code>{cpu}%</code> | '
    FREE =                      '<b>📭 Free:</b> <code>{free}</code>'
    Ram = '\n➢<b>💿 RAM:</b> <code>{ram}%</code> | '
    uptime =                     '<b>⏰ Uptime:</b> <code>{uptime}</code>'
    DL = '\n<b>🔻 DL:</b> <code>{DL}/s</code> | '
    UL =                        '<b>🔺 UL:</b> <code>{UL}/s</code>'

    ###--------BUTTONS-------
    PREVIOUS = '⏪'
    REFRESH = '📑 Halaman : {Page}'
    NEXT = '⏭️'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = '<b>🏷️ Nama:</b> <code>{content}</code>\n<b>⚠️ File/folder ini sudah tersedia di drive!</b>\n\n<b>📑 Daftar Hasilnya:</b>'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>🎲 Counting:</b> <code>{LINK}</code>\n\n<b>⏳ Please Wait...</b>'
    COUNT_NAME = '➢<b>🏷️ Name:</b> <code>{COUNT_NAME}</code>\n'
    COUNT_SIZE = '➢<b>💾 Size: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '➢<b>📜 Type: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '➢<b>🗂️ SubFolders: </b>{COUNT_SUB}\n'
    COUNT_FILE = '➢<b>📂 Files: </b>{COUNT_FILE}\n'
    COUNT_CC =   '➢<b>👤 User: </b>{COUNT_CC}\n\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>🔍 Mencari :</b> <code>{NAME}</code>'
    LIST_FOUND = '<b>ℹ️ Ditemukan {NO} Hasil untuk </b> <code>{NAME}</code>'
    LIST_NOT_FOUND = '<b>☹️ Tidak di temukan </b> <code>{NAME}</code>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<b>💩 Tidak ada tugas yg sedang berjalan</b>
    
👑 <b><u>Bot Stats</u></b>
➢<b>🖥️ CPU:</b> <code>{cpu}%</code> | <b>💿 RAM:</b> <code>{ram}%</code>
➢<b>📭 Free:</b> <code>{free}</code> | <b>⏰ Uptime:</b> <code>{uptime}</code>
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''㊂ <b><u>Pengaturan Pengguna</u></b>
        
➢<b>👤 Nama :</b> {NAME}
➢<b>🔖 NamaPengguna :</b> {USERNAME}
➢<b>🆔 ID :</b> <code>{ID}</code>
➢<b>🔮 DC :</b> <code>{DC}</code>
➢<b>🗣️ Bahasa :</b> <code>{LANG}</code>

'''

    UNIVERSAL = '''㊂ <b><u>Umum</u></b>

➢<b>📺 YT-DLP Options :</b> <code>{YT}</code>
➢<b>🚧 Tugas Harian :</b> <code>{DT}</code> per hari
➢<b>🟢 Terakhir Digunakan :</b> <code>{LAST_USED}</code>
➢<b>📜 MediaInfo :</b> <code>{MEDIAINFO}</code>
➢<b>🕵️ Bot PM :</b> <code>{BOT_PM}</code>
➢<b>📩 Save Mode :</b> <code>{SAVE_MODE}</code>

'''

    MIRROR = '''㊂ <b><u>Mirror/Clone</u></b>

➢<b>☁️ Mirror Harian:</b> <code>{DM}</code> per hari</i>
➢<b>Ⓟ Prefix :</b> <code>{MPREFIX}</code>
➢<b>Ⓢ Suffix :</b> <code>{MSUFFIX}</code>
➢<b>🌈 Remname :</b> <code>{MREMNAME}</code>
➢<b>🧿 DDL Server(s) :</b> <code>{DDL_SERVER}</code>
➢<b>🎀 RClone :</b> <code>{RCLONE}</code>
➢<b>📮 User TD :</b> <code>{TMODE}</code>
➢<b>📝 TD Info:</b> <code>{USERTD}</code>

'''

    LEECH = '''㊂ <b><u>Leech Settings</u></b>

➢<b>📂 Leech Harian  : </b><code>{DL}</code> per hari
➢<b>⚙️ Leech Type :</b> <code>{LTYPE}</code>
➢<b>🖼️ Thumbnail :</b> <code>{THUMB}</code>
➢<b>♈ Split Size :</b> <code>{SPLIT_SIZE}</code>
➢<b>♐ Equal Splits :</b> <code>{EQUAL_SPLIT}</code>
➢<b>♒ Media Group :</b> <code>{MEDIA_GROUP}</code>
➢<b>📄 Caption :</b> <code>{LCAPTION}</code>
➢<b>Ⓟ Prefix :</b> <code>{LPREFIX}</code>
➢<b>Ⓢ Suffix :</b> <code>{LSUFFIX}</code>
➢<b>📦 Dump :</b> <code>{LDUMP}</code>
➢<b>🌈 Remname :</b> <code>{LREMNAME}</code>

'''

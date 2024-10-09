#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = 'Original_Rᴇᴘᴏ'
    ST_BN1_URL = 'https://gitlab.com/Jot4349/WZML-X-ADVANCE'
    ST_BN2_NAME = 'Update'
    ST_BN2_URL = 'https://t.me/NordBotz'
    ST_MSG = '''<blockquote><i>Bot ini dapat melakukan mirror semua tautan, file, dan torrent Anda ke Google Drive atau cloud rclone lainnya, ke Telegram, atau ke server DDL. Ketik {help_command} untuk mendapatkan daftar perintah yang tersedia.</b></blockquote>'''
    ST_BOTPM = '''<i>Sekarang, bot ini akan mengirim semua file dan tautan Anda ke sini. Mulai menggunakan ...</i>'''
    ST_UNAUTH = '''<blockquote><i>Anda bukan pengguna yang diizinkan! Deploy bot WZML-X-ADVANCE Mirror-Leech Anda sendiri.</i></blockquote>'''
    OWN_TOKEN_GENERATE = '''
Token sementara bukan milik Anda! \nSilakan buat sendiri'''
    USED_TOKEN = '''<b>Token sementara sudah di gunakan!</b>\n\n<i>nSilakan buat sendiri'.</i>'''
    LOGGED_PASSWORD = '''<b>Bot sudah berhasil masuk dengan pasword </b>\n\n<i>Sudah tidak memelukan token sementara lagi.</i>'''
    ACTIVATE_BUTTON = 'Aktifkan token sementara'
    TOKEN_MSG = '''<b><u>Memvuat token login sementara!</u></b>
<b>Tᴇᴍᴘ Tᴏᴋᴇɴ:</b> <code>{token}</code>
<b>Vᴀʟɪᴅɪᴛʏ:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ Diaktifkan ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Bot berhasil login!</b>'
    INVALID_PASS = '<b>Pasword salah</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bᴏᴛ Pᴇʀᴍᴀɴᴇɴᴛ Lᴏɢɪɴ Sᴜᴄᴄᴇssғᴜʟʟʏ!</b>'
    LOGIN_USED = '<b>Bᴏᴛ Lᴏɢɪɴ Usᴀɢᴇ :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Lihat Log'
    WEB_PASTE_BT = '📨 Wᴇʙ Pᴀsᴛᴇ (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Dasar'
    USER_BT = 'Pengguna'
    MICS_BT = 'Lainnya'
    O_S_BT = 'Pemilik & Admin'
    CLOSE_BT = 'Tutup'
    HELP_HEADER = "㊂ <b><i>Petunjuk menggunakan menu bantuan!</i></b>\n\n<b>Nᴏᴛᴇ: <i>Klik pada PERINTAH mana pun untuk melihat detail kecil lainnya.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''🌀<b><i>Bot statistik :</i></b>
• <b>Waktu Aktive Bot :</b> {bot_uptime}

• <b><i>RAM ( MEMORY ) :</i></b>
• {ram_bar} {ram}%
• <b>U :</b> {ram_u} • <b>F :</b> {ram_f} • <b>T :</b> {ram_t}

• <b><i>VIRTUAL RAM :</i></b>
• {swap_bar} {swap}%
• <b>U :</b> {swap_u} • <b>F :</b> {swap_f} • <b>T :</b> {swap_t}

• <b><i>HDD :</i></b>
• {disk_bar} {disk}%
• <b>Tᴏᴛᴀʟ Dɪsᴋ Rᴇᴀᴅ :</b> {disk_read}
• <b>Tᴏᴛᴀʟ Dɪsᴋ Wʀɪᴛᴇ :</b> {disk_write}
• <b>U :</b> {disk_u} • <b>F :</b> {disk_f} • <b>T :</b> {disk_t}
    
    '''
    SYS_STATS = '''🌀 <b><i>Os Sʏsᴛᴇᴍ :</i></b>
• <b>Waktu nyala OS :</b> {os_uptime}
• <b>Versi OS :</b> {os_version}
• <b>Os Aʀᴄʜ :</b> {os_arch}

🌀 <b><i>Nᴇᴛᴡᴏʀᴋ Sᴛᴀᴛs :</i></b>
• <b>Uᴘʟᴏᴀᴅ Dᴀᴛᴀ:</b> {up_data}
• <b>Dᴏᴡɴʟᴏᴀᴅ Dᴀᴛᴀ:</b> {dl_data}
• <b>Pᴋᴛs Sᴇɴᴛ:</b> {pkt_sent}k
• <b>Pᴋᴛs Rᴇᴄᴇɪᴠᴇᴅ:</b> {pkt_recv}k
• <b>Tᴏᴛᴀʟ I/O Dᴀᴛᴀ:</b> {tl_data}

• <b>Cᴘᴜ :</b>
• {cpu_bar} {cpu}%
• <b>Cᴘᴜ Fʀᴇǫᴜᴇɴᴄʏ :</b> {cpu_freq}
• <b>Sʏsᴛᴇᴍ Aᴠɢ Lᴏᴀᴅ :</b> {sys_load}
• <b>P-Cᴏʀᴇ(s) :</b> {p_core} • <b>V-Cᴏʀᴇ(s) :</b> {v_core}
• <b>Tᴏᴛᴀʟ Cᴏʀᴇ(s) :</b> {total_core}
• <b>Usᴀʙʟᴇ Cᴘᴜ(s) :</b> {cpu_use}
    '''
    REPO_STATS = '''🌀 <b><i>Repository info :</i></b>
• <b>Bot Updated        :</b> {last_commit}
• <b>Versi Saat inu    :</b> {bot_version}
• <b>Versi Terbaru    :</b> {lat_version}
• <b>Log Perubahan     :</b> {commit_details}

🌀 <b>Rᴇᴍᴀʀᴋs :</b> <code>{remarks}</code>
    '''
    BOT_LIMITS = '''🌀 <b><i>Bot limits :</i></b>
<blockquote expandable>• <b>Dɪʀᴇᴄᴛ Lɪᴍɪᴛ :</b> {DL} Gʙ
• <b>Torent Limit  :</b> {TL} Gʙ
• <b>GDʀɪᴠᴇ Lɪᴍɪᴛ   :</b> {GL} Gʙ
• <b>Yᴛ-Dʟᴘ Lɪᴍɪᴛ   :</b> {YL} Gʙ
• <b>Pʟᴀʏʟɪsᴛ Lɪᴍɪᴛ :</b> {PL}
• <b>Mᴇɢᴀ Lɪᴍɪᴛ     :</b> {ML} Gʙ
• <b>Cʟᴏɴᴇ Lɪᴍɪᴛ    :</b> {CL} Gʙ
• <b>Lᴇᴇᴄʜ Lɪᴍɪᴛ    :</b> {LL} Gʙ

• <b>Tᴏᴋᴇɴ Vᴀʟɪᴅɪᴛʏ         :</b> {TV}
• <b>Usᴇʀ Tɪᴍᴇ Lɪᴍɪᴛ        :</b> {UTI} / Tᴀsᴋ
• <b>Usᴇʀ Pᴀʀᴀʟʟᴇʟ Tᴀsᴋs    :</b> {UT}
• <b>Bᴏᴛ Pᴀʀᴀʟʟᴇʟ Tᴀsᴋs     :</b> {BT}</blockquote>
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>Menyalakan Ulang...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''🌀 <b><i>Bot berhasil di nyalakan</i></b>
• <b>Tanggl         :</b> {date}
• <b>Waktu         :</b> {time}
• <b>ZonaWaktu    :</b> {timz}
• <b>Versi           :</b> {version}'''
    RESTARTED = '''🌀 <b><i>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ!</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Tes ping........</i>'
    PING_VALUE = '<b>Bot aktive✅</b>\n<code>{value} ᴍs..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<blockquote><b><i>Tugas di mulai</i></b>
• <b>Mᴏᴅᴇ:</b> {Mode}
• <b>Bʏ:</b> {Tag}\n\n"""
    LINKS_SOURCE = """➲Sumber <b>:</b>
• <b>Ditambahkan pada :</b> {On}</blockquote>
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
{Source}
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "<blockquote>➲ <b><u>Tᴀsᴋ Sᴛᴀʀᴛᴇᴅ :</u></b>\n\n• <b>Link:</b> <a href='{msg_link}'>Cʟɪᴄᴋ Hᴇʀᴇ</a></blockquote>"
    L_LOG_START =           "<blockquote>➲ <b><u>Lᴇᴇᴄʜ Sᴛᴀʀᴛᴇᴅ :</u></b>\n\n• <b>Usᴇʀ :</b> {mention} ( #ID{uid} )\n• <b>Sᴏᴜʀᴄᴇ :</b> <a href='{msg_link}'>Cʟɪᴄᴋ Hᴇʀᴇ</a></blockquote>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b><i>{Name}</i></b>\n\n'
    SIZE =                  '• <b>Ukuran</b> : {Size}\n'
    ELAPSE =                '• <b>Waktu</b>: {Time}\n'
    MODE =                  '• <b>Mode</b> : {Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '• <b>Total File</b> : {Files} Files\n'
    L_CORRUPTED_FILES =     '• <b>File Rusak</b> : {Corrupt}\n'
    L_CC =                  '• <b>Pengguna</b> : {Tag}\n'
    PM_BOT_MSG =            '➲ <b><i>File(s) sudah dikirim</i></b>'
    L_BOT_MSG =             '➲ <b><i>File dikirim ke PM</i></b>'
    L_LL_MSG =              '➲ <b><i>Untuk menghindari penghapusan files berkala, segera amankan files Anda</i></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '• <b>Type</b>: {Mimetype}\n'
    M_SUBFOLD =             '• <b>Sub Folder</b> : {Folder}\n'
    TOTAL_FILES =           '• <b>Total File</b> : {Files}\n'
    RCPATH =                '• <b>Jalur Penyimpanan</b> : {RCpath}\n'
    M_CC =                  '• <b>Pengguna</b> : {Tag}\n'
    M_BOT_MSG =             '➲ <b><i>Link download di kirim ke PM dan segera download file anda sebelum ada penghapusan berkala</b></blockquote>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Tautan Unduhan'
    SAVE_MSG =        '📨 Simpan Pesan'
    RCLONE_LINK =     '♻️ RCʟᴏɴᴇ Lɪɴᴋ'
    DDL_LINK =        '📎 Tautan {Serv} '
    SOURCE_URL =      '🔐 Sumber Tautan'
    INDEX_LINK_F =    '🗂 Iɴᴅᴇx Lɪɴᴋ'
    INDEX_LINK_D =    '⚡ Iɴᴅᴇx Lɪɴᴋ'
    VIEW_LINK =       '🌐 Lihat Tautan'
    CHECK_PM =        '📥 Lihat di PM bot'
    CHECK_LL =        '🖇 Vɪᴇᴡ ɪɴ Lɪɴᴋs Lᴏɢ'
    MEDIAINFO_LINK =  '📃 MᴇᴅɪᴀIɴғᴏ'
    SCREENSHOTS =     '🖼 SᴄʀᴇᴇɴSʜᴏᴛs'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<blockquote><code>{Name}</code></blockquote>\n'

    #####---------PROGRESSIVE STATUS-------
    STATUS =            '\n• {Status}'
    BAR =                           '{Bar}'
    PROCESSED =         '\n• 💿 : {Processed}'
    SPEED =             '\n• 🚀 : {Speed}'
    
    ETA =               '\n• ⏰ : {Eta}'
    ELAPSED =           '\n• ⏳ : {Elapsed}'
    ENGINE =            '\n• 🚂 : {Engine}'
    STA_MODE =          '\n• ⚒️ : {Mode}'
    SEEDERS =           '\n• 🧲 : {Seeders} • '
    LEECHERS =                                           '👾 : {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n• <b>Sɪᴢᴇ: </b>{Size}'
    SEED_SPEED =     '\n• <b>Sᴘᴇᴇᴅ: </b> {Speed} • '
    UPLOADED =                                     '<b>Uᴘʟᴏᴀᴅᴇᴅ: </b> {Upload}'
    RATIO =          '\n• <b>Rᴀᴛɪᴏ: </b> {Ratio} • '
    TIME =                                         '<b>Tɪᴍᴇ: </b> {Time}'
    SEED_ENGINE =    '\n• <b>Eɴɢɪɴᴇ:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n• <b>Sɪᴢᴇ: </b>{Size}'
    NON_ENGINE =     '\n• <b>Eɴɢɪɴᴇ:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n• 🙎‍♂️ : <code>{User}</code> • '
    ID =                                                        ' (<code>{Id}</code>)'
    BTSEL =          '\n• <b>☑ :</b> {Btsel}'
    CANCEL =         '\n\n⚠️{Cancel} \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n'

    ####------FOOTER--------
    FOOTER = '🌀 <b><i>Bᴏᴛ Sᴛᴀᴛs</i></b>\n'
    TASKS =  '• <b>Tᴀsᴋs:</b> {Tasks}\n'
    BOT_TASKS = '• <b>Tᴀsᴋs:</b> {Tasks}/{Ttask} • <b>Aᴠʟ:</b> {Free}\n'
    Cpu = '• <b>Cᴘᴜ:</b> {cpu}% • '
    FREE =                      '<b>F:</b> {free} [{free_p}%]'
    Ram = '\n• <b>Rᴀᴍ:</b> {ram}% • '
    uptime =                     '<b>UᴘTɪᴍᴇ:</b> {uptime}'
    DL = '\n• <b>🔽 :</b> {DL}/s • '
    UL =                        '<b>🔼 :</b> {UL}/s</blockquote>'

    ###--------BUTTONS-------
    PREVIOUS = '◀️'
    REFRESH = 'Pᴀɢᴇs\n{Page}'
    NEXT = '▶️'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'File sudah tersedia di Google Drive.\nSemua disini {content} Hasil nya: '
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>Cᴏᴜɴᴛɪɴɢ:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\n•\n'
    COUNT_SIZE = '• <b>Sɪᴢᴇ: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '• <b>Tʏᴘᴇ: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '• <b>SᴜʙFᴏʟᴅᴇʀs: </b>{COUNT_SUB}\n'
    COUNT_FILE = '• <b>Fɪʟᴇs: </b>{COUNT_FILE}\n'
    COUNT_CC =   '• <b>Bʏ: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Pencarian untuk  <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Ditemukan {NO} Hasil untuk <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'Tidak di temukan untuk kata kunci <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<i>Tidak ada tugas yg sedang berjalan 😊</i>
    
<blockquote>🌀 <b><i>Bᴏᴛ Sᴛᴀᴛs</i></b>
• <b>Cᴘᴜ:</b> {cpu}% • <b>F:</b> {free} [{free_p}%]
• <b>Rᴀᴍ:</b> {ram} • <b>UᴘTɪᴍᴇ:</b> {uptime}<b/lockquote>
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''㊂ <b><u>Usᴇʀ Sᴇᴛᴛɪɴɢs :</u></b>
        
•<b> Nᴀᴍᴇ : </b>{NAME} ( <code>{ID}</code> )
•<b> Usᴇʀɴᴀᴍᴇ  :</b> {USERNAME}
•<b> Tᴇʟᴇɢʀᴀᴍ DC :</b> {DC}'''

    UNIVERSAL = '''㊂ <b><u>Uɴɪᴠᴇʀsᴀʟ Sᴇᴛᴛɪɴɢs : {NAME}</u></b>

•<b> YT-DLP Oᴘᴛɪᴏɴs :</b> <b><code>{YT}</code></b>
•<b> Dᴀɪʟʏ Tᴀsᴋs :</b> <code>{DT}</code> ᴘᴇʀ ᴅᴀʏ
•<b> Lᴀsᴛ Bᴏᴛ Usᴇᴅ :</b> <code>{LAST_USED}</code>
•<b> Usᴇʀ Sᴇssɪᴏɴ :</b> <code>{USESS}</code>
•<b> MᴇᴅɪᴀIɴғᴏ Mᴏᴅᴇ :</b> <code>{MEDIAINFO}</code>
•<b> Sᴀᴠᴇ Mᴏᴅᴇ :</b> <code>{SAVE_MODE}</code>
•<b> Usᴇʀ Bᴏᴛ PM :</b> <code>{BOT_PM}</code>'''

    MIRROR = '''㊂ <b><u>Mɪʀʀᴏʀ/Cʟᴏɴᴇ Sᴇᴛᴛɪɴɢs : {NAME}</u></b>

•<b> RCʟᴏɴᴇ Cᴏɴғɪɢ :</b> <i>{RCLONE}</i>
•<b> Mɪʀʀᴏʀ Pʀᴇғɪx :</b> <code>{MPREFIX}</code>
•<b> Mɪʀʀᴏʀ Sᴜғғɪx :</b> <code>{MSUFFIX}</code>
•<b> Mɪʀʀᴏʀ Rᴇᴍɴᴀᴍᴇ :</b> <code>{MREMNAME}</code>
•<b> DDL Sᴇʀᴠᴇʀ(s) :</b> <i>{DDL_SERVER}</i>
•<b> Usᴇʀ TD Mᴏᴅᴇ :</b> <i>{TMODE}</i>
•<b> Tᴏᴛᴀʟ Usᴇʀ TD(s) :</b> <i>{USERTD}</i>
•<b> Dᴀɪʟʏ Mɪʀʀᴏʀ :</b> <code>{DM}</code> ᴘᴇʀ ᴅᴀʏ'''

    LEECH = '''㊂ <b><u>Lᴇᴇᴄʜ Sᴇᴛᴛɪɴɢs ғᴏʀ {NAME}</u></b>

•<b> Dᴀɪʟʏ Lᴇᴇᴄʜ :</b> <code>{DL}</code ᴘᴇʀ ᴅᴀʏ
•<b> Lᴇᴇᴄʜ Tʏᴘᴇ :</b> <i>{LTYPE}</i>
•<b> Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ :</b> <i>{THUMB}</i>
•<b> Lᴇᴇᴄʜ Sᴘʟɪᴛ Sɪᴢᴇ :</b> <code>{SPLIT_SIZE}</code>
•<b> Eǫᴜᴀʟ Sᴘʟɪᴛs :</b> <i>{EQUAL_SPLIT}</i>
•<b> Mᴇᴅɪᴀ Gʀᴏᴜᴘ :</b> <i>{MEDIA_GROUP}</i>
•<b> Lᴇᴇᴄʜ Cᴀᴘᴛɪᴏɴ :</b> <code>{LCAPTION}</code>
•<b> Lᴇᴇᴄʜ Pʀᴇғɪx :</b> <code>{LPREFIX}</code>
•<b> Lᴇᴇᴄʜ Sᴜғғɪx :</b> <code>{LSUFFIX}</code>
•<b> Lᴇᴇᴄʜ Dᴜᴍᴘs :</b> <code>{LDUMP}</code>
•<b> Lᴇᴇᴄʜ Rᴇᴍɴᴀᴍᴇ :</b> <code>{LREMNAME}</code>'''

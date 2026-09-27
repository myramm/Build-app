label jos01_find_josie:
    scene expression background(776, 464, 3.) as stage
    show josephine a_sides:
        offset (-175, 200)
    show anon f_shy_low with dissolve
    josephine f_surprised a_frustrated "{b}[firstname]{/b}?!"

    josephine "Apa yang kamu lakukan di sini?"

    show josephine f_concerned a_sides
    show anon b_dressed_pickup
    with {'master': fastdissolve}
    anon "Mencarimu."

    show anon b_onbed_sit f_normal with {'master': vpunch}:
        yoffset 250
    josephine "{i}*Terkesiap*{/i} Apakah kamu datang untuk menyelamatkanku?"

    anon f_confused "Hah?"

    anon "Menyelamatkanmu?!"

    josephine "Ayahku yang bodoh mengambil ponselku lagi dan menolak mengembalikannya sampai semua dokumen di lemari arsip ini beres."

    anon f_normal "Apa susahnya itu?"

    josephine "Dia ingin itu diatur berdasarkan tanggal, pabrikan, nomor model, warna, dan informasi pelanggan!"

    anon "Oh oke, itu banyak tapi masih bisa dilakukan..."

    josephine @ f_eyeroll a_point_back "Ya, tapi lihatlah ukurannya!"

    josephine f_angry_down a_sides @ f_angry_closed a_paper_angry "Aku akan terjebak di sini selamanya!!!"

    anon @ f_laugh "Hehe, tidak, kamu tidak akan..."

    josephine f_concerned "Hmm?"

    anon "Ayo, aku akan membantumu."

    josephine f_normal "Benar-benar?"

    anon "Ya kenapa tidak."

    anon "Anda menghemat banyak uang untuk membeli mobil yang saya butuhkan, dan mungkin saya akan menemukan beberapa informasi berguna..."

    show anon b_dressed_pickup with dissolve:
        yoffset 0
    pause .3
    hide anon with dissolve
    josephine @ f_eyeroll "Saya meragukannya..."

    show josephine with slowdissolve:
        flip
        xoffset 150
    josephine "... Itu hanya sekumpulan dokumen mobil yang bodoh."

    show anon b_dressed_pickup with dissolve:
        flip
    pause .3
    show anon b_onbed_sit with {'master': dissolve}:
        yoffset 250
    anon @ f_surprised "Saya yakin kuitansi dari mobil yang dibeli orang Rusia ada di sana!"

    anon @ f_laugh "Bahkan mungkin ada alamat atau informasi perbankan..."

    josephine f_concerned "Mengapa Anda begitu peduli dengan orang-orang Rusia ini?"

    anon f_worried "Ehh, ceritanya panjang."

    josephine f_normal "Yah, sepertinya aku tidak punya urusan lain..."

    pause
    josephine "Tumpahkan itu."

    anon "{i}*Sigh*{/i} Baiklah... Tapi bekerja dan mendengarkan pada saat yang sama, ya?"

    josephine f_angry "Uh, baiklah."


    scene location_dealership_office_cutscene03
    show text _ ("I spent the next few hours organizing the dealership's receipts as {b}Josephine{/b} sat nearby, doing everything she could think of to avoid work...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... It didn't really bother me though.\nShe may have been a terrible work partner but she was a surprisingly attentive audience.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Offering condolences at my father's death and gasping when I told her about the constant harassment from the Russian Mafia.") as caption with dissolve
    pause

    scene expression background(776, 464, 3.) as stage
    show josephine a_sides:
        flip
        offset (150, 200)
    show anon a_receipts f_worried_low:
        flip
        yoffset 200
    with fade
    josephine "Jadi pria {b}Tony{/b} ini hanya membantumu karena kebaikan hatinya?"

    anon "Ya, sejauh ini."

    josephine "Hmm, terdengar mencurigakan bagiku..."

    josephine "Dia menginginkan sesuatu darimu, aku yakin."


    if M_anon.finished_state(S_ano11_init):
        anon f_worried "T-tidak, dia tidak..."

        anon f_worried_low "Maksudku-"

        josephine f_surprised "{i}*Terkesiap*{/i} Dia MEMINTA sesuatu darimu!"

        anon f_hurt @ -m_talk "..."
        josephine f_sexy "Apa itu?!"

        anon f_worried_low "T-tidak ada."

        josephine "Oh, ayolah... aku ingin tahu!"

        anon "Aku tidak bisa memberitahumu."

        josephine f_concerned "Silakan?!"

        anon f_worried "Tidak."

        josephine a_crossed f_bored @ f_eyeroll "Ugh, laaaaaa!"

    else:
        anon f_worried "Tidak, menurutku dia tidak menginginkan apa pun dariku..."

        anon "... {b}Tony{/b} adalah pria yang baik."

        josephine f_concerned "Ya, mantan narapidana baik yang memiliki koneksi mafia..."

        josephine f_normal @ f_eyeroll "Saya yakin itulah masalahnya."

        anon @ f_laugh "Hehe, itu benar!"

        josephine f_bored "Kamu sangat naif..."


    show anon f_worried_low
    pause
    show josephine f_surprised
    pause .2
    hide josephine with dissolve
    anon "Hei, tunggu sebentar..."

    show anon b_dressed_pickup with dissolve
    pause
    anon b_dressed f_surprised_low a_receipts2 "!!!" with hpunch
    anon "Tanda terima ini bertuliskan nama ayahku!"

    show anon b_dressed_pickup with dissolve:
        unflip
        xoffset 500
    pause
    anon b_dressed f_surprised_low a_receipts_point "Begitu pula yang ini!"

    pause
    anon "!!!"
    anon "Semua kuitansi ini mencantumkan namanya!"

    anon a_receipts2 "Yang ini bertanggal hanya beberapa minggu sebelum dia meninggal!"

    pause
    anon "Dia membeli lima Mobil Kota Abraham hitam..."

    anon f_surprised_down "... Untuk tiga ratus tujuh puluh lima ribu dolar?!?!"


    if M_rump.state is None:
        josephine "Itu pasti salah satu kuitansi Rusia."

        josephine "Mereka selalu membeli mobil mewah berwarna hitam dalam jumlah besar seperti itu."

        anon f_worried_left "T-tapi, itu tidak masuk akal..."

    else:
        josephine "Apakah itu mengejutkan Anda?"

        josephine "Anda bilang dia mencuci uang untuk massa, kan?"

        anon f_worried_left "Y-ya, aku hanya belum siap untuk menemukan sebanyak itu..."


    show anon f_worried a_receipts with {'master': dissolve}:
        flip
        xoffset -50

    if M_rump.state is None:
        anon "Mengapa ayahku menjadi-"

    else:
        anon "Maksudku, ini-"


    scene josephine b_chair f_sexy
    anon "!!!" with hpunch
    anon "Apa yang kamu lakukan?!"

    josephine f_confused "Umm, merasa nyaman?"

    josephine "Duh."

    anon "K-kamu telanjang..."

    josephine f_sexy @ f_laugh "hehe!"

    josephine "Lihat sesuatu yang kamu suka?"

    anon "..."
    josephine "Anda bisa datang dan melihat lebih dekat, tahu?"

    anon "{i}*Gulp*{/i} B-benarkah?"

    josephine @ -m_talk "Mhmm."


    scene expression background(712, 400, 3.) as stage
    show josephine b_naked_sexy f_sexy:
        flip
        xoffset 150
    show anon f_flirt_low a_receipts:
        flip
        xoffset -50
    with fade
    josephine "Mengapa kamu tidak meletakkan itu dan melepas celanamu?"

    anon f_worried "A-apa, di kantor ini?"

    josephine @ -m_talk "Mhmm."

    josephine "Saya pikir kita mendapat sedikit istirahat, bukan?"

    pause
    anon f_thinking_down "Menurut Anda, mungkinkah saya bisa membuat salinannya terlebih dahulu?"

    show anon f_surprised
    show josephine f_angry a_hips b_naked m_talk
    with fastdissolve
    josephine -m_talk "Bung, serius?"

    josephine "Aku melemparkan diriku padamu di sini!!"

    anon f_worried "Y-ya, aku tahu... Hanya saja-"

    josephine a_crossed @ -m_talk "..."

    if M_rump.state is None:
        anon "Ini mungkin bisa membantuku mencari tahu apa yang terjadi dengan ayahku, kau tahu?"

    else:
        anon "Polisi mungkin bisa menggunakan ini untuk membangun kasus ayahku!"


    show josephine f_concerned
    pause
    josephine a_hips "Ya, kamu benar."

    josephine "Saya minta maaf."

    anon "Tidak, kamu tidak perlu-"

    josephine "Sebaiknya ambil saja, {b}[firstname]{/b}."

    anon "Benar-benar?"

    josephine "Ya."

    anon "Bukankah ayahmu akan marah?"

    josephine f_sexy @ a_gimme "Dia mungkin bahkan tidak akan menyadarinya..."

    josephine @ f_laugh "... Dan jika dia melakukannya, hal terburuk apa yang bisa terjadi?"

    josephine "Kami sudah tahu dia tidak akan memecat saya."

    show anon a_receipts_pocket f_flirt_low behind josephine with dissolve
    pause
    anon a_idle "Terima kasih, {b}Josephine{/b}."

    josephine "Ya, ya..."

    show josephine b_naked_jerk a_idle f_sexy_down with dissolve:
        xoffset -50
    josephine "... Bisakah kita mengencangkannya sekarang?"

    show josephine a_unzip2
    show anon a_surprised b_shirt
    with dissolve
    anon "!!!"
    josephine "Semua dokumen ini membuatku merasa sangat jengkel dan aku perlu mengeluarkan tenaga."

    show josephine b_naked a_sides:
        xoffset 340
    show anon b_shirt od_dick3 f_flirt
    with dissolve
    show anon od_dick4
    anon "A-apakah kamu tidak khawatir seseorang akan datang ke sini?"

    show anon od_empty f_flirt_low a_sides
    show josephine b_naked_jerk a_jerk:
        xoffset -50
    with dissolve
    josephine "Mereka tidak akan datang ke sini."


    if M_rump.state is None:
        josephine "Tidak dengan kunjungan walikota."

    else:
        josephine "Tidak dengan kunjungan manajer regional."


    anon "Saya rasa itu benar."

    josephine "Dan bahkan jika mereka melakukannya..."

    josephine "... Bukannya kamu perlu merasa minder."

    show josephine b_naked_grab f_sexy:
        xoffset -450
    hide anon
    with {'master': dissolve}
    josephine "Ayo, potong mangkuk."

    anon "Tolong, berhenti memanggilku seperti itu..."

    hide josephine with {'master': dissolve}
    josephine "Hehehe!"


    call scene_josie_sex

    scene location_dealership_office_cutscene01
    sato "{b}Josephine?{/b}" with hpunch
    josephine "{b}Ayah{/b}?"

    anon "!!!"

    scene location_dealership_office_cutscene02 with fastfade
    anon "Ini bukan-"

    anon "Maksudku, kami tidak-"

    sato "KELUARKAN PENISMU DARI PUTRIKU!!!"

    pause

    scene expression background(712, 400, 3.) as stage
    show anon b_shirt f_worried a_empty od_dick1:
        flip
        xoffset 120
    show anon_arms_dressed_a_cover_boner:
        flip
        xoffset 120
    show josephine b_naked a_crossed f_angry:
        xoffset -100
    show sato f_angry:
        flip
        xoffset -70
    with fade
    josephine "Apa-apaan ini, {b}Ayah{/b}?!"

    josephine "Pernahkah Anda mendengar tentang mengetuk?"

    sato "Tidak di kantor saya sendiri!"

    sato "Apa yang kamu pikirkan?!"

    josephine "Umm, menurutku pekerjaan ini membosankan sekali dan pacar baruku punya penis yang luar biasa!"

    sato @ f_surprised "A-apa?!"

    josephine "Anda bertanya, {b}Ayah{/b}!"

    sato "Itu bukan-"

    sato "Grr, kamu tahu maksudku!"

    anon "Aku mungkin harus pergi..."

    sato "Kamu tetap di sana!"

    josephine @ f_angry_back "Tetap di sana!"

    anon f_sad_down @ f_surprised "Oh oke..."

    sato a_crossed "Ini adalah perilaku yang tidak dapat diterima, nona muda!"

    josephine "Pfft, apa yang akan kamu lakukan, pecat aku?!"

    sato "Oh, saya yakin Anda akan menyukainya, bukan?!"

    pause
    josephine f_angry_closed a_frustrated "Kaulah yang mengurungku di sini tanpa ponselku!"

    josephine "Menurutmu apa yang akan terjadi?!"

    show josephine f_angry
    sato "Saya pikir kamu akan melakukan pekerjaanmu!"

    sato "Tidak untuk mengacaukan pelanggan di meja SAYA!!!"

    josephine "Dia bukan hanya pelanggan, ayah!"

    josephine a_idle @ a_gimme "Dia pacarku!"

    anon @ f_confused "Hmm, pacar?"

    anon f_worried "Saya tidak sadar kami memberi label-"

    josephine f_angry_back "Diam, {b}[firstname]{/b}!!"

    anon f_sad_down @ f_surprised "Benar, maaf."

    show josephine f_angry
    sato "Saya tidak peduli apakah dia Raja Inggris, Anda tidak boleh melakukan hal seperti ini di tempat kerja..."

    josephine "Hah!"

    josephine "Kalau begitu, sebaiknya kau pecat aku sekarang, Ayah..."

    josephine "Karena pacarku dan aku akan MENCINTAI SEMUA dealer bodoh ini!"

    josephine f_angry_back "Benar kan, {b}[firstname]{/b}?"

    anon f_worried "Uhh..."

    pause
    anon "... Saya tidak tahu apa yang Anda ingin saya katakan saat ini."

    show josephine f_eyeroll

    if M_kim.state is None:
        kim "{b}Tuan. Sato{/b}?"

    else:
        yoyo "{b}Tuan. Sato{/b}?"


    show josephine f_angry
    sato "Jangan sekarang, {b}Kim{/b}!"

    sato "Saya sedang menghadapi situasi di sini!"


    if M_kim.state is None:
        kim "Oh, ehh..."

    else:
        yoyo "Oh, ehh..."


    pause

    if M_rump.state is None:
        kim "... {b}Walikota Rump{/b} akan berangkat."

    elif M_kim.state is None:
        kim "... Manajer regional akan pergi."

    else:
        yoyo "... Manajer regional akan pergi."


    sato @ f_angry_closed a_facepalm "{i}*Huh*{/i} Tentu saja dia..."


    if M_rump.state is None:
        sato f_normal "Bisakah Anda mengenakan pakaian saja saat saya mengantar Walikota keluar?"

    else:
        sato f_normal "Bisakah Anda mengenakan pakaian saja saat saya mengantar bos saya keluar?"


    sato "Kami akan membahas ini ketika saya kembali."

    josephine @ f_eyeroll "Ya, terserah..."

    josephine a_gimme "... Berikan ponselku."

    show sato a_phone_pocket f_sad_down with dissolve
    pause .5
    sato a_phone_give f_normal "Di Sini."

    show josephine a_phone f_normal_down
    show sato a_idle
    with dissolve
    pause
    sato "Tolong, jangan lakukan apa pun sampai aku kembali."

    josephine "Ya, kita akan lihat."

    show sato f_sad_down with {'master': dissolve}:
        xoffset -600
        xzoom 1
    sato "{i}*Huh*{/i}"

    hide sato with dissolve
    pause
    josephine @ -m_talk "..."
    hide anon_arms_dressed_a_cover_boner
    show anon a_sides:
        unflip
        xoffset 0
    with dissolve
    anon "{i}*Ehem*{/i}"

    anon "Itu aneh..."

    josephine f_sexy "Hehe, ya."

    josephine "Maaf tentang itu."

    show anon b_flour f_looking_down with dissolve:
        yoffset 110
    pause
    show anon b_dressed f_confused a_idle with dissolve:
        yoffset 0
    anon "Jadi, aku pacarmu sekarang?"

    josephine "Sejauh yang dia tahu, kamu memang begitu."

    anon "Benar."

    anon "Oke."

    anon f_worried_left a_behind_head @ -m_talk "..."
    pause
    josephine f_bored "Anda mungkin harus pergi."

    anon f_shy "Fiuh, ya... Tadinya aku mau bilang..."

    josephine "Sekali lagi terima kasih telah membantu saya hari ini."

    anon f_normal @ f_laugh a_wave "Terima kasih kembali."

    josephine "Maaf kami belum menyelesaikannya... Anda tahu..."

    anon "Jangan khawatir."

    anon "Sampai jumpa lagi."

    josephine f_normal_down "Oke."

    pause
    show josephine b_naked_mc_kiss_cheek f_surprised
    hide anon
    with dissolve
    pause
    show anon f_worried:
        xoffset 100
    show josephine b_naked
    with dissolve
    josephine f_concerned "Apa yang sedang kamu lakukan?"

    anon "Aku tidak tahu."

    anon "aku baru dalam hal ini..."

    show josephine f_eyeroll
    pause
    show josephine b_naked_kiss:
        xoffset -150
    hide anon
    with dissolve
    anon "!!!"
    pause
    show josephine b_naked a_idle f_sexy:
        xoffset -100
    show anon:
        xoffset 100
    with dissolve
    josephine "Sekarang serius, pergilah."

    anon "Baiklah."

    hide anon with dissolve
    pause
    josephine @ -m_talk "..."
    show josephine f_normal_down a_phone with dissolve
    pause

    $ player.go_to(L_dealership_showroom)
    scene expression player.location.background_blur as stage with fade
    show anon f_worried with dissolve
    anon @ -m_talk "( Sepertinya pantainya cerah. )"

    anon @ -m_talk "(Saya harus segera keluar dari sini sebelum {b}Tuan Sato{/b} kembali.)"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

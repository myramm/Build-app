label jos01_spot_sato:
    if M_rump.state is None:
        jump jos01_spot_sato.ronald

    if M_kim.state is None:
        jump jos01_spot_sato.kim

    jump jos01_spot_sato.yoyo


label jos01_spot_sato.ronald:
    show sato f_smiling a_empty:
        xoffset -77
    show rump f_smirk a_handshake_sato:
        xzoom -1
    show kim f_smirk:
        xoffset 100
    rump "Oh, yang pasti."

    rump "Sang istri sangat senang dengan hal itu."

    show sato a_idle
    show rump a_idle
    with dissolve
    rump "Ini adalah mesin yang berkualitas tentunya."

    sato "Senang sekali mendengarnya, {b}Pak. pantat{/b}!"

    sato "Saya tidak dapat memberi tahu Anda betapa kami menghargai bisnis Anda!"

    rump @ a_finger "Oh, Anda bisa menunjukkan apresiasi Anda pada musim gugur ini dengan suara Anda."

    sato "Tentu saja, Pak!"

    sato "Anda dapat mengandalkan saya."

    rump "Itu yang ingin saya dengar, {b}Pak. Sato{/b}."

    rump "Anda tahu, inilah pria yang harus Anda ucapkan terima kasih!"

    show rump a_handshake_kim:
        xoffset 142
    show kim a_empty behind rump:
        xoffset 50
    with dissolve
    rump "Dia penjual yang hebat!"

    show kim a_rub:
        xoffset 100
    show rump a_idle:
        xoffset 0
    with dissolve
    kim "Oh, Anda juga baik hati, {b}Tuan. Walikota{/b}."

    rump "Tolong, {b}Kimmy{/b}... Hubungi saya {b}Ronald{/b}."

    kim "Sangat buruk, {b}Ronard{/b}."

    rump "Saya ingin tahu apakah Anda mau memberi saya waktu berduaan dengan teman baru saya di sini, {b}Tuan. Sato{/b}?"

    sato "Oh, tentu saja, Pak!"

    sato "Saya akan segera berada di sana, di meja depan, jika Anda memerlukan sesuatu..."

    rump "Terima kasih."

    hide sato with dissolve
    pause .5
    show kim a_wave with dissolve:
        xoffset -100
    kim a_idle @ a_wave "Ayo, kita pergi ke garasi."

    kim "Lebih pribadi."

    hide rump
    hide kim
    with dissolve

    scene expression background(240, 480, 6.) as stage
    show anon f_skeptical
    with fade
    anon @ -m_talk "(Hmm?)"

    anon @ -m_talk "( Walikota berteman dengan {b}Kim{/b}? )"

    anon @ -m_talk "(Sesuatu yang mencurigakan sedang terjadi di sini...)"

    pause
    anon @ -m_talk "( ... Dan dimana {b}Josephine{/b}? )"

    pause
    anon f_grin @ -m_talk "(Saya harus menyelidikinya.)"

    hide anon with dissolve
    return


label jos01_spot_sato.kim:
    show kim f_angry behind sato
    show sato a_paper_show f_angry:
        xoffset 200
        xzoom -1
    sato "Angka penjualan kami turun hampir tujuh puluh persen!"

    show sato a_phone_pocket with {'master': dissolve}
    kim m_talk "Saya kira Anda sudah siap, {b}Pak. Sato{/b}!"

    show sato a_hips with {'master': dissolve}
    kim f_baby_cry -m_talk "{b}Walikota Bokong{/b} jadilah penjara!"

    kim "Kita harus menunggu sayang baru dengan klien besar!"

    sato a_crossed f_confused "Berapa lama waktu yang dibutuhkan?!"

    sato "Manajer regional akan berada di sini setiap saat dan dia akan menginginkan jawaban!"

    kim a_rub f_smirk "Tidak apa-apa, Anda akan memintanya untuk segera membeli mobil busuk."

    kim a_counter_raised "{b}Kim{/b} nomor satu, saresman terbaik!"

    kim a_idle "Tidak pernah adil!"

    sato f_angry @ -m_talk "Hmph."

    pause
    sato a_idle f_normal "Baiklah, saya sarankan Anda mulai menelepon {i}klien besar{/i} ini segera..."

    sato "... Dan suruh dia bergegas, karena pekerjaan kita mungkin sangat bergantung padanya!"

    kim a_scare f_baby_cry "Y-ya, {b}Kim{/b} temui mereka sekarang!"

    kim a_rub f_normal "Jangan khawatir."

    sato "Saya khawatir, {b}Kim{/b}."

    sato "Saya sangat khawatir."

    show kim f_baby_cry
    pause
    show kim f_surprised
    sato "Pergi."

    kim f_baby_cry "Y-ya, {b}Kim{/b} perbaiki... Begini!"

    kim f_smirk "{b}Kim{/b} nomor satu!"

    hide kim
    show sato f_angry:
        xoffset -300
        xzoom 1
    with {'master': dissolve}
    kim "Saresman terbaik!"

    show sato a_facepalm f_angry_closed with {'master': dissolve}
    kim "Tidak pernah adil!"

    hide sato with dissolve

    scene expression background(240, 480, 6.) as stage
    show anon f_brag
    with fade
    anon @ -m_talk "( Sepertinya {b}Kim{/b} mengalami kesulitan sekarang karena {b}Rump{/b} berada di balik jeruji besi... )"

    anon @ f_grin -m_talk "( ... Saya yakin {b}Josephine{/b} menyukainya! )"

    pause
    anon f_confused @ -m_talk "(Hmm?)"

    anon @ -m_talk "(Ngomong-ngomong tentang {b}Josephine{/b}, dimana dia? )"

    anon @ -m_talk "(Dia pasti ada di sini di suatu tempat...)"

    hide anon with dissolve
    return


label jos01_spot_sato.yoyo:
    show sato f_smiling:
        xoffset 200
        xzoom -1
    show yoyo
    yoyo "Sekali lagi terima kasih atas pekerjaannya, {b}Bpk. Sato{/b}."

    yoyo "{b}Kim{/b} sangat antusias dengan peluang ini."

    sato "Oh, dengan senang hati, sayang."

    sato "Kakakmu membawa banyak bisnis untuk kami..."

    sato "...Jadi setidaknya itulah yang bisa kulakukan."

    pause
    sato f_normal "Saya sangat menyesal mendengar apa yang terjadi."

    yoyo "Ya, itu membuat suasana di kampung halaman di Korea menjadi sangat bau."

    yoyo "Keluarga kami mendesak {b}Kim{/b} datang dan memperbaiki kerusakan yang terjadi pada reputasi kami."

    sato a_hips f_smiling "Oh, aku tahu semua tentang rasa malu keluarga... Percayalah."

    sato "Heh, aku mendapat banyak hal dari putriku!"

    yoyo @ -m_talk "..."
    sato f_sad @ -m_talk "..."
    sato "Kau tahu, karena dia umm..."

    show sato a_idle with {'master': dissolve}
    yoyo @ -m_talk "..."
    sato f_sad_down "... Y-yah, ibunya meninggal... Dan kami uhh..."

    yoyo @ -m_talk "..."
    sato "...Belum benar-benar pulih-"

    show sato f_surprised
    pause
    sato f_sad "Err, Sudahlah."

    sato "Hehe, itu tidak terlalu penting."

    pause
    sato "{i}*Gulp*{/i} Kamu uhh, kalau begitu, bicaralah dengan kakakmu?"

    sato "Apakah dia baik-baik saja?"

    yoyo "Dia saat ini dipenjara di penjara Amerika."

    sato f_uneasy "Y-ya, tentu saja... Aku hanya bermaksud mengatakan, jika ada yang bisa kulakukan... Hanya-"

    yoyo a_stop "Tidak, tidak apa-apa."

    yoyo "Kembalikan kami bergerak maju dan fokus pada upaya masa depan."

    show yoyo a_idle with {'master': dissolve}
    sato f_normal "Benar, tentu saja."

    yoyo "Anda bilang, manajer regional datang hari ini?"

    sato @ f_confused -m_talk "Hmm?"

    sato "Oh iya... Tapi ehh, itu hanya kunjungan rutin... Tidak ada yang perlu dikhawatirkan."

    yoyo "Sebaliknya, {b}Kim{/b} percaya bahwa kunjungan rutin adalah kesempatan untuk menjalin hubungan yang lebih baik."

    show sato f_confused
    yoyo "Seseorang harus selalu berusaha untuk memberikan kesan yang baik, terutama kepada mereka yang memiliki kekuatan besar."

    sato f_sad "Umm, ya... Itu saran yang sangat bagus."

    yoyo "Mungkin Anda ingin {b}Kim{/b} berbicara dengannya?"

    yoyo "Saya punya banyak ide yang bisa meningkatkan angka penjualan kita..."

    yoyo "... Dan sentuhan feminin sering kali lebih baik diterima oleh pria yang berkedudukan tinggi."

    sato f_confused "K-kamu ingin bertemu dengannya?"

    yoyo @ f_quizzical "Jika tidak terlalu merepotkan?"

    sato f_normal "Umm, tidak... Tidak masalah."

    sato f_smiling "Saya akan dengan senang hati memperkenalkan Anda."

    yoyo "Sangat bagus."

    yoyo "Jika kamu permisi?"

    yoyo "{b}Kim{/b} ingin pergi dan menyegarkan diri sebelum manajer wilayah datang."

    sato "Y-ya, tentu saja."

    show sato f_confused_low
    show yoyo b_dressed_bow
    with {'master': dissolve}
    pause
    show sato f_confused
    yoyo b_dressed "Terima kasih."

    hide yoyo
    show sato f_uneasy:
        xoffset -300
        xzoom 1
    with {'master': dissolve}
    sato f_uneasy "{i}*Gulp*{/i} Wow... Okay."

    hide sato with dissolve

    scene expression background(240, 480, 6.) as stage
    show anon a_surprised f_shock
    with fade
    anon @ -m_talk "( That's {b}Kim{/b}'s sister?! )"

    anon a_sides f_worried @ -m_talk "( I have a bad feeling about this... )"

    anon f_thinking @ -m_talk "( ... And where's {b}Josephine{/b}?! )"

    anon f_confused @ -m_talk "( I don't see her anywhere! )"

    anon @ -m_talk "(Saya harus menyelidikinya.)"

    return


label jos01_find_sato:
    show anon with dissolve
    anon "Halo?"

    sato f_smiling "Greetings and welcome to-"

    sato f_normal "Oh, it's you again."

    sato "Look, I'm afraid my daughter can't play with you today... We're very busy!"

    anon f_worried "Play with me?"

    sato "Or whatever it is you crazy kids do..."

    sato "We have a very important man visiting us today and I don't want her pulling any shenanigans!"

    anon "Oh oke..."

    sato "Come back another day."

    pause
    hide anon with dissolve

    scene expression background(240, 480, 6.) as stage with fade
    show anon a_thinking f_thinking with dissolve:
        flip
        xoffset -400
    anon @ -m_talk "( Hmm, I guess that explains why {b}Josephine{/b} isn't at the front desk... )"

    anon @ -m_talk "( She has to be around here somewhere, perhaps {b}I should look for her{/b}? )"

    hide anon with dissolve
    return


label jos01_find_sato.repeat:
    scene expression background(240, 480, 6.) as stage
    show anon f_worried with dissolve:
        xoffset 300
    anon @ -m_talk "( No, he's not going to tell me where {b}Josephine{/b} is. )"

    anon @ -m_talk "( She has to be around here somewhere, perhaps I should {b}look for her{/b}? )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

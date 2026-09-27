label liu_button_lobby:
    show anon with dissolve
    liu "Selamat datang di {b}Saga Finansial{/b}."

    liu f_happy "Bagaimana saya bisa membantu-"


    if M_anon.finished_state(S_ano28_clue):
        show liu a_mouth_cover f_surprised
        with {'master': dissolve}
        liu "{b}[firstname]{/b}!!"

        anon a_wave "Hei, Liu."

        show anon a_sides
        show liu a_point_self
        with {'master': dissolve}
        liu "Apakah kamu datang menemuiku?"

        show liu a_sides
        with {'master': dissolve}
    else:

        show liu a_sides f_nervous
        with {'master': dissolve}
        liu "O-oh, kamu kembali..."

        anon "Halo lagi, Liu."


    menu liu_button_lobby.choice:

        "Nomor apartemen?" if M_anon.is_state(S_ano23_done, S_ano24_init):
            jump liu_button_lobby.apartment

        "uang ayah." if M_anon.is_state(S_ano28_cash):
            jump ano28_cash_liu_money

        "Apakah Tina ada?" if M_tina.is_state(S_tin02_init):
            if L_bank_cubicle.is_here(M_tina):
                jump tin02_init_liu
            jump liu_button_lobby.tina
        "akun saya.":

            jump liu_button_lobby.account

        "Tentang ayahku..." if not M_anon.finished_state(S_ano28_clue):
            jump liu_button_lobby.father

        "Bagaimana kabarmu?" if M_anon.finished_state(S_ano14_find):
            if M_anon.finished_state(S_ano28_clue):
                jump liu_button_lobby.upbeat
            jump liu_button_lobby.unsure

        "Seks." if M_anon.finished_state(S_ano28_clue):
            jump liu_button_lobby.suggest
        "Saya harus pergi.":

            pass

    if M_anon.finished_state(S_ano28_clue):
        anon f_worried "Aku harus pergi."

        liu f_sexy a_sides "Ingat, untuk datang ke apartemenku nanti, oke?"

        anon f_flirt "Jangan khawatir, saya akan melakukannya."

        liu f_happy "Sampai jumpa lagi, {b}[firstname]{/b}."

        anon f_normal "Sampai jumpa, {b}Liu{/b}."

    else:

        anon f_normal "Semoga harimu menyenangkan."

        liu "Ya, kamu juga."


    hide anon with dissolve
    return


label liu_button_lobby.account:
    anon f_normal "Di mana saya dapat mengakses akun saya?"

    liu f_normal "Cara termudah adalah dengan menggunakan salah satu mesin ATM kami."

    liu @ a_point_away "Faktanya, ada satu di belakang Anda."

    show anon f_normal_left
    liu "Di sana, di dinding seberang."

    anon f_normal "Baiklah terima kasih."

    liu f_worried "Tidak masalah."

    jump liu_button_lobby.choice


label liu_button_lobby.anything:
    anon f_confused "Apa pun?"

    liu "Ya, apa pun yang Anda inginkan!"

    show liu f_sexy o_blush
    with {'master': dissolve}
    liu "aku milikmu."

    show anon a_thinking f_thinking
    show liu f_nervous_lipbite
    with {'master': dissolve}
    anon @ -m_talk "Hmm."

    anon "Saya akan menghubungi Anda kembali mengenai hal itu."

    show anon a_idle f_normal
    show liu f_worried -o_blush
    with dissolve
    jump liu_button_lobby.choice


label liu_button_lobby.apartment:
    anon f_worried @ f_confused "Dimana apartemenmu lagi?"

    liu f_normal "Kami tinggal di {b}Kompleks Apartemen Beachside Heights, kamar 204{/b}."

    anon f_normal "Oh benar."

    anon "Saya ingat sekarang."

    liu "{b}Kim{/b} biasanya bekerja hingga larut malam jadi jika Anda datang di malam hari, kita akan punya banyak waktu untuk mengintip."

    anon "Sempurna."

    jump liu_button_lobby.choice


label liu_button_lobby.boss:
    show liu f_nervous_back o_blush with {'master': dissolve}
    liu "Ssst, {b}[firstname]{/b}!!!"

    show anon f_normal
    show liu a_cover f_nervous
    with {'master': dissolve}
    liu "Kita tidak bisa melakukan itu sekarang!"

    anon "Kenapa?"

    liu "Bosku ada di sini..."

    show liu -o_blush
    with {'master': dissolve}
    liu "... dia bisa-"

    anon f_confused "Maksudmu {b}Tina{/b}?"

    liu "Ya!"

    show anon f_normal

    menu:
        "Saya yakin dia tidak akan keberatan.":
            jump liu_button_lobby.risky
        "Kita bisa memintanya untuk bergabung dengan kita?":

            jump liu_button_lobby.threesome
        "Lain kali saja.":

            pass

    anon "Tidak apa-apa, kita bisa bertemu lagi nanti di tempatmu."

    liu f_worried "Ya..."

    show liu a_nervous f_worried_down with {'master': dissolve}
    liu "... Kecuali, sekarang sore hari akan terasa seperti selamanya!"

    anon f_flirt "Antisipasi justru membuatnya lebih baik, Anda tahu?"

    show liu a_sides f_nervous_lipbite with {'master': dissolve}
    liu @ -m_talk "Tidak."

    pause
    liu f_nervous "Berhentilah menggodaku, {b}[firstname]{/b}!"

    anon f_normal "Hehe, maaf."

    pause
    anon @ f_thinking -m_talk "( Bukankah {b}Liu{/b} menyebutkan sebelumnya bahwa {b}Tina datang terlambat pada hari Selasa{/b}? )"

    jump liu_button_lobby.choice


label liu_button_lobby.father:
    anon f_confused "Apakah kamu yakin tidak ada lagi yang bisa kamu ceritakan padaku?"

    liu f_nervous @ f_nervous_back "aku uhh-"

    pause

    if M_anon.finished_state(S_ano14_find):
        jump liu_button_lobby.rump

    anon "Apakah Anda mengenalnya dengan baik?"

    liu "Y-ya, kami-"

    show liu f_worried_down
    pause
    liu f_worried "Maksudku, tidak... Kami hanya rekan kerja."

    liu @ a_holdup "Lihat, {b}[firstname]{/b}..."

    liu "Ayahmu adalah pria yang sangat baik dan aku berduka atas kematiannya, tapi aku-"

    anon @ -m_talk "..."
    liu "Saya benar-benar tidak tahu apa-apa."

    anon f_worried @ -m_talk "(Dia berbohong.)"

    liu f_worried_down "Saya berharap saya melakukannya..."

    anon @ -m_talk "(Kenapa dia tidak memberitahuku?)"

    liu f_worried "Sepertinya Anda dan teman Anda sedang melalui masa sulit saat ini, dan saya bersimpati, ya."

    liu "Aku berharap masih ada lagi yang bisa kulakukan untukmu..."

    anon @ -m_talk "(Pasti ada sesuatu yang bisa kulakukan agar dia terbuka padaku...)"

    pause
    anon @ a_thinking f_thinking -m_talk "(...Mungkin aku hanya perlu mencari momen yang tepat?)"

    jump liu_button_lobby.choice


label liu_button_lobby.risky:
    anon "Dia akan baik-baik saja dengan itu."

    show liu a_nervous f_worried_down with {'master': dissolve}
    liu "Ya benar."

    liu f_worried "Saya akhirnya mendapatkan semua keuntungan dari pekerjaan ini dan Anda ingin saya mengambil risiko kehilangan pekerjaan ini?"

    anon "{b}Tina{/b} tidak akan memecatmu karena hal seperti itu."

    liu f_curious "Bagaimana Anda bisa yakin?"

    show anon a_behind_head f_worried_surprised with {'master': dissolve}
    anon "aku uhh..."

    show anon f_worried_left
    pause
    show anon a_sides f_worried with {'master': dissolve}
    liu "Lihat, kamu tidak tahu pasti!"

    anon f_normal "Nah, kalau kamu dipecat, itu akan memberi kita lebih banyak waktu luang bersama..."

    show liu a_sides f_happy with {'master': dissolve}
    liu "Haha, lucu sekali."

    liu f_nervous "Kita seharusnya tidak melakukannya, {b}[firstname]{/b}..."

    liu f_worried "... aku minta maaf."

    anon "Oh, tidak apa-apa."

    anon "Saya mengerti."

    liu f_nervous "Mengapa kamu tidak datang saja ke tempatku malam ini sepulang kerja?"

    liu f_sexy "Aku akan menebusnya padamu kalau begitu."

    anon "Kedengarannya bagus."

    jump liu_button_lobby.choice


label liu_button_lobby.rump:
    anon f_worried "Tolong, {b}Liu{/b}... Aku khawatir apa yang akan terjadi pada teman-temanku jika semua ini terus berlanjut..."

    show liu f_worried
    anon "... Informasi apa pun berguna, sekecil apa pun."

    liu "Y-yah, saya tahu {b}Frank{/b} sedang mengontrak beberapa pekerjaan dengan {b}Walikota Rump{/b}..."

    anon f_normal "Ya, aku sendiri yang memikirkannya."

    pause
    anon "Pernahkah dia menyebutkan pekerjaan apa itu?"

    show liu f_nervous_back a_cover with dissolve
    anon "Atau mungkin siapa lagi yang terlibat?"

    liu f_nervous "Umm... T-tidak, menurutku tidak..."

    anon "Apa kamu yakin?"

    liu "Itu terjadi beberapa waktu yang lalu... A-dan ingatanku tidak begitu bagus..."

    anon f_worried @ -m_talk "(Dia berbohong lagi.)"

    liu a_sides "Saya benar-benar minta maaf, {b}[firstname]{/b}..."

    liu "... Saya berharap saya bisa lebih membantu."

    anon f_thinking_down @ -m_talk "(Saya kira dia masih tidak mempercayai saya.)"

    anon f_normal "Tidak apa-apa, {b}Liu{/b}."

    anon "Saya mengerti."

    liu f_normal "Saya yakin polisi akan menjaga keamanan teman Anda."

    anon "Ya, saya harap begitu."

    anon @ -m_talk "(Saya hanya harus terus memainkan permainan menunggu untuk saat ini...)"

    anon @ -m_talk "( ... Dan mudah-mudahan, ada kesempatan lain yang muncul. )"

    jump liu_button_lobby.choice


label liu_button_lobby.sex:
    show liu a_mouth_cover f_surprised o_blush with {'master': dissolve}
    liu "Apa sekarang?!"

    anon f_happy "Ya."

    liu a_nervous f_worried "Kita tidak bisa melakukan itu, saya sedang bekerja!"

    show anon f_skeptical with dissolve:
        xoffset -500
        xzoom -1
    pause
    show anon a_point_back f_confused with {'master': dissolve}:
        xoffset 0
        xzoom 1
    anon "Aww, ayolah, hampir tidak ada orang di sini..."

    show liu f_ashamed_down
    pause
    show anon a_sides f_brag with {'master': dissolve}
    anon "... Dan bosmu tidak akan datang sampai sore ini, kan?"

    liu a_behind f_nervous "Y-ya."

    anon f_normal "Mari kita menyelinap ke belakang sebentar..."

    show liu f_nervous_lipbite
    anon "... Itu akan sepadan, aku janji."

    liu f_nervous_lipbite_back @ -m_talk "Tidak."

    pause
    liu f_worried "Oke, tapi kita harus cepat!"

    hide liu with {'master': dissolve}
    anon f_brag "Hehe, ya."

    anon f_happy "\"Cepat.\""

    anon f_flirt "Benar sekali."

    hide anon with dissolve

    scene location_bank_office_printer
    show liu b_dressed_kiss_2:
        xoffset 250
    with fade
    liu "MM."

    pause
    show anon a_sides f_shy behind liu:
        xoffset 200
    show liu a_close_blouse b_dressed_disheveled f_nervous o_blush:
        xoffset 0
    with {'master': dissolve}
    liu "Ini nakal sekali, {b}[firstname]{/b}!"

    anon f_flirt "Heh, ini akan menjadi jauh lebih nakal."

    anon f_shy_down "Mengapa kamu tidak naik ke mesin fotokopi itu?"

    show anon f_flirt
    show liu a_sides f_nervous_down:
        xoffset 475
        xzoom -1
    with {'master': dissolve}
    liu @ -m_talk "Hmm?"

    show liu a_behind f_sexy:
        xoffset 0
        xzoom 1
    with {'master': dissolve}
    liu "Y-ya, oke."

    show anon f_flirt_low
    show liu a_sides f_nervous_down
    with dissolve
    show liu a_skirt_up_pull2 b_dressed_disheveled_skirt_up f_nervous_lipbite_back with {'master': dissolve}
    anon "Ya Tuhan, kamu seksi sekali!"

    show liu b_dressed_disheveled_skirt_pull_down_panties f_nervous_down with dissolve
    pause
    show anon f_flirt
    show liu a_shy b_dressed_disheveled_skirt_up f_sexy_lipbite
    with {'master': dissolve}
    liu f_sexy "Ya?"

    anon f_flirt "Ayo, naik ke sana."

    show anon a_remove_shorts f_shy_down
    show liu b_dressed_disheveled_jump1 f_nervous_down
    with dissolve
    show anon b_shirt_undress_bottom
    show liu b_dressed_disheveled_jump2 f_nervous_laugh
    with dissolve
    show anon a_sides b_shirt f_flirt od_dick1
    show liu b_dressed_disheveled_printer f_sexy_lipbite
    with dissolve
    pause
    show anon f_surprised_low
    show liu b_dressed_disheveled_printer_open
    with dissolve
    pause
    anon f_flirt_low "Itu pemandangan yang indah!"

    show anon od_dick2
    show liu f_surprised_down
    with dissolve
    show anon od_dick3 with dissolve
    show anon od_dick4 with dissolve
    pause
    liu f_laugh "hehe!"

    show liu f_sexy_lipbite
    anon f_flirt "Sekarang berbaringlah."


    call scene_liu_sex_office.repeat
    $ unlock_scene('liu', '02_unlocked')

    scene location_bank_office_printer
    show anon a_sides b_shirt f_shy:
        xoffset 200
    show liu a_sides b_dressed_disheveled_after_sex f_ashamed_down

    if _return == 'inside':
        show liu f_sexy

    with fade

    if _return == 'inside':
        liu "Celana dalamku akan penuh dengan air manimu sepanjang hari ini..."

        show anon f_shy_low
        show liu f_sexy_lipbite
        anon "Hehe, maaf."

        liu f_nervous_down "Itu menetes ke pahaku..."

        anon f_worried "... Kamu ingin aku mengambilkanmu tisu?"

        liu f_nervous "T-tidak, aku akan mengurusnya."

    else:

        liu "Apakah ini benar-benar terlihat?"

        show liu f_nervous_lipbite
        anon f_worried_low "Tidak, tidak juga."

        show anon f_shy
        liu f_nervous "Oke, bagus."


    show liu a_close_blouse b_dressed_disheveled_skirt_up f_nervous_lipbite
    with dissolve
    pause
    show anon b_shirt_undress_bottom f_looking_down
    show liu b_dressed_disheveled_skirt_pull_down_panties f_nervous_down
    with dissolve
    pause
    show anon a_remove_shorts b_dressed
    show liu a_skirt_up_pull2 b_dressed_disheveled_skirt_up
    with dissolve
    pause
    show anon a_sides f_shy_low
    show liu b_dressed_disheveled_skirt_pull1
    with dissolve
    pause
    show anon f_shy
    show liu a_sides b_dressed_disheveled f_happy
    with {'master': dissolve}
    liu f_happy "Heh, aku hampir tidak bisa berdiri!"

    show anon a_handshake f_worried
    show liu f_nervous_down
    with {'master': dissolve}
    anon "Apakah kamu akan baik-baik saja?"

    liu f_happy "Y-ya, aku akan baik-baik saja."

    show anon a_sides f_shy
    with {'master': dissolve}
    liu f_sexy "Fiuh, panas sekali, {b}[firstname]{/b}..."

    liu "... Aku masih kesemutan."

    anon "Hehe."

    show anon b_empty f_surprised:
        xoffset 175
    show liu b_dressed_disheveled_hug_surprised behind anon:
        xoffset 175
    with dissolve
    pause .4
    show anon b_empty f_happy_closed
    show liu b_dressed_disheveled_hug
    with dissolve
    pause
    liu "Anda mungkin harus pergi dulu, agar tidak ada yang curiga."

    anon @ f_normal_closed "Baiklah."

    pause
    liu "Sampai jumpa nanti?"

    anon f_normal_low "Tentu saja."

    show anon b_dressed f_normal behind liu
    show liu a_close_blouse b_dressed_disheveled f_nervous_down:
        xoffset -75
    with dissolve
    pause
    show anon a_wave:
        xoffset 200
    show liu f_nervous o_blush:
        align (0, 0)
        crop (0, 0, 1024, 353)
    show liu a_sides b_dressed as body behind anon:
        align (0, 1.)
        crop (0, 353, 1024, 415)
        xoffset -75
    with {'master': dissolve}
    anon "Semoga harimu menyenangkan, {b}Liu{/b}."

    liu f_happy "Saya pasti akan melakukannya."

    hide anon
    show liu f_happy_closed
    show liu a_cover as body
    with dissolve
    pause
    return 'afterglow'


label liu_button_lobby.suggest:
    anon f_flirt "Punya sedikit waktu untuk \"bersenang-senang\"?"


    if M_tina.where in L_bank.get_all_children_inclusive():
        jump liu_button_lobby.boss

    if game.timer.is_dow(1) and game.timer.is_morning():
        jump liu_button_lobby.sex

    show liu f_worried o_blush with {'master': dissolve}
    liu "Ssst, {b}[firstname]{/b}!!!"

    show anon f_normal
    show liu a_hold_arm
    with {'master': dissolve}
    liu "Kita tidak bisa melakukan itu sekarang!"

    anon f_confused "Kenapa?"

    show liu -o_blush
    with {'master': dissolve}
    liu "Lihatlah ke sekeliling, ada orang di mana-mana, bahkan satpam pun mengawasi!"

    show anon a_surprised f_surprised_left
    with {'master': dissolve}
    liu f_ashamed_down "Saya satu-satunya teller yang bertugas saat ini, jadi saya akan dirindukan."

    show anon a_sides f_confused_back
    with {'master': dissolve}
    anon @ -m_talk "( Kapan saya melihat penjaga yang mengantuk itu bertugas? {b}Selasa pagi{/b}? )"

    show anon f_worried
    liu f_worried "Maaf, {b}[firstname]{/b}."

    anon f_shy "Jangan khawatir."

    show liu a_sides f_nervous
    with {'master': dissolve}
    anon "Saya mengerti."

    liu "Mungkin jika kita tidak terlalu sibuk aku bisa-"

    show anon a_wave f_normal with {'master': dissolve}
    anon f_normal "Tidak apa-apa, {b}Liu{/b}. Aku bisa menghubungimu nanti."

    show anon a_sides with {'master': dissolve}
    liu f_happy "Benar-benar?!"

    liu f_sexy "Aku pasti akan menebusnya padamu."

    anon f_normal "Kedengarannya bagus."

    jump liu_button_lobby.choice


label liu_button_lobby.threesome:
    anon f_thinking "Mungkin dia bisa bergabung?"

    show liu a_mouth_cover f_surprised with {'master': dissolve}
    liu "Ya ampun, bisakah kamu bayangkan?!"

    pause
    show anon f_normal
    show liu a_hold_arm f_nervous o_blush
    with {'master': dissolve}
    liu "Saya yakin dia seperti pemakan pria di balik pintu tertutup!"

    show liu f_nervous_lipbite_back
    anon f_happy "Y-ya, mungkin..."

    show liu f_nervous_lipbite
    anon f_normal "... Kamu ingin mencari tahu?"

    show liu a_sides f_happy with {'master': dissolve}
    liu "Heh, berhenti menggodaku!"

    show liu f_nervous -o_blush
    with {'master': dissolve}
    liu "{b}Tina{/b} bukan tipe cewek seperti itu."

    anon "Jika Anda berkata demikian."

    jump liu_button_lobby.choice


label liu_button_lobby.tina:
    anon f_normal "Apakah Tina ada?"

    if game.timer.is_weekend():
        liu f_worried "Maaf, tidak. Dia hanya bekerja pada {b}hari kerja{/b}."

    else:
        liu f_worried "Maaf, tidak. Dia tidak akan masuk sampai nanti {b}sore ini{/b}."

    show anon f_worried
    liu f_curious "Apakah ada yang bisa saya bantu?"

    anon "Tidak, tidak, tidak apa-apa."

    liu f_normal "Baiklah, apakah ada hal lain yang bisa saya lakukan untuk Anda hari ini?"

    anon @ f_thinking "Hmm..."

    jump liu_button_lobby.choice


label liu_button_lobby.upbeat:
    anon "Bagaimana kabarmu?"

    liu f_happy "Saya luar biasa!"

    show anon f_brag
    liu "Setiap hari terasa lebih cerah sekarang karena {b}Kim{/b} telah tiada dan kamu ada dalam hidupku."

    liu "Aku akan melakukan apa saja untuk membuatmu bahagia seperti kamu telah membuatku bahagia, {b}[firstname]{/b}!"


    menu:
        "Apa pun?":
            jump liu_button_lobby.anything
        "Senyummu sudah cukup.":

            pass

    anon f_happy "Melihat senyum indahmu saja sudah membuatku bahagia, {b}Liu{/b}."

    anon "Anda adalah orang yang luar biasa dan Anda pantas mendapatkan kebahagiaan."

    liu f_nervous "Aduh, {b}[firstname]{/b}... Kamu terlalu baik padaku."

    show liu f_nervous_back
    pause
    liu f_nervous "Mendekatlah."

    show anon f_confused_low
    show liu b_dressed_lean_whisper f_sexy
    with dissolve
    pause
    show anon b_spook f_confused:
        xoffset 150
    with dissolve
    liu "Mengapa kamu tidak datang ke apartemenku malam ini?"

    anon f_surprised "Oh?"

    liu "Aku akan melakukan lebih dari sekedar tersenyum untukmu..."

    anon f_flirt "{i}*Gulp*{/i} Y-ya, oke."

    show anon f_shy_high
    show liu a_mouth_cover b_dressed f_laugh
    with {'master': dissolve}
    liu "hehe!"

    show anon a_sides b_dressed f_shy:
        xoffset 0
    show liu a_idle f_happy
    with dissolve
    jump liu_button_lobby.choice


label liu_button_lobby.unsure:
    anon f_shy "Bagaimana kabarmu?"

    show liu a_point_self f_surprised o_blush with {'master': dissolve}
    liu "A-aku?"

    anon f_normal "Ya."

    anon "Harimu menyenangkan?"

    show liu a_cover f_nervous_back with {'master': dissolve}
    liu "Ya ampun... aku uhh..."

    liu "... Y-ya, menurutku begitu."

    anon f_confused "Anda tidak yakin?"

    liu f_nervous "T-tidak, benar, hanya saja..."

    liu "... Aku tidak terlalu terbiasa dengan orang-orang yang bertanya tentang hariku."

    anon f_surprised "Tidak?"

    pause
    anon f_confused "Bahkan bukan suamimu?"

    show liu a_sides f_ashamed_down -o_blush with {'master': dissolve}
    liu "Tentu saja tidak."

    liu "{b}Kim{/b} tidak pernah suka berbasa-basi."

    anon f_thinking_down "Hmm, begitu."

    anon a_thinking @ -m_talk "(Saya kira itu tidak mengejutkan.)"

    show anon a_sides f_worried
    with {'master': dissolve}
    anon @ -m_talk "(Gadis ini benar-benar pantas mendapatkan yang lebih baik.)"

    jump liu_button_lobby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

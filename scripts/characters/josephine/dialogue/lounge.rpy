label josie_button_lounge:
    show josephine a_phone f_normal_down
    show anon f_shy_low with dissolve
    anon "Hei, apa yang terjadi?"

    josephine f_angry_down "Ssst!"

    anon f_surprised_low "{b}Yosephine{/b}?"

    josephine "Diam, aku sedang menonton streamer favoritku!"

    anon f_worried_low "Oh, umm... Oke?"

    show josephine f_normal_down

    label josie_button_lounge.choice:
    menu:
        "Foto pribadi." if M_anon.is_state(S_ano07_perk):
            jump ano07_hint_josie
        "Siapa streamer favoritmu?":

            jump josie_button_lounge.stream
        "Kamu ingin bermesraan?":

            if M_anon.finished_state(S_ano09_blow):
                jump josie_button_lounge.invite
            jump josie_button_lounge.flirt

        "Seks oral?" if M_anon.finished_state(S_ano09_blow):
            jump josie_button_lounge.blowjob

        "Seks?" if M_josie.finished_state(S_jos02_init):
            jump josie_button_lounge.sex
        "Sampai jumpa.":

            pass

    anon f_shy_low "Sampai jumpa."

    josephine @ -m_talk "..."
    show anon f_worried_low
    pause
    anon f_unimpressed @ a_wave "Saya mengucapkan, selamat tinggal {b}Josephine{/b}!"

    josephine f_angry_down "Bung, streaming."

    josephine "Ssst."

    show josephine f_normal_down
    anon "Ugh."

    hide anon with dissolve
    return


label josie_button_lounge.blowjob:
    anon f_flirt_low "Tidakkah Anda merasa sedang ingin memberi?"

    josephine a_phone f_normal_down "Jangan sekarang, {b}[firstname]{/b}."

    josephine "Aku sedang menonton streamingku."

    anon f_worried_low "Ayolah, ini akan lebih menyenangkan daripada aliran seni bodoh."

    josephine @ f_eyeroll "Pfft, bagimu mungkin..."

    josephine "Coba lagi nanti."

    anon f_sad_down "Uh, baiklah."

    return


label josie_button_lounge.flirt:
    anon f_flirt_low "Kamu ingin bermesraan?"

    josephine f_angry_down "Apakah kamu gila?!"

    josephine "Saatnya streaming, pergilah!"

    anon f_unimpressed_low "Baiklah, sialan."

    show josephine f_normal_down
    jump josie_button_lounge.choice


label josie_button_lounge.invite:
    anon f_flirt_low "Kamu ingin bermesraan?"

    josephine "Siapa kamu, dua belas tahun?"

    show anon f_confused_low
    pause
    josephine "Saatnya streaming, pergilah!"

    anon f_unimpressed_low "Baiklah, sialan."

    jump josie_button_lounge.choice


label josie_button_lounge.sex:
    anon f_shy_low "Ingin berhubungan seks?"

    josephine f_concerned @ -m_talk "Hmm?"

    josephine "Kawan, waktunya streaming!"

    josephine f_normal_down "Silakan duduk dan menonton bersama saya."

    show anon f_worried_low

    if not M_josie.once('sex_chair'):
        jump chat_josie_sex_chair

    menu:
        "Celana lepas?":
            jump chat_josie_sex_chair.repeat
        "Bawa itu.":

            pass

    show anon a_point f_flirt_low
    with {'master': dissolve}
    anon "Atau Anda bisa membawanya saja?"

    pause
    show josephine f_annoyed
    pause
    show anon a_sides f_grin_low
    with {'master': dissolve}
    pause
    josephine f_eyeroll "Uh, baiklah."

    show josephine a_undress1 f_normal_down
    show anon b_flour f_looking_down behind josephine:
        offset (-100, 110)
    with dissolve
    pause
    show anon b_shirt od_dick4 f_flirt a_sides:
        yoffset 0
    show josephine b_undershirt a_undress2 f_normal_down:
        offset (-370, 0)
    with slowdissolve
    pause
    show josephine a_idle with dissolve
    pause
    show anon f_flirt_low
    show josephine b_topless
    with dissolve
    pause
    show josephine b_topless_undress5 with dissolve
    pause
    show anon f_surprised_down
    show josephine b_topless_undress6
    with dissolve
    pause
    show anon f_flirt
    show josephine b_naked a_phone f_normal_down
    with dissolve
    pause
    anon f_worried @ -m_talk "..."
    anon "Apakah kamu akan naik ke meja atau-"

    josephine f_concerned @ -m_talk "Hmm?"

    josephine f_normal @ f_eyeroll "Oh benar."

    josephine "Maaf."

    hide josephine with dissolve
    show anon f_worried:
        flip
        xoffset -600
    with {'master': dissolve}
    josephine "Siap saat Anda siap, potong mangkuk."

    anon f_unimpressed "Berhenti memanggilku seperti itu!!"

    hide anon with {'master': dissolve}
    josephine "hehe!"


    call scene_josie_sex.afternoon
    $ unlock_scene('josie', '02_unlocked', variant='afternoon')

    scene expression background(496, 384, 2.75) as stage
    show anon b_flour f_looking_down:
        flip
        yoffset 110
    show josephine b_naked a_phone f_normal_down:
        flip
        xoffset 150
    with fade
    josephine @ -m_talk "..."
    show anon b_dressed f_unimpressed with dissolve:
        yoffset 0
    anon "Dan Anda kembali menelepon lagi..."

    josephine f_concerned "Apa, kita sudah selesai, bukan?"

    anon "Ya, saya kira."

    show josephine f_normal_down
    pause
    josephine f_sexy_down @ f_sexy "Permintaan lagu saya akan muncul berikutnya..."

    pause
    anon "Sampai jumpa lagi, {b}Josephine{/b}."

    josephine "Sampai jumpa, {b}[firstname]{/b}."

    hide anon with dissolve
    return 'afterglow'


label josie_button_lounge.stream:
    anon f_shy_low "Siapa streamer favoritmu?"

    josephine @ -m_talk "Hmm?"

    josephine "Oh, dia pria Somalia norak bernama {b}DarkCookie{/b}."

    josephine "Dia membuat game dewasa yang didanai oleh penggemar ini, dan dia mengalirkan dirinya sendiri untuk membuat karya seni untuk game tersebut hampir setiap hari sekitar {b}14.00 EST{/b}."

    anon f_surprised_low "Setiap hari?"

    josephine "Biasanya tidak di akhir pekan."

    josephine "... Atau jika dia sakit."

    josephine @ f_laugh "Artinya, SEPANJANG WAKTU!"

    anon f_skeptical @ -m_talk "..."
    josephine "Sebenarnya agak gila."

    josephine @ f_laugh "Saya pikir Bubble Boy mungkin memiliki sistem kekebalan yang lebih baik daripada dia."

    anon f_shy_low "Dan dia streamer favoritmu?"

    josephine @ -m_talk "Mhmm."

    anon "Mengapa?"

    josephine "Entahlah, aku hanya suka menjebaknya."

    anon "Oh, masalah trolling itu lagi..."

    josephine "Ditambah lagi, obrolannya penuh dengan cowok-cowok haus yang mudah tertipu."

    josephine "Mereka seperti, terus-menerus mengirimiku foto penis..."

    josephine "Saya punya banyak koleksi."

    anon f_surprised_low "Anda punya banyak koleksi foto penis?"

    josephine "Benar sekali."

    anon f_flirt_low "Dan Anda menikmatinya?"

    josephine "Tidak juga."

    show anon f_surprised_teeth_low
    pause 1
    anon f_worried_low "Maaf, saya tidak menerima banding tersebut."

    josephine "Ya, menurutku itu agak sulit untuk dijelaskan..."

    anon f_shy_low "Ya, apa pun yang membuat perahu Anda melayang."

    josephine "Oh lihat, dia sedang melakukan polling!"

    josephine "Saya suka ini."

    pause
    josephine @ f_laugh "Pfft, hahahaah!"

    josephine "Kenapa dia begitu membenci Ratu Inggris?!"

    show anon f_worried_low
    pause
    josephine f_angry_down "Ya Tuhan, jangan {i}Pertarungan Kung Fu{/i} lagi..."

    josephine "Aku muak dengan lagu ini!"

    anon "Benar, baiklah... Selamat menikmati."

    josephine "Tolong, lewati saja!"

    show josephine f_normal_down
    jump josie_button_lounge.choice


label chat_josie_sex_chair:
    anon "... Apakah kamu tidak pernah bosan dengan hal itu?"

    josephine f_confused "Um, bukan?"

    pause
    show josephine a_phone_show f_sexy
    with {'master': dissolve}
    josephine "Lihat, dia menggambar boobies hari ini."

    show anon a_surprised f_surprised_low
    with {'master': dissolve}
    anon "Astaga!!"

    anon "Apakah gadis itu hamil?"

    show anon a_sides
    with {'master': dissolve}
    josephine @ f_laugh "Hehe, ya."

    anon f_disgusted_low "Sepertinya dia menelan kursi bean bag!"

    josephine "Saya pikir itu seharusnya dilebih-lebihkan untuk efek komedi..."

    anon f_worried_low "Ya ampun, kuharap begitu."

    show josephine a_phone f_sexy_down
    with {'master': dissolve}
    josephine "... Atau mungkin dia sedang mengerami seekor walrus di sana?"

    josephine "Sejujurnya, dengan dia... bisa jadi salah satunya."

    anon "eh."

    show anon f_disgusted_low
    josephine f_sexy "Lihat, ini sangat menghibur!"

    josephine "Ayo duduk."

    show anon a_thinking f_thinking
    show josephine f_sexy_down
    with {'master': dissolve}
    anon @ -m_talk "Hmm?"

    show anon a_point f_confused_low
    with {'master': dissolve}
    anon "Bisakah kita menontonnya tanpa celana?"

    show josephine f_annoyed
    pause
    show anon a_sides f_happy_low
    with {'master': dissolve}
    anon "Maksudku, aku akan menontonnya sepenuhnya... jika kita bisa..."

    anon "... Kamu tahu."

    pause
    show anon f_grin_low
    with {'master': fastdissolve}
    pause
    josephine f_eyeroll "{i}*Huh*{/i} Baiklah, baiklah."

    josephine f_bored_down "Geser saja celana dalamku ke bawah."

    anon f_happy_low "Manis!"

    jump chat_josie_sex_chair.tail


label chat_josie_sex_chair.repeat:
    show anon a_sides f_confused_low
    with {'master': dissolve}
    anon "Bisakah kita menontonnya tanpa celana?"

    show josephine f_annoyed
    josephine "Aku tahu kamu akan mengatakan itu..."

    pause
    show anon f_grin_low
    with {'master': fastdissolve}
    pause
    josephine "{i}*Huh*{/i} Baiklah, baiklah."

    josephine "Geser saja celana dalamku ke bawah."

    anon f_happy_low "Manis!"

    jump chat_josie_sex_chair.tail


label chat_josie_sex_chair.tail:
    call scene_josie_sex_chair.repeat
    $ unlock_scene('josie', '03_unlocked')
    $ renpy.dynamic(where=_return)

    call josie_button_stage
    show josephine a_phone f_normal_down
    show anon b_shirt_undress_bottom
    with fade
    pause
    show anon a_remove_shorts b_dressed f_shy_down
    with {'master': dissolve}
    anon "Jadi uhh..."

    show anon a_sides b_dressed f_normal_low
    with {'master': dissolve}

    if where == 'outside':
        anon "... Kamu sadar ada air mani di seluruh punggungmu, ya?"

    else:
        anon "... Itu menyenangkan!"


    josephine @ -m_talk "Mhmm."

    show anon f_confused_low
    pause
    anon "Anda bahkan tidak mendengarkan saya sekarang, bukan?"

    josephine @ -m_talk "Mhmm."

    show anon f_worried_low
    pause
    anon "Benar."

    show anon f_unimpressed_low
    pause
    show anon a_wave
    with {'master': dissolve}
    anon "Baiklah, sampai jumpa lagi... kurasa."

    josephine @ -m_talk "Mhmm."

    hide anon
    with {'master': dissolve}
    pause
    josephine f_sexy_down "Ya Tuhan, dia menggambar kotoran lagi!"

    show josephine a_phone_show f_sexy
    with {'master': dissolve}
    josephine "Anda harus memeriksa ini-"

    show josephine f_confused
    pause
    show josephine a_phone
    with {'master': dissolve}
    josephine "{b}[firstname]{/b}?!"

    return 'afterglow'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

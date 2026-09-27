label josie_button_sex:
    if game.timer.is_day():
        jump josie_button_sex.morning

    jump josie_button_sex.evening
    return


label josie_button_sex.morning:
    scene expression background(496, 384, 2.75) as stage
    show josephine b_naked a_phone f_normal_down:
        flip
        xoffset 150
    show anon with dissolve:
        flip
    josephine @ -m_talk "..."
    anon "Wah, kamu nongkrong di sini sambil telanjang ya?"

    josephine f_sexy "Heh, diam dan lepaskan celana itu."

    anon "Baiklah."

    show anon b_flour f_looking_down with dissolve:
        yoffset 110
    pause
    show anon b_shirt od_dick4 f_normal with dissolve:
        yoffset 0
    josephine f_sexy_down "Kau tahu, aku mulai berpikir pekerjaan ini tidak terlalu buruk..."

    anon "Hehe, benarkah?"

    hide josephine with dissolve
    josephine "Siap saat Anda siap, potong mangkuk."

    anon f_unimpressed "Berhenti memanggilku seperti itu!!"

    hide anon with {'master': dissolve}
    josephine "hehe!"


    call scene_josie_sex.morning
    $ unlock_scene('josie', '02_unlocked', variant='morning')

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
    josephine f_sexy "Aku bilang pada mereka aku baru saja berhubungan seks di ruang istirahat di tempat kerja..."

    anon f_surprised "Benar-benar?"

    josephine "Hehe, ya."

    josephine "Mereka sangat cemburu saat ini."

    show anon f_normal
    pause
    anon "Sampai jumpa lagi, {b}Josephine{/b}."

    josephine "Sampai jumpa, {b}[firstname]{/b}."

    hide anon with dissolve
    return 'afterglow'


label josie_button_sex.evening:
    scene josephine b_chair f_sexy
    anon "!!!"
    josephine "Lihat sesuatu yang kamu suka?"

    anon "Wah, kamu seksi!"

    josephine @ f_laugh "hehe!"

    josephine "Tidak terlalu khawatir sekarang, ya?"

    anon "..."
    josephine "Ayo, aku ingin mengantarmu ke meja ayahku..."

    anon "O-oke."


    call scene_josie_sex_desk.repeat
    $ unlock_scene('josie', '04_unlocked')

    if _return == 'inside':
        jump josie_button_sex.inside
    if _return == 'outside':
        jump josie_button_sex.outside

    scene expression background(712, 400, 3.) as stage
    show anon b_flour f_looking_down:
        flip
        offset (-50, 110)
    show josephine b_naked f_sexy:
        flip
        xoffset 150
    with fade
    josephine @ -m_talk "..."
    show anon b_dressed f_worried with dissolve:
        yoffset 0
    anon "Dimana ponselmu?"

    josephine @ -m_talk "Hmm?"

    josephine "Ah, aku tidak tahu..."

    josephine @ f_eyeroll "... Siapa yang peduli?"

    pause
    anon @ f_confused "Apakah kamu merasa baik-baik saja?"

    josephine "Mmm, aku merasa luar biasa."

    josephine "Kita harus melakukan ini lebih sering..."

    anon f_normal "Heh, aku akan kecewa karenanya."

    show josephine b_naked_kiss:
        xoffset 200
    hide anon
    with dissolve
    pause
    show josephine b_naked:
        xoffset 150
    show anon b_dressed:
        flip
        xoffset -50
    with dissolve
    josephine "Kalau begitu, itu kencan."

    anon "Hehe."

    hide anon with dissolve
    return 'afterglow'


label josie_button_sex.inside:
    scene expression background(712, 400, 3.) as stage
    show anon b_flour f_looking_down:
        flip
        offset (-50, 110)
    show josephine a_phone b_naked f_angry_down:
        flip
        xoffset 150
    with fade
    josephine "Cih, bajingan itu!"

    show anon a_sides b_dressed f_worried:
        yoffset 0
    with {'master': dissolve}
    anon "Uh oh, bagaimana sekarang?"

    josephine "Saya baru saja diberitahu bahwa mereka menaikkan diskon karyawan menjadi lima belas persen!"

    anon f_confused "Cukup bagus, bukan?"

    josephine f_annoyed "Sangat bagus."

    pause
    josephine "Sayang sekali aku tidak bekerja di sana lagi!"

    show anon f_worried
    show josephine f_angry_down
    pause
    show anon a_shy_neck f_worried_back_low
    with {'master': dissolve}
    anon "Ya, itu memalukan."

    pause
    show anon f_worried
    show josephine f_bored_down
    with {'master': dissolve}
    pause
    show anon a_sides
    with {'master': dissolve}
    anon "Bagaimanapun, aku akan menemuimu nanti..."

    show anon a_wave f_shy
    with {'master': dissolve}
    anon "... Sampai jumpa!"

    josephine "Ya, ya."

    hide anon with dissolve
    josephine f_eyeroll "{i}*Huh*{/i} Dealer mobil bodoh dengan ayahku yang bodoh."

    return 'afterglow'


label josie_button_sex.outside:
    scene expression background(712, 400, 3.) as stage
    show anon b_flour f_looking_down:
        offset (-50, 110)
        xzoom -1
    show josephine a_hips b_naked f_angry_down:
        xoffset -450
    with fade
    josephine "Kemana perginya ponselku?"

    show anon a_sides b_dressed f_confused:
        yoffset 0
    with {'master': dissolve}
    anon "Apa maksudmu?"

    show anon f_worried
    show josephine a_sides f_confused:
        xoffset 150
        xzoom -1
    with {'master': dissolve}
    josephine "Menurutmu apa maksudku?!"

    show josephine a_gimme f_annoyed
    with {'master': dissolve}
    josephine "Itu benar-benar lenyap!"

    show anon f_confused
    show josephine a_sides
    with {'master': dissolve}
    anon "Bagaimana kamu bisa kehilangannya?"

    josephine f_eyeroll "Oh, entahlah..."

    josephine f_annoyed "... Itu mungkin ada hubungannya dengan kamu yang tanpa basa-basi membuangku dari penismu seperti aku adalah boneka kain sialan!"

    show anon a_behind_head f_shy
    with {'master': dissolve}
    anon "Heh, aku memang melakukan itu, bukan?"

    show josephine a_crossed f_angry
    with {'master': dissolve}
    pause
    show anon a_sides f_worried
    with {'master': dissolve}
    anon "Yah, aku minta maaf..."

    show josephine f_eyeroll
    anon f_shy "... Ketelnya hampir mendidih dan saya harus berpikir cepat!"

    show anon f_shy_low
    hide josephine
    with {'master': dissolve}
    josephine "Apa benda itu terguling di bawah rak buku atau semacamnya?!"

    anon f_confused_low "Mungkin?"

    pause
    josephine "Tidak, itu juga tidak ada."

    show anon f_surprised:
        xoffset -500
    with {'master': dissolve}
    anon "Ya ampun, apakah ini waktunya?!"

    show anon:
        xoffset 0
        xzoom 1
    with {'master': dissolve}
    anon f_worried_low "Kau tahu, aku sangat ingin tinggal dan membantumu melihat, tapi sekarang sudah sangat larut..."

    show anon f_worried
    show josephine a_hips b_naked f_angry_down:
        xoffset 500
        xzoom -1
    with {'master': dissolve}
    anon "... Dan aku tidak ingin induk semangku mulai khawatir, jadi..."

    show anon f_surprised:
        xoffset -100
    show josephine a_frustrated
    with {'master': dissolve}
    josephine @ f_angry_closed "Grr, itu tidak ada dimanapun!!"

    pause
    show anon a_wave f_shy
    show josephine a_sides
    with {'master': dissolve}
    anon "... Oke, sampai jumpa!"

    hide anon with dissolve
    show josephine a_hips f_pouting
    with {'master': dissolve}
    josephine "Aku harus menghentikannya!"

    return 'afterglow'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

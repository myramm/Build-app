label nadya_button_office:
    show anon b_sit with {'master': dissolve}:
        xoffset -250
    anon "Yah, kamu terlihat nyaman."

    nadya "Ya."

    show nadya b_dressed_couch_relax with {'master': dissolve}
    nadya "Anda dapat mengatakan banyak hal buruk tentang ayah saya tetapi sulit untuk disangkal, dia memiliki selera yang bagus."

    pause
    nadya "Ayo, duduklah lebih dekat jika Anda mau...."

    nadya "... Saya tidak menggigit."

    show anon f_happy

    menu nadya_button_office.choice:
        "Jadi bagaimana rasanya menjadi penanggung jawab?":
            jump nadya_button_office.boss
        "Dimana {b}Katya{/b}?":

            jump nadya_button_office.katya
        "Seks":

            jump nadya_button_office.sex
        "Saya tidak bisa tinggal.":

            pass

    anon f_shy "Aku tidak bisa tinggal, {b}Nadya{/b}."

    show nadya b_dressed_couch f_pouting with {'master': dissolve}
    nadya "Tidak?"

    nadya "Ya, itu sangat disayangkan."

    nadya f_sexy "Saya menantikan saat-saat seksi dengan ayam cantik Anda."

    anon "Maaf."

    show anon a_shy_neck f_shy with {'master': dissolve}
    anon "Mungkin lain kali?"

    nadya f_normal "Ya, ya... Lain kali."

    show anon a_idle
    with {'master': dissolve}
    nadya "{b}Katya{/b} akan melayani saya sebagai gantinya."

    anon f_normal "Baiklah, baiklah... Selamat malam, {b}Nadya{/b}."

    nadya "Farewell, {b}[firstname]{/b}." (show_native="Do svidaniya, {b}[firstname]{/b}.")
    return


label nadya_button_office.blowjob:
    anon f_shy "Mulutmu terasa sangat enak terakhir kali..."

    nadya f_confused "Anda ingin membuat saat-saat seksi di mulut saya?"

    show anon f_shy_low
    pause
    nadya f_normal "Baiklah..."

    show anon f_shy
    nadya "... Tapi saya harap Anda berencana membalas budi suatu hari nanti!"

    anon f_flirt "Itu mungkin bisa diatur."

    pause
    nadya f_sexy "Datang."

    show anon a_idle b_sit_naked_up f_shy_low od_naked_dick3:
        xoffset 0
    with dissolve
    pause

    call scene_nadya_blowjob.repeat
    $ unlock_scene('nadya', '01_unlocked')

    call nadya_button_stage
    show nadya b_naked_couch a_cig_smoking
    show anon b_sit_back_remove_shorts2 f_worried_down od_dick1:
        xoffset -250
    with fade
    pause
    show anon a_remove_shorts1 b_sit
    show nadya a_down_cig f_pouting o_smoke
    with dissolve
    pause
    show anon a_idle b_sit f_worried
    show nadya f_normal -o_smoke
    with {'master': dissolve}
    nadya "Di sana."

    nadya "Rokok terasa lebih enak."

    anon f_confused "Anda harus benar-benar berhenti merokok, tahu?"

    nadya f_frowning "Bah!"

    anon f_worried "Serius, itu buruk bagimu."

    show anon f_surprised
    nadya @ f_eyeroll "\"Serius, ini buruk bagimu.\""

    show anon f_unimpressed
    nadya "Kalian orang Amerika jadi sangat banci akhir-akhir ini..."

    nadya "... Saya tidak tahu bagaimana Anda memenangkan perang dingin."

    anon @ -m_talk "..."
    nadya "Hindari ceramah konyolmu dan beri tahu {b}Svetlana{/b} untuk mengirim {b}Katya{/b}."

    show anon f_tired
    nadya f_normal "Dia akan menghabisiku."

    anon f_sad_down "Y-ya, oke."

    nadya f_happy "Anak baik."

    hide anon
    show nadya a_cig_smoking
    with dissolve
    pause
    show nadya a_down_cig f_pouting o_smoke with dissolve
    pause
    show nadya f_happy -o_smoke with dissolve
    pause

    call svetlana_button_stage
    show svetlana a_crossed f_concerned:
        xoffset 150
        xzoom -1
    with fade
    show anon a_sides with dissolve:
        xoffset 100
        xzoom -1
    svetlana "Berakhir begitu cepat?"

    anon f_worried "Ya, um..."

    show anon a_point_back
    with {'master': dissolve}
    anon "... Dia meminta {b}Katya{/b}."

    show svetlana a_sides f_smirk with {'master': dissolve}
    svetlana "Hehe, itu tidak mengherankan."

    show anon a_sides
    with {'master': dissolve}
    svetlana "{b}Katya{/b} sangat terampil dengan lidah."

    anon f_shy "Ya, itulah yang saya dengar."

    svetlana f_laugh "Hehe, aku akan menjemputnya."

    svetlana f_happy "Selamat menempuh perjalanan pulang."

    anon f_normal "Terima kasih."

    return


label nadya_button_office.bow:
    anon "Bagaimana kalau kamu berbaring miring lagi?"

    nadya f_happy "Ya."

    show anon f_happy
    nadya "Ini posisi yang bagus!"

    nadya "Saya sangat menyukainya."


    call scene_nadya_sex_office.repeat
    $ unlock_scene('nadya', '02_unlocked')

    call nadya_button_stage
    show nadya b_naked_couch
    show anon b_sit_back_remove_shorts2 f_shy_down od_dick1:
        xoffset -250
    with fade
    pause
    show anon a_remove_shorts1 b_sit with {'master': dissolve}
    nadya "Ini adalah saat-saat seksi yang bagus."

    show anon a_idle b_sit f_normal with {'master': dissolve}
    anon "Ya, benar."

    nadya f_sexy "Anda segera kembali, kami melakukan lebih banyak."

    anon f_flirt "Sangat."

    nadya f_normal "Farewell, {b}[firstname]{/b}." (show_native="Do svidaniya, {b}[firstname]{/b}.")
    anon f_normal "Selamat tinggal, {b}Nadya{/b}."

    hide anon with dissolve

    call svetlana_button_stage
    show svetlana f_smirk:
        xoffset 150
        xzoom -1
    with fade
    show anon a_sides with dissolve:
        xoffset 100
        xzoom -1
    svetlana "Sepertinya Anda berhasil menyenangkannya sekali lagi."

    anon f_brag "Ya, saya yakin begitu."

    svetlana "Dia mengalami banyak orgasme... Saya dengar."

    show anon a_rub f_worried with {'master': dissolve}
    anon "Oh, benar... ummm... maaf."

    svetlana f_curious @ -m_talk "Hmm?"

    show anon a_sides with {'master': dissolve}
    anon "Saya yakin ini canggung bagi Anda, karena harus mendengarkan kami."

    svetlana f_smirk "No..." (show_native="Nyet...")
    svetlana "... Saya tidak keberatan."

    show anon f_normal
    pause
    svetlana "Sejujurnya, ini menarik."

    show anon a_shy_neck f_shy_left of_blush with {'master': dissolve}
    anon "Oh?"

    show anon f_shy
    svetlana "Mungkin, {b}Nona Chernyshevsky{/b} akan membiarkan saya berjaga dari seberang pintu di masa depan, ya?"

    show anon a_sides with {'master': dissolve}
    anon "Heh, ya... Mungkin."

    show anon f_normal -of_blush
    with dissolve
    pause
    return


label nadya_button_office.boss:
    anon f_normal "Jadi, bagaimana kepemimpinan yang cocok untuk Anda?"

    show nadya a_up f_happy with {'master': dissolve}
    nadya "Luar biasa."

    nadya "Saya melakukan sesuka saya dan semua orang mematuhinya."

    show nadya a_idle
    with {'master': dissolve}
    nadya "Kami akhirnya mendapat untung dan sekarang bisnis kami sah, kami tidak punya masalah lagi dengan polisi."

    anon "Itu bagus untuk didengar."

    nadya "Ya."

    pause
    nadya f_normal "Apakah kamu sudah mengambil keputusan?"

    anon f_confused @ -m_talk "Hmm?"

    nadya "Tawaran saya..."

    nadya "... Untuk pekerjaan."

    anon f_shy "Oh, umm... Tidak, maaf."

    anon "Saya perlu waktu lagi."

    nadya f_frowning "{i}*Huh*{/i} Baiklah."

    pause
    nadya f_sexy "Hehe."

    anon f_confused "Apa?"

    show nadya a_up f_bored with {'master': dissolve}
    nadya "Sepanjang hari, itu adalah, \"Ya, bos.\" atau \"Segera bos!\""

    show nadya a_idle
    with {'master': dissolve}
    nadya f_pouting "Kamu satu-satunya orang yang memberitahuku bahwa aku harus menunggu..."

    anon "Oh?"

    nadya f_sexy "Itu menggairahkan saya."

    anon f_flirt "{i}*Gulp*{/i} Begitu."

    jump nadya_button_office.choice


label nadya_button_office.katya:
    anon f_normal "Tahukah kamu dimana {b}Katya{/b} berada?"

    nadya f_normal "Aku memberinya libur malam."

    nadya "Untuk melakukan apa yang dia mau."

    nadya "Dia telah terbukti menjadi penasihat bisnis yang sangat baik dan saya akan membuatnya bahagia."

    anon f_confused "Oh?"

    nadya "Pria Amerika tampaknya sangat... rentan terhadap pesonanya."

    show nadya a_up f_happy
    with {'master': dissolve}
    nadya "Mereka berusaha sekuat tenaga untuk menyenangkannya."

    anon f_shy "Y-ya, aku bisa melihatnya."

    show nadya a_idle with dissolve
    jump nadya_button_office.choice


label nadya_button_office.sex:
    anon f_shy "Mungkin Anda ingin-"

    nadya f_sexy "Aku selalu mendambakan saat-saat seksi bersamamu, {b}[firstname]{/b}."

    pause
    show nadya b_dressed_couch with {'master': dissolve}
    nadya "Mari kita singkirkan pakaian, ya?"

    show nadya a_undress1 f_sexy_down with {'master': dissolve}
    anon "Ide bagus."

    show anon f_shy_low
    show nadya b_dressed_couch_undress2
    with dissolve
    pause
    show anon a_surprised f_surprised_high behind nadya
    show nadya b_dressed_couch_undress3
    with dissolve
    pause
    show anon f_surprised_down o_sit_boner
    show nadya a_undress4 b_naked_couch behind anon
    with dissolve
    pause
    show anon a_idle f_flirt_low
    show nadya a_undress5
    with dissolve
    pause
    show nadya a_undress6 f_happy_back with dissolve
    pause
    show nadya a_idle f_happy with dissolve
    pause
    nadya "Di sana."

    show anon f_flirt
    nadya "Anda suka menonton, ya?"

    anon "{i}*Gulp*{/i} Y-ya, benar."

    show anon f_flirt_low
    show nadya f_sexy_down
    pause
    nadya f_sexy "Sekarang giliranmu."

    anon f_confused @ -m_talk "Hmm?"

    nadya f_bored @ -m_talk "..."
    show anon a_behind_head f_shy of_blush with {'master': dissolve}
    anon "Oh benar."

    anon "Maaf."

    show nadya f_sexy_down
    show anon a_remove_shorts1 f_shy_down
    with dissolve
    pause
    show anon b_sit_back_remove_shorts2 -o_sit_boner od_dick_spring with {'master': dissolve}
    nadya f_laugh "hehe!"

    show anon b_sit_naked_remove_shirt od_dick2
    with {'master': dissolve}
    nadya f_sexy_down @ -m_talk "MM."

    show anon a_idle b_sit_naked f_flirt with {'master': dissolve}
    nadya f_sexy "Saya juga suka menonton."

    nadya "Kamu pria yang sangat cantik, {b}[firstname]{/b}."

    show anon a_shy_neck f_shy_left with {'master': dissolve}
    anon @ -m_talk "..."
    nadya f_laugh "hehe!"

    show anon f_shy
    pause
    show anon a_idle with {'master': dissolve}
    nadya f_sexy "Jadi..."

    nadya "... Apa yang kita lakukan sekarang?"


    menu:
        "Seks oral.":
            call nadya_button_office.blowjob
        "Seks.":

            call nadya_button_office.bow

    show svetlana a_wave with {'master': dissolve}
    svetlana "Farewell, {b}[firstname]{/b}." (show_native="Do svidaniya, {b}[firstname]{/b}.")
    show anon a_wave with {'master': dissolve}
    anon "Selamat tinggal, {b}Svet{/b}."

    show svetlana a_sides
    hide anon
    with dissolve
    return 'afterglow'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

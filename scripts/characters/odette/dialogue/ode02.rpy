label ode02_init_odette:
    odette f_smirk "Kamu tidak akan takut padaku, kan?"

    anon f_worried "{i}*Meneguk*{/i} T-tidak."

    anon "Aku hanya memastikan kamu masih ingin melakukannya..."

    odette "Tentu saja."

    show anon f_hurt
    pause
    odette @ f_laugh "Heh, jangan khawatir {b}[firstname]{/b}... Pasti menyenangkan."

    show anon f_worried
    odette "{b}temui aku di sana saat bulan purnama berikutnya{/b}, oke?"


    $ renpy.dynamic(ttl=game.timer.days_until_lunar(.5))
    $ renpy.dynamic(day=game.timer.dayOfWeek(delta=ttl, full=True))

    if game.timer.is_fullmoon():
        odette @ f_wink "Maksudku malam ini!"

        anon f_surprised "Y-ya, oke..."

    elif ttl > 21:
        odette @ f_sad "Yang terakhir baru saja berakhir, jadi akan memakan waktu beberapa minggu."

        anon "Oh baiklah."

    elif ttl > 14:
        odette @ f_pouting "Yang terakhir baru terjadi sekitar seminggu yang lalu, jadi yang berikutnya belum akan terjadi dalam beberapa minggu."

        anon "Ya baiklah."

    elif ttl > 7:
        odette @ f_shy "Yang berikutnya tinggal seminggu lagi, saya sangat bersemangat!"

        anon "Secepat itu?"

        odette @ f_laugh "Khawatir, kawan?"

    elif ttl > 1:
        odette "Yang berikutnya ada di [day], saya harap Anda siap!"

        anon f_shy "Apakah saya punya pilihan?"

        odette @ f_laugh "Hehe, tidak!"

    else:
        odette @ f_wink "Oh, dan {i}peringatan spoiler{/i}: Itu besok!"

        anon f_surprised @ -m_talk "{i}*Meneguk*{/i}"


    show anon f_normal
    return


label ode02_tomb_odette:
    scene odette b_vamp_front f_vamp_tongue
    anon "( !!! )" with hpunch
    anon "{b}Odette{/b}?"

    anon "Apakah itu kamu?"


    scene black with fasteyeshut
    pause .05

    scene odette b_vamp_front_normal with fasteyeopen
    odette "Hei, sobat besar..."

    odette "... Senang sekali Anda akhirnya bergabung dengan saya di tempat tinggal saya yang sederhana."


    scene location_crypt_side
    show odette b_vamp_sitting_cape_normal f_smirk
    show anon f_worried:
        xoffset -150
    with fade
    anon "Tempat tinggalmu yang sederhana?"

    anon "I-ini ruang bawah tanah!"

    odette @ f_laugh "Hehe, luar biasa bukan?"

    anon f_worried_low "aku... Umm-"

    odette "Anda seharusnya sudah melihatnya sebelum saya datang..."

    show anon f_worried
    odette "... Itu mengerikan!"

    anon "Y-ya, ini agak... Tidak wajar, bukan?"

    odette f_happy_up "Tidak sehat?"

    pause
    odette f_smirk @ f_laugh "Apakah kamu mengatakan kamu tidak menyukai rumah baruku?"

    anon a_behind_head "Salah..."

    odette "Anda tidak menganggapnya erotis?"

    anon f_surprised a_sides "Erotis?!"

    odette @ f_happy_up "Semua roh ini dikuburkan di sini..."

    odette "... Bisakah kamu merasakan mereka memperhatikanmu?"

    show anon f_worried a_surprised_up_both with {'master': dissolve}:
        flip
        xoffset -650
    anon "A-mengamatiku?"

    show odette b_vamp_normal f_tired_happy_lipbite with dissolve:
        xoffset -480
    pause
    show anon f_surprised_teeth
    odette f_smirk "Mmm, aku merasa kesemutan di punggungku hanya dengan memikirkannya..."

    show anon a_surprised_shoulders:
        unflip
        xoffset -150
    show odette f_laugh:
        xoffset -200
    with {'master': dissolve}
    anon "!!!"
    show anon f_skeptical a_sides
    with {'master': dissolve}
    odette "Hehehehe!"

    show anon f_worried_low
    pause
    anon "Apa yang kamu kenakan?"

    show odette f_smirk
    anon f_frown_down a_point_down "Dan dimana sepatumu?"

    show anon f_surprised_low a_sides behind odette
    show odette b_vamp_show:
        xoffset -250
    with dissolve
    odette "Apakah kamu menyukainya?"

    odette "Ini kostum Halloweenku dari tahun lalu."

    show odette b_vamp_normal f_smirk:
        xoffset -150
    show anon f_worried
    with dissolve
    odette "Atau, yah... Setidaknya itu jubah dari kostum halloweenku."

    anon "Anda mungkin tidak boleh bertelanjang kaki di sini."

    odette "Sisanya hanya akan menghalangi kita, bukan begitu?"

    anon f_frown_down "Maksudku, kamu akan terkena cacing tambang atau semacamnya..."

    odette @ f_laugh "Hehehe!"

    show anon f_worried
    show odette f_drink a_blood_cup_drink
    with dissolve
    odette "Hmm!"

    anon "A-apa yang kamu minum di sana?"

    show odette f_smirk a_idle with dissolve
    odette "Oh ini?"

    show odette with {'master': dissolve}:
        xoffset -225
    odette "Hanya sedikit anggur merah... Apakah kamu mau?"

    anon "Aku ehh... Tidak, sebaiknya aku tidak melakukannya..."

    odette "Ayolah, aku bersikeras!"

    anon "T-tidak, sungguh itu-"

    show odette a_blood_cup_force
    show anon f_smoke a_up
    with {'master': dissolve}
    anon "!!!"
    pause
    odette "Itu saja."

    odette "Minumlah dalam-dalam, kawan."

    show odette a_idle
    show anon f_worried a_sides
    with dissolve
    anon "Eugh, bagiku itu tidak terasa seperti anggur..."

    odette "Heh, itu perpaduan yang sangat istimewa."

    odette "Saya membuatnya sendiri."

    show odette f_drink a_blood_cup_drink with dissolve
    anon "Benar-benar?"

    show odette a_idle f_smirk with dissolve
    anon "Bukankah itu seharusnya manis?"

    pause
    anon "Karena itu lebih seperti rasa asin..."

    anon "... Rasanya agak manis juga."

    show odette a_blood_cup_force
    show anon f_smoke a_up
    with dissolve
    odette "Ssst."

    anon "!!!"
    odette "Ini akan membuat Anda merasa luar biasa, percayalah."

    pause
    show odette a_idle
    show anon f_disgusted a_sides
    with dissolve
    anon "Eh, kawan..."

    anon "Ini sangat tebal."

    odette @ -m_talk "Mhmm."

    show odette f_drink a_blood_cup_drink behind anon
    show anon a_surprised_hands f_surprised_low
    with dissolve
    pause
    anon "Lenganku terasa aneh."

    show odette a_idle f_smirk o_blood
    with dissolve
    odette "Itu berarti itu berhasil."

    show anon a_surprised_lips f_surprised_down with dissolve
    anon "N mah robekan biaya kebas..."

    odette @ f_laugh "hehe!"

    anon a_sides f_surprised "Apa namamu?"

    odette "Sangat normal, {b}[firstname]{/b}."

    odette a_blood_cup_throw "Jangan khawatir, kepala kecilmu yang cantik."

    show odette a_blood_wipe o_empty with dissolve
    anon @ -m_talk "Hmm."

    show odette a_undress1 with dissolve
    pause
    show odette b_naked a_vamp_undress2
    show anon a_surprised_hands f_surprised_low
    with dissolve
    anon "Ah joo sial?"

    show odette a_idle with dissolve
    anon "Kaz tidak tahu-"

    jump odette_button_crypt.resume
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

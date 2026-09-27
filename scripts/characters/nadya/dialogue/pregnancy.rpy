label nadya_pregnancy_notify:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"


    scene expression game.timer.image('location_warehouse_office_couch{}') as underlay:
        xoffset -671
    show nadya a_phone_talk b_dressed_couch:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        xzoom -1
    anon @ -m_talk "Hmm?"

    show anon a_phone f_normal_low with dissolve
    pause
    show anon a_phone_talk f_normal with dissolve:
        xoffset 500
        xzoom 1
    show expression stage as stage at phoneleft with phoneleft.show
    anon "{b}Nadya{/b}?"

    nadya "Ya, ini aku."

    anon "Wow, menurutku kamu belum pernah meneleponku sebelumnya... Tidak sekali pun."

    anon "Apakah semuanya baik-baik saja?"

    nadya f_happy "Saya punya kabar baik!"

    nadya "Anda sekarang adalah ayah bagi pemimpin masa depan Bratva!"

    anon f_confused "Hah?"

    nadya "Kamu... Apakah papa."

    anon "Apa yang kamu bicarakan?"

    nadya f_eyeroll "Ugh, baiklah... kujelaskan pelan-pelan...."

    nadya f_worried "... Kita sering membuat momen-momen seksi, ya?"

    anon "Ya?"

    nadya "Dan Anda menembakkan cairan seksi Anda jauh di dalam vagina..."

    anon "Eh ya?"

    nadya "... Ini membuat sayang."

    anon f_surprised_teeth @ -m_talk "!!!"
    anon f_shy "J-jadi, kamu hamil?!"

    nadya f_happy "Da, dan kamu adalah papa."

    pause
    nadya f_sexy "Saya mengharapkan pembayaran tunjangan anak sebesar satu juta dolar."

    anon f_surprised "WHAT?!" with hpunch
    nadya "Kamu punya waktu satu bulan atau aku akan membunuh temanmu..."

    nadya "... Mengerti?"

    anon f_worried_surprised "A- Tidak!"

    anon "Aku tidak bisa memikirkan-"

    nadya f_laugh "Hah!!"

    nadya f_happy "Tenang, kawan cantik... itu lelucon!"

    show anon b_dressed_catch_breath
    with {'master': dissolve}
    nadya "Saya tidak butuh uang."

    anon "Hah... hah..."

    show nadya f_confused
    pause
    anon "Ya Tuhan..."

    pause
    show anon b_dressed f_unimpressed with dissolve
    pause
    anon "... Kamu hampir membuatku terkena serangan jantung!"

    nadya f_laugh "Hahahahahaha!"

    nadya f_happy "Anda lupa, saya wanita bisnis yang sah sekarang."

    show anon f_tired
    nadya "Saya menghasilkan uang untuk bayi yang tak terbatas."

    nadya "Tidak masalah."

    anon f_shy "B-benar, ya."

    anon "Fiuh!"

    nadya f_frowning "Tapi ketahuilah ini..."

    nadya "... Kamu akan menjadi ayah yang baik pada anak ini atau aku akan memotong ayam cantikmu!"

    anon "Heh, apakah itu lelucon lain?"

    nadya "No." (show_native="Nyet.")
    show anon f_worried_surprised
    nadya "Kali ini serius."

    show anon f_shock
    nadya "Saya akan memasaknya di tungku gudang dan menaruhnya di roti hotdog..."

    nadya "... Terapkan kenikmatan dan kemudian buat Anda memakannya!"

    show anon f_surprised_down o_boner with {'master': dissolve}
    anon @ -m_talk "..."
    nadya "Memahami?!"

    anon f_worried "{i}*Gulp*{/i} Y-ya?"

    nadya f_happy "Bagus!"

    nadya "Kemudian kita selesai berbicara."

    pause
    nadya "Datanglah ke gudang dan kita akan merayakannya."

    anon "O-oke."

    nadya "Farewell, {b}[firstname]{/b}" (show_native="Do svidaniya, {b}[firstname]{/b}.")
    show nadya a_phone with {'master': dissolve}
    anon "Sampai jumpa, {b}Nadya{/b}."

    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    show anon a_phone f_worried_low with dissolve
    anon @ -m_talk "(Oke, wanita itu menakutkan...)"

    show anon a_pocket f_worried with dissolve:
        xoffset 0
        xzoom -1
    show anon a_surprised f_surprised_down with {'master': fastdissolve}
    anon @ -m_talk "( ... Dan kenapa ini terus terjadi?! )"

    show anon a_sides f_thinking_down with {'master': dissolve}
    anon @ -m_talk "(Saya mungkin harus mencari konseling.)"

    hide anon with dissolve
    return True


label nadya_pregnancy_notify.repeat:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"


    scene expression game.timer.image('location_warehouse_office_couch{}') as underlay:
        xoffset -671
    show nadya a_phone_talk b_dressed_couch:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        xzoom -1
    anon @ -m_talk "Hmm?"

    show anon a_phone f_normal_low with dissolve
    pause
    show anon a_phone_talk f_normal with dissolve:
        xoffset 500
        xzoom 1
    show expression stage as stage at phoneleft with phoneleft.show
    anon "{b}Nadya{/b}?"

    nadya "Ya, ini aku."

    anon f_confused "Apakah semuanya baik-baik saja?"

    nadya "Saya punya kabar baik!"

    nadya f_happy "Kami akan memiliki anak lagi."

    anon f_surprised "Satu lagi?!"

    nadya @ -m_talk "Mhmm."

    anon f_normal "Itu luar biasa!"

    nadya "Datanglah ke gudang dan kita akan merayakannya."

    anon "O-oke."

    nadya "Farewell, {b}[firstname]{/b}" (show_native="Do svidaniya, {b}[firstname]{/b}.")
    anon "Sampai jumpa, {b}Nadya{/b}."

    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    show anon a_phone f_normal_low with dissolve
    anon @ -m_talk "(Saya kira saya akan menjadi seorang papa lagi...)"

    anon f_grin @ -m_talk "(... Sungguh mengasyikkan!)"

    hide anon with dissolve
    return True


label nadya_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_normal with dissolve
    anon "Sepertinya aku mendapat pesan teks."

    hide anon with dissolve
    return


label nadya_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_surprised a_phone with dissolve
    anon "{b}Nadya{/b} punya bayi?!"

    anon "Sialan!"

    pause
    anon "Sebaiknya saya pergi ke {b}klinik{/b} untuk memeriksanya."

    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

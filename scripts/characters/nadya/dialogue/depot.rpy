label nadya_button_depot:
    $ renpy.dynamic(rng=random.random())

    pause .1
    show nadya f_surprised
    show svetlana f_surprised

    if rng < .33:
        show svetlana a_surprised
        "{i}*CRASH*{/i}" with hpunch
        show svetlana a_sides
    elif rng < .66:
        "{i}*Eeeeeeohhmmmm*{/i}" with hpunch
    else:
        "{i}*Glugglugglugglug*{/i}"

        show svetlana a_crossed

    show nadya a_angry f_angry:
        xoffset 675
        xzoom -1
    with {'master': dissolve}

    if rng < .66:
        nadya "Hei, hati-hati!"

    else:
        nadya "Hei, jangan minum barang dagangannya!"


    show svetlana:
        xoffset 450
    with {'master': dissolve}

    if rng < .33:
        nadya "Jika Anda memecahkan vodka, saya memotong gajinya!"

    elif rng < .66:
        nadya "Forklift bukan mainan!"

    else:
        nadya "Ini bukan Rusia!"

        nadya "Bekerja sekarang, minum nanti!"


    svetlana f_eyeroll "What a bunch of idiots... " (show_native="Chto za kucha idiotov...")
    show anon a_wave behind nadya with {'master': dissolve}:
        xoffset -100
    anon "Hai, {b}Nadya{/b}."

    show nadya a_idle f_confused:
        xoffset 100
        xzoom 1
    show svetlana a_sides f_curious:
        xoffset -100
        xzoom 1
    with {'master': dissolve}
    nadya @ -m_talk "Hmm?"

    show svetlana f_happy
    nadya f_normal "Oh, hello, {b}[firstname]{/b}." (show_native="Oh, privet, {b}[firstname]{/b}.")
    show anon a_sides
    with {'master': dissolve}
    nadya "Apa yang membawamu ke gudang?"


    menu nadya_button_depot.choice:
        "Bagaimana bisnisnya?":
            jump nadya_button_depot.business
        "Halo, {b}Svetlana{/b}.":

            if M_svetlana.finished_state(S_sve01_lewd):
                jump nadya_button_depot.greet
            else:
                $ M_svetlana.trigger(T_sve01_init)
                jump nadya_button_depot.envy
        "Seks.":

            jump nadya_button_depot.sex
        "Hanya menyapa.":

            pass

    anon f_normal "Saya baru saja berada di lingkungan sekitar dan meskipun saya akan menyapa."

    nadya f_confused "Ini ritual kencan Amerika?"

    anon f_confused "Eh, bukan?"

    nadya f_happy "Oh, jadi kamu melakukan kunjungan khusus karena kamu menyukaiku, ya?"

    anon "Uhh, tentu saja."

    anon f_normal "Ya, ayo kita lakukan itu."

    svetlana f_smirk_back a_hips "I think the boy is in love." (show_native="Dumayu, mal'chik vlyublen.")
    nadya f_happy "Who could blame him?" (show_native="Kto mog yego vinit'?")
    nadya f_sexy "Mengapa kamu tidak kembali malam ini sepulang kerja?"

    show svetlana f_smirk
    nadya "Kita bisa membuat saat-saat seksi hingga matahari terbit."

    anon f_flirt "{i}*Gulp*{/i} Sampai matahari terbit?"

    anon "Y-ya, mungkin..."

    nadya f_happy "Bagus."

    nadya "Nanti."

    anon f_normal a_wave "Sampai jumpa, {b}Nadya{/b}."

    pause
    anon a_idle "{b}Svet{/b}."

    svetlana a_wave "Farewell, {b}[firstname]{/b}." (show_native="Do svidaniya, {b}[firstname]{/b}.")
    hide anon with dissolve
    return


label nadya_button_depot.business:
    anon f_normal "Bagaimana kabar bisnis barunya, Nadya?"

    nadya "Ehh, bagus."

    nadya "Vodka menghasilkan banyak uang."

    show nadya a_angry f_angry:
        xoffset 675
        xzoom -1
    show svetlana f_concerned_back
    with {'master': dissolve}
    nadya "Despite the fact that my workers are idiots!" (show_native="Pri tom chto moi rabochiye idioty!")
    show nadya a_idle with dissolve
    pause
    nadya f_normal "Saya sedang mempertimbangkan ekspansi mungkin..."

    anon f_confused "Oh ya?"

    show nadya:
        xoffset 100
        xzoom 1
    show svetlana f_happy
    with {'master': dissolve}
    anon "Lebih banyak vodka atau sesuatu yang berbeda?"

    nadya "Ini belum diputuskan."

    show anon f_normal
    nadya "Saya mempunyai banyak minat."

    nadya "Mungkin sesuatu untuk wanita akan baik."

    nadya f_angry "Aku bosan dengan pria bodoh!"

    show svetlana a_hips f_annoyed with {'master': dissolve}:
        xoffset 450
        xzoom -1
    svetlana "I agree." (show_native="Ya soglasen.")
    anon f_surprised "Hah."

    anon f_shy "Baiklah, semoga berhasil, menurutku..."

    show svetlana a_sides f_normal with {'master': dissolve}:
        xoffset -100
        xzoom 1
    nadya f_sexy "Heh, aku tidak butuh keberuntungan..."

    nadya "... Saya orang Rusia."

    show svetlana f_smirk_back
    nadya "Kami memanfaatkan peluang dengan menguasai bola dan menekan."

    show anon a_behind_head
    show svetlana f_smirk
    with {'master': dissolve}
    anon "{i}*Gulp*{/i} Benar."

    show anon a_sides
    with {'master': dissolve}
    anon "Mengerti."

    jump nadya_button_depot.choice


label nadya_button_depot.envy:
    show anon a_wave f_normal with {'master': dissolve}
    anon "Hai, {b}Svet{/b}."

    show nadya a_sides f_surprised with {'master': dissolve}
    svetlana f_surprised "Ehh..."

    svetlana "... H-halo."

    nadya f_angry "Have you been flirting with my man?!" (show_native="Ty flirtoval s moim muzhchinoy?!")
    show anon a_surprised f_surprised_teeth
    show svetlana a_up f_timid:
        xoffset 450
        xzoom -1
    with {'master': dissolve}
    svetlana "No, I would never do that!" (show_native="Net, ya by nikogda etogo ne sdelal!")
    svetlana "I swear!" (show_native="Ya klyanus'!")
    show anon a_sides
    show svetlana a_sides
    show nadya a_crossed
    with {'master': dissolve}
    nadya @ -m_talk "Hmph."

    anon f_worried "Um, apakah ada masalah?"

    show nadya a_point_angry:
        xoffset -275
    show svetlana:
        xoffset -100
        xzoom 1
    with {'master': dissolve}
    nadya "Anda ingin membuat momen seksi dengan {b}Svetlana{/b}?!"

    show anon f_worried_surprised a_surprised_up with {'master': dissolve}
    anon "APA?!"

    anon "T-tidak, aku tidak-"

    show nadya a_hips
    anon a_sides "Err, maksudku aku... hanya berusaha bersikap sopan... itu saja."

    nadya "Menurutmu dia cantik?"

    anon f_shy "Yah, maksudku... Ya, dia cantik tapi aku tidak berusaha untuk-"

    show nadya a_finger
    show svetlana f_happy_down
    with {'master': dissolve}
    nadya "Lebih cantik dariku?!"

    anon f_surprised "Hah?!"

    anon "aku tidak bilang-"

    nadya a_point "Kamu ingin aku berbagi penis cantikmu dengan pengawal, ya?!"

    show anon a_rub f_shy of_blush
    show svetlana o_blush
    with {'master': dissolve}
    anon "Astaga, apakah ada yang menyalakan pemanasnya atau apa?!"

    show svetlana f_timid_down
    anon "Sebab, tiba-tiba terasa sangat panas di sini..."

    nadya a_hips "Dengarkan aku, anak Amerika..."

    show anon f_surprised a_surprised
    show svetlana f_surprised
    with {'master': dissolve}
    nadya "... Tidak ada yang meniduri {b}Svetlana{/b} tanpa saya bilang begitu!"

    nadya "Memahami?!"

    show anon a_sides f_worried -of_blush
    show svetlana f_concerned
    with {'master': dissolve}
    anon "Dengar, serius... Aku hanya berusaha bersikap sopan."

    nadya a_crossed @ -m_talk "Mhmm."

    pause
    show svetlana -o_blush with {'master': dissolve}
    nadya f_frowning "Baiklah."

    show nadya a_idle:
        xoffset 675
        xzoom -1
    show svetlana f_concerned_back
    with dissolve
    show nadya a_point with {'master': dissolve}:
        xoffset 100
        xzoom 1
    nadya "Tapi aku terus mengawasimu, ya?"

    show svetlana f_concerned
    anon f_shy "Y-ya, aku mengerti."

    show nadya a_idle f_happy
    show svetlana f_normal
    with {'master': dissolve}
    nadya "Bagus."

    jump nadya_button_depot.choice


label nadya_button_depot.greet:


    jump nadya_button_depot.envy


label nadya_button_depot.sex:
    show anon a_behind_head f_shy of_blush with {'master': dissolve}
    anon "Aku bertanya-tanya... apakah... erm..."

    nadya f_sexy "Oh, kamu ingin membuat momen seksi sekarang?"


    if M_svetlana.finished_state(S_sve01_lewd):
        menu:
            "Ya, tolong!":
                anon "Ya-"

            "Dengan Svetlana?":

                if M_svetlana.once('ask_nadya'):
                    jump nadya_button_depot.svet
                else:
                    jump nadya_button_depot.wonder

    show anon a_sides f_surprised
    show svetlana f_timid:
        xoffset 450
        xzoom -1
    with {'master': dissolve}
    svetlana "Eh, maaf {b}Nona Chernyshevsky{/b} tapi {b}Katya{/b} telah menjadwalkan pertemuan dengan-"

    show anon f_worried_surprised
    nadya f_frowning "Saya sangat mengetahui jadwal!"

    nadya "{b}Katya{/b} dapat mengatur rapatnya sendiri hari ini."

    svetlana "D-da, tentu saja."

    svetlana "Permintaan maaf."

    show anon f_shy
    nadya f_normal "Pintu jaga."

    nadya "Saya membawa {b}[firstname]{/b} ke area kargo untuk mengabadikan momen-momen seksi."

    svetlana f_normal "Sesuai keinginan Anda, {b}Nona Chernyshevsky{/b}."

    show svetlana:
        xoffset -100
        xzoom 1
    show nadya a_point f_sexy:
        xoffset -275
    with {'master': dissolve}
    nadya "Ayo, kita berangkat sekarang."

    show anon f_worried:
        xoffset -600
        xzoom -1
    hide nadya
    with {'master': dissolve}
    anon "Tepat di belakangmu."

    hide anon with dissolve
    pause
    show svetlana a_crossed f_timid
    with {'master': dissolve}
    svetlana "{i}*Huh*{/i}"


    scene expression background(304, 368, 4, l=L_warehouse_cargo) as stage
    show thug f_surprised
    show nadya a_crossed f_frowning:
        xoffset 150
        xzoom -1
    with fade
    pause
    jab "{b}Nona Chernyshevsky{/b}!"

    jab "saya-"

    pause
    jab "Kenapa kamu datang ke ruang penyimpanan?!"

    nadya "Keluar."

    jab f_confused "Keluar?!"

    jab "Tapi aku belum selesai dengan-"

    show anon f_confused behind nadya with {'master': dissolve}:
        xoffset -100
    nadya f_angry "Anda membalas pembicaraan?!"

    show thug a_defensive f_concerned with {'master': dissolve}
    jab "T-tidak, aku tidak-"

    show anon a_surprised f_surprised_teeth o_boner
    show thug f_wincing
    show nadya a_angry:
        xoffset 225
    nadya "{b}Jab{/b}, get the fuck out!" with hpunch
    show anon a_sides f_surprised_down
    show thug a_idle f_concerned
    with {'master': dissolve}
    jab "Tentu saja!"

    show anon a_facepalm f_worried_down
    with {'master': dissolve}
    jab "Maaf!"

    show anon a_sides f_worried
    with {'master': dissolve}
    jab "aku pergi sekarang."

    show anon:
        xoffset -600
        xzoom -1
    show nadya a_hips f_eyeroll
    hide thug
    with dissolve
    pause
    show nadya a_hips f_frowning with {'master': dissolve}:
        xoffset -350
        xzoom 1
    nadya "Dia adalah pekerja yang setia dan baik..."

    show anon:
        xoffset -100
        xzoom 1
    with {'master': dissolve}
    nadya "... Tapi otaknya sebesar kacang tanah!"

    anon "Jika Anda berkata demikian."

    nadya "Apakah benar."

    pause
    show nadya a_sides f_happy_back:
        xoffset 450
        xzoom -1
    with {'master': dissolve}
    nadya "Sekarang..."

    show anon f_surprised_down
    show nadya f_sexy_down:
        xoffset -125
        xzoom 1
    with {'master': dissolve}
    nadya "... Mari kita lihat ayam cantikmu, ya?"

    show anon f_worried_left of_blush with {'master': dissolve}
    anon "Um, di sini?"

    show anon f_worried
    nadya f_sexy "Ya."

    anon "Bukankah Anda lebih suka pergi ke kantor Anda?"

    show nadya a_crossed f_frowning with {'master': dissolve}
    nadya "No." (show_native="Nyet.")
    nadya "{b}Katya{/b} membutuhkan kantor untuk urusan penting."

    nadya "Saya tidak akan mengganggu saat-saat seksi."

    pause
    show nadya a_hips f_pouting with {'master': dissolve}
    nadya "Sekarang, lepas celananya."

    anon "Baiklah."

    show nadya f_sexy_down
    anon f_worried_down "Hmm..."

    show anon a_remove_shorts_boner -o_boner with dissolve
    show anon b_shirt_undress_bottom o_boner -of_blush
    show nadya a_sides f_surprised_down
    with dissolve
    pause
    show anon a_sides b_shirt f_worried -o_boner od_dick4 of_blush with {'master': dissolve}
    nadya f_sexy_down "Hmm, anak baik."

    show anon f_shy
    pause
    show nadya a_idle f_sexy with {'master': dissolve}
    nadya "Ayam besarmu membuatku sangat bersemangat..."

    show anon f_surprised_low
    show nadya a_undress1 f_sexy_down
    with dissolve
    show nadya b_dressed_undress2 with dissolve
    pause
    show anon f_flirt_low
    show nadya a_hips b_pantless o_pantless_cum_drip
    with {'master': dissolve}
    nadya f_sexy "... Ayo lihat..."

    show anon f_flirt
    hide nadya
    with dissolve

    call scene_nadya_sex_cargo.repeat
    $ unlock_scene('nadya', '03_unlocked')

    scene expression background(304, 368, 4, l=L_warehouse_cargo) as stage
    show nadya a_sides b_pantless f_happy:
        xzoom -1

    if _return == 'inside':
        show nadya o_pantless_cum_drip

    with fade
    nadya "Ayo..."

    show anon a_sides b_shirt f_shy_low:
        xoffset -50
        xzoom -1
    show nadya b_dressed_undress2 f_sexy_high -o_pantless_cum_drip
    with {'master': dissolve}
    nadya "... Kami kembali ke gudang sekarang."

    show anon f_shy
    show nadya a_undress1 b_dressed f_happy
    with dissolve
    pause
    show nadya a_hips with {'master': dissolve}
    anon f_worried "Tunggu sebentar..."

    show anon a_point_down f_confused_low:
        xoffset 450
        xzoom 1
    show nadya f_confused
    with {'master': dissolve}
    anon "... Kita akan meninggalkan kekacauan ini di sini saja?"

    show anon f_disgusted_low
    nadya "Eh, ya?"

    show anon a_sides f_disgusted with dissolve:
        xoffset -50
        xzoom -1
    pause
    nadya f_normal "Jangan menyibukkan diri dengan kekacauan."

    nadya "{b}Jab{/b} akan dibersihkan."

    show anon a_surprised f_worried_surprised with {'master': dissolve}
    anon "{b}Jab{/b}?"

    pause
    show nadya f_confused
    anon "Kau benar-benar akan membuatnya membersihkan-"

    show anon a_sides f_surprised_left_low with dissolve
    pause
    anon f_worried "M-ya uhh..."

    nadya f_sexy "Jus waktu seksi?"

    anon f_shy "Y-ya."

    nadya f_laugh "Haha!"

    nadya f_normal "Tentu saja."

    nadya "Apakah tugasnya membereskan kekacauanku."

    anon f_worried "Oke, tapi-"

    nadya "Jangan khawatir dengan {b}Jab{/b}."

    nadya "Anggap saja itu penebusan dosa atas semua uang yang dia ambil darimu dan teman-temannya... Eh?"

    show anon a_rub f_shy with {'master': dissolve}
    anon "Baiklah, saya rasa itu masuk akal."

    show anon b_empty f_surprised_down
    show nadya b_dressed_kiss_cheek_shirt:
        xoffset -50
    show anon_overlay_dick_shirt_od_dick2 as dick:
        xoffset -50
        xzoom -1
    with dissolve
    pause
    show anon a_sides b_shirt f_happy
    show nadya a_sides b_dressed f_happy:
        xoffset 250
    hide dick
    with {'master': dissolve}
    nadya "Ini menyenangkan."

    nadya "Kami melakukan lebih banyak lagi nanti."

    anon "Kedengarannya bagus."

    nadya "Farewell, {b}[firstname]{/b}." (show_native="Do svidaniya, {b}[firstname]{/b}.")
    show anon a_wave
    hide nadya
    with {'master': dissolve}
    anon "Farewell, {b}Nadya{/b}." (show_native="Do svidaniya, {b}Nadya{/b}.")
    pause
    show anon a_sides with dissolve
    pause .4
    show anon a_surprised_up_both f_surprised_down with dissolve
    pause
    show anon b_shirt_undress_bottom with dissolve
    show anon a_remove_shorts b_dressed with dissolve
    show anon a_sides f_surprised with dissolve
    pause
    show anon a_surprised f_surprised_left with dissolve
    pause
    show anon a_sides f_worried with dissolve
    hide anon with dissolve
    return 'afterglow'


label nadya_button_depot.svet:
    anon "A-dengan {b}Svetlana{/b}?"

    show anon a_sides
    with {'master': dissolve}
    nadya f_confused "{b}Svetlana{/b}, apakah kamu berminat untuk saat-saat seksi?"

    show svetlana a_hips f_smirk:
        xoffset 450
        xzoom -1
    with {'master': dissolve}
    svetlana "Aku selalu dalam mood untuk saat-saat seksi..."

    show nadya a_shoo f_happy
    with {'master': dissolve}
    nadya "Hehe, pergi."

    show nadya a_hips
    show svetlana f_happy
    with {'master': dissolve}
    nadya "Nikmati dirimu sendiri."

    show anon a_empty b_empty f_surprised:
        xoffset -546
        xzoom -1
    show svetlana b_dressed_pull_anon:
        xoffset -500
        xzoom 1
    with {'master': dissolve}
    svetlana "Thank you, {b}Nadya{/b}." (show_native="Spasibo, {b}Nadya{/b}.")
    hide anon
    hide svetlana
    with {'master': dissolve}
    nadya "Don't break him." (show_native="Ne slomay yego.")
    svetlana "I won't!" (show_native="Ya ne budu!")

    scene expression background(512, 416, 2.8, l=L_warehouse_furnace) as stage
    show thug:
        xoffset -200
    with fade
    show svetlana b_dressed_pull_anon f_happy
    show anon a_empty b_empty f_surprised:
        xoffset -46
        xzoom -1
    show thug f_surprised
    with {'master': dissolve}
    pause
    show anon a_surprised b_dressed f_worried
    show svetlana b_dressed f_annoyed:
        xzoom -1
    show thug a_defensive
    with {'master': dissolve}
    svetlana "Kalahkan, {b}Jab{/b}!"

    show anon a_sides
    show thug a_sides f_concerned
    with {'master': dissolve}
    jab "Apa lagi?!"

    show anon f_surprised
    show svetlana f_glaring
    pause
    show anon f_worried:
        xoffset 454
        xzoom 1
    show thug a_confused f_confused_down:
        xoffset 700
        xzoom -1
    show svetlana f_normal
    with {'master': dissolve}
    jab "... Bunch of assholes." (show_native="... Kucha pridurkov.")
    hide thug
    show svetlana a_undress f_happy_down
    with {'master': dissolve}
    pause
    show svetlana b_naked
    with {'master': dissolve}
    anon "Aku merasa kasihan padanya."

    show svetlana b_naked_undress
    with {'master': dissolve}
    pause
    show anon:
        xoffset -46
        xzoom -1
    show svetlana a_sides b_naked f_happy
    with {'master': dissolve}
    svetlana "Anda dapat mengundangnya kembali untuk menonton jika Anda mau?"

    anon f_normal "Yah, aku tidak merasa {i}itu{/i} buruk..."

    svetlana @ f_laugh "hehe!"

    svetlana "Sekarang buka baju, kita harus cepat."

    label nadya_button_depot.merge:
    show anon a_surprised f_shy_down
    with {'master': dissolve}
    anon "Oh benar."

    show svetlana f_smirk_low
    show anon b_shirt_undress_bottom
    with {'master': dissolve}
    pause
    show anon a_sides b_shirt f_flirt
    with {'master': dissolve}
    svetlana f_smirk "Lovely." (show_native="Prekrasnyy.")

    menu:
        "Seks oral.":
            anon "Mungkin Anda bisa..."

            show anon f_flirt_down
            show svetlana f_curious
            pause
            show svetlana f_curious_low
            pause
            svetlana f_curious "Kamu ingin aku menyedotmu?"

            anon f_flirt "Ya, tolong."

            show svetlana a_hips f_concerned
            with {'master': dissolve}
            svetlana "Hmm, aku mengharapkan sesuatu yang lebih... saling memuaskan."

            show anon a_surprised_up_both f_worried
            with {'master': dissolve}
            anon "Yah, kita tidak perlu-"

            svetlana f_smirk "... Tapi menurutku kamu bisa berhutang satu padaku."

            show anon a_sides f_flirt
            with {'master': dissolve}
            anon "Y-ya, benar-benar..."

            anon "... Aku selalu siap untuk-"

            show anon od_dick2
            with {'master': dissolve}
            svetlana f_annoyed "Duduk dan tutup mulut."

            show anon a_salute f_worried_surprised od_dick_spring
            with {'master': dissolve}
            anon "Ya, Bu!"

            hide anon
            show svetlana a_sides f_happy_down:
                xoffset -500
                xzoom 1
            with {'master': dissolve}
            pause

            call scene_svetlana_furnace_blowjob.repeat
            $ unlock_scene('svetlana', '01_unlocked', variant='repeat')
        "Seks.":

            anon "Jadi kamu ingin-"

            svetlana "Ya."

            svetlana "Aku akan menunggumu lagi, seperti sebelumnya."

            show anon od_dick2
            show svetlana f_smirk_low
            with {'master': dissolve}
            anon "Y-ya, tentu saja..."

            show anon od_dick_spring
            with {'master': dissolve}
            anon "... Terakhir kali luar biasa, kami-"

            show anon od_dick4
            show svetlana a_hips f_smirk
            with {'master': dissolve}
            svetlana f_annoyed "Diam dan berbaring."

            show anon a_salute f_worried_surprised
            with {'master': dissolve}
            anon "Ya, Bu!"

            hide anon
            show svetlana a_sides f_happy_down:
                xoffset -500
                xzoom 1
            with {'master': dissolve}
            pause

            call scene_svetlana_furnace_cowgirl.repeat
            $ unlock_scene('svetlana', '02_unlocked', variant='repeat')

    scene expression background(512, 416, 2.8, l=L_warehouse_furnace) as stage
    show svetlana a_undress b_naked f_happy_down:
        xzoom -1
    show anon a_remove_shorts f_happy:
        xoffset -200
        xzoom -1
    with fade
    anon "Ya, seperti biasa... itu luar biasa!"

    show anon a_sides
    show svetlana b_dressed
    with {'master': dissolve}
    svetlana "Saya juga menikmatinya."

    show svetlana a_sides f_happy
    with {'master': dissolve}
    svetlana "Penismu luar biasa!"

    anon @ f_brag "Kau tahu, aku tidak pernah bosan mendengarnya..."

    svetlana f_smirk "Heh, saya harus kembali ke {b}Nona Chernyshevsky{/b}."

    anon f_worried "Oh benar.."

    anon "Kurasa aku harus pergi juga."

    anon f_shy "Terima kasih untuk uhh-"

    show anon a_behind_head
    with {'master': dissolve}
    anon "Kamu tahu."

    hide anon
    show svetlana b_dressed_kiss
    with {'master': dissolve}
    anon "!!!"
    svetlana @ -m_talk "MM."

    pause
    show anon a_sides b_dressed f_flirt_grin:
        xoffset -200
        xzoom -1
    show svetlana b_dressed f_happy
    with {'master': dissolve}
    svetlana "Dengan senang hati."

    show anon:
        xoffset 300
        xzoom 1
    show svetlana a_sides:
        xoffset 575
    with {'master': dissolve}
    pause
    hide svetlana
    show anon a_wipe f_drink
    with {'master': dissolve}
    anon @ -m_talk "{i}*Fiuh*{/i}"

    show anon a_sides f_tired_happy
    with {'master': dissolve}
    pause
    anon f_flirt_grin @ -m_talk "(Tentu saja dari Rusia dengan cinta.)"

    hide anon with dissolve
    return 'afterglow'


label nadya_button_depot.wonder:
    anon f_shy "Jadi, hei... aku bertanya-tanya..."

    nadya f_confused @ -m_talk "Hmm?"

    show anon a_sides
    with {'master': dissolve}
    anon f_shy_left "... Suatu hari, ketika {b}Svetlana{/b} dan saya... Anda tahu..."

    show nadya f_frowning
    show svetlana a_fist_mouth f_glaring
    with {'master': dissolve}
    svetlana @ -m_talk "{i}*Melegakan tenggorokan*{/i}"

    show anon f_worried
    show svetlana a_crossed
    with {'master': dissolve}
    pause
    show anon f_worried_surprised
    pause
    anon "Aku uhh... a-apa itu hanya terjadi satu kali saja atau-"

    show anon a_surprised_shoulders f_surprised_teeth
    show nadya a_point_angry f_angry:
        xoffset -275
    show svetlana a_facepalm f_eyeroll
    with {'master': dissolve}
    nadya "ANDA LEBIH INGIN {b}SVETLANA{/b} DARIPADA SAYA?!"

    show anon a_surprised_up_both f_worried_surprised
    show svetlana a_sides f_bored
    with {'master': dissolve}
    anon "A-apa, TIDAK!"

    show anon -of_blush
    with {'master': dissolve}
    anon "aku tidak-"

    show nadya a_angry:
        xoffset -325
    with {'master': dissolve}
    nadya "ANDA MELAKUKANNYA!"

    nadya "ANDA BILANG BEGITU!"

    show anon a_cover_boner
    with {'master': dissolve}
    anon "T-tidak, tidak!"

    nadya "KAMU SUKA PAYUDARA BESAR {b}SVETLANA{/b} DAN BERPIKIR PUSSYNYA LEBIH KETAT DARI PUNYAKU?!"

    show anon f_shock
    pause
    nadya "HAH?!"

    anon f_worried_surprised "saya-"

    nadya "{b}SVETLANA{/b} TAHAN DIA!"

    show anon f_surprised_teeth
    show nadya a_knife_pull
    with {'master': dissolve}
    svetlana f_concerned "Ya, {b}Nona Chernyshevsky{/b}."

    show anon a_empty b_empty f_confused_back
    show svetlana b_dressed_restrain_anon:
        xoffset -218
        xzoom -1
    show nadya a_knife
    with {'master': dissolve}
    anon "T-tunggu, apa yang kamu-"

    show anon f_afraid
    show nadya a_knife_brandish
    with {'master': dissolve}
    nadya "AKU AKAN MEMOTONG BOLAMU DAN MENYEDIAKANNYA KE PANTATMU!!!"

    anon "TIDAK TIDAK TIDAK!"

    anon f_worried_surprised "Aku tidak lebih suka {b}Svetlana{/b} daripada kamu, aku bersumpah!!"

    anon "Saya hanya mencoba untuk menjadi inklusif!"

    nadya "AKU AKAN MENARIK UsusMU MELALUI LUBANG KONTOL!!!"

    anon f_afraid_close "Eeeep!"

    pause
    show nadya f_happy
    show svetlana f_happy
    pause
    show nadya a_knife f_laugh
    show svetlana f_laugh
    with {'master': dissolve}
    nadya "HAH!"

    show nadya b_dressed_laugh
    with {'master': dissolve}
    nadya "Hahahahahaha!!!"

    show anon f_afraid_peek
    svetlana "hehe!"

    anon f_surprised_low "Apa-"

    nadya "Ahahaha!!!"

    show anon f_surprised
    show nadya a_knife b_dressed f_happy
    show svetlana f_happy
    with {'master': dissolve}
    nadya @ f_happy "Anda seharusnya memiliki-"

    show anon f_confused
    show nadya a_knife_pull
    with {'master': dissolve}
    nadya @ f_happy "Lihat wajahmu!!"

    show anon f_confused_low
    show nadya a_sides b_dressed_laugh f_laugh
    show svetlana f_laugh
    with {'master': dissolve}
    nadya "Hahahaah!"

    show anon a_ouch b_dressed f_disgusted_low
    show svetlana b_dressed
    with {'master': dissolve}
    svetlana "hehe!"

    anon "... I-itu hanya lelucon?"

    show anon a_sides f_worried
    show nadya b_dressed f_happy
    show svetlana f_happy
    with {'master': dissolve}
    nadya "Saya tidak peduli dengan siapa Anda membuat momen seksi!"

    nadya f_pouting "Apa, menurutmu kami eksklusif?!"

    anon @ f_confused "T-tidak?"

    nadya f_normal "{b}[firstname]{/b}, saya kepala Bratva..."

    nadya "...Saya tidak akan terikat pada siapa pun."

    anon f_worried @ -m_talk "Hmm..."

    show nadya a_hips
    with {'master': dissolve}
    nadya "Aku bercinta dengan siapa pun yang kuinginkan, kapan pun aku mau."

    nadya "Memahami?"

    show anon a_point_back
    with {'master': dissolve}
    anon "... J-jadi tidak apa-apa jika {b}Svetlana{/b} dan aku-"

    nadya f_happy "Tentu saja!"

    show nadya a_shoo
    with {'master': dissolve}
    nadya "Pergi, pergi."

    show nadya a_sides
    with {'master': dissolve}
    nadya "Bersenang-senanglah!"

    show anon a_empty b_empty f_surprised:
        xoffset -546
        xzoom -1
    show svetlana b_dressed_pull_anon:
        xoffset -500
        xzoom 1
    with {'master': dissolve}
    svetlana "Thank you, {b}Nadya{/b}." (show_native="Spasibo, {b}Nadya{/b}.")
    hide anon
    hide svetlana
    with {'master': dissolve}
    nadya "Don't break him." (show_native="Ne slomay yego.")
    svetlana "I won't!" (show_native="Ya ne budu!")

    scene expression background(512, 416, 2.8, l=L_warehouse_furnace) as stage
    with fade
    show svetlana b_dressed_pull_anon f_happy
    show anon a_empty b_empty f_surprised:
        xoffset -46
        xzoom -1
    with {'master': dissolve}
    pause
    show anon a_surprised b_dressed
    show svetlana b_dressed:
        xzoom -1
    with {'master': dissolve}
    anon "Apakah kamu terlibat dalam hal itu?!"

    svetlana "Tentu saja itu ideku."

    anon f_skeptical "Dengan serius?"

    svetlana "Ada baiknya untuk mengingatkan Anda siapa bos di sini, ya?"

    show anon a_sides f_unimpressed
    with {'master': dissolve}
    pause
    show svetlana a_undress
    with {'master': dissolve}
    svetlana "Mengesankan, Anda tidak membuat diri Anda kesal."

    show anon f_unimpressed_low
    show svetlana b_naked f_happy_down
    with {'master': dissolve}
    anon "Ya terima kasih."

    show anon f_flirt_low
    show svetlana b_naked_undress
    with {'master': dissolve}
    pause
    show thug f_surprised behind anon:
        xoffset 150
    show svetlana a_sides b_naked f_normal
    with {'master': dissolve}
    jab "Apa yang terjadi di ruang tungku?!"

    show anon f_surprised:
        xoffset 325
        xzoom 1
    with {'master': dissolve}
    svetlana f_annoyed "{b}Jab{/b} tersesat!"

    show anon f_worried
    jab f_concerned "Tapi ini kamarku..."

    show anon f_worried_left
    show svetlana a_hips
    with {'master': dissolve}
    svetlana "You don't have a room, idiot." (show_native="U tebya net mesta, idiot.")
    show thug f_angry
    svetlana "Sekarang enyahlah!"

    show anon f_worried
    pause
    show svetlana f_glaring
    pause
    show svetlana f_normal
    show thug a_confused f_confused_down:
        xoffset 700
        xzoom -1
    with {'master': dissolve}
    jab "I'm so sick of this. Can't get any peace!" (show_native="Zayebali, blyad'. Nigde v pokoye ne ostavyat!")
    hide thug
    with {'master': dissolve}
    pause
    show anon f_worried behind svetlana:
        xoffset -175
        xzoom -1
    with {'master': dissolve}
    anon "Itu aneh."

    show svetlana a_sides
    with {'master': dissolve}
    svetlana "Jangan pedulikan dia."

    svetlana "Buka baju, kita harus cepat."

    anon f_confused @ -m_talk "Hmm?"

    jump nadya_button_depot.merge
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

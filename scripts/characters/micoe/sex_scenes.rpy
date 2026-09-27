label micoe_bj_scene_repeatable:
    scene expression player.location.background_blur
    show player 10 at left
    show micoe:
        flip
    with dissolve
    player_name "Ingat ketika Anda membantu saya... Umm, ekstrak sampel saya untuk pengujian."

    show player 5
    show micoe f_sexy
    micoe "Maksudmu, saat aku menghisap penismu di kamar mandi?"

    show player 11
    player_name "!!!"
    show player 29 with dissolve
    player_name "Y-ya."

    show player 3
    micoe @ f_laugh "Hehehe, menurutku kita sudah tidak perlu malu lagi, {b}[firstname]{/b}."

    micoe "Anda di sini untuk memberi saya rasa lagi?"

    show player 17 with dissolve
    player_name "Eh ya."

    hide player
    show micoe b_pulling
    with dissolve
    micoe "Ayo manis."


    $ player.go_to(L_hospital_room_bathroom)
    scene expression player.location.background_blur
    show player 13f at right
    show micoe f_sexy
    with dissolve
    micoe "Apa yang kamu tunggu?"

    micoe "Keluarkan ayam itu!"

    show player 14f
    player_name "O-oke."

    show player 261b with dissolve
    pause
    show player 263b at Position (xoffset=-150)
    show micoe b_knees
    with dissolve
    pause
    show micoe b_knees_talk
    micoe "Mmm, aku akan menghisap ayam cantik ini kapan saja kamu mau, {b}[firstname]{/b}!"


    $ M_micoe.set('sex speed', .12)
    $ anim_toggle = True
    $ animated = True
    scene expression player.location.background_closeup
    show expression AnimatedImage("micoe_bj", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], M_micoe) as micoe_bj at Position(xalign = 0.0, yoffset = 0)
    with dissolve
    micoe "{i}*Menyeruput*{/i}"

    player_name "Ya Tuhan..."

    player_name "Rasanya luar biasa, {b}Micoe{/b}."

    micoe "Mmhmm!"

    return

label micoe_bj_scene:
    $ player.go_to(L_hospital_room_bathroom)
    scene expression player.location.background_blur
    show player 691b with dissolve
    player_name "Baiklah, dia bilang aku hanya perlu ejakulasi ke dalam cangkir ini..."

    show player 261bf with dissolve
    pause
    $ M_player.set("sex speed", .4)
    show player 694_694b with dissolve
    pause
    player_name "(Ayo.)"

    pause
    pause
    player_name "..."
    pause
    pause
    player_name "( Hmm, biasanya tidak memakan waktu selama ini... )"

    pause
    $ M_player.set("sex speed", .3)
    show player 694_694b
    pause
    player_name "(Ayolah, hal bodoh!)"

    "{i}*Ketuk* *Ketuk*{/i}"

    show player 695 with hpunch
    player_name "!!!"
    show player 692d
    player_name "Y-ya?"

    show player 692c
    micoe "Semuanya baik-baik saja di sana, harimau?"

    show player 692d
    player_name "aku uhh..."

    player_name "Saya tidak yakin."

    show player 692c
    micoe "Masalah?"

    show player 692d
    player_name "Umm... Demam panggung, ya?"

    show micoe:
        flip
        xoffset 200
    with dissolve
    show player 692d
    player_name "Wah, apa yang kamu-"

    show player 692c
    micoe "Ssst, biarkan aku melihatnya..."

    show player 692d
    player_name "Tidak, sungguh itu-"

    hide player
    show micoe b_jerk1:
        unflip
        xoffset 26
    player_name "!!!" with hpunch
    micoe "Wow, kamu adalah salah satu anak yang berbakat!"

    show micoe b_jerk
    micoe "Pacarmu itu adalah wanita yang beruntung!"

    player_name "..."
    player_name "!!!"
    show micoe b_dressed a_idle
    show player 263c at right
    with dissolve
    micoe "Ini dia."

    micoe @ f_laugh "Masalah terpecahkan!"

    show player 262b
    player_name "Hehe."

    show player 263c
    micoe "Aku akan menyerahkannya padamu sekarang..."

    pause
    show micoe f_sexy
    micoe "... Kecuali, kamu lebih suka aku tinggal di sini dan membantu?"

    show player 262g with dissolve
    player_name "A-apa maksudmu?"

    show player 262e
    micoe "Saya bisa tinggal dan memberikan sedikit... Bantuan medis."

    show micoe f_empty a_fingersuck with dissolve
    show player 262g
    player_name "O-oh!"

    show player 262e
    pause
    show player 262g
    player_name "saya tidak..."

    show player 262e
    menu:
        "Tidak.":
            show player 262d with dissolve
            player_name "Itu, aku... menurutku temanku tidak-"

            player_name "Maksudku, pacar akan senang tentang itu..."

            show player 262c
            show micoe f_sexy a_idle with dissolve
            micoe "Dia tidak perlu mencari tahu."

            show player 262d
            player_name "Uhh, sungguh... aku baik-baik saja."

            show player 262c
            micoe "Baiklah, tampan dan setia."

            micoe "Baiklah, saya menghormatinya."

            show micoe f_normal_down
            micoe "Mmm, apa yang akan kulakukan padamu..."

            player_name "..."
            show micoe f_sexy
            micoe "{i}*Ahem*{/i} Saya akan berada di luar jika Anda berubah pikiran."

            show player 262d
            player_name "T-terima kasih..."

            show player 262c
            hide micoe with dissolve
            pause
            show player 262b
            player_name "Sialan!"

            player_name "Yah, aku pasti sulit sekarang."

            player_name "Sebaiknya aku kembali bekerja."

            show player 263c
            scene black with fade
            pause

            scene expression "backgrounds/location_hospital_room_day_blur.jpg"
            show micoe
            show player 691df at right
            with dissolve
            player_name "Ini dia."

            show player 691cf
            show micoe f_laugh
            micoe "Ya Tuhan!"

            $ renpy.end_replay()
            call expression game.dialog_select("diane_check_up_results")

            $ M_diane.trigger(T_diane_cup_o_jizz)
            $ player.go_to(L_hospital_floor2)
            $ game.main()
        "Ya.":

            show player 263c
            player_name "..."
            show player 262b
            player_name "Oke."

            show player 263c
            show micoe f_sexy
            micoe "Oh, aku berharap kamu akan mengatakan itu!"

            show micoe b_knees_talk with dissolve:
                xoffset 200
            show player 263b
            micoe "Aku menginginkanmu begitu aku melihatmu di ruang tunggu itu."

            show micoe b_knees
            show player 262h
            player_name "Anda melakukannya?"


            scene expression player.location.background_closeup
            show micoe_bj look
            with dissolve
            micoe "Mmmhmm."

            show micoe_bj talk
            micoe "... Dan kemudian saya melihat penis besar yang Anda sembunyikan dan saya hampir tidak bisa mengendalikan diri!"

            show micoe_bj look
            player_name "Anda benar-benar maju, Anda tahu itu?"


            $ anim_toggle = True
            $ animated = True
            $ M_micoe.set('sex speed', .12)
            show expression AnimatedImage("micoe_bj", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], M_micoe) as micoe_bj at Position(xalign = 0.0, yoffset = 0)
            player_name "!!!" with hpunch
            player_name "BENAR-BENAR MAJU!!"

            micoe "Mmmhmmph!"

            jump micoe_bj_loop

label micoe_bj_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("micoe_bj", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], M_micoe) as micoe_bj at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("micoe_bj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "micoe_bj {}".format(pose_list[pose_counter]) as micoe_bj at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("micoe_bj_hscene_dialog")
        $ animcounter += 1
    call screen micoe_bj_options

label micoe_bj_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        player_name "Sialan!{p=1}{nw}"

    if animcounter == 1 and randomizer() > 50:
        micoe "{i}*Menyeruput*{/i}{p=1}{nw}"

    if animcounter == 2 and randomizer() < 50:
        player_name "Kamu benar-benar ahli dalam hal ini!{p=2}{nw}"

    if animcounter == 3 and randomizer() > 50:
        player_name "Saya semakin dekat...{p=2}{nw}"

        if M_micoe.get("sex speed") > 0.061:
            $ M_micoe.set("sex speed", M_micoe.get("sex speed") - 0.03)
        player_name "Ya Tuhan!{p=1}{nw}"

    return

label micoe_bj_cum:
    if M_diane.is_state(S_diane_jizz_checkup_extra_hand):
        player_name "Ahh, ini dia!"

        pause
        show micoe_bj cum
        player_name "HNNGGG!!!" with flash
        pause
        player_name "Haah... Haah..."

        pause

        scene expression player.location.background_closeup
        show player 263c at right
        show micoe f_full a_cup1
        with dissolve
        pause
        show micoe f_spit a_cup2 with dissolve
        micoe "{i}*Meludah*{/i}"

        show micoe f_laugh a_cup3 with dissolve
        micoe "Mmm, rasanya cukup subur bagiku!"

        show micoe f_sexy
        show player 262b
        player_name "Itu luar biasa!"

        show player 263c
        micoe "Terima kasih."

        micoe "Kembalilah, dan kita akan melakukannya lagi kapan-kapan, ya?"

        show player 262b
        player_name "Y-ya, oke."

        show player 263c
        show micoe f_laugh
        micoe "hehe."

        hide micoe with dissolve
        pause
        show player 261b with dissolve
        pause
        hide player with dissolve

        scene expression "backgrounds/location_hospital_room_day_blur.jpg"
        call expression game.dialog_select("diane_check_up_results")
        $ M_diane.trigger(T_diane_cup_o_jizz)
    else:

        player_name "Oh sial."

        pause
        player_name "aku akan keluar!"

        player_name "aku akan-"

        show micoe_bj cum
        player_name "HNNGGG!!!" with flash
        pause
        player_name "Haaah... Haah..."

        show micoe_bj mouth_full with dissolve
        micoe "Ahhh."

        show micoe_bj look with dissolve
        micoe "MM."

        show micoe_bj talk with dissolve
        micoe "Hehehe!"


        scene expression player.location.background_blur
        show player 261b at right
        show micoe
        with dissolve
        pause
        show player 14f
        player_name "Wow, kamu menelannya!"

        show player 13f with dissolve
        show micoe f_sexy
        micoe "saya tahu..."

        micoe "Aku gadis yang nakal, bukan?"

        show player 29f with dissolve
        player_name "Y-ya..."

        show player 13f with dissolve
        micoe @ f_laugh "Hehehe!"

        pause
        micoe "Baiklah, manis."

        micoe "Saya harus kembali bekerja."

        show player 14f
        player_name "Oke."

        show player 13f
        micoe "Kembalilah dan temui aku segera, oke?"

        show player 14f
        player_name "Saya akan."

        hide micoe
        show player 13 at left
        with dissolve
        pause
        show player 29 with dissolve
        player_name "... Wah!"

        hide player with dissolve
        $ game.timer.tick()
    $ persistent.cookie_jar["Micoe"]["unlocked"] = True
    $ persistent.cookie_jar["Micoe"]["gallery"]["01_unlocked"] = True
    $ renpy.end_replay()
    $ player.go_to(L_hospital_floor2)
    $ game.main()

label diane_check_up_results:
    show player 13f at right
    show micoe f_normal a_cup3
    with dissolve
    micoe "Saya belum pernah melihat orang mengisi seluruh cangkir!"

    show player 14f
    player_name "Hehe, ya."

    show player 13f
    micoe "Aku akan segera membawanya ke laboratorium."

    micoe "Jika kamu hanya ingin menunggu di sini, pacarmu akan segera kembali."

    show player 14f
    player_name "Baiklah terima kasih."

    show player 13f
    show micoe a_idle:
        flip
        xoffset -300
    with dissolve
    pause
    show micoe:
        unflip
        xoffset 0
    with dissolve
    micoe "Anda tahu, jika hubungan dengan pacar Anda tidak berjalan mulus."

    show micoe f_sexy
    micoe "Anda harus kembali dan menemui saya."

    micoe "Aku akan mengguncang duniamu, Nak."

    show micoe f_wink
    show player 29f with dissolve
    player_name "Y-ya, oke."

    show player 3f at Position (xoffset=-8)
    show micoe f_laugh
    micoe "Hehe, kamu lucu sekali!"

    show micoe f_sexy
    show player 29f
    player_name "T-terima kasih."

    show player 3f at Position (xoffset=-8)
    hide micoe with dissolve
    pause
    show player 12f with dissolve
    player_name "Wow, itu adalah wanita yang sangat maju..."

    show player 13f with None
    show diane b_gown:
        flip
    with dissolve
    diane "Hai, tampan."

    show player 14f
    player_name "Hai, {b}Diane{/b}."

    player_name "Apa keputusannya?"

    show player 13f
    diane "Saya belum yakin."

    show player 10f
    player_name "Oh?"

    show player 13f
    diane "Perawat seharusnya kembali dengan hasilnya."

    show player 14f
    player_name "Y-ya, milikku juga."

    show player 13f
    show diane b_gown_dress f_down_front with dissolve
    show player 426f
    pause
    show diane b_casual_remove6 with dissolve
    pause
    show diane b_casual_remove5 f_normal with dissolve
    diane "Semuanya baik-baik saja di pihak Anda?"

    show diane b_casual_remove4 with dissolve
    show player 5f
    player_name "Hmm?"

    show diane b_casual_remove1 with dissolve
    show player 17f
    player_name "Oh ya!"

    show diane b_casual with dissolve
    show player 14f
    player_name "Tidak ada masalah."

    show player 13f
    diane "Bagus."

    pause
    diane "Saya kira kita hanya perlu-"

    "{i}*Ketuk* *Ketuk*{/i}"

    show player 14f
    player_name "Masuk."

    show player 13f zorder 1 with None
    show diane zorder 0:
        unflip
        xoffset -150
    show micoe
    with dissolve
    micoe "Baiklah, saya sudah mendapatkan hasilnya di sini."

    show diane f_sad
    diane "Oh, tolong jadilah kabar baik..."

    diane "Aku tidak mandul, kan?"

    micoe @ f_laugh "Haha, tidak sayang."

    show diane f_normal
    micoe "Kamu tidak mandul."

    micoe "Dengan bertambahnya usia Anda, hal itu tidak akan mudah tetapi Anda pasti masih bisa hamil."

    diane "Oh, sungguh melegakan!"

    show player 14f
    player_name "Bagaimana dengan saya?"

    show player 13f
    micoe "Sebaliknya Anda sangat subur!"

    micoe "Dokter bilang dia terkejut saya tidak hamil hanya dengan membawa botol itu ke laboratorium."

    show micoe f_laugh
    show diane f_laugh
    show player 17f
    micoe "Haha!"

    diane "Haha!"

    show micoe f_normal
    player_name "..."
    show diane f_normal
    show player 13f
    micoe "Jadi kalian berdua sebaiknya berangkat."

    diane "Ada lagi yang perlu kami ketahui?"

    micoe "Pastikan Anda melakukan hubungan intim sesering mungkin untuk mendapatkan peluang terbaik."

    show diane f_smirk
    diane "Itu seharusnya tidak menjadi masalah..."

    show player 3f at Position (xoffset=-8) with dissolve
    show micoe f_sexy
    micoe "Anda wanita yang beruntung."

    show diane f_laugh
    diane "Apa aku tidak mengetahuinya!"

    show diane f_normal
    show micoe f_normal
    pause
    show diane f_normal:
        flip
        xoffset 300
    with dissolve
    diane "Ayo tampan."

    diane "{b}Ayo kembali ke rumah{/b}."

    diane "saya kelelahan."

    show player 13f with dissolve
    show diane zorder 0:
        unflip
        xoffset -150
    with dissolve
    micoe "Semoga beruntung!"

    show player 14f
    player_name "Terima kasih!"

    hide player
    hide diane
    hide micoe
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

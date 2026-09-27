label dewitt_dialogue_office_dewitt_eve_meet_up:
    scene expression game.timer.image("dewitt_office_c{}")
    show player 10 with dissolve
    player_name "Saya harus memberinya ruang untuk saat ini."

    player_name "Dan saya juga harus {b}mengunjungi Eve di taman pada malam hari{/b}."

    return

label dewitt_dialogue_office_dewitt_end_intro:
    scene expression game.timer.image("dewitt_office_c{}")
    show dewitt 18 at left
    show player 14f at right
    with dissolve
    player_name "Hai, {b}Melodi{/b}!"

    show player 13f
    show dewitt 19
    dewitt "Mmm, hai {b}[firstname]{/b}!"

    dewitt "Aku berharap kamu akan datang mengunjungiku malam ini..."

    show dewitt 18
    show player 14f
    player_name "Heh, kamu sedang ingin bersenang-senang?"

    show player 13f
    show dewitt 19
    dewitt "Aku selalu bersemangat untukmu, {b}[firstname]{/b}."

    dewitt "Kamu ingin langsung melakukannya atau haruskah aku menari untukmu dulu?"

    show dewitt 18
    return

label dewitt_dialogue_office_dewitt_end_dance:
    show dewitt 19
    dewitt "Silakan duduk, sayang."

    scene expression game.timer.image("dewitt_office_sex{}")
    $ M_dewitt.set("sex speed", 0.125)
    show dewitts 1
    show dewitt cloths 1b
    show player dewitts 1 zorder 2 at left
    with dissolve
    pause
    hide dewitts
    hide dewitt
    show expression AnimatedImage("dewitt_twerk", [1,2,3,4,5,6,7,8,9,10], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    with dissolve
    dewitt "Hmm..."

    dewitt "Kamu suka itu, sayang?"

    player_name "Oh ya!"

    show player dewitts 1b with hpunch
    show player dewitts 1 with dissolve
    dewitt "Oh!"

    dewitt "Saya suka ketika Anda melakukan itu!"

    pause
    dewitt "Saya pikir saya harus kehilangan beberapa pakaian ini!"

    dewitt "Bagaimana menurutmu, gula?"

    player_name "Y-ya!"

    hide dewitts
    hide dewitt_twerk
    hide dewitt
    hide player
    with dissolve

    scene expression game.timer.image("dewitt_office_c{}")
    show dewitt 20 zorder 1 with dissolve
    pause
    show dewitt 31b with dissolve
    pause
    show dewitt 32b with dissolve
    pause
    show dewitt 29 with dissolve
    dewitt "Ayo ganti musiknya juga!"

    show dewitt 35b at Position (xoffset=354) with dissolve
    pause

    show player 626 zorder 0 at Position (xpos=550) with dissolve
    pause
    show dewitt 36 at Position (xoffset=354)
    dewitt "Dan apa yang kamu lakukan di belakang sana?"

    dewitt "Pernahkah kamu mendengar bahwa kamu tidak boleh menyentuh para penari?"

    show dewitt 35 at Position (xoffset=354)

    show player 629
    show player_hand 629b_629c zorder 2 at Position (xpos=550)
    with dissolve
    player_name "Ups..."

    show player 628
    show dewitt 36 at Position (xoffset=354)
    dewitt "Bo nakal-"


    show player_hand 629d
    show dewitt 37 at Position (xoffset=290) with hpunch
    show player 626
    hide player_hand
    with dissolve
    dewitt "Hai!"

    show dewitt 38 at Position (xoffset=290)
    show player 627
    with dissolve
    dewitt "Kembalilah ke sofa itu, nakal!"


    $ M_dewitt.set("sex speed", 0.125)
    scene expression game.timer.image("dewitt_office_sex{}")
    show dewitts 1
    show dewitt cloths 1c
    show player dewitts 1 zorder 2 at left
    with dissolve
    dewitt "Mmm, bagaimana keadaannya sekarang?"

    hide dewitts
    hide dewitt
    show expression AnimatedImage("dewitt_twerk", ["1c","2c","3c","4c","5c","6c","7c","8c","9c","10c"], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    with dissolve
    player_name "Kamu sangat seksi, {b}Melodi{/b}!"

    dewitt "Heh, terima kasih, gula!"

    pause
    show player dewitts 1b with hpunch
    show player dewitts 1 with dissolve
    dewitt "Hmm!"

    dewitt "Dasar anak nakal!"

    dewitt "Kamu membuatku basah kuyup!"

    pause
    dewitt "Anda siap untuk final?"

    player_name "Ya, Bu!"

    dewitt "Hehe, perhatikan baik-baik..."

    scene black with fade
    pause 0.25
    $ M_dewitt.set("sex speed", 0.125)
    scene expression game.timer.image("dewitt_office_sex{}")
    show dewitts 1
    show player dewitts 1 zorder 2 at left
    with dissolve
    dewitt "Mmm, lihat aku mengerjakan vagina ini, sayang!"

    hide dewitts
    show expression AnimatedImage("dewitt_twerk", ["1b","2b","3b","4b","5b","6b","7b","8b","9b","10b"], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    with dissolve
    pause
    show player dewitts 1b with hpunch
    show player dewitts 1 with dissolve
    dewitt "Sial!"

    dewitt "Aku tidak tahan lagi, sayang!"

    dewitt "Aku butuh penis sebesar itu!"

    pause
    return


label dewitt_dialogue_office_dewitt_end_bj:
    show player 14f
    player_name "Bisakah kamu memberiku BJ lagi?"

    show player 13f
    show dewitt 19 with dissolve
    dewitt "Saya ingin sekali!"

    dewitt "Anda tahu saya pernah memainkan beberapa seruling sebelumnya."

    dewitt "Tapi seruling kulitmu adalah yang terbaik yang pernah kunikmati saat membungkus bibirku."

    dewitt "Tapi cukup bicara, izinkan saya memberi Anda pertunjukan pribadi lainnya."

    scene black with fade

    $ M_dewitt.set("sex speed", 0.175)
    scene expression game.timer.image("dewitt_office_bj{}")
    show dewitt bj 1 at left
    with dissolve
    pause
    show dewitt bj 2
    pause
    show dewitt bj 3
    pause
    show dewitt bj 4
    pause
    hide dewitt
    show expression AnimatedImage("dewitts_bj", [1,2,3,4,5,6,7,8,9,10,11,12], M_dewitt) as dewitts_bj
    return

label dewitt_dialogue_office_dewitt_end_sex:
    show dewitt 19
    dewitt "Saya berharap Anda ingin langsung bergabung!"

    dewitt "Mari kita lihat siapa yang paling cepat melepaskan pakaiannya!"

    show dewitt 20 with dissolve
    show player 26f
    player_name "Apa tidak ada hitungan mundur?"

    show dewitt 31f with dissolve
    show player 8f with dissolve
    dewitt "Tidak!"

    show dewitt 32f with dissolve
    show player 261 with dissolve
    pause
    show dewitt 18b with dissolve

    show player 263 with dissolve
    pause
    show dewitt 19b
    dewitt "Sepertinya aku menang!"

    dewitt "Sekarang buat aku cum!"

    show player 262
    player_name "Ya, Bu!"

    label dewitt_twerk_end:
        scene black with fade
        pause 0.25
        scene expression game.timer.image("dewitt_office_sex{}")
        show dewitts 1
        show player dewitts 2 zorder 2 at left
        with dissolve
        dewitt "Berikan padaku, {b}[firstname]{/b}!"

        hide player
        show dewitts 3 at left
        with dissolve
        dewitt "Berhenti bermain-main di sana! Saya tidak sabar!"

        show dewitts 4
        dewitt "Di sini, gula..."

        show dewitts 5 with dissolve
        pause
        $ M_dewitt.set("sex speed", 0.125)
        show expression AnimatedImage("dewitts", [5,6,7,8,9,10,11,12,13,14], M_dewitt) as dewitts
        $ anim_toggle = True
    jump expression game.dialog_select("dewitt_sex_loop")

label dewitt_dialogue_office_intro:
    scene expression game.timer.image("dewitt_office_c{}")
    show dewitt 1b at left
    show player 14f at right
    with dissolve
    player_name "Halo, {b}Nona Dewitt{/b}."

    show player 13f
    show dewitt 2b
    dewitt "Halo, {b}[firstname]{/b}!"

    dewitt "Apakah Anda memerlukan sesuatu?"

    show dewitt 1b
    return

label dewitt_dialogue_office_flute_lessons:
    show player 26f
    player_name "Saya berharap Anda dapat membantu mengajari saya cara menguasai seruling saya."

    show player 13f
    show dewitt 19 with dissolve
    dewitt "Saya berharap Anda akan bertanya!"

    dewitt "Temui aku di sini malam ini dan kita bisa bermain bersama!"

    hide player
    show dewitt 6 at right
    with dissolve
    dewitt "Dan jangan terlambat atau aku harus bermain solo."

    return

label dewitt_dialogue_office_leave:
    show player 14f
    player_name "Tidak saat ini."

    show player 13f
    show dewitt 2b
    dewitt "Baiklah. Semoga harimu menyenangkan!"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

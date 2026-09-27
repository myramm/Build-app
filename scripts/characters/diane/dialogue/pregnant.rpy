label diane_button_event_pregnancy:
    $ M_diane.pregnancy.set('announced_pregnancy')


    scene expression player.location.background_blur
    show diane b_naked

    if not M_diane.pregnancy.number_of_babies:
        jump diane_button_event_pregnancy.initial
    jump diane_button_event_pregnancy.repeat


label diane_button_event_pregnancy.initial:
label diane_button_event_pregnancy.repeat:
    show diane f_cheese
    show player 13 at left with dissolve
    show diane f_laugh
    diane "{b}[firstname]{/b}!!"

    show player 10
    show diane f_cheese
    player_name "Apa keadaan darurat besarnya?!"

    show player 5
    show diane f_laugh
    diane "Kami berhasil!"

    diane "saya hamil!"

    show diane f_cheese
    show player 14
    player_name "Anda?!"

    player_name "Apa kamu yakin?!"

    show player 13
    show diane f_laugh
    diane "Saya yakin!"

    diane "Kamu akan menjadi seorang ayah!"

    show diane f_cheese
    show player 14
    player_name "aku akan-"

    show player 18
    show diane f_normal
    pause
    diane "Kamu baik-baik saja?"

    show player 14
    player_name "Hmm?"

    player_name "Y-ya!"

    player_name "Ini berita bagus, {b}Diane{/b}!"

    player_name "Saya sangat senang!"

    hide player
    show diane b_kiss_naked
    with dissolve
    pause
    show player 13 at left
    show diane b_naked f_laugh
    with dissolve
    diane "Hmm, aku juga!"

    diane "Oh, ini sangat mengasyikkan!"

    show diane f_normal
    diane "Saya tidak pernah menyangka akan mendapat kesempatan ini!"

    pause
    show diane f_laugh
    diane "Oh terima kasih, {b}[firstname]{/b}!"

    diane "Terima kasih, terima kasih, terima kasih!!!"

    hide player
    show diane b_kiss_naked
    with dissolve
    pause
    show player 14 at left
    show diane b_naked f_cheese
    with dissolve
    player_name "Hehe, sama-sama..."

    show player 13
    show diane f_normal
    pause
    show player 14
    player_name "Jadi apa yang harus aku..."

    player_name "{i}*Ahem*{/i} Ada yang bisa saya bantu?"

    show player 13




    diane "Hmm?"

    diane "Oh tidak!"

    diane "Terus lakukan semua yang telah Anda lakukan."

    diane "Tetaplah menjadi luar biasa, {b}[firstname]{/b}!"

    show player 14
    player_name "Itu, saya pasti bisa melakukannya!"

    show player 13
    show diane f_laugh
    diane "hehe!"

    hide player
    hide diane
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label anna_button_yoga_room_dialogue_pre:
    scene yoga_room_night
    show old_anna 2 at right
    show player 13 at left
    with dissolve
    anna "Halo, {b}[firstname]{/b}."

    show old_anna 1
    show player 14
    player_name "Hai, {b}Anna{/b}."

    show player 13
    show old_anna 2
    anna "Ada apa?"

    show old_anna 1
    return

label anna_button_yoga_room_dialogue_wheres_mrsj:
    show player 14
    player_name "Saya mencari {b}Nyonya. Johnson{/b}."

    show player 30
    player_name "Tahukah kamu di mana aku bisa menemukannya?"

    show player 5
    show old_anna 2
    anna "Biasanya dia mengajar pada siang hari."

    anna "Dia pasti sudah sampai di rumah sekarang..."

    show old_anna 1
    show player 14
    player_name "Oh. Jadi begitu. Terima kasih!"

    show player 13
    show old_anna 3
    anna "Tidak masalah!"

    return

label anna_button_yoga_room_dialogue_yoga:
    show player 10
    player_name "Apakah Anda ingin berlatih beberapa pose yoga dengan saya?"

    show player 5
    show old_anna 3
    anna "Tentu saja!!"

    show old_anna 2
    anna "Saya suka ketika seseorang dapat membantu saya mencapai... Postur yang sulit..."

    show old_anna 1
    show player 33
    player_name "Benar, Anda cukup fleksibel seingat saya."

    show player 13
    show old_anna 2
    anna "Baiklah, ayo cari matras yoga..."

    hide old_anna
    scene location_gym_yoga_front
    with fade
    show player 413 at left
    show old_anna 13
    with dissolve
    anna "Posisi manakah yang harus kita latih?"

    return

label anna_button_yoga_room_dialogue_post:
    show player 36 with dissolve
    player_name "Sebenarnya sudahlah, sampai jumpa lagi."

    show player 1
    show old_anna 2
    with dissolve
    anna "Oh oke, semoga malammu menyenangkan!"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

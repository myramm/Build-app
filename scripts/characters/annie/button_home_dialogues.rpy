label annie_button_home_intro:
    show player 10 at left
    show old_annie 6 at right
    with dissolve
    player_name "Hai, {b}Annie{/b}."

    show player 5
    show old_annie 5
    annie "{b}[firstname]{/b}?!"

    show old_annie 4
    annie "Apa yang kamu lakukan di rumahku?"

    show old_annie 6
    show player 12
    player_name "Itu pertanyaan yang bagus sebenarnya..."

    show player 5
    show old_annie 5
    annie "Bukankah kamu punya pekerjaan rumah yang harus kamu kerjakan?!"

    show old_annie 6
    show player 10
    player_name "Aku salah... Ya, agak..."

    show player 5
    pause
    show old_annie 5
    annie "Baiklah, berhentilah menggangguku dan lakukanlah!"

    show old_annie 6
    return

label annie_button_home_menu_alright_sheesh:
    show player 10 at left
    show old_annie 6 at right
    player_name "Oke oke!"

    player_name "Anda benar-benar harus menghilangkan tongkat itu."

    show player 5
    show old_annie 5
    annie "Apa yang kamu bicarakan?"

    show old_annie 6
    show player 14
    player_name "Anda tahu, yang ada di pantat Anda."

    show player 13
    show old_annie 8
    annie "Apakah kamu ingin ditahan?!"

    annie "Saya akan menulis surat kepada Anda, di sini dan sekarang!"

    show old_annie 1
    show player 12
    player_name "Kita bahkan tidak bersekolah, {b}Annie{/b}!"

    show player 5
    show old_annie 17 with dissolve
    annie "Itu saja, aku mendapatkan bantalan penahananku-"

    show old_annie 6 with dissolve
    show player 10
    player_name "Oke, berhenti!"

    player_name "Aku berangkat, astaga!"

    hide player
    hide old_annie
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

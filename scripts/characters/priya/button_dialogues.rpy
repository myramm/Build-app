label priya_button_intro:
    scene expression player.location.background_blur
    show player 5 at left
    show priya f_angry a_point
    with dissolve
    priya "Kamu lagi?!"

    priya "Apa yang kamu lakukan disini?!"

    show priya a_crossed with dissolve
    pause
    priya "Apakah Anda memiliki beberapa hasil untuk dilaporkan?"

    return

label priya_button_menu_no:
    show priya f_angry a_crossed
    show player 24 at left
    player_name "Tidak, maaf."

    player_name "aku hanya-"

    show player 5
    show priya a_point with dissolve
    priya "Ini adalah area terlarang karena suatu alasan!"

    priya "Kamu tidak bisa datang dan pergi sesukamu..."

    show priya a_crossed with dissolve
    show player 10
    player_name "Maafkan aku, {b}Priya{/b}."

    show player 24
    player_name "saya..."

    player_name "aku akan pergi..."

    show player 5
    show priya f_facepalm a_facepalm with dissolve
    priya "{i}*Huh*{/i}"

    priya "Tidak, aku minta maaf... aku minta maaf."

    show priya f_hopeful a_idle with dissolve
    priya "Aku tidak bermaksud membentakmu."

    show priya f_normal
    priya "Hanya saja... Berbahaya bagimu berada di sini."

    priya "Jadi tolong, jangan kembali kecuali Anda memiliki sesuatu untuk dilaporkan."

    show player 10
    player_name "O-oke."

    hide player
    hide priya
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

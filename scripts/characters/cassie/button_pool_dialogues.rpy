label cassie_pool_dialogue_rules:
    scene location_pool_closeup1
    show cassie 2 at right
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    cassie "Bisakah saya membantu Anda dengan sesuatu?"

    show cassie 4
    if wearing_swimsuit:
        show player 45
    else:
        show player 108f
    player_name "Umm... Apa lagi aturannya?"

    if wearing_swimsuit:
        show player 53f
    else:
        show player 1
    show cassie 2
    cassie "Yah, kamu tidak bisa berenang dengan pakaianmu..."

    show cassie 3
    cassie "Anda harus {b}menggunakan salah satu ruang ganti untuk mengenakan baju renang{/b}!"

    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    show cassie 4
    player_name "Oh. Besar! Terima kasih!"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

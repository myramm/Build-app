label kassy_first_visit:
    show player 1f at right
    show kassy:
        flip
    with dissolve
    kassy "Selamat datang di {b}Dewa Asmara{/b}. Nama saya {b}Kassy{/b}, adakah yang bisa saya bantu temukan hari ini?"

    show player 2f
    player_name "Tidak, terima kasih, aku hanya melihat sekeliling."

    show player 1f
    kassy "Baiklah. Baiklah, beri tahu saya jika Anda memerlukan bantuan."

    show player 2f
    player_name "Akan berhasil! Terima kasih, {b}Kassy{/b}."

    show player 1f
    kassy "Dengan senang hati!"

    return

label kassy_repeat:
    show player 2f at right
    show kassy at flip
    with dissolve
    player_name "Hai {b}Kassy{/b}!"

    show player 1f
    kassy "Halo, ada yang bisa saya bantu?"

    show player 2f
    player_name "Tidak ada apa-apa saat ini, hanya browsing."

    show player 1f
    kassy "Baiklah. Baiklah, hubungi aku jika kamu butuh sesuatu."

    show player 2f
    player_name "Akan berhasil! Terima kasih, {b}Kassy{/b}."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

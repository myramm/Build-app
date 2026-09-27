label button_ross_paint_with_body:
    scene expression player.location.background_closeup
    show old_ross 1 at left
    show player 2f at right
    with dissolve
    player_name "Kamu bilang kamu punya satu teknik terakhir untuk mengajariku?"

    show old_ross 2
    show player 1f
    ross "Oh ya! Itu bagus juga!"

    ross "Tapi aku tidak bisa mengajarimu di sini. Anda harus datang menemui saya di {b}kantor saya{/b} {b}malam ini{/b}."

    show old_ross 1
    show player 2f
    player_name "Kedengarannya sangat luar biasa!"

    player_name "Sampai jumpa di sana, {b}Nona Ross{/b}."

    return

label button_ross_end_intro:
    scene expression player.location.background_closeup
    show player 1f at right
    show old_ross 2 at left
    with dissolve
    ross "Itu pahlawan kecilku!"

    show player 2f
    show old_ross 1
    player_name "Heh, hei {b}Nona Ross{/b}."

    show player 1f
    show old_ross 13 with dissolve
    ross "Apakah Anda sibuk {b}malam ini{/b}?"

    ross "Saya berharap Anda mungkin tertarik untuk mempelajarinya lagi... {i}Pelajaran privat{/i}?"

    ross "Aku hanya ingin mengajarimu lebih banyak..."

    show old_ross 12
    return

label button_ross_end_yes:
    show player 2f
    player_name "Tentu, kedengarannya luar biasa!"

    show player 1f
    show old_ross 11
    ross "Luar biasa!"

    ross "Datang saja {b}kunjungi saya di kantor saya{/b} nanti hari ini."

    show old_ross 10
    show player 2f
    player_name "Saya tidak sabar!"

    show player 1f
    show old_ross 11
    ross "Sekarang, apakah ada hal lain yang bisa saya bantu?"

    show old_ross 10
    return

label button_ross_end_no:
    show player 10f
    player_name "Oh, saya tidak bisa malam ini, {b}Nona Ross{/b}..."

    player_name "... Saya punya rencana lain."

    show player 11f
    show old_ross 25
    ross "Ah, sayang sekali."

    ross "... Beritahu aku jika ada perubahan."

    show old_ross 11
    ross "Aku akan selalu menyediakan waktu untukmu, {b}[firstname]{/b}."

    show player 1f
    ross "Sekarang, apakah ada hal lain yang bisa saya bantu?"

    show old_ross 10
    return

label button_ross_get_paint_grace_reminder:
    scene expression player.location.background_closeup
    show player 2f at right
    show old_ross 10 at left
    player_name "... Kepada siapa saya harus {b}bertanya tentang cat{/b} lagi?"

    show player 1f
    show old_ross 11
    ross "Mulailah dengan {b}Malam{/b}."

    ross "Jika kita beruntung, dia mungkin punya cat tambahan di rumah yang bisa kita gunakan."

    show player 2f
    show old_ross 10
    player_name "Baiklah, aku akan pergi dan bertanya padanya."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

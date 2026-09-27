label ronda_pool_dialogue_pre_cassie_fun:
    show ronda b_swim
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    ronda @ -m_talk "..."
    ronda "Apa yang kamu lakukan di sini?"

    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    player_name "Baru saja berolahraga!"

    player_name "Saya pikir saya harus memulai dari suatu tempat, dan ini dapat membantu saya bersiap untuk kualifikasi!"

    if wearing_swimsuit:
        show player 51
    else:
        show player 11
    ronda "Dengar, aku tidak membantumu, apalagi masuk ke dalam air bersamaan denganmu... Jadi lupakan saja, oke?"

    if wearing_swimsuit:
        show player 53
    else:
        show player 26
    player_name "Tidak apa-apa!"

    player_name "aku bisa mengaturnya sendiri..."

    if wearing_swimsuit:
        show player 51
    else:
        show player 11
    ronda @ f_eyeroll "Ugh... Terserah."

    return

label ronda_pool_dialogue_after_cassie_fun:
    show ronda b_swim f_upset
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    ronda "Di sini untuk mengunjungi {b}Cassie{/b} sedikit?"

    if wearing_swimsuit:
        show player 51f
    else:
        show player 12
    player_name "Uhh... Aku di sini hanya untuk berenang?"

    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ronda "Kamu bisa berhenti berpura-pura..."

    ronda "... Anda di sini bukan untuk berlatih, seperti saya."

    if wearing_swimsuit:
        show player 51f
    else:
        show player 12
    player_name "Uhh... Oke?"

    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ronda @ f_upset_angry "Ugh... Kau menyedihkan."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

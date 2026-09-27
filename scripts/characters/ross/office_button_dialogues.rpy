label button_ross_office_generic_pre_hscene:
    scene expression player.location.background_closeup
    show old_ross 11 at left
    show player 1f at right
    with dissolve
    ross "Halo, {b}[firstname]{/b}."

    ross "Senang sekali Anda mengunjungi saya!"

    show old_ross 10
    show player 2f
    player_name "Hai, {b}Nona Ross{/b}."

    show old_ross 11
    show player 1f
    ross "Apa yang bisa saya lakukan untuk Anda?"

    return

label button_ross_office_generic_post_hscene:
    scene expression player.location.background_closeup
    show old_ross 10 at left
    show player 2f at right
    with dissolve
    player_name "Hai, {b}Nona Ross{/b}!"

    show player 1f
    show old_ross 27 with dissolve
    ross "{b}[firstname]{/b}! Senang bertemu denganmu!"

    show old_ross 13 with dissolve
    ross "... Saya harap Anda di sini untuk pelajaran privat lainnya?"

    return

label ross_dialogue_office_private_lessons:
    show old_ross 12
    show player 2f
    player_name "Ya, aku menyukainya!"

    show old_ross 13
    show player 1f
    ross "Mmm, cepat dan kunci pintunya!"

    show old_ross 12
    show player 2f
    player_name "O-oke..."

    return

label ross_dialogue_office_leave:
    scene expression player.location.background_closeup
    show old_ross 10 at left
    show player 2f at right
    player_name "Ah, aku tidak butuh apa pun."

    player_name "Maaf mengganggumu."

    show old_ross 11
    show player 1f
    ross "Tidak merepotkan, {b}[firstname]{/b}!"

    ross "Membantu seniman muda berbakat adalah keahlianku!"

    show old_ross 10
    show player 2f
    player_name "Hehe, oke."

    player_name "aku harus pergi..."

    show old_ross 11
    show player 1f
    ross "Ah, baiklah."

    ross "Sampai jumpa, {b}[firstname]{/b}."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

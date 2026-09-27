label annie_dialogue_music_classroom_intro:
    show player 2
    player_name "Hai, {b}Annie{/b}."

    show player 1
    show old_annie 3
    annie "Saya mencoba berkonsentrasi."

    show old_annie 1
    show player 3
    player_name "..."
    show player 29 with dissolve
    player_name "Maaf-"

    show player 3 with dissolve
    show old_annie 7
    annie "SAYA BERKONSENTRASI!"

    show old_annie 6
    show player 2f
    player_name "Dan aku pergi!"

    player_name "Astaga..."

    hide player
    hide old_annie
    with dissolve
    return

label annie_dialogue_ross_ask_model:
    show player 2 at left
    show old_annie 1 at right
    player_name "Saya sedang mengerjakan proyek untuk {b}Miss Ross{/b} dan itu memerlukan model langsung."

    player_name "Apakah Anda tertarik?"

    show player 1
    show old_annie 3
    annie "Tidak bisa melakukannya. Saya punya putaran!"

    show player 10
    show old_annie 1
    player_name "Hah?"

    show player 11
    show old_annie 4
    annie "Aku harus berpatroli untuk mencari penjahat!"

    annie "Minggir dari hadapanku!"

    hide old_annie
    hide player
    show player 12f
    with dissolve

    player_name "Baiklah, sialan!"

    player_name "Aneh..."

    return

label annie_dialogue_leave:
    show player 14
    player_name "Hai {b}Annie{/b}!"

    show old_annie 5
    show player 1
    annie "Lakukan dengan cepat!"

    show old_annie 6
    show player 17
    player_name "Oh, tidak ada... Aku hanya menyapa!"

    show old_annie 4
    show player 18
    annie "Aku sedang bertugas memantau aula... Dan kamu membuang-buang waktuku."

    show old_annie 6
    show player 11
    player_name "..."
    show player 12
    player_name "Baiklah. Maaf mengganggumu. Astaga!"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

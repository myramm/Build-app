label button_consuela_intro:
    show player 10 at left
    show consuela
    with dissolve
    player_name "Hey there, {b}Consuela{/b}."
    show player 5
    show consuela f_unsure
    consuela "Hello, {b}Mister [firstname]{/b}."
    show consuela f_normal
    show player 12
    player_name "You can just call me {b}[firstname]{/b}..."
    show player 5
    show consuela f_unsure
    consuela "¿Qué?"
    consuela "No hablo inglés."
    show consuela f_normal
    show player 10
    player_name "Oh, uhh..."
    show player 5
    pause
    consuela @ -m_talk "..."
    show player 3 with dissolve
    player_name "..."
    show consuela f_unsure
    consuela "Ehh... I clean now."
    consuela "¿Sí?"
    show consuela f_normal
    show player 10 with dissolve
    player_name "Oh, yes."
    player_name "Err, I mean... Sí!"
    show player 14
    player_name "Thank you, {b}Consuela{/b}."
    show player 13
    consuela "You're welcome, {b}Mister [firstname]{/b}."
    hide player
    hide consuela
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

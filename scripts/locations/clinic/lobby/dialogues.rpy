label hospital_desk_caught_dialogue:
    scene hospital_desk
    show roz_desk at left
    show player 13f at right
    with None
    show old_roz 1 behind roz_desk at left
    if Game.is_christmas():
        show xtra 35 zorder 2 at Position(xalign = 0.1, yalign = 0.251)
    with easeinleft
    show player 22f
    show old_roz 2
    with hpunch
    roz "Can I help you?"

    show old_roz 1
    show player 10f
    player_name "Erm... I..."

    show player 11f
    return

label hospital_jizz_checkup:
    scene hospital_desk
    show old_roz 1 at left
    if Game.is_christmas():
        show xtra 35 zorder 2 at Position(xalign = 0.1, yalign = 0.251)
    show roz_desk at left
    show player 13f at right
    show diane b_casual:
        xoffset -250
    with dissolve
    diane "H-halo."

    show old_roz 2
    roz "Ya?"

    show old_roz 1
    diane "I have an appointment for a check up."

    show old_roz 11b at Position (xoffset=-40) with dissolve
    roz "Hmm."

    pause
    show old_roz 2 with dissolve
    roz "{b}Diane{/b}?"

    show old_roz 1
    diane "Itu benar."

    show old_roz 2
    roz "Go on up to the second floor exam room and change into a gown."

    roz "The nurse will be up to see you momentarily."

    show old_roz 1
    diane "O-oke."

    show diane:
        flip
        xoffset 300
    with dissolve
    diane "C'mon, {b}[firstname]{/b}."

    hide player
    hide diane
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

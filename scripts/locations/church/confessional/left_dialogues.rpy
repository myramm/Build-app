label confessional_left_empty:
    scene church_confession
    show player 283 at Position(xpos=280)
    with dissolve
    player_name "Bless me Father, for I have sinned."

    show player 278
    player_name "..."
    show player 284
    player_name "......"
    show player 280
    player_name "Father?"

    player_name "( There's no one here? )"

    show player 10
    player_name "( I guess there's no priest around at this time... )"

    hide player
    hide church_confession
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

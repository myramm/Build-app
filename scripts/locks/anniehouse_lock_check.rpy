label anniehouse_lock_check:
    scene expression player.location.background_blur

    if game.timer.is_night() and destination != L_annie_front:
        show player 10 with dissolve
        player_name "( It's pretty late, I should be getting home. )"

        hide player with dissolve
        $ player.go_to(L_annie_front)
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

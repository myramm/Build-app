label gym_lock_check:
    scene expression player.location.background_blur

    if game.timer.is_night() and destination != L_gym_front:
        show anon with dissolve
        anon @ -m_talk "( It's closed now, I can come back tomorrow. )"

        hide anon with dissolve
        $ player.go_to(L_gym_front)
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

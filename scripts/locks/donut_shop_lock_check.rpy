label donut_shop_lock_check:
    scene expression player.location.background_blur

    if destination == L_donutshop_interior and game.timer.is_dark():
        show anon with dissolve
        anon @ -m_talk "( I should come back during the day while they're open. )"
        hide anon with dissolve
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label dealership_intro:
    scene expression player.location.background_blur
    show anon with dissolve
    anon @ -m_talk "( Hmm, this place is smaller than I imagined... )"
    anon @ f_surprised_teeth -m_talk "( I wonder what they'll have in my price range? )"
    pause
    if game.timer.is_night():
        anon @ -m_talk "( I should {b}come back tomorrow and talk with somebody{/b}. )"
    else:
        anon @ -m_talk "( I should {b}head inside and talk with somebody{/b}. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

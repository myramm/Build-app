label bank_lobby_intro:
    scene expression player.location.background_blur
    show anon with dissolve:
        xoffset 300
    anon f_surprised "( Whoa. )"

    anon f_normal @ -m_talk "( This place has changed a lot since the last time I was in here... )"

    pause
    anon @ -m_talk "( I should {b}find an employee{/b} to speak with about {b}[deb_name]{/b}'s loan. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

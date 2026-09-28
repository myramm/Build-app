label ano21_home_home_lobby:
    scene expression player.location.background_blur
    show anon f_worried with dissolve
    debbie "I just can't believe it!"
    jenny "Seriously?"
    debbie "He always seemed like such a nice guy on the TV..."
    show anon f_skeptical with dissolve:
        flip
        xoffset -500
    anon @ -m_talk "( Hmm? )"
    anon f_worried @ -m_talk "( It sounds like the girls are in the living room. )"
    jenny "Umm, no he didn't."
    jenny "It was so obvious he was faking all that stuff."
    anon @ -m_talk "( What in the heck are they talking about? )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

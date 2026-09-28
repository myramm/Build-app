label ano12_dark_warehouse:
    scene expression player.location.background_blur
    show anon f_worried a_sides with dissolve:
        flip
        xoffset 200
    anon @ -m_talk "( Okay, I can do this... )"
    anon @ -m_talk "( I just need to find a good spot to scope the place out. )"
    anon f_snarky @ -m_talk "( They'll never even know I'm here. )"
    hide anon with dissolve
    return


label ano12_oops_warehouse_door:
    scene expression player.location.background_blur
    show anon f_surprised with dissolve:
        flip
        xoffset 200
    anon @ -m_talk "( I can't just waltz in the front door! )"
    anon f_thinking @ -m_talk "( There should be a place along the perimeter where I can observe without being seen. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

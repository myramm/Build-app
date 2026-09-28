label mel01_init_net:
    scene expression background(400, 392, 5.) as stage
    show anon f_worried with dissolve:
        xoffset 250
    anon @ -m_talk "( {b}Melonia{/b} looks mad, and there's no way I manage to sneak past... )"
    anon @ -m_talk "( Perhaps I should just bite the bullet and {b}speak to her{/b}? )"
    hide anon with dissolve
    return


label mel01_hint_net:
    scene expression background(600, 512, 3.) as stage
    show anon f_worried with dissolve:
        xoffset 250
    anon @ -m_talk "( I better speak to {b}Ricky{/b} first. )"
    anon f_surprised_teeth @ -m_talk "( I don't want to find out what {b}Melonia{/b} might do if she catches me running around the garden! )"
    hide anon with dissolve
    return


label mel01_find_net:
    scene expression background(896, 504, 3.5) as stage
    show anon a_net f_normal_low with dissolve:
        flip
    anon @ -m_talk "( Hmm. )"
    anon @ -m_talk "( This must be what {b}Ricky{/b} was talking about. )"
    anon @ -m_talk "( {b}I should bring it to him{/b}. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

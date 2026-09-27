label jos01_init_dealership_showroom:
    scene expression player.location.background_blur
    show anon f_surprised with dissolve
    anon @ -m_talk "(Hmm?)"


    if M_rump.state is None:
        anon @ -m_talk "( Is that {b}Mayor Rump{/b}?! )"

        anon f_skeptical @ -m_talk "( What is he doing here? )"


    elif M_kim.state is None:
        anon @ -m_talk "( It looks like {b}Josephine{/b}'s father is arguing with {b}Kim{/b} about something... )"

        anon f_confused @ -m_talk "( ... I wonder what that's about? )"

    else:

        anon @ -m_talk "( I've never seen that girl before... )"

        anon f_confused @ -m_talk "( ... I wonder who she is? )"


    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

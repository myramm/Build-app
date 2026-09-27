label treehouse_lock_check:
    scene expression player.location.background_blur

    if M_anon.is_state(S_ano16_tree) and player.location == L_treehouse_interior:
        show anon f_surprised with dissolve
        anon @ -m_talk "( ?!! )"
        anon @ -m_talk "( What has he got there? I have to know. )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano16_tree) and motion not in route(L_treehouse,
                                                               L_treehouse_ladder,
                                                               L_treehouse_interior):

        anon "( {b}Erik{/b}'s waiting for me {b}up there{/b}. )"

    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

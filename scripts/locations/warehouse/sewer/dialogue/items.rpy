label warehouse_sewer_pipe_dialogue:
    $ renpy.dynamic(count=M_player.increment('sewer', 1))

    scene expression background(312, 360, 2.5, l=L_warehouse_sewer) with None
    show anon:
        flip
        xoffset -250

    if M_anon.is_state(S_ano27_jabb):
        show anon o_sewage

    if count in (2, 5):
        show anon f_unimpressed
    elif count == 3:
        show anon f_worried
    else:
        show anon f_disgusted_low

    with dissolve

    if count == 1:
        anon @ -m_talk "..."
    elif count == 2:
        anon @ -m_talk "( Nope. )"

    elif count == 3:
        anon @ -m_talk "( Y-you can't make me! )"

    elif count == 4:
        anon @ -m_talk "( Nuh, uh! )"

    elif count == 5:
        anon @ -m_talk "( You know there's a word for players like you... )"

        $ M_player.set('sewer', 1)

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

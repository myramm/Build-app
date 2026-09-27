label jenXX_pink_extra:
    call scene_ivy_jane
    $ unlock_scene('Ivy', '06_unlocked')

    scene location_pink_any_closeup
    show location_pink_any_closeup_counter as counter
    show anon a_sides f_grin of_blush:
        xoffset -250
        xzoom -1

    if M_jenny.is_state(S_jenny_bring_toy_back):
        show anon a_toy1 f_shy_low
        with fade
        anon @ -m_talk "( Besides, {b}Jenny will be expecting me with her new toy{/b}. )"

        show anon a_backpack f_shy_down
        with {'master': dissolve}
        pause
        hide arms
        show anon a_sides f_grin
        with {'master': dissolve}
    else:

        with fade

    anon @ -m_talk "( Good thing I peeked, I could have completely missed that! )"

    hide anon with dissolve
    return


label jenXX_pink_extra.repeat:
    call scene_ivy_jane.repeat
    $ unlock_scene('Ivy', '06_unlocked')

    scene location_pink_any_closeup
    show location_pink_any_closeup_counter as counter
    show anon a_surprised f_surprised o_boner:
        xoffset 300
    with fade
    anon @ -m_talk "..."
    show anon a_sides f_laugh
    with {'master': dissolve}
    anon @ -m_talk "( I can't believe they're still going! )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

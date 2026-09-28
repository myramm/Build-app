label diaXX_pink_extra:
    call scene_ivy_vera
    $ unlock_scene('Ivy', '05_unlocked')

    scene location_pink_any_closeup
    show location_pink_any_closeup_counter as counter
    show anon a_shy_neck f_shy_left o_boner of_blush:
        xoffset 100
        xzoom -1
    with fade
    anon @ -m_talk "( ... It's probably time {b}I get this package back to Diane{/b}. )"
    hide anon with dissolve
    return


label diaXX_pink_extra.repeat:
    call scene_ivy_vera.repeat
    $ unlock_scene('Ivy', '05_unlocked')
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

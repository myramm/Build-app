label ano25_done_apt_hall3:
    scene location_apt_hall3_301_closeup as stage
    show location_apt_hall3_302_closeup_door2 as door behind stage
    with None
    show location_apt_hall3_302_closeup_door1 as door
    show anon a_reach f_grin:
        xoffset 200
    with dissolve
    show anon a_sides with dissolve:
        xoffset -300
        xzoom -1
    anon @ -m_talk "( Success! )"
    anon f_normal @ -m_talk "( Now I just need to {b}meet Tony at the bank on Tuesday morning{/b}. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

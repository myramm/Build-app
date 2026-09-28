label maria_lounge_knock:
    scene location_apt_hall3_301_closeup as stage
    show location_apt_hall3_302_closeup_door1 as door behind stage
    show location_apt_hall3_301_closeup as doorframe:
        crop (768, 0, 256, 768)
        right
    show anon a_knock with dissolve
    "{i}*Knock* *Knock*{/i}"
    show anon a_sides with dissolve
    pause

    if M_maria.where in L_maria_lounge.get_all_children_inclusive():
        jump maria_lounge_knock.answer

    pause
    anon @ -m_talk "( Huh... I guess there's nobody home. )"
    anon @ -m_talk "( I'll come back later. )"
    hide anon with dissolve
    return True


label maria_lounge_knock.answer:
    show location_apt_hall3_302_closeup_door2 as door with dissolve
    show maria b_magic behind doorframe with dissolve
    maria "Hi, {b}[firstname]{/b}!"
    maria "Come on in."
    hide maria with dissolve
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

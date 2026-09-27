label liu_lounge_knock:
    scene location_apt_hall2_204_closeup as stage
    show location_apt_hall2_204_closeup_door1 as door behind stage
    show location_apt_hall2_204_closeup as doorframe:
        crop (768, 0, 256, 768)
        right
    show anon a_knock with dissolve
    "{i}*Ketuk* *Ketuk*{/i}"

    show anon a_sides with dissolve
    pause

    if M_liu.where in L_liu_lounge.get_all_children_inclusive():
        if M_liu.pregnancy.stage == 1:
            jump liu_lounge_knock.pregnant1
        elif 2 <= M_liu.pregnancy.stage <= 4:
            jump liu_lounge_knock.pregnant2
        elif M_liu.pregnancy.stage:
            jump liu_lounge_knock.baby
        else:
            jump liu_lounge_knock.answer

    pause
    anon @ -m_talk "( Huh... I guess there's nobody home. )"

    anon @ -m_talk "( I'll come back later. )"

    hide anon with dissolve
    return True


label liu_lounge_knock.answer:
    show location_apt_hall2_204_closeup_door2 as door with dissolve
    show liu b_robe_hair f_surprised behind doorframe with {'master': dissolve}
    liu "{b}[firstname]{/b}!!!"

    show liu b_robe_hug
    show anon b_empty f_grin
    with dissolve
    anon @ -m_talk "!!!"
    anon f_shy "Hai, {b}Liu{/b}."

    liu "I'm so happy you're here!"

    anon f_normal "Ya, aku juga."

    show anon b_dressed
    show liu b_robe_hair f_happy:
        xoffset -75
    with dissolve
    anon "Apa yang terjadi?"

    show liu a_shy with {'master': dissolve}

    if L_liu_lounge.is_here(M_liu):
        liu "I was just sitting down to tea..."

    else:
        liu "I was just laying in bed, reading..."


    anon "Oh ya?"

    anon a_sides "That sounds nice."


    if L_liu_lounge.is_here(M_liu):
        liu "Come in and join me, please..."

    else:
        liu "Come in, please... make yourself at home."


    anon "Baiklah terima kasih."

    hide liu with dissolve
    hide anon with dissolve
    return


label liu_lounge_knock.baby:
    show location_apt_hall2_204_closeup_door2 as door with dissolve
    show liu a_baby b_robe_hair f_happy behind doorframe with {'master': dissolve}
    liu "{b}[firstname]{/b}!"

    show anon f_happy
    liu f_happy_baby "Look, Daddy's come to visit us."

    hide liu
    with {'master': dissolve}
    liu "Come and say hello."

    hide anon with dissolve
    return


label liu_lounge_knock.pregnant1:
    show location_apt_hall2_204_closeup_door2 as door with dissolve
    show liu b_robe_magic f_surprised behind doorframe with {'master': dissolve}
    liu "{b}[firstname]{/b}!"

    show liu b_robe_hug
    show anon b_empty f_happy_closed
    with dissolve
    liu "I'm so happy you came to visit!"

    show anon b_dressed f_happy
    show liu b_robe_magic f_happy:
        xoffset -75
    with dissolve
    pause
    hide liu with {'master': dissolve}
    liu "Come on in!"

    hide anon with dissolve
    return


label liu_lounge_knock.pregnant2:
    liu "Hello? Who is it?"

    anon "It's {b}[firstname]{/b}."

    anon "I came to see how you're doing."

    show location_apt_hall2_204_closeup_door2 as door with dissolve
    liu "Quickly, don't let anyone see!"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

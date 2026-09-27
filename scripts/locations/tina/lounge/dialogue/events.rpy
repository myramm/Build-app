label tina_lounge_knock:
    scene location_apt_hall3_301_closeup as stage
    show location_apt_hall3_301_closeup_door1 as door behind stage
    show location_apt_hall3_301_closeup as doorframe:
        crop (768, 0, 256, 768)
        right
    show anon a_knock with dissolve
    "{i}*Ketuk* *Ketuk*{/i}"

    show anon a_sides with dissolve
    pause

    if M_tina.where in L_tina_lounge.get_all_children_inclusive():
        if M_tina.outfit.get == 'naked':
            jump tina_lounge_knock.naked
        elif M_tina.pregnancy.stage:
            jump tina_lounge_knock.pregnant
        else:
            jump tina_lounge_knock.answer

    pause
    anon @ -m_talk "( There's no answer... )"

    anon @ -m_talk "( I'll come back later. )"

    hide anon with dissolve
    return True


label tina_lounge_knock.answer:
    show location_apt_hall3_301_closeup_door2 as door with dissolve
    show tina b_magic f_surprised behind doorframe with dissolve
    tina "{b}[firstname]{/b}?"

    show tina f_sad:
        xoffset -200
    show location_apt_hall3_301_closeup_door1 as door behind stage
    with dissolve
    tina "Apa yang kamu lakukan di sini?"


    menu:
        "I wanted to see you.":
            jump tina_lounge_knock.schedule

        "I'm here to see Becca." if M_becca.finished_state(S_bec00_done):
            jump tina_lounge_knock.becca
        "Hanya menyapa.":

            pass

    anon f_normal "Hanya menyapa."

    tina f_normal "Just in the neighborhood, huh?"

    anon "Cukup banyak."


    if 4 <= game.timer._dow <= 5:
        tina f_sexy "You know, you should swing by {b}the bank{/b} on Monday."

    else:
        tina f_sexy "You know, you should swing by {b}the bank{/b} tomorrow."


    tina "We can schedule a little fun."

    anon "Yeah, that sounds good."

    tina @ f_laugh "Saya tidak sabar."

    anon "Sampai jumpa lagi."

    tina "So long, babyface."

    hide anon with dissolve
    return True


label tina_lounge_knock.becca:
    if M_becca.where not in L_tina_lounge.get_all_children_inclusive():
        tina f_suspicious "Becca?"

        tina f_sad "I'm sorry, [firstname]. She's not home at the moment."

        anon f_worried "Ohh... Well... I guess I'll call back later then."

        tina f_normal "So long, babyface."

        hide anon with dissolve
        return True

    if not M_becca.finished_state(S_bec01_init):
        $ M_becca.trigger(T_bec01_init)
        jump bec01_init_tina_threshold
    else:

        show tina b_casual
        tina f_surprised "Ah, benarkah?"

        anon f_worried "Is that okay?"

        tina f_normal "Ya, tentu saja."

        show anon f_normal
        tina "She's in her bedroom doing homework..."

        show location_apt_hall3_301_closeup_door2 as door
        show tina a_sides:
            xzoom -1
            xoffset 515
        with {'master': dissolve}
        tina "... You can head on back."

        hide tina
        with {'master': dissolve}
        anon "Terima kasih."

        hide anon
        with {'master': dissolve}
        tina "I'll be in my room if you need me."

        show location_apt_hall3_301_closeup_door1 as door
        with {'master': dissolve}
        anon "Dingin."


    return


label tina_lounge_knock.naked:
    tina "Siapa itu?"

    anon "It's {b}[firstname]{/b}."

    anon "I came to see how you're doing."

    show location_apt_hall3_301_closeup_door2 as door with dissolve
    tina "Quick, come inside!"

    hide anon with dissolve
    return


label tina_lounge_knock.pregnant:
    show location_apt_hall3_301_closeup_door2 as door with dissolve
    show tina b_magic behind doorframe with dissolve
    tina f_sexy "Hi, {b}[firstname]{/b}, come to check up on us?"

    hide tina with {'master': dissolve}
    tina "Masuk."

    hide anon with dissolve
    return


label tina_lounge_knock.schedule:
    anon f_flirt "I wanted to see you."

    tina "This isn't a good time."

    anon f_shy "Oh, right... {b}Becca{/b}'s here, huh?"

    tina f_sexy "Come see me at work and we'll schedule something."

    anon "Y-ya, oke."


    if 4 <= game.timer._dow <= 5:
        anon f_normal "I'll swing by {b}the bank{/b} on Monday."

    else:
        anon f_normal "I'll swing by {b}the bank{/b} tomorrow."


    tina @ f_laugh "Saya tidak sabar."

    anon "Sampai jumpa lagi."

    tina "So long, babyface."

    hide anon with dissolve
    return True


label tina_lounge_sex:
    scene location_apt_hall3_301_closeup as stage
    show location_apt_hall3_301_closeup_door1 as door behind stage
    show anon a_knock with dissolve
    "{i}*Ketuk* *Ketuk*{/i}"

    show anon a_sides with dissolve
    pause

    scene tina b_doorway f_sexy with fade
    tina "Well, hello there."

    tina "You're right on time."

    anon "Apakah saya?"

    tina "Heh, come on in."


    scene expression background(744, 420, 3.5) as stage
    show tina b_lingerie
    with fade
    show anon f_shy with dissolve
    anon "{i}*Gulp*{/i} So, I assume {b}Becca{/b} is-"

    tina "Shh, don't worry about my daughter."

    tina "She's not going to bother us tonight."

    show tina a_remove_cloth1 with dissolve
    anon "Y-ya, oke."

    tina a_remove_cloth2 @ f_eyeroll "Help me get undressed."

    show tina b_lingerie_back1
    show anon b_tina_lingerie1 f_flirt_low
    with dissolve
    anon "Ya, Bu!"

    pause
    show anon b_tina_lingerie2
    show tina b_lingerie_back2
    with dissolve
    tina "Mm, I've been thinking about this all day."

    show tina b_lingerie_back3
    show anon b_dressed f_skeptical
    with dissolve
    anon "Oh ya?"

    pause
    show tina b_lingerie_back_bend with dissolve
    show anon f_flirt_low
    tina "I'm so wet for you right now..."

    pause
    show tina b_naked a_undress1 f_normal_down with dissolve
    pause
    show tina b_naked_undress2 with dissolve
    pause
    show tina b_naked a_idle f_sexy with dissolve
    tina "Ngh, why are you still wearing clothes?!"

    show anon f_thinking a_thinking with dissolve
    pause
    show tina b_naked_crossed f_eyeroll with dissolve
    pause
    hide anon
    show tina b_naked_mc_throw:
        flip
    with dissolve
    anon "!!!"
    hide tina with dissolve
    anon "Wah!"

    tina "hehe!"


    call scene_tina_sex_lounge.repeat
    $ unlock_scene('tina', '01_unlocked', variant='repeat')

    scene expression background(744, 420, 3.5) as stage
    show tina b_naked_disheveled f_sexy:
        xoffset -132
    show anon f_flirt:
        xoffset 150
    with fade
    tina "Heh, you better get out of here before {b}Rebecca{/b} gets home."

    anon "Y-ya, oke."

    show anon b_empty
    show tina b_naked_disheveled_kiss
    with dissolve
    pause
    show anon b_dressed
    show tina b_naked_disheveled
    with dissolve
    tina "It's always a pleasure, {b}[firstname]{/b}."

    anon "See ya, {b}Tina{/b}."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

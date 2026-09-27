label scene_tina_lounge_doggy:

    return


label scene_tina_lounge_doggy.pre:
    show tina_body_b_sex_doggy_insert as anim behind anon_body
    show tina_body_b_sex_doggy_insert_leg as leg behind anon_arm
    return


label scene_tina_lounge_doggy.insert:
    hide leg
    show tina_lounge_doggy 1 as anim
    return


label scene_tina_lounge_doggy.animate:
    show tina_lounge_doggy as anim
    return


label scene_tina_lounge_doggy.loop:
    call screen scene_tina_lounge_doggy_controls

    if _return:
        return _return

    python hide:
        blocks = 5
        limit = 2

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_tina_lounge_doggy.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_tina_lounge_doggy.loop


label scene_tina_lounge_doggy.dialogue(opt, rng=-1):
    if opt == 1:
        if rng < 0:
            tina "Halo!"


        anon "Bagaimana rasanya?"

        tina "Hmm, luar biasa!"


    elif opt == 2:
        tina "Ya, begitu saja!"


    elif opt == 3:
        tina "Ya Tuhan!!"


    elif opt == 4:
        tina "Ya, pukullah!"

        tina "Pukul vagina itu!"


        if rng < .4:
            anon "Ahh!!"


    elif opt == 5:
        anon "Astaga, pantatmu bagus!"


    return


label scene_tina_lounge_doggy.switch:
    anon "Ini, ganti aku."

    hide anim
    show anon b_tina_sex
    show tina b_sex_talk
    with {'master': dissolve}
    tina "Hah?"

    anon "Aku ingin menjadi yang teratas sebentar."

    tina "Benar-benar?"

    pause
    tina "Anda yakin bisa mengatasinya?"

    anon "{i}*Gulp*{/i} Saya kira begitu..."

    tina "Hehe, baiklah kalau begitu..."

    call scene_tina_sex_lounge.stage
    with {'master': dissolve}
    pause
    show tina b_sex_inbetween f_sexy_down behind anon
    with {'master': dissolve}
    pause

    $ M_tina.set('sex speed', 1. / 8)

    hide anon
    show tina f_sexy_left
    show tina_body_b_sex_doggy_insert_anon as anon_body
    show tina_body_b_sex_doggy_insert_arm as anon_arm
    with {'master': dissolve}
    tina "... Tunjukkan padaku apa yang kamu punya, Babyface!"

    hide tina
    call scene_tina_lounge_doggy.pre
    with {'master': dissolve}
    pause
    hide anon_body
    hide anon_arm
    call scene_tina_lounge_doggy.insert
    with {'master': dissolve}
    tina "Oh wah!!!"

    call scene_tina_lounge_doggy.animate
    with {'master': dissolve}
    call scene_tina_lounge_doggy.dialogue (1)
    pause
    call scene_tina_lounge_doggy.dialogue (2)
    pause
    call scene_tina_lounge_doggy.dialogue (3)
    pause
    call scene_tina_lounge_doggy.dialogue (4)
    pause
    call scene_tina_lounge_doggy.dialogue (5)
    pause
    call scene_tina_lounge_doggy.loop
    jump scene_tina_sex_lounge.switch


screen scene_tina_lounge_doggy_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Switch') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_tina.set, 'sex speed',
                                 1 / (1 / M_tina.get('sex speed') - 2)),
                        Return(False))
                sensitive M_tina.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_tina.set, 'sex speed',
                                 1 / (1 / M_tina.get('sex speed') + 2)),
                        Return(False))
                sensitive M_tina.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

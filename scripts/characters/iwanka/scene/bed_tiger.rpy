label scene_iwanka_bed_tiger:

    return


label scene_iwanka_bed_tiger.insert:
    hide anon
    show iwanka_body_b_sex_ride_insert as anim
    return


label scene_iwanka_bed_tiger.animate:
    show iwanka_bed_tiger as anim
    return


label scene_iwanka_bed_tiger.loop:
    call screen scene_iwanka_bed_tiger_controls

    if _return:
        return _return

    python hide:
        blocks = 6
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_iwanka_bed_tiger.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_iwanka_bed_tiger.loop


label scene_iwanka_bed_tiger.dialogue(opt, rng=-1):
    if opt == 1:
        iwanka "Ya, kamu suka itu?"

        anon "Saya bersedia!"


    elif opt == 2:
        if rng < 0:
            iwanka "Jauh lebih baik daripada ibuku yang bodoh, ya?"

            anon "Hah?!"


        iwanka "Katakan padaku aku lebih baik!"


        if rng < 0 and not M_melonia.finished_state(S_mel05_init):
            anon "Entahlah, aku belum-"

            iwanka "KATAKAN!!"


        if rng < .3:
            anon "Gah, kamu lebih baik!"

            iwanka "Ya?"


        anon "Jauh lebih baik!"

        iwanka "Ngh, aku tahu itu!!"


    elif opt == 3:
        anon "Sobat, {b}Iwanka{/b}, payudaramu luar biasa!"

        iwanka "Hehe, sebaiknya mereka..."

        iwanka "... Ayahku membayar mahal untuk itu!"


    elif opt == 4:
        anon "Fiuh, ini luar biasa!"

        iwanka "Eh ya!"


    elif opt == 5:
        if rng < .6:
            iwanka "Ahhh, sial!!"


        iwanka "Kamu pasti yang terbesar..."

        iwanka "... aku pernah..."

        iwanka "... Selesaikan ini dengan."


    elif opt == 6:
        anon "Oh ya..."

        anon "... Persis seperti itu!"

        iwanka "Mhmm!"


    return


label scene_iwanka_bed_tiger.switch:
    iwanka "Ini, bergulinglah."

    call scene_iwanka_sex.insert
    with {'master': dissolve}
    anon "Hmm?"

    iwanka "Heh, supaya aku bisa mendahuluimu..."

    anon "Oh."

    call scene_iwanka_sex.pre
    with {'master': dissolve}
    anon "Baiklah, keren!"

    show iwanka_overlay_o_sex_dick_pre as iwanka
    with {'master': dissolve}
    pause

    $ M_iwanka.set('sex speed', 1. / 8)

    hide anon_body
    hide anon_leg
    hide iwanka
    show iwanka_body_b_sex_ride_anon as anon
    with {'master': dissolve}
    iwanka "... Aku ingin mengajakmu jalan-jalan."

    call scene_iwanka_bed_tiger.insert
    with {'master': dissolve}
    anon "Bersiaplah!"

    show iwanka_bed_tiger 4 as anim
    with {'master': dissolve}
    iwanka "Oof, harium!"

    anon "Haah!!"

    call scene_iwanka_bed_tiger.animate
    with {'master': dissolve}
    pause
    call scene_iwanka_bed_tiger.dialogue (1)
    pause
    call scene_iwanka_bed_tiger.dialogue (2)
    pause
    call scene_iwanka_bed_tiger.dialogue (3)
    pause
    call scene_iwanka_bed_tiger.dialogue (4)
    pause
    call scene_iwanka_bed_tiger.dialogue (5)
    pause
    call scene_iwanka_bed_tiger.dialogue (6)
    pause
    call scene_iwanka_bed_tiger.loop
    jump scene_iwanka_sex.switch


screen scene_iwanka_bed_tiger_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Switch') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_iwanka.set, 'sex speed',
                                 1 / (1 / M_iwanka.get('sex speed') - 2)),
                        Return(False))
                sensitive M_iwanka.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_iwanka.set, 'sex speed',
                                 1 / (1 / M_iwanka.get('sex speed') + 2)),
                        Return(False))
                sensitive M_iwanka.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

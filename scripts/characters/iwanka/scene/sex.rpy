label scene_iwanka_sex(venue='yacht'):
    $ M_iwanka.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='first')

    call scene_iwanka_sex.prelude
    with fade
    iwanka "Bagaimana pemandangannya bagus ya?"

    anon "{i}*Gulp*{/i} Y-ya, enak sekali!"

    call scene_iwanka_sex.stage
    with {'master': dissolve}
    iwanka "Nah, tunggu apa lagi?"

    call scene_iwanka_sex.pre
    with {'master': dissolve}
    iwanka "Persetan denganku, {b}[firstname]{/b}!"

    call scene_iwanka_sex.insert
    with {'master': dissolve}
    iwanka "Hmm, itu dia!"

    call scene_iwanka_sex.slam
    iwanka "Ngh!!" with hpunch
    iwanka "Ya ampun, itu penis yang besar!"

    jump scene_iwanka_sex.merge


label scene_iwanka_sex.prelude:
    if venue == 'yacht':
        scene iwanka b_presex_yacht
    else:
        scene iwanka b_presex_iwanka_room
    return


label scene_iwanka_sex.stage:
    if venue == 'yacht':
        scene location_boat_interior_bed_sex
    else:
        scene location_rump_iwanka_bed_sex
    show iwanka b_sex_pre_after
    return


label scene_iwanka_sex.pre:
    show iwanka_body_b_sex_pre_after_anon as anon_body behind iwanka
    show iwanka b_sex_pre_after o_pre
    show iwanka_body_b_sex_pre_after_anon_leg as anon_leg
    return


label scene_iwanka_sex.insert:
    hide anim
    hide anon_body
    hide anon_leg
    show iwanka b_sex_insert_pullout o_insert_pullout
    return


label scene_iwanka_sex.slam:
    hide iwanka
    show iwanka_body_b_sex_anim 1 as anim
    return


label scene_iwanka_sex.animate:
    hide iwanka
    show iwanka_body_b_sex_anim as anim
    return


label scene_iwanka_sex.loop:
    call screen scene_iwanka_sex_controls

    if _return:
        return _return

    python hide:
        blocks = 4
        limit = 2

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_iwanka_sex.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_iwanka_sex.loop


label scene_iwanka_sex.dialogue(opt, rng=-1):
    if opt == 1:
        iwanka "Wah!"


    elif opt == 2:
        iwanka "Ya, itu dia!"


    elif opt == 3:
        iwanka "Anda menyukainya, {b}[firstname]{/b}?"

        anon "Ya!{p=1}{nw}"


    elif opt == 4:
        iwanka "Kamu suka melihatku melompat-lompat di atas ayam berdaging besar itu?!"

        anon "Ah, ya!"


        if rng < .4:
            iwanka "Katakan padaku betapa kamu menyukainya!"


        anon "Sangat banyak!!"


        if rng < .4:
            anon "Ahh, aku sangat menyukainya!!"


    return


label scene_iwanka_sex.switch:
    iwanka "Haah... Haah..."

    iwanka "... Oke, aku perlu istirahat."

    anon "Oh?"

    call scene_iwanka_bed_tiger.insert
    with {'master': dissolve}
    iwanka "Anda ingin beralih kembali ke doggy?"

    hide anim
    show iwanka_body_b_sex_ride_anon as anon_body
    with {'master': dissolve}
    anon "Ya tentu saja!"


    $ M_iwanka.set('sex speed', 1. / 8)

    call scene_iwanka_sex.pre
    show iwanka_overlay_o_sex_dick_pre as iwanka
    with {'master': dissolve}
    pause
    call scene_iwanka_sex.pre
    with {'master': dissolve}
    iwanka "Ya, ini jauh lebih baik."

    call scene_iwanka_sex.insert
    with {'master': dissolve}
    pause
    call scene_iwanka_sex.animate
    with {'master': dissolve}
    iwanka "Tidak!!"

    pause
    jump scene_iwanka_sex.resume


label scene_iwanka_sex.repeat(venue):
    $ M_iwanka.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='repeat')

    call scene_iwanka_sex.prelude
    with fade
    iwanka "Umm, ada apa?"

    anon "Tidak ada apa-apa, aku hanya mengagumi pemandangannya..."

    iwanka "Nah, lakukan itu nanti!"

    call scene_iwanka_sex.stage
    with {'master': dissolve}
    iwanka "Saat ini, aku hanya ingin kamu meniduriku."

    anon "Ya baiklah."

    call scene_iwanka_sex.pre
    with {'master': dissolve}
    iwanka "Oh, aku sangat menginginkan ini."

    call scene_iwanka_sex.insert
    with {'master': dissolve}
    anon "Wow, kamu benar-benar basah!"

    call scene_iwanka_sex.slam
    iwanka "Haah!" with hpunch
    label scene_iwanka_sex.merge:
    call scene_iwanka_sex.animate
    with {'master': dissolve}
    call scene_iwanka_sex.dialogue (1)
    pause
    call scene_iwanka_sex.dialogue (2)
    pause
    call scene_iwanka_sex.dialogue (3)
    pause
    call scene_iwanka_sex.dialogue (4)
    pause
    label scene_iwanka_sex.resume:
    call scene_iwanka_sex.loop

    if _return == 'switch':
        jump scene_iwanka_bed_tiger.switch

    iwanka "aku akan keluar!"

    anon "Saya juga!"

    pause
    iwanka "OH!!"

    iwanka "EM!!"

    iwanka "Aduh!!!"

    iwanka "NGGHHH!!!"

    hide anim

    if _return == 'inside':
        show iwanka b_sex_cum
    else:
        show iwanka b_sex_insert_pullout o_cum

    anon "HNNGGG!!!" with flash

    if _return == 'inside':
        show xray_iwanka_sex with fastdissolve:
            align (0, 0)
    else:
        show iwanka_overlay_o_sex_dick_cum3
        show iwanka o_empty

    pause
    hide xray_iwanka_sex
    with {'master': dissolve}
    anon "Haah... Haah..."


    if _return == 'inside':
        show iwanka b_sex_insert_pullout o_insert_pullout
        with {'master': dissolve}

    pause

    if _return == 'inside':
        show iwanka_body_b_sex_pre_after_anon as anon_body behind iwanka
        show iwanka b_sex_pre_after o_after
        show iwanka_body_b_sex_pre_after_anon_leg as anon_leg
        with {'master': dissolve}

    anon "Itu luar biasa!"

    iwanka "Benar, bukan?"

    pause
    iwanka "Umm, bisakah kamu mengambilkanku handuk?"

    anon "Hmm?"


    if _return == 'inside':
        iwanka "Air manimu bocor keluar dari tubuhku ke seprai..."

        call call_pregnancy_minigame (None, M_iwanka)
    else:

        iwanka "Aku seperti, tercakup dalam air manimu..."


    return


label scene_iwanka_sex.first:
    call scene_iwanka_sex ('yacht')
    return


label scene_iwanka_sex.yacht:
    call scene_iwanka_sex.repeat ('yacht')
    return


label scene_iwanka_sex.bedroom:
    call scene_iwanka_sex.repeat ('bedroom')
    return


label scene_iwanka_sex.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['iwanka']['variants']['02_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_boat_bridge) with fade
        menu:
            "Kapal Pesiar (Pertama)" if 'first' in variants:
                jump scene_iwanka_sex.first

            "Kapal Pesiar (Ulangi)" if 'yacht' in variants:
                jump scene_iwanka_sex.yacht

            "Kamar Tidur (Ulangi)" if 'bedroom' in variants:
                jump scene_iwanka_sex.bedroom
    else:

        jump expression 'scene_iwanka_sex.{}'.format(next(iter(variants)))

    return


screen scene_iwanka_sex_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            if M_anon.finished_state(S_ano20_done):
                textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')
            if variant == 'repeat':
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

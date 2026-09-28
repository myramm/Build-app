label scene_khadne_crates_sex:
    $ M_khadne.set('sex speed', 1. / 6)
    $ renpy.dynamic(variant='first')

    call scene_khadne_crates_sex.stage
    with fade
    anon "You ready?"
    khadne "{i}*Gulp*{/i} I think so."
    anon "Here it comes."
    call scene_khadne_crates_sex.insert
    with dissolve
    khadne @ -m_talk "{i}*Iiitthh*{/i}"
    anon "How's that feel?"
    khadne f_moan "Ngh, it hurts!"
    anon "Alright, I won't go any further..."
    khadne @ -m_talk "{i}*Whimpers*{/i}"
    anon "Breathe."
    khadne f_nervous "{i}*Phew*{/i} Haah... Haah... {i}*Phew*{/i}"
    anon "That's it..."
    anon "... Give your body time to adjust."
    khadne "{i}*Phew*{/i} Haah... Haah... {i}*Phew*{/i}"
    khadne "I think maybe it working..."
    anon "Yeah?"
    khadne "{i}*Phew*{/i} Haah... Haah... {i}*Phew*{/i}"
    anon "I'm gonna start moving a little, okay?"
    khadne "O-okay."
    call scene_khadne_crates_sex.animate
    with dissolve
    pause
    khadne "{i}*Whimper*{/i}"
    anon "Breathe, {b}Khadne{/b}."
    khadne "{i}*Phew*{/i} Haah... Haah... {i}*Phew*{/i}"
    anon "There ya go."
    pause
    anon "Still hurting?"
    khadne "Yes, but not so bad."
    anon "You want me to stop?"
    khadne "N-no."
    pause
    khadne "Ahh!"
    anon "Better?"
    khadne "I think so..."
    khadne "... Yes."
    pause
    khadne "Oh my god..." (show_native="O moy Bog...")
    anon "Feeling good?"
    khadne "Mhmm!"
    pause
    anon "Can I speed up?"
    khadne "Yes."
    $ M_khadne.set('sex speed', 1. / 10)
    pause
    call scene_khadne_crates_sex.dialogue (1)
    pause
    call scene_khadne_crates_sex.dialogue (2)
    pause
    call scene_khadne_crates_sex.dialogue (3)
    pause
    label scene_khadne_crates_sex.resume:
    call scene_khadne_crates_sex.loop
    anon "I don't think I can last much longer..."
    khadne "You want make cum?"
    anon "... Yeah!"
    khadne "Ahh!!"
    pause
    khadne "Do it!"
    khadne "Make cum for me!"
    anon "Haaah!!"
    pause
    anon "Oh, god..."
    anon "... Here it comes!"
    khadne "Yes!!"
    pause

    hide anim
    if _return == 'inside':
        show khadne crates_sex b_cum
    else:
        show khadne crates_sex b_base f_moan m_talk o_cumshot

    anon "HNNGGG!!!" with flash

    if _return == 'inside':
        show xray_side as xray:
            anchor (.5, .5)
            pos (250 + 386, 250 + 179)
            rotate 4
            rotate_pad False
            xzoom -1
            zoom .75
        with {'master': fastdissolve}
    else:
        show khadne o_cumshot3

    khadne "NGGHHH!!!"
    pause
    hide xray

    if _return == 'inside':
        show khadne b_base f_moan m_talk o_pullout
        with {'master': dissolve}

    anon "Haah... Haah..."
    show khadne f_normal
    anon "Phew!"
    return _return


label scene_khadne_crates_sex.stage:
    scene location_warehouse_hostage_vodka_crate_up_any
    show khadne crates_sex
    return


label scene_khadne_crates_sex.insert:
    show khadne b_insert f_moan_teeth
    return


label scene_khadne_crates_sex.animate:
    hide khadne
    show khadne_crates_sex_body_b_anim as anim
    return


label scene_khadne_crates_sex.loop:
    call screen scene_khadne_crates_sex_controls

    if _return:
        return _return

    python hide:
        blocks = 3 if variant == 'first' else 4
        limit = 2

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_khadne_crates_sex.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_khadne_crates_sex.loop


label scene_khadne_crates_sex.dialogue(opt, rng=-1):

    if opt == 1:
        khadne "Oh, wow!" (show_native="Vot eto da!")
        anon "You like that?"
        khadne "Yes!"

        if rng < .2:
            khadne "It's so different than before!"
            anon "I told you."

    elif opt == 2:
        khadne "Oh, fuck me!" (show_native="Oh, trakhni menya!")

        if rng < .4:
            anon "Hmm?"
            khadne "Fuck me, {b}[firstname]{/b}!"

        anon "Yes, ma'am!"

    elif opt == 3:
        if rng < .5:
            khadne "So good!" (show_native="Tak khorosho!")

        if rng < .3:
            khadne "Fuck my pussy, {b}[firstname]{/b}!" (show_native="Trakhni moyu kisku, {b}[firstname]{/b}!")

        anon "Damn, you're sexy."
        khadne "Ahh!!"

    elif opt == 4:
        khadne "Harder!"

        if rng < .25:
            anon "Whoa, careful you don't knock over the bottles!"

    return


label scene_khadne_crates_sex.first:
    jump scene_khadne_crates_sex


label scene_khadne_crates_sex.repeat:
    $ M_khadne.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='repeat')

    call scene_khadne_crates_sex.stage
    with fade
    anon "Just remember to tell me if I'm going to fast, okay?"
    khadne "Y-yeah, okay."
    call scene_khadne_crates_sex.insert
    with dissolve
    khadne f_nervous @ f_moan_teeth -m_talk "!!!"
    anon "You good?"
    khadne "Very."
    anon "Awesome!"
    call scene_khadne_crates_sex.animate
    with dissolve
    pause
    call scene_khadne_crates_sex.dialogue (1)
    pause
    call scene_khadne_crates_sex.dialogue (2)
    pause
    call scene_khadne_crates_sex.dialogue (3)
    pause
    call scene_khadne_crates_sex.dialogue (4)
    pause
    jump scene_khadne_crates_sex.resume


label scene_khadne_crates_sex.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['khadne']['variants']['02_unlocked'])
    $ M_anon._cleared_states[S_ano27_done] = True

    if len(variants) > 1:
        scene expression background(l=L_warehouse_storage) with fade
        menu:
            "First" if 'first' in variants:
                jump scene_khadne_crates_sex.first

            "Repeat" if 'repeat' in variants:
                jump scene_khadne_crates_sex.repeat

    jump expression 'scene_khadne_crates_sex.{}'.format(next(iter(variants)))


screen scene_khadne_crates_sex_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_khadne.set, 'sex speed',
                                 1 / (1 / M_khadne.get('sex speed') - 2)),
                        Return(False))
                sensitive M_khadne.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_khadne.set, 'sex speed',
                                 1 / (1 / M_khadne.get('sex speed') + 2)),
                        Return(False))
                sensitive M_khadne.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

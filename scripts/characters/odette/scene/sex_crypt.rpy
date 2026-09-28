label scene_odette_sex_crypt:

    return


label scene_odette_sex_crypt.stage:
    scene location_crypt_sex
    show odette b_sex_vamp_base o_pre
    show location_crypt_sex_throne_overlay as armrest
    return


label scene_odette_sex_crypt.insert:
    hide anim
    show odette b_sex_vamp_insert d_insert
    return


label scene_odette_sex_crypt.animate:
    hide odette
    show odette_body_b_sex_vamp_anim as anim behind armrest
    return


label scene_odette_sex_crypt.loop:
    call screen scene_odette_sex_crypt_controls

    if _return:
        return _return

    python hide:
        blocks = 7
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_odette_sex_crypt.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_odette_sex_crypt.loop


label scene_odette_sex_crypt.dialogue(opt, rng=-1):

    if opt == 1:
        odette "Oh, I've dreamed about this for so long!"
        odette "It feels incredible!"

    elif opt == 2:
        odette "Fuck me, {b}[firstname]{/b}!"

        if rng < .3:
            odette "Fuck my filthy vampire pussy!"
            anon "AMPUR?"
            anon "Wazzit-"

        odette "Harder!"

    elif opt == 3:
        if rng < .6:
            anon "Ur hinga nals er iggin n mah ack!"

        odette "Tell me I'm your queen!"

        if rng < .3:
            anon "Huh?"
            odette "Say it!"

        anon "Ur mah Keen."
        odette "Yes!"

    elif opt == 4:
        odette "Can you feel them watching us?"
        anon "Hoo?"
        odette "The spirits of the recently departed."
        odette "It gets me so wet!"
        anon "Errh gud!"

    elif opt == 5:
        odette "Yeah, that's it!{p=2}{nw}"
        odette "Ahhhh!{p=1}{nw}"

    elif opt == 6:
        odette "You like that, {b}[firstname]{/b}?{p=2}{nw}"
        anon "Errh gud!{p=1}{nw}"

    elif opt == 7:
        if rng < .2:
            odette "Fuuuuck!{p=1}{nw}"
            odette "I'm gonna cum!{p=1}{nw}"

    return


label scene_odette_sex_crypt.switch:
    call scene_odette_crypt_cowgirl.insert
    with {'master': dissolve}
    odette "Okay, okay..."
    odette "... You'd better stand back up."
    anon "Hmm?"
    call scene_odette_crypt_cowgirl.stage
    with {'master': dissolve}
    odette "You'll feel better, trust me."
    anon "Ugh, ogay."

    scene location_crypt_side
    show odette b_naked_vamp_pull_anon f_smirk:
        xoffset -250
        xzoom -1
    show anon b_empty f_worried:
        xoffset -275
        xzoom -1
    with fade
    odette "Did that help?"
    anon f_shy "Mm, ridle bid."
    show odette:
        xoffset -175
        xzoom 1
    show anon f_surprised_shock_food:
        xoffset -150
        xzoom 1
    with {'master': dissolve}
    odette "Good..."
    show odette b_vamp_sitting:
        xoffset 0
    show anon a_cannoli_gobble b_shirt od_dick4
    with {'master': dissolve}
    odette "... Now throw it back in there, big fella!"
    show anon f_disgusted_wince
    with {'master': dissolve}
    anon "{i}*Gulp*{/i}"

    $ M_odette.set('sex speed', 1. / 8)

    call scene_odette_sex_crypt.stage
    with fade
    odette "Hurry up!"
    show odette b_sex_vamp_insert d_rub f_down
    with {'master': dissolve}
    anon "Ib trynin."
    show odette b_sex_vamp_base o_pre
    with {'master': dissolve}
    odette "Ngh!"
    call scene_odette_sex_crypt.insert
    with {'master': dissolve}
    odette "Ahh!"
    anon "God ib!"
    call scene_odette_sex_crypt.animate
    with {'master': dissolve}
    jump scene_odette_sex_crypt.resume


label scene_odette_sex_crypt.cum(where):
    odette "Oh, fuck!"
    odette "I'm gonna cum!"
    anon "Meh eww!"
    anon "Iz gon-"
    odette "NGGHHH!!!"
    hide anim

    if where == 'inside':
        show odette b_sex_vamp_cum behind armrest
    else:
        show odette b_sex_vamp_base o_cumshot f_down behind armrest

    anon "HNNGGG!!!" with flash

    if where == 'inside':
        show xray_odette_vamp_sex with fastdissolve:
            align (0, 0)
        pause
        hide xray_odette_vamp_sex
    else:
        show odette_overlay_sex_vamp_base_o_cumshot03
        show odette o_empty

    if where == 'inside':
        show odette b_sex_vamp_insert f_down o_pullout
        with dissolve

    anon "Haah... Haah..."

    if where == 'inside':
        show odette b_sex_vamp_base o_after with dissolve

    odette "Mmm, it's so warm."
    show odette f_normal
    anon "Yeah."
    anon "Iz aught... N harr..."
    odette "Hehehe!"
    return


label scene_odette_sex_crypt.repeat:
    $ M_odette.set('sex speed', 1. / 8)

    call scene_odette_sex_crypt.stage
    with fade
    odette "Just put it inside me, {b}[firstname]{/b}!"
    show odette b_sex_vamp_insert d_rub f_down
    with {'master': dissolve}
    odette "Ahh!"
    anon "Ib trynin."
    show odette b_sex_vamp_base o_pre
    with {'master': dissolve}
    anon "eberphing o red n hare."
    call scene_odette_sex_crypt.insert
    with {'master': dissolve}
    odette "Ngh!"
    anon "God ib."
    call scene_odette_sex_crypt.animate
    with {'master': dissolve}
    pause
    call scene_odette_sex_crypt.dialogue (1)
    pause
    call scene_odette_sex_crypt.dialogue (1)
    pause
    call scene_odette_sex_crypt.dialogue (3)
    pause
    call scene_odette_sex_crypt.dialogue (4)
    pause
    call scene_odette_sex_crypt.dialogue (5)
    pause
    call scene_odette_sex_crypt.dialogue (6)
    pause
    call scene_odette_sex_crypt.dialogue (7)
    pause

    label scene_odette_sex_crypt.resume:
    call scene_odette_sex_crypt.loop

    if _return == 'switch':
        jump scene_odette_crypt_cowgirl.switch

    call scene_odette_sex_crypt.cum (_return)
    return


label scene_odette_sex_crypt.replay:
    jump scene_odette_sex_crypt.repeat


screen scene_odette_sex_crypt_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')
            textbutton _('Switch') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_odette.set, 'sex speed',
                                 1 / (1 / M_odette.get('sex speed') - 2)),
                        Return(False))
                sensitive M_odette.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_odette.set, 'sex speed',
                                 1 / (1 / M_odette.get('sex speed') + 2)),
                        Return(False))
                sensitive M_odette.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label scene_iwanka_sex(venue='yacht'):
    $ M_iwanka.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='first')

    call scene_iwanka_sex.prelude
    with fade
    iwanka "How's this for a nice view, huh?"
    anon "{i}*Gulp*{/i} Y-yeah, it's very nice!"
    call scene_iwanka_sex.stage
    with {'master': dissolve}
    iwanka "Well, what are you waiting for?"
    call scene_iwanka_sex.pre
    with {'master': dissolve}
    iwanka "Fuck me, {b}[firstname]{/b}!"
    call scene_iwanka_sex.insert
    with {'master': dissolve}
    iwanka "Mmm, that's it!"
    call scene_iwanka_sex.slam
    iwanka "Ngh!!" with hpunch
    iwanka "Oh em gee, that's a big fucking dick!"
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
        iwanka "Oh, wow!"

    elif opt == 2:
        iwanka "Yeah, that's it!"

    elif opt == 3:
        iwanka "You like that, {b}[firstname]{/b}?"
        anon "Yes!{p=1}{nw}"

    elif opt == 4:
        iwanka "You like watching me bounce on that big meaty cock?!"
        anon "Ahh, yes!"

        if rng < .4:
            iwanka "Tell me how much you like it!"

        anon "So much!!"

        if rng < .4:
            anon "Ahh, I like it so much!!"

    return


label scene_iwanka_sex.switch:
    iwanka "Haah... Haah..."
    iwanka "... Okay, I need a break."
    anon "Oh?"
    call scene_iwanka_bed_tiger.insert
    with {'master': dissolve}
    iwanka "You wanna switch back to doggy?"
    hide anim
    show iwanka_body_b_sex_ride_anon as anon_body
    with {'master': dissolve}
    anon "Yeah, sure!"

    $ M_iwanka.set('sex speed', 1. / 8)

    call scene_iwanka_sex.pre
    show iwanka_overlay_o_sex_dick_pre as iwanka
    with {'master': dissolve}
    pause
    call scene_iwanka_sex.pre
    with {'master': dissolve}
    iwanka "Yeah, this is much better."
    call scene_iwanka_sex.insert
    with {'master': dissolve}
    pause
    call scene_iwanka_sex.animate
    with {'master': dissolve}
    iwanka "Ngh!!"
    pause
    jump scene_iwanka_sex.resume


label scene_iwanka_sex.repeat(venue):
    $ M_iwanka.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='repeat')

    call scene_iwanka_sex.prelude
    with fade
    iwanka "Umm, what's the hold up?"
    anon "Nothing, I was just admiring the view..."
    iwanka "Well, do that later!"
    call scene_iwanka_sex.stage
    with {'master': dissolve}
    iwanka "Right now, I just want you to fuck me."
    anon "Yeah, alright."
    call scene_iwanka_sex.pre
    with {'master': dissolve}
    iwanka "Oh, I have so been craving this."
    call scene_iwanka_sex.insert
    with {'master': dissolve}
    anon "Wow, you're really wet!"
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

    iwanka "I'm gonna cum!"
    anon "Me too!"
    pause
    iwanka "OH!!"
    iwanka "EM!!"
    iwanka "GEEEE!!!"
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

    anon "That was awesome!"
    iwanka "It was, wasn't it?"
    pause
    iwanka "Umm, can you get me a towel?"
    anon "Hmm?"

    if _return == 'inside':
        iwanka "Your cum is leaking out of me onto the sheets..."
        call call_pregnancy_minigame (None, M_iwanka)
    else:

        iwanka "I'm like, covered in your cum..."

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
            "Yacht (First)" if 'first' in variants:
                jump scene_iwanka_sex.first

            "Yacht (Repeat)" if 'yacht' in variants:
                jump scene_iwanka_sex.yacht

            "Bedroom (Repeat)" if 'bedroom' in variants:
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

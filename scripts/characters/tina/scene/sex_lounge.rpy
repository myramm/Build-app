label scene_tina_sex_lounge:
    $ M_tina.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='first')

    call scene_tina_sex_lounge.stage
    with fade
    pause
    show tina b_sex_insert_pullout
    with {'master': dissolve}
    pause
    show tina b_sex_talk f_moan
    with {'master': dissolve}
    anon "!!!"
    tina f_normal @ f_moan "Haah!"
    tina "Oh, fuck!"
    pause
    tina "Now that's a big dick!"
    anon "Oh my god..."
    anon "I can't believe this is happening!"
    call scene_tina_sex_lounge.animate
    with {'master': dissolve}
    pause
    tina @ -m_talk "Mmm!"
    anon "I'm gonna cum!"
    hide anim
    show anon b_tina_sex
    show tina b_sex_talk
    with {'master': dissolve}
    tina "No!"
    anon "Wha-"
    anon "Why did you stop?!"
    tina "You are not allowed to cum until I say so!"
    anon "Huh?!"
    anon "T-that's not-"
    tina "It's my next instruction!"
    anon @ -m_talk "..."
    tina "And you're gonna follow my instructions, aren't you, babyface?"
    anon "I mean, I'll try..."
    call scene_tina_sex_lounge.animate
    with {'master': dissolve}
    tina "I can't hear you!"
    anon "Haah!"
    pause
    call scene_tina_sex_lounge.dialogue (1)
    pause
    call scene_tina_sex_lounge.dialogue (2)
    pause
    call scene_tina_sex_lounge.dialogue (3)
    pause
    call scene_tina_sex_lounge.dialogue (4)
    call scene_tina_sex_lounge.loop
    tina "I'm almost..."
    pause
    tina "... Almost there!"
    tina "Holy fuck!"
    pause
    tina "Haah!"
    pause
    tina "HAAAH!!"
    anon "{b}Tina{/b}, I can't-"
    pause
    tina "Look at me!"
    anon "Uh huh?"
    tina "We're gonna cum together!"
    tina "Say it!"
    anon "We're gonna cum together."
    pause
    tina "HERE!"
    tina "IT!!"
    tina "COMES!!!"
    call scene_tina_sex_lounge.cum (_return)
    return


label scene_tina_sex_lounge.stage:
    scene location_tina_lounge_sex
    show anon b_tina_sex
    show tina b_sex_laydown_getup
    return


label scene_tina_sex_lounge.insert:
    show tina b_sex_insert_pullout
    return


label scene_tina_sex_lounge.animate:
    hide anon
    hide tina
    show tina_lounge_cowgirl as anim
    return


label scene_tina_sex_lounge.loop:
    call screen scene_tina_sex_lounge_controls

    if _return:
        return _return

    python hide:
        blocks = 4 if variant == 'first' else 7
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_tina_sex_lounge.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_tina_sex_lounge.loop


label scene_tina_sex_lounge.dialogue(opt, rng=-1):
    if opt == 1:
        tina "Say you will follow my instructions!"
        anon "Y-yes!"

        if rng < .2:
            anon "I will follow your-"
            anon "Oh god!"

        tina "Good boy."

    elif opt == 2:
        tina "Ahh!"
        anon "This is-"

    elif opt == 3:
        tina "It's so fucking thick!"
        anon "You're going too fast!"
        tina "Focus, babyface!"

    elif opt == 4:
        tina "Just breathe."

    elif opt == 5:
        tina "Give it to me big boy!"

    elif opt == 6:
        anon "You are so sexy!"
        tina "Oh, yeah?"

    elif opt == 7:
        anon "I love your big tits!"
        tina "What else do you like?"

        if rng < 0 or 0 <= rng < .3:
            anon "That fiery red hair!"
            tina "Keep going!"

        if rng < 0 or .3 <= rng < .6:
            anon "Those beautiful blue eyes."
            tina "Ahh!"

        if rng < 0 or .6 <= rng < 1:
            anon "This thick, luscious ass."
            tina "Oh, {b}[firstname]{/b}..."

    return


label scene_tina_sex_lounge.switch:
    tina "Here, lemme get on top again."
    anon "Hmm?"
    tina "I wanna finish on top."
    call scene_tina_lounge_doggy.insert
    with {'master': dissolve}
    anon "Oh, uhh..."
    show tina b_sex_doggy_insert_anon as anon_body
    show tina_body_b_sex_doggy_insert_arm as anon_arm
    call scene_tina_lounge_doggy.pre
    with {'master': dissolve}
    anon "... Yeah, alright."
    hide anim
    hide leg
    show tina b_sex_inbetween f_sexy_left behind anon_body
    with {'master': dissolve}
    pause

    $ M_tina.set('sex speed', 1. / 8)

    hide anon_body
    hide anon_arm
    show tina f_sexy_down
    show anon b_tina_sex
    with {'master': dissolve}
    pause
    show anon behind tina
    jump scene_tina_sex_lounge.merge


label scene_tina_sex_lounge.cum(where):
    hide anim

    if where == 'inside':
        show tina b_sex_cum
    else:
        show tina b_sex_cumshot
        show tina_sex_body_cumshot_dick

    anon "HNNGGG!!!" with flash

    if where == 'inside':
        show xray_tina_top with fastdissolve:
            align (0, 0)

    tina "NGGHHH!!!"
    show anon b_tina_sex behind tina
    show tina b_sex_talk

    if where == 'inside':
        hide xray_tina_top
    else:
        show tina_overlay_sex_o_cumshot behind tina
        hide tina_sex_body_cumshot_dick

    with {'master': dissolve}
    pause
    anon "Haah... Haah..."
    anon "Wow!"
    anon "That was..."
    tina "Vigorous?"
    anon "Y-yeah."
    tina "Hehe!"

    if where == 'inside':
        call call_pregnancy_minigame (None, M_tina)
    return


label scene_tina_sex_lounge.first:
    jump scene_tina_sex_lounge


label scene_tina_sex_lounge.repeat:
    $ M_tina.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='repeat')

    call scene_tina_sex_lounge.stage
    with fade
    pause
    label scene_tina_sex_lounge.merge:
    show tina b_sex_insert_pullout
    with {'master': dissolve}
    pause
    show tina b_sex_talk f_moan
    with {'master': dissolve}
    anon "!!!"
    tina f_normal @ f_moan "Haah!"
    pause
    tina "Mmm, I'm so glad {b}Tony{/b} sent you!"
    anon "Y-yeah, me too!"
    call scene_tina_sex_lounge.animate
    with {'master': dissolve}
    call scene_tina_sex_lounge.dialogue (5)
    pause
    call scene_tina_sex_lounge.dialogue (6)
    pause
    call scene_tina_sex_lounge.dialogue (7)
    pause
    label scene_tina_sex_lounge.resume:
    call scene_tina_sex_lounge.loop

    if _return == 'switch':
        jump scene_tina_lounge_doggy.switch

    tina "I'm gonna cum!"
    anon "Me too!"
    tina "Together then!"
    pause
    tina "Almost!"
    tina "There!!"
    call scene_tina_sex_lounge.cum (_return)
    return


label scene_tina_sex_lounge.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['tina']['variants']['01_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_tina_lounge) with fade
        menu:
            "First" if 'first' in variants:
                jump scene_tina_sex_lounge.first

            "Repeat" if 'repeat' in variants:
                jump scene_tina_sex_lounge.repeat

    jump expression 'scene_tina_sex_lounge.{}'.format(next(iter(variants)))


screen scene_tina_sex_lounge_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')
            if variant == 'repeat':
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

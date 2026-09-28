label scene_liu_sex_bedroom:
    $ M_liu.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='first')

    call scene_liu_sex_bedroom.stage
    with fade
    liu "Hurry!"
    call scene_liu_sex_bedroom.pre
    with {'master': dissolve}
    liu "{b}[firstname]{/b}... Please!"
    call scene_liu_sex_bedroom.insert
    with {'master': dissolve}
    liu "Ahh!!!"
    pause
    liu "Oh god!"
    liu "You're so big!"
    pause
    call scene_liu_sex_bedroom.animate
    with {'master': dissolve}
    liu "Ngh!!!"
    pause
    anon "Are you okay?"
    liu "Yes!"
    liu "Yes!!"
    pause
    liu "I've never..."
    liu "... Felt anything..."
    liu "... Like this before!"
    pause
    anon "Good?"
    liu "YES!!"
    pause
    liu "I had no idea..."
    liu "... It could be..."
    liu "... Like this!!"
    pause
    liu "I'm gonna-"
    pause
    liu "Haaaah... I'M GONNA-"
    pause
    liu "{i}*Whimpers*{/i}"
    pause
    show liu b_sex_bed_surprise as anim
    kim "AIYAH!!" with hpunch
    kim "WHAT YOU DOING?!"
    anon "Hmm?"
    return


label scene_liu_sex_bedroom.stage:
    scene expression game.timer.image('location_liu_bedroom_sex{}')
    show liu b_sex_bed_pre
    return


label scene_liu_sex_bedroom.pre:
    show liu od_insert
    return


label scene_liu_sex_bedroom.insert:
    show liu b_sex_bed_base
    show anon liu_sex_bedroom
    return


label scene_liu_sex_bedroom.animate:
    hide anon
    hide liu
    show liu_sex_bed_anim as anim
    return


label scene_liu_sex_bedroom.loop:
    call screen scene_liu_sex_bedroom_controls

    if _return:
        return _return

    python hide:
        blocks = 6
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_liu_sex_bedroom.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_liu_sex_bedroom.loop


label scene_liu_sex_bedroom.dialogue(opt, rng=-1):
    if opt == 1:
        liu "{b}[firstname]{/b}!"

    elif opt == 2:
        liu "Oh, fuck me!"

    elif opt == 3:
        anon "You're squeezing me so tight!"
        liu "Fuck me, {b}[firstname]{/b}!!"

    elif opt == 4:
        anon "Oh, wow!"
        liu "Ahh!"

    elif opt == 5:
        liu "You feel amazing!"

    elif opt == 6:
        liu "{i}*Whimpers*{/i}"

    return


label scene_liu_sex_bedroom.switch:
    show liu_bedroom_thirst 5 as anim
    with {'master': dissolve}
    liu "Mmm."

    $ M_liu.set('sex speed', 1. / 8)

    show liu_sex_bed_anim 1 as anim
    with {'master': dissolve}
    pause .5
    call scene_liu_sex_bedroom.animate
    with {'master': dissolve}
    jump scene_liu_sex_bedroom.resume


label scene_liu_sex_bedroom.cum(where):
    liu "I'm gonna cum!"
    anon "Me too!"
    pause
    liu "Oh, god!!"
    liu "Oh my god!!"
    pause
    liu "{b}[firstname]{/b}!!!"
    liu "NGGHHH!!!"
    hide anim

    if where == 'inside':
        show liu b_sex_bed_cum
    else:
        show liu b_sex_bed_pre od_cumshot

    anon "HNNGGG!!!" with flash

    if where == 'inside':
        show xray_liu_sex_bed with fastdissolve
        pause
        hide xray_liu_sex_bed with {'master': dissolve}
    else:

        show liu od_cumshot3

    anon "Haah... Haah..."
    return where


label scene_liu_sex_bedroom.first:
    $ M_liu.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='first')

    call scene_liu_sex_bedroom.stage
    with fade
    call scene_liu_sex_bedroom.pre
    with {'master': dissolve}
    liu "It's so big, I can barely-"
    pause
    call scene_liu_sex_bedroom.insert
    with {'master': dissolve}
    liu "Ngh!"
    pause
    anon "Take it slow, I don't want you to hurt yourself..."
    liu "Y-yeah, okay."
    pause
    call scene_liu_sex_bedroom.animate
    with {'master': dissolve}
    pause
    liu "Mmm, god."
    jump scene_liu_sex_bedroom.merge


label scene_liu_sex_bedroom.repeat:
    $ M_liu.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='repeat')

    call scene_liu_sex_bedroom.stage
    with fade
    call scene_liu_sex_bedroom.pre
    with {'master': dissolve}
    pause
    call scene_liu_sex_bedroom.insert
    with {'master': dissolve}
    liu "Ngh!"
    anon "Oh god, {b}Liu{/b}..."
    pause
    call scene_liu_sex_bedroom.animate
    with {'master': dissolve}
    liu "Haah!"
    pause
    liu "Yes!!"
    label scene_liu_sex_bedroom.merge:
    call scene_liu_sex_bedroom.dialogue (1)
    pause
    call scene_liu_sex_bedroom.dialogue (2)
    pause
    call scene_liu_sex_bedroom.dialogue (3)
    pause
    call scene_liu_sex_bedroom.dialogue (4)
    pause
    call scene_liu_sex_bedroom.dialogue (5)
    pause
    call scene_liu_sex_bedroom.dialogue (6)
    label scene_liu_sex_bedroom.resume:
    call scene_liu_sex_bedroom.loop

    if _return == 'switch':
        jump scene_liu_bedroom_thirst.switch

    call scene_liu_sex_bedroom.cum (_return)

    if _return == 'inside':
        show anon liu_sex_bedroom
        show liu b_sex_bed_base
        with dissolve
        pause
        liu "That was a amazing!"
        anon "Heh, thanks."
        liu "I can feel it inside..."
        liu "... It's so warm."
        pause
        hide anon
        show liu b_sex_bed_pre o_after
        with dissolve
        pause
        show liu b_sex_bed_cuddle with {'master': dissolve}
        anon "Would you like me to get you anything?"
        anon "A towel or some-"
        liu "N-no, it's okay."
    else:

        liu "That was incredible!"
        anon "Heh, thanks."
        liu "You came so much!"
        show liu b_sex_bed_cuddle with dissolve
        pause
        anon "Let me get you a towel or something."
        liu "N-no, it's okay."

    liu "Could you just stay here like this, with me, for a little while?"
    liu "... Please."
    pause
    anon "Y-yeah, okay."
    liu "Thanks, {b}[firstname]{/b}."
    pause

    if _return == 'inside':
        call call_pregnancy_minigame (None, M_liu)
    return


label scene_liu_sex_bedroom.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['liu']['variants']['01_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_liu_bedroom) with fade
        menu:
            "First" if 'first' in variants:
                jump scene_liu_sex_bedroom.first

            "Repeat" if 'repeat' in variants:
                jump scene_liu_sex_bedroom.repeat

    jump expression 'scene_liu_sex_bedroom.{}'.format(next(iter(variants)))


screen scene_liu_sex_bedroom_controls():
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
                action (Function(M_liu.set, 'sex speed',
                                 1 / (1 / M_liu.get('sex speed') - 2)),
                        Return(False))
                sensitive M_liu.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_liu.set, 'sex speed',
                                 1 / (1 / M_liu.get('sex speed') + 2)),
                        Return(False))
                sensitive M_liu.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

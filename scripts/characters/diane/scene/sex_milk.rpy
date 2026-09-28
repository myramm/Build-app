label scene_diane_sex_milk:

    return


label scene_diane_sex_milk.animate:
    show diane_sex_milk_anim as body
    return


label scene_diane_sex_milk.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                call scene_diane_sex_milk.animate
                $ animated = True
            pause 5
            call scene_diane_sex_milk.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = range(1, 10)
            $ poses_done = []
            while poses_done != pose_list:
                show expression "diane_sex_milk_anim {}".format(
                    pose_list[pose_counter]) as body
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_diane_sex_milk.dialogue
        $ animcounter += 1
    call screen scene_diane_sex_milk_controls()
    if not _return:
        jump scene_diane_sex_milk.loop
    return _return


label scene_diane_sex_milk.dialogue:
    $ renpy.dynamic(rng=renpy.random.random())

    if animcounter == 0 and rng <= .33:
        diane "Oh, I missed this!"
        anon "Yeah, me too."
    elif animcounter == 0 and rng <= .66:
        anon "Man, this hay is kinda itchy on my butt..."
        diane "Hmm?"
        anon "... N-nothing, never mind."
    elif animcounter == 0 and rng <= .77:
        diane "Ahh!!"
    elif animcounter == 0 and rng <= .88:
        diane "OH, GOD!!!"
    elif animcounter == 0 and rng <= .99:
        anon "Oh, god!"

    elif animcounter == 1 and rng <= .33:
        anon "I'm really glad we're doing it again."
        diane "Mhmm!!"
    elif animcounter == 1 and rng <= .66:
        diane "Ngh, I just love this dick..."
        diane "... Pounding..."
        diane "... Into my pussy!"

    elif animcounter == 2 and rng <= .33:
        diane "Give it to me, {b}[firstname]{/b}!"
        diane "It's so good!"
    elif animcounter == 2 and rng <= .66:
        diane "Breed me, {b}[firstname]{/b}!"
        diane "Flood my womb!!"
        anon "Ahh!"
    elif animcounter == 2 and rng <= .99:
        diane "You like me riding you?"
        anon "Yes!"
        if rng <= .77:
            pause
            diane "Riding you in this filthy barn?"
            anon "YES!!!"
            diane "AHH!!!"

    return


label scene_diane_sex_milk.repeat(outfit='naked'):
    python:
        renpy.dynamic(anim_toggle=True, animated=True, animcounter=0,
                      pose_counter=0, pose_list=None, poses_done=None)
        M_diane.set('sex speed', 1 / 8.)

    scene location_barn_hay_stack_milk
    show diane_sex_milk_base as body
    show diane_sex_milk_rub01 as dick
    show diane a_empty b_empty f_sex_milk_happy_down
    with fade
    anon "Wow, you're really wet, {b}Diane{/b}!"
    show diane f_sex_milk_sexy_back
    with {'master': fastdissolve}
    diane "It's those milking sessions..."
    hide diane
    hide dick
    $ renpy.dynamic(face='diane_face_f_sex_milk_sexy_back')
    show diane_sex_milk_rub as body
    with {'master': dissolve}
    anon "!!!"
    $ renpy.dynamic(face='diane_face_f_sex_milk_moan')
    diane @ -m_talk "... Ngh!"
    show diane_sex_milk_insert as body
    with {'master': dissolve}
    anon "Haah!"
    call scene_diane_sex_milk.animate
    with {'master': dissolve}
    pause

    call scene_diane_sex_milk.loop

    anon "{b}Diane{/b}, I'm gonna-"
    anon "I'm gonna-"
    diane "Me too!!"
    pause
    diane "NGGHHH!!!"
    hide animation
    show diane_sex_milk_cum as body
    show diane_sex_milk_squirt_cum as milk
    anon "HNNGGG!!!" with flash
    show xray_diane_sex_milk as xray
    with {'master': fastdissolve}
    pause
    hide xray
    show diane_sex_milk_base as body
    show diane a_empty b_empty f_sex_milk_exhausted_down m_talk
    show diane_sex_milk_squirt_base as milk
    with {'master': dissolve}
    anon "Haah... Haah..."
    show diane f_sex_milk_happy_down -m_talk
    with {'master': fastdissolve}
    diane "Heh, I guess there was still a bit left in there..."
    show diane f_sex_milk_embarrassed_back
    with {'master': fastdissolve}
    anon "I'll get it."
    show diane f_sex_milk_concerned_back
    with {'master': fastdissolve}
    diane @ -m_talk "... Hmm?"
    show diane_sex_milk_pump_base as body
    show diane f_sex_milk_exhausted_down
    show diane_sex_milk_squirt02 as milk
    show diane_sex_milk_squirt06 as pump
    with {'master': dissolve}
    diane "Oh, I dunno if we should-"
    hide milk
    hide pump
    show diane_sex_milk_pump as body
    show diane f_sex_milk_moan
    with {'master': dissolve}
    diane "Ngh!!"
    with {'master': fastdissolve}
    anon "There we go..."
    show diane f_sex_milk_ecstasy
    with {'master': fastdissolve}
    diane @ -m_talk "Fffuuuuu-"
    show diane f_sex_milk_moan
    with {'master': fastdissolve}
    anon "... Just let it all out."
    pause
    diane "Squeeze my udder harder, {b}[firstname]{/b}!"
    anon "Like this?"
    diane "Yes!!"
    pause
    show diane_sex_milk_pump_base as body
    show diane f_sex_milk_moan
    show diane_sex_milk_squirt02 as milk
    show diane_sex_milk_squirt05 as pump
    with {'master': dissolve}
    diane "Haah... Haah..."
    show diane f_sex_milk_exhausted_down
    with {'master': fastdissolve}
    anon "Is that everything?"
    show diane f_sex_milk_embarrassed_back
    with {'master': fastdissolve}
    diane "I think so..."
    hide pump
    show diane_sex_milk_base as body
    show diane f_sex_milk_happy_down
    show diane_sex_milk_squirt_base as milk
    with {'master': dissolve}
    pause
    hide diane
    show diane_sex_milk_pullout as body
    show diane_sex_milk_squirt_pullout as milk
    with {'master': dissolve}
    diane "... Phew!"
    call call_pregnancy_minigame (None, M_diane)
    return


label scene_diane_sex_milk.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['Diane']['variants']['08_unlocked'])

    if len(variants) > 1:
        scene expression im.Blur('backgrounds/location_barn_day.jpg', 1.7) with fade
        menu:
            "Cowsuit" if 'cow' in variants:
                call scene_diane_sex_milk.repeat ('cow')

            "Naked" if 'naked' in variants:
                call scene_diane_sex_milk.repeat ('naked')
    else:

        call scene_diane_sex_milk.repeat (next(iter(variants)))

    return


screen scene_diane_sex_milk_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_diane.set, 'sex speed',
                                 1 / (1 / M_diane.get('sex speed') - 2)),
                        Return(False))
                sensitive M_diane.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_diane.set, 'sex speed',
                                 1 / (1 / M_diane.get('sex speed') + 2)),
                        Return(False))
                sensitive M_diane.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

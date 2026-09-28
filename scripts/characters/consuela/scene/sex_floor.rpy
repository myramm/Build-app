label scene_consuela_sex_floor:

    return


label scene_consuela_sex_floor.ready:
    show consuela b_floor f_confused
    show consuela_mc_body_floor base
    show consuela_mc_dick_floor pre
    return


label scene_consuela_sex_floor.pre:
    show consuela b_floor_base o_empty
    show consuela_mc_body_floor insert_pullout
    hide consuela_mc_dick_floor
    return


label scene_consuela_sex_floor.insert:
    hide consuela_mc_body_floor
    hide consuela
    if M_consuela.outfit.get == "naked":
        show consuela_floor_naked 1 as consuela_floor
    else:
        show consuela_floor 1
    return


label scene_consuela_sex_floor.animate:
    python:
        anim_toggle = True
        animated = True
        M_consuela.set('sex speed', .12)
    if M_consuela.outfit.get == "naked":
        show expression AnimatedImage("consuela_floor_naked", [1,2,3,4,5,6,7], M_consuela) as consuela_floor at Position(xalign=0., yoffset=0)
    else:
        show expression AnimatedImage("consuela_floor", [1,2,3,4,5,6,7], M_consuela) as consuela_floor at Position(xalign=0., yoffset=0)
    return


label scene_consuela_sex_floor.loop:
    $ M_consuela.set('sex_location', 'floor')
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                if M_consuela.outfit.get == "naked":
                    show expression AnimatedImage("consuela_floor_naked", [1,2,3,4,5,6,7], M_consuela) as consuela_floor at Position(xalign=0., yoffset=0)
                else:
                    show expression AnimatedImage("consuela_floor", [1,2,3,4,5,6,7], M_consuela) as consuela_floor at Position(xalign=0., yoffset=0)
                $ animated = True
            pause 5
            call scene_consuela_sex_floor.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7]
            $ poses_done = []
            while poses_done != pose_list:
                if M_consuela.outfit.get == "naked":
                    show expression "consuela_floor_naked {}".format(pose_list[pose_counter]) as consuela_floor at Position(xalign=0., yoffset=0)
                else:
                    show expression "consuela_floor {}".format(pose_list[pose_counter]) as consuela_floor at Position(xalign=0., yoffset=0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_consuela_sex_floor.dialogue
        $ animcounter += 1
    call screen scene_consuela_sex_floor_controls
    if not _return:
        jump scene_consuela_sex_floor.loop
    return _return


label scene_consuela_sex_floor.dialogue:
    if animcounter == 0 and randomizer() < 50:
        anon "You like that?{p=1}{nw}"
        consuela "Si, papi!{p=1}{nw}"
        consuela "I like!{p=1}{nw}"
        pause 1
        consuela "OH, I LIKE!!!{p=1}{nw}"
    if animcounter == 1 and randomizer() > 50:
        consuela "¡Oh papi!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 50:
        consuela "Fuck me!{p=1}{nw}" (show_native="¡Que me jodan!")
        consuela "Fuck your dirty little maid!{p=2}{nw}" (show_native="¡A la mierda con tu criada sucia!")
    return


label scene_consuela_sex_floor.inside:
    hide consuela_floor
    show consuela b_floor_cum
    anon "HNNGGG!!!" with flash
    show xray_consuela floor with fastdissolve:
        align (0,0)
    consuela "NGGHHH!!!"
    hide xray_consuela
    show consuela b_floor_base
    show consuela_mc_body_floor insert_pullout
    with dissolve
    pause
    anon "Haah... Haah..."
    show consuela b_floor f_normal_down
    show consuela_mc_body_floor base
    show consuela_mc_dick_floor after
    show consuela o_floor_after_cum_drip
    with dissolve
    anon "Wow!"
    consuela "My god!" (show_native="¡Santo cielo!")
    consuela "That was amazing!" (show_native="¡Eso fue increíble!")
    consuela "Hehe!"
    anon "I came inside you..."
    consuela "Hmm?"
    consuela "Oh, es okay."
    anon "But you could get pregnant..."
    consuela "I doubt we conceive." (show_native="Dudo que concibamos.")
    consuela "Very unlikely at my age." (show_native="Muy poco probable a mi edad.")
    anon "..."
    consuela "No worry, okay?"
    anon "O-okay."

    call call_pregnancy_minigame (None, M_consuela)
    return


label scene_consuela_sex_floor.outside:
    hide consuela_floor
    show consuela b_floor_base
    show consuela_mc_body_floor base
    show consuela_mc_dick_floor cumshot
    anon "HNNGGG!!!" with flash
    consuela "NGGHHH!!!"
    show consuela b_floor f_normal_down
    show consuela o_floor_after_cumshot
    show consuela_mc_dick_floor after
    with dissolve
    pause
    anon "Haah... Haah..."
    anon "That was awesome!"
    consuela "My god!" (show_native="¡Santo cielo!")
    consuela "I'm a mess..." (show_native="Soy un desastre...")
    consuela "Hehe!"
    return


label scene_consuela_sex_floor.repeat:
    if renpy.get_mode() == 'say':
        call scene_consuela_sex_floor.ready
        with {'master': dissolve}
    else:
        scene location_beach_house_kitchen_floor
        call scene_consuela_sex_floor.ready
        with fade
    consuela "Like an animal?" (show_native="¿Como un animal?")
    call scene_consuela_sex_floor.pre
    with dissolve
    anon "You'd better hold on..."
    consuela "¿Qué?"
    call scene_consuela_sex_floor.insert
    with fastdissolve
    consuela "!!!"
    call scene_consuela_sex_floor.animate
    with dissolve
    consuela "Oh my god!" (show_native="¡Ay dios mío!")
    consuela "Ahh!!"
    label scene_consuela_sex_floor.resume:
    call scene_consuela_sex_floor.loop
    if _return == 'switch':
        jump scene_consuela_sex_floor_anal.switch
    anon "I'm getting close!"
    consuela "I'm coming!" (show_native="¡Me vengo!")
    pause
    consuela "¡Gracias!!"
    if _return == 'inside':
        call scene_consuela_sex_floor.inside
    else:
        call scene_consuela_sex_floor.outside
    return


label scene_consuela_sex_floor.replay:
    python:
        M_consuela.set('doing_anal', False)
        M_consuela.set('done_anal', True)
    jump scene_consuela_sex_floor.repeat


label scene_consuela_sex_floor.switch:
    hide consuela_floor
    call scene_consuela_sex_floor.pre
    with dissolve
    consuela "Ay!!!"
    call scene_consuela_sex_floor.insert
    with fastdissolve
    consuela "!!!"
    call scene_consuela_sex_floor.animate
    with dissolve
    consuela "My pussy again?" (show_native="¿Mi coño de nuevo?")
    consuela "Mmm, you're driving me wild, {b}Mister [firstname]{/b}!" (show_native="¡Mmm, me estás volviendo loca, {b}Mister [firstname]{/b}!")
    anon "You are the best maid ever, {b}Consuela{/b}!"
    consuela "Si, best maid!"
    consuela "Fuck good!"
    pause
    consuela "Ahh!!!"
    jump scene_consuela_sex_floor.resume


screen scene_consuela_sex_floor_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')

            if M_consuela.get('sex_location') == 'floor':
                textbutton _('Anal') action Return('switch')
            elif M_consuela.get('done_anal'):
                textbutton _('Vaginal') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_consuela.set,
                                 'sex speed',
                                 M_consuela.get('sex speed') + 0.03),
                        Return(False))
                sensitive M_consuela.get('sex speed') < .12
            textbutton _('Faster »'):
                action (Function(M_consuela.set,
                                 'sex speed',
                                 M_consuela.get('sex speed') - 0.03),
                        Return(False))
                sensitive M_consuela.get('sex speed') > .061
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

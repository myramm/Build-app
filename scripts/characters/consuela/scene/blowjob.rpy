label scene_consuela_blowjob:
    scene location_beach_house_kitchen_bj
    call scene_consuela_blowjob.animate
    with fade
    pause
    anon "You know, this wasn't in the job description when I said you could work here..."
    call scene_consuela_blowjob.loop
    if _return:
        call scene_consuela_blowjob.inside
    return


label scene_consuela_blowjob.animate:
    python:
        anim_toggle = True
        animated = True
        M_consuela.set('sex speed', .10)
    if M_consuela.outfit.get == "naked":
        show expression AnimatedImage("consuela_bj_naked", [1,2,3,4,5,6,7,8,9,10,11,12], M_consuela) as consuela_bj at Position(xalign=0., yoffset=0)
    else:
        show expression AnimatedImage("consuela_bj", [1,2,3,4,5,6,7,8,9,10,11,12], M_consuela) as consuela_bj at Position(xalign=0., yoffset=0)
    return


label scene_consuela_blowjob.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_consuela.outfit.get == "naked":
                    show expression AnimatedImage("consuela_bj_naked", [1,2,3,4,5,6,7,8,9,10,11,12], M_consuela) as consuela_bj at Position(xalign=0., yoffset=0)
                else:
                    show expression AnimatedImage("consuela_bj", [1,2,3,4,5,6,7,8,9,10,11,12], M_consuela) as consuela_bj at Position(xalign=0., yoffset=0)
                $ animated = True
            pause 5
            call scene_consuela_blowjob.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10,11,12]
            $ poses_done = []
            while poses_done != pose_list:
                if M_consuela.outfit.get == "naked":
                    show expression "consuela_bj_naked {}".format(pose_list[pose_counter]) as consuela_bj at Position(xalign=0., yoffset=0)
                else:
                    show expression "consuela_bj {}".format(pose_list[pose_counter]) as consuela_bj at Position(xalign=0., yoffset=0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_consuela_blowjob.dialogue
        $ animcounter += 1
    call screen scene_consuela_blowjob_controls
    if not _return:
        jump scene_consuela_blowjob.loop
    return _return


label scene_consuela_blowjob.dialogue:
    if animcounter == 0 and randomizer() < 20:
        anon "Oh, that's nice.{p=1}{nw}"
    if animcounter == 1 and randomizer() < 20:
        anon "Oh, wow!{p=1}{nw}"
        consuela "{i}*Sluuuuuuurp*{/i}{p=1}{nw}"
    elif animcounter == 1 and randomizer() < 50:
        consuela "{i}*Glllcck*{/i}{p=1}{nw}"
        consuela "Mmm.{p=1}{nw}"
    if animcounter == 2 and randomizer() < 20:
        anon "You are the best maid ever, {b}Consuela{/b}!{p=2}{nw}"
    if animcounter == 3 and randomizer() < 20:
        anon "Oh yeah, clean it {b}Consuela{/b}.{p=1.5}{nw}"
        consuela "Hehe!{p=1}{nw}"
    return


label scene_consuela_blowjob.inside:
    anon "I can't hold it!"
    pause
    anon "{b}Consuela{/b}, I can't-"
    pause
    hide consuela_bj
    show consuela b_bj_cum
    anon "HNNGGG!!!" with flash
    pause
    show consuela b_bj_talking with dissolve
    consuela "Oh, {b}Mister [firstname]{/b}!" (show_native="¡Ay {b}Mister [firstname]{/b}!")
    anon "Phew..."
    consuela "That was a lot!" (show_native="¡Eso fue mucho!")
    consuela "Hehehe!"
    return


label scene_consuela_blowjob.repeat:
    if L_beachhouse_kitchen.is_here(M_consuela):
        scene location_beach_house_kitchen_bj
    else:
        scene location_beach_house_entrance_bj
    call scene_consuela_blowjob.animate
    with fade
    pause
    call scene_consuela_blowjob.loop
    if _return:
        call scene_consuela_blowjob.inside
    return


label scene_consuela_blowjob.replay:
    python:
        M_consuela.place(place=L_beachhouse_kitchen)
        M_consuela.force(flag=True)
    jump scene_consuela_blowjob.repeat


screen scene_consuela_blowjob_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return('inside')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_consuela.set,
                                 'sex speed',
                                 M_consuela.get('sex speed') + 0.015),
                        Return(False))
                sensitive M_consuela.get('sex speed') < .10
            textbutton _('Faster »'):
                action (Function(M_consuela.set,
                                 'sex speed',
                                 M_consuela.get('sex speed') - 0.015),
                        Return(False))
                sensitive M_consuela.get('sex speed') > .071
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

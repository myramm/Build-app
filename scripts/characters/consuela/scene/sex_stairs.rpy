label scene_consuela_sex_stairs:

    return

label scene_consuela_sex_stairs.ready:
    show consuela b_stairs
    show consuela_mc_body_stairs base
    show consuela_mc_dick_stairs pre
    return


label scene_consuela_sex_stairs.pre:
    show consuela_mc_body_stairs insert_pullout
    hide consuela_mc_dick_stairs
    return


label scene_consuela_sex_stairs.insert:
    hide consuela_mc_body_stairs
    hide consuela
    if M_consuela.outfit.get == "naked":
        show consuela_stairs_naked 1 as consuela_stairs
    else:
        show consuela_stairs 1
    return


label scene_consuela_sex_stairs.animate:
    python:
        anim_toggle = True
        animated = True
        M_consuela.set('sex speed', .12)
    if M_consuela.outfit.get == "naked":
        show expression AnimatedImage("consuela_stairs_naked", [1,2,3,4,5,6,7], M_consuela) as consuela_stairs at Position(xalign=0., yoffset=0)
    else:
        show expression AnimatedImage("consuela_stairs", [1,2,3,4,5,6,7], M_consuela) as consuela_stairs at Position(xalign=0., yoffset=0)
    return


label scene_consuela_sex_stairs.loop:
    $ M_consuela.set('sex_location', 'stairs')
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                if M_consuela.outfit.get == "naked":
                    show expression AnimatedImage("consuela_stairs_naked", [1,2,3,4,5,6,7], M_consuela) as consuela_stairs at Position(xalign=0., yoffset=0)
                else:
                    show expression AnimatedImage("consuela_stairs", [1,2,3,4,5,6,7], M_consuela) as consuela_stairs at Position(xalign=0., yoffset=0)
                $ animated = True
            pause 5
            call scene_consuela_sex_stairs.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7]
            $ poses_done = []
            while poses_done != pose_list:
                if M_consuela.outfit.get == "naked":
                    show expression "consuela_stairs_naked {}".format(pose_list[pose_counter]) as consuela_stairs at Position(xalign=0., yoffset=0)
                else:
                    show expression "consuela_stairs {}".format(pose_list[pose_counter]) as consuela_stairs at Position(xalign=0., yoffset=0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_consuela_sex_stairs.dialogue
        $ animcounter += 1
    call screen scene_consuela_sex_stairs_controls
    if not _return:
        jump scene_consuela_sex_stairs.loop
    return _return


label scene_consuela_sex_stairs.dialogue:
    if animcounter == 0 and randomizer() > 50:
        consuela "Oh, daddy!{p=1}{nw}" (show_native="¡Ay papi!")
    if animcounter == 1 and randomizer() < 50:
        consuela "Fuck your dirty little maid!{p=1}{nw}" (show_native="¡A la mierda con tu criada sucia!")
        anon "Oh, I love it when you talk to me in Spanish!{p=1}{nw}"
    if animcounter == 2 and randomizer() > 50:
        consuela "Fuck me harder!{p=1}{nw}" (show_native="¡Cógeme más duro!")
        if M_consuela.get("sex speed") > 0.061:
            $ M_consuela.set("sex speed", M_consuela.get("sex speed") - 0.03)
        anon "You're so tight!{p=1}{nw}"
    return


label scene_consuela_sex_stairs.inside:
    hide consuela_stairs
    show consuela b_stairs_cum
    anon "HNNGGG!!!" with flash
    show xray_consuela stairs with fastdissolve:
        align (0,0)
    consuela "NGGHHH!!!"
    hide xray_consuela
    show consuela b_stairs
    show consuela_mc_body_stairs insert_pullout
    show consuela_overlay_o_mc_stairs_pullout
    with dissolve
    pause
    anon "Haah... Haah..."
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


label scene_consuela_sex_stairs.outside:
    hide consuela_stairs
    show consuela b_stairs
    show consuela_mc_body_stairs cumshot
    show consuela_mc_dick_stairs cumshot
    anon "HNNGGG!!!" with flash
    consuela "NGGHHH!!!"
    show consuela_overlay_o_stairs_cumshot_dick_after
    show consuela_mc_body_stairs base
    show consuela_mc_dick_stairs pre
    with dissolve
    pause
    anon "Haah... Haah..."
    anon "That was awesome!"
    consuela "My god!" (show_native="¡Santo cielo!")
    consuela "I'm a mess..." (show_native="Soy un desastre...")
    consuela "Hehe!"
    return


label scene_consuela_sex_stairs.repeat:
    scene location_beach_house_entrance_stairs
    call scene_consuela_sex_stairs.ready
    with fade
    anon "Here it comes."
    call scene_consuela_sex_stairs.pre
    with dissolve
    consuela "Yes, give it to me!" (show_native="¡Sí, dámelo!")
    call scene_consuela_sex_stairs.insert
    with fastdissolve
    consuela "!!!" with hpunch
    consuela "So deep!" (show_native="¡Tan profunda!")
    call scene_consuela_sex_stairs.animate
    with dissolve
    consuela "Haah!"
    call scene_consuela_sex_stairs.loop
    consuela "Spank me daddy!" (show_native="¡Azotadme papi!")
    anon "I'm going to cum!"
    consuela "Si, cum!"
    pause
    anon "Ahh!!"
    consuela "Cum for me, papi!"
    pause
    if _return == 'inside':
        call scene_consuela_sex_stairs.inside
    else:
        call scene_consuela_sex_stairs.outside
    return


label scene_consuela_sex_stairs.replay:
    jump scene_consuela_sex_stairs.repeat


screen scene_consuela_sex_stairs_controls():
    tag quick_menu

    vbox:
        xalign .5
        ypos 700

        hbox:
            xalign .5

            imagebutton:
                idle 'sexb_keepgoing_n'
                hover 'sexb_keepgoing_h'
                action Return(False)

            imagebutton:
                idle 'sexb_cuminside_n'
                hover 'sexb_cuminside_h'
                action Return('inside')

            imagebutton:
                idle 'sexb_cumoutside_n'
                hover 'sexb_cumoutside_h'
                action Return('outside')

        hbox:
            xalign .5

            if M_consuela.get('sex speed') < .12:
                imagebutton:
                    idle 'sexb_slower_n'
                    hover 'sexb_slower_h'
                    action (Function(M_consuela.set,
                                     'sex speed',
                                     M_consuela.get('sex speed') + 0.03),
                            Return(False))

            if M_consuela.get('sex speed') > .061:
                imagebutton:
                    idle 'sexb_faster_n'
                    hover 'sexb_faster_h'
                    action (Function(M_consuela.set,
                                     'sex speed',
                                     M_consuela.get('sex speed') - 0.03),
                            Return(False))

screen scene_consuela_sex_stairs_controls():
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

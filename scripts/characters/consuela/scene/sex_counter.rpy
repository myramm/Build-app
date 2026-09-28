label scene_consuela_sex_counter:
    scene location_beach_house_kitchen_counter
    call scene_consuela_sex_counter.ready
    with fade
    anon "Are you sure about this?"
    consuela "Si, I want!"
    consuela "Give it to me, papi!"
    call scene_consuela_sex_counter.pre
    with dissolve
    anon "Alright."
    call scene_consuela_sex_counter.insert
    with fastdissolve
    consuela "{i}*Gasp*{/i}"
    consuela "So big!" (show_native="¡Está enorme!")
    anon "You alright?"
    consuela "S-si."
    consuela "Umm, slowly... Okay?"
    anon "Okay."
    call scene_consuela_sex_counter.animate
    with dissolve
    consuela "Oh my god!" (show_native="¡Ay dios mío!")
    consuela "Hah!"
    pause
    anon "Wow, you're so tight, {b}Consuela{/b}..."
    anon "Guess it's been a while for you, huh?"
    consuela "Yes!" (show_native="¡Si!")
    consuela "Oh yes, daddy!" (show_native="¡Ay si, papi!")
    call scene_consuela_sex_counter.loop
    consuela "Oh, daddy!" (show_native="¡Ay, papi!")
    consuela "Fuck my pussy!" (show_native="¡Cógeme!")
    consuela "Harder!" (show_native="¡Más duro!")
    pause
    anon "I'm gonna cum!"
    consuela "Si!"
    consuela "Give it to me!" (show_native="¡Dámelo!")
    pause
    anon "I'm gonna-"
    if _return == 'inside':
        call scene_consuela_sex_counter.inside
    else:
        call scene_consuela_sex_counter.outside
    return


label scene_consuela_sex_counter.ready:
    show consuela b_counter
    show consuela_mc_body_kitchen base
    show consuela_mc_dick_kitchen pre
    return


label scene_consuela_sex_counter.pre:
    show consuela o_kitchen_after
    show consuela_mc_body_kitchen insert_pullout
    hide consuela_mc_dick_kitchen
    return


label scene_consuela_sex_counter.insert:
    if M_consuela.outfit.get == "naked":
        show consuela_kitchen_naked 1 as consuela_kitchen
    else:
        show consuela_kitchen 1
    hide consuela_mc_body_kitchen
    hide consuela o_kitchen_after
    return


label scene_consuela_sex_counter.animate:
    python:
        anim_toggle = True
        animated = True
        M_consuela.set('sex speed', .12)
    if M_consuela.outfit.get == "naked":
        show expression AnimatedImage("consuela_kitchen_naked", [1,2,3,4,5,6,7], M_consuela) as consuela_kitchen at Position(xalign=0., yoffset=0)
    else:
        show expression AnimatedImage("consuela_kitchen", [1,2,3,4,5,6,7], M_consuela) as consuela_kitchen at Position(xalign=0., yoffset=0)
    return


label scene_consuela_sex_counter.loop:
    $ M_consuela.set('sex_location', 'counter')
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_consuela.outfit.get == "naked":
                    show expression AnimatedImage("consuela_kitchen_naked", [1,2,3,4,5,6,7], M_consuela) as consuela_kitchen at Position(xalign=0., yoffset=0)
                else:
                    show expression AnimatedImage("consuela_kitchen", [1,2,3,4,5,6,7], M_consuela) as consuela_kitchen at Position(xalign=0., yoffset=0)
                $ animated = True
            pause 5
            call scene_consuela_sex_counter.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7]
            $ poses_done = []
            while poses_done != pose_list:
                if M_consuela.outfit.get == "naked":
                    show expression "consuela_kitchen_naked {}".format(pose_list[pose_counter]) as consuela_kitchen at Position(xalign=0., yoffset=0)
                else:
                    show expression "consuela_kitchen {}".format(pose_list[pose_counter]) as consuela_kitchen at Position(xalign=0., yoffset=0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_consuela_sex_counter.dialogue
        $ animcounter += 1
    call screen scene_consuela_sex_counter_controls
    if not _return:
        jump scene_consuela_sex_counter.loop
    return _return


label scene_consuela_sex_counter.dialogue:
    if animcounter == 0 and randomizer() < 50:
        consuela "Ahh!!{p=1}{nw}"
    if animcounter == 1 and randomizer() > 50:
        consuela "This is amazing!{p=2}{nw}" (show_native="¡Esto es increíble!")
        consuela "Don't stop!{p=1}{nw}" (show_native="No pares!")
    if animcounter == 2 and randomizer() < 50:
        consuela "Oh, fuck me!{p=1}{nw}"
        consuela "Fuck me, papi!{p=1}{nw}"
        anon "This is so hot!{p=2}{nw}"
    if animcounter == 3 and randomizer() > 50:
        consuela "More.{p=1}{nw}"
        anon "More?{p=1}{nw}"
        consuela "Si, more!{p=1}{nw}"
        if M_consuela.get("sex speed") > 0.061:
            $ M_consuela.set("sex speed",
                             M_consuela.get("sex speed") - 0.03)
    return


label scene_consuela_sex_counter.inside:
    hide consuela_kitchen
    show consuela b_counter_cum
    anon "HNNGGG!!!" with flash
    show xray_consuela counter with fastdissolve:
        align (0,0)
    consuela "NGGHHH!!!"
    hide xray_consuela
    show consuela b_counter o_kitchen_after
    show consuela_mc_body_kitchen insert_pullout
    show consuela_overlay_o_mc_kitchen_pullout
    show consuela_overlay_o_kitchen_after_cum
    with dissolve
    pause
    anon "Haah... Haah..."
    call scene_consuela_sex_counter.ready
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


label scene_consuela_sex_counter.outside:
    hide consuela_kitchen
    show consuela b_counter o_kitchen_after
    show consuela_mc_body_kitchen cumshot
    show consuela_mc_dick_kitchen cumshot
    anon "HNNGGG!!!" with flash
    consuela "NGGHHH!!!"
    pause
    anon "Haah... Haah..."
    anon "That was awesome!"
    consuela "My god!" (show_native="¡Santo cielo!")
    consuela "I'm a mess..." (show_native="Soy un desastre...")
    consuela "Hehe!"
    return


label scene_consuela_sex_counter.repeat:
    scene location_beach_house_kitchen_counter
    call scene_consuela_sex_counter.ready
    with fade
    consuela "Mmm, this is the best part of my day." (show_native="Mmm, esta es la mejor parte de mi día.")
    call scene_consuela_sex_counter.pre
    with dissolve
    anon "You ready?"
    consuela "Si."
    call scene_consuela_sex_counter.insert
    with fastdissolve
    consuela "!!!"
    consuela "Oh, papi!"
    call scene_consuela_sex_counter.animate
    with dissolve
    consuela "Your cock is so big!" (show_native="¡Tu verga está muy grande!")
    pause
    consuela "This makes me very envious of my daughter..." (show_native="Esto me da mucha envidia de mi hija...")
    consuela "I hope you'll still fuck me after marrying her?" (show_native="¿Espero que todavía me cojas después de casarte con ella?")
    anon "Hmm?"
    consuela "I say, harder papi!"
    anon "O-okay."
    pause
    consuela "Ahh!"
    call scene_consuela_sex_counter.loop
    anon "I'm getting close!"
    consuela "Don't stop!" (show_native="¡No pares!")
    consuela "Faster!" (show_native="¡Más rápido!")
    pause
    anon "Here it comes!"
    if _return == 'inside':
        call scene_consuela_sex_counter.inside
    else:
        call scene_consuela_sex_counter.outside
    return


label scene_consuela_sex_counter.replay:
    jump scene_consuela_sex_counter.repeat


screen scene_consuela_sex_counter_controls():
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

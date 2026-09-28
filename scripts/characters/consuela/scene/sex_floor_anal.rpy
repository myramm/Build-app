label scene_consuela_sex_floor_anal:
    return


label scene_consuela_sex_floor_anal.ready:
    show consuela b_floor f_normal_down
    show consuela_mc_body_floor base
    show consuela_mc_dick_floor pre
    return

label scene_consuela_sex_floor_anal.pre:
    show consuela b_floor_base o_empty
    show consuela_mc_body_floor insert_pullout_anal
    hide consuela_mc_dick_floor
    return

label scene_consuela_sex_floor_anal.insert:
    hide consuela_mc_body_floor
    hide consuela
    if M_consuela.outfit.get == "naked":
        show consuela_floor_anal_naked 4 as consuela_floor
    else:
        show consuela_floor_anal 4 as consuela_floor
    return

label scene_consuela_sex_floor_anal.animate:
    python:
        anim_toggle = True
        animated = True
        M_consuela.set('sex speed', .12)
    if M_consuela.outfit.get == "naked":
        show expression AnimatedImage("consuela_floor_anal_naked", [4,5,6,7,1,2,3], M_consuela) as consuela_floor at Position(xalign=0., yoffset=0)
    else:
        show expression AnimatedImage("consuela_floor_anal", [4,5,6,7,1,2,3], M_consuela) as consuela_floor at Position(xalign=0., yoffset=0)
    return


label scene_consuela_sex_floor_anal.loop:
    $ M_consuela.set('sex_location', 'floor_anal')
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                if M_consuela.outfit.get == "naked":
                    show expression AnimatedImage("consuela_floor_anal_naked", [1,2,3,4,5,6,7], M_consuela) as consuela_floor at Position(xalign=0., yoffset=0)
                else:
                    show expression AnimatedImage("consuela_floor_anal", [1,2,3,4,5,6,7], M_consuela) as consuela_floor at Position(xalign=0., yoffset=0)
                $ animated = True
            pause 5
            call scene_consuela_sex_floor_anal.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7]
            $ poses_done = []
            while poses_done != pose_list:
                if M_consuela.outfit.get == "naked":
                    show expression "consuela_floor_anal_naked {}".format(pose_list[pose_counter]) as consuela_floor at Position(xalign=0., yoffset=0)
                else:
                    show expression "consuela_floor_anal {}".format(pose_list[pose_counter]) as consuela_floor at Position(xalign=0., yoffset=0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_consuela_sex_floor_anal.dialogue
        $ animcounter += 1
    call screen scene_consuela_sex_floor_controls
    if not _return:
        jump scene_consuela_sex_floor_anal.loop
    return _return


label scene_consuela_sex_floor_anal.dialogue:
    jump scene_consuela_sex_floor.dialogue


label scene_consuela_sex_floor_anal.inside:
    hide consuela_floor
    show consuela b_floor_cum o_floor_cum_anal
    anon "HNNGGG!!!" with flash
    consuela "NGGHHH!!!"
    show consuela b_floor_base o_empty
    show consuela_mc_body_floor insert_pullout_anal
    with dissolve
    pause
    anon "Haah... Haah..."
    return


label scene_consuela_sex_floor_anal.outside:
    jump scene_consuela_sex_floor.outside


label scene_consuela_sex_floor_anal.resume:
    call scene_consuela_sex_floor_anal.loop
    if _return == 'switch':
        jump scene_consuela_sex_floor.switch
    anon "I'm going to cum."
    consuela "Si, cum!"
    consuela "I cum!"
    pause
    consuela "Papi!!!"
    if _return == 'inside':
        call scene_consuela_sex_floor_anal.inside
    else:
        call scene_consuela_sex_floor_anal.outside
    return


label scene_consuela_sex_floor_anal.switch:
    if not M_consuela.get('done_anal'):
        jump scene_consuela_sex_floor_anal.first
    else:
        if not M_consuela.once('doing_anal'):
            jump scene_consuela_sex_floor_anal.initial
        jump scene_consuela_sex_floor_anal.repeat


label scene_consuela_sex_floor_anal.first:
    hide consuela_floor
    call scene_consuela_sex_floor_anal.ready
    with dissolve
    consuela @ -m_talk "Hmm?"
    consuela "What's the matter, {b}Mister [firstname]{/b}?" (show_native="¿Qué pasa, {b}Mister [firstname]{/b}?")
    consuela "Why you stop?"
    anon "{b}Consuela{/b}, have you ever tried anal?"
    consuela "A-anal?"
    pause
    consuela "You want?"
    anon "I mean, yeah... If you don't mind?"
    consuela "Si, I do."
    anon "... So we can try it?"
    consuela "I just said I would try it, didn't I?" (show_native="Solo dije que lo intentaría, ¿no?")
    anon "..."
    consuela "Si, anal."
    anon "Awesome."
    consuela "Just go slowly, okay?" (show_native="Solo ve despacio, ¿de acuerdo?")
    call scene_consuela_sex_floor_anal.pre
    with dissolve
    consuela "I've never had anything up there bef-" (show_native="Nunca he tenido nada allí ant-")
    call scene_consuela_sex_floor_anal.insert
    with fastdissolve
    consuela "AY!!!"
    consuela "I said go slowly!" (show_native="¡Dije que fuera despacio!")
    anon "Are you alright?"
    pause
    consuela "S-slowly..."
    anon "Oh, alright."
    anon "My bad."
    call scene_consuela_sex_floor_anal.animate
    with dissolve
    consuela "{i}*iiitthhh*{/i} Ahh!"
    anon "Does it hurt?"
    consuela "Of course it hurts, I have a giant cock in my ass!" (show_native="Por supuesto que duele, ¡tengo una polla gigante en mi culo!")
    anon "..."
    pause
    anon "Should I stop?"
    consuela "No, es okay."
    consuela "I do for you."
    pause
    consuela "Ngghhh!"
    consuela "It's so deep!" (show_native="¡Es tan profundo!")
    pause
    consuela "It doesn't hurt so much anymore." (show_native="Ya no duele tanto.")
    anon "Hmm?"
    consuela "Faster, papi!"
    anon "Oh, it's feeling good now?"
    $ M_consuela.set('sex speed', .09)
    consuela "Si, good!"
    pause
    consuela "Ay, papi!"
    consuela "It feels REALLY good!" (show_native="¡Se siente REALMENTE bien!")
    anon "I don't know what that-"
    consuela "DON'T STOP!"
    pause
    call scene_consuela_sex_floor_anal.loop
    anon "{b}Consuela{/b}, I can't-"
    consuela "Faster, papi!"
    consuela "I'm so close!" (show_native="¡Estoy tan cerca!")
    pause
    anon "Here it comes!"
    consuela "Si, cum!"
    call scene_consuela_sex_floor_anal.inside
    show consuela b_floor f_normal_down
    show consuela_mc_body_floor base
    show consuela_mc_dick_floor after
    with dissolve
    consuela "That was..." (show_native="Eso fue...")
    return


label scene_consuela_sex_floor_anal.initial:
    hide consuela_floor
    call scene_consuela_sex_floor_anal.pre
    with dissolve
    consuela "Ay!!!"
    call scene_consuela_sex_floor_anal.insert
    with fastdissolve
    consuela "!!!"
    call scene_consuela_sex_floor_anal.animate
    with dissolve
    anon "You like that?"
    consuela "Si, {b}Mister [firstname]{/b}!"
    pause
    consuela "Fuck me, daddy!" (show_native="¡Follame, papi!")
    anon "Mmm!"
    consuela "Fuck my ass!" (show_native="¡A la mierda mi culo!")
    pause
    consuela "Oh, that's good!" (show_native="¡Ay, qué bueno!")
    consuela "It's so deep!" (show_native="¡Es tan profundo!")
    pause
    consuela "Thank you, daddy!" (show_native="¡Gracias, papi!")
    consuela "GRACIAS!!!"
    jump scene_consuela_sex_floor_anal.resume


label scene_consuela_sex_floor_anal.repeat:
    hide consuela_floor
    call scene_consuela_sex_floor_anal.pre
    with dissolve
    consuela "Ay!!!"
    call scene_consuela_sex_floor_anal.insert
    with fastdissolve
    consuela "!!!"
    call scene_consuela_sex_floor_anal.animate
    with dissolve
    consuela "My poor asshole!" (show_native="¡Mi pobre gilipollas!")
    pause
    consuela "You're going to break me!" (show_native="¡Me vas a romper!")
    consuela "AHHH!!!"
    pause
    consuela "I can't take it, daddy!" (show_native="¡No puedo soportarlo, papi!")
    anon "Hmm?"
    consuela "Cum for me!"
    consuela "Please!" (show_native="¡Por favor!")
    jump scene_consuela_sex_floor_anal.resume
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

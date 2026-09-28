label eve_sex_front_intro:
    if player.location == L_tattooparlor_tent:
        scene expression "backgrounds/location_tattoo_tent_sex_front.jpg"
    else:
        scene expression "backgrounds/location_tattoo_bedroom_sex_front.jpg"
    if _in_replay:
        $ player.go_to(L_tattooparlor_bedroom)
        if persistent.eve_bulge_unlocked:
            show screen popup_trap with dissolve
            call screen empty()
            if _return:
                $ M_eve.set('biggus_dickus', '_alt')
            else:
                $ M_eve.set('biggus_dickus', '')
            hide screen popup_trap with dissolve
        else:
            $ M_eve.set('biggus_dickus', '')
    show eve b_front_pre
    show eve_sex_front_face_mc normal_talk
    anon "Come here!"
    show eve_sex_front_face_mc normal_down
    eve "!!!"
    if (not M_eve.get("sex_front_1st_time") or _in_replay) and not M_eve.get("biggus_dickus"):
        menu:
            "Vaginal!":
                label eve_girl_vag_front:
                $ M_eve.set("sex_front_anal", False)
                show eve b_front_insert
                show eve_sex_front_face_mc normal_down
                with dissolve
                eve "!!!"
                pause
                eve "Fuuuuck!"
                pause
                $ anim_toggle = True
                $ animated = True
                $ M_eve.set('sex speed', .12)
                hide eve
                hide eve_sex_front_face_mc
                show expression AnimatedImage("eve_sex_front", [1,2,3,4,5,6], M_eve) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
                with dissolve
                pause
                eve "Oh my god!"
                eve "You're so deep inside me!"
                pause
                eve "Harder {b}[firstname]{/b}!"
                anon "Hmm?"
                eve "Fuck me harder!"
                jump eve_sex_front_loop
            "Anal!":

                pass

    $ M_eve.set("sex_front_anal", not M_eve.get("biggus_dickus"))
    jump eve_anal_front

label eve_sex_back_intro:
    eve "Hehe, okay."
    label eve_sex_back_intro_replay:
    if player.location == L_tattooparlor_tent:
        scene expression "backgrounds/location_tattoo_tent_sex_back.jpg" with None
    else:
        scene expression "backgrounds/location_tattoo_bedroom_sex_back.jpg" with None
    if _in_replay:
        $ player.go_to(L_tattooparlor_bedroom)
        if persistent.eve_bulge_unlocked:
            show screen popup_trap with dissolve
            call screen empty()
            if _return:
                $ M_eve.set('biggus_dickus', '_alt')
            else:
                $ M_eve.set('biggus_dickus', '')
            hide screen popup_trap with dissolve
        else:
            $ M_eve.set('biggus_dickus', '')
    show eve b_back_pre
    if M_eve.get("biggus_dickus"):
        show eve_overlay_sex_back o_pre_alt
    with dissolve
    pause
    anon "You ready?"
    eve "Y-yeah, I think so."
    show eve b_back_insert
    hide eve_overlay_sex_back
    with dissolve
    eve "!!!"
    pause
    eve "Fuuuuck!"
    pause
    hide eve
    hide eve_overlay_sex_back
    $ M_eve.set('sex speed', .08)
    if M_eve.get("biggus_dickus"):
        show expression AnimatedImage("eve_sex_back_alt", [1,2,3,4,5,6,7,8,9], M_eve) as eve_sex_back at Position(xalign = 0.0, yoffset = 0)
    else:
        show expression AnimatedImage("eve_sex_back", [1,2,3,4,5,6,7,8,9], M_eve) as eve_sex_back at Position(xalign = 0.0, yoffset = 0)
    pause
    anon "Mmm, you are so tight..."
    eve "{i}*Whimper*{/i}"
    pause
    eve "Harder, {b}[firstname]{/b}..."
    anon "Hmm?"
    if M_eve.get("biggus_dickus"):
        eve "Fuck my ass harder!"
    else:
        eve "Fuck me harder!"
    $ anim_toggle = True
    $ animated = True
    jump eve_sex_back_loop

label eve_anal_front:
    eve "Hehe!"
    pause
    if M_eve.get("sex_front_1st_time"):
        if M_eve.get("biggus_dickus"):
            eve "Mmm, give it to me {b}[firstname]{/b}..."
            show eve b_front_insert
            show eve_sex_front_face_mc normal_down
            eve "{i}*Gasp*{/i}" with hpunch
            eve "Fuuuuck!"
            $ anim_toggle = True
            $ animated = True
            $ M_eve.set('sex speed', .12)
            hide eve
            hide eve_sex_front_face_mc
            show expression AnimatedImage("eve_sex_front_alt", [1,2,3,4,5,6], M_eve) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
            with dissolve
            pause
            eve "Holy shi-"
            pause
            eve "Haah, fuck me!"
            eve "Fuck my ass, {b}[firstname]{/b}!"
            pause
            eve "Ahhhh!"
            anon "You're so tight!"
        else:
            eve "Mmm, fuck me, {b}[firstname]{/b}!"
            show eve b_front_insert_anal
            show eve_sex_front_face_mc normal_down
            with dissolve
            eve "W-wait, that's not-"
            hide eve
            hide eve_sex_front_face_mc
            show eve_sex_front_anal 1
            eve "{i}*Gasp*{/i}" with hpunch
            pause
            anon "{b}Eve{/b}?"
            anon "What's wrong?"
            eve "Y-you're in my ass right now..."
            anon "Oh, crap... I'm sorry!"
            anon "I didn't-"
            eve "It's okay."
            eve "Keep going."
            anon "You're sure?"
            eve "Y-yeah, I wanna try it."
            anon "Alright."
            pause
            $ anim_toggle = True
            $ animated = True
            $ M_eve.set('sex speed', .12)
            hide eve_sex_front_anal
            show expression AnimatedImage("eve_sex_front_anal", [1,2,3,4,5,6], M_eve) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
            with dissolve
            eve "!!!"
            eve "Ow, ow, ow!"
            anon "Should I stop?"
            eve "No, don't stop!"
            pause
            eve "It's so deep, {b}[firstname]{/b}!"
            pause
            anon "Is it starting to feel good?"
            eve "Y-yes, I think so."
            pause
            eve "Try going faster."
            anon "Okay."
            $ M_eve.set('sex speed', .09)
            eve "Holy shi-"
    else:
        label eve_girl_anal_front:
        if M_eve.get("biggus_dickus"):
            show eve b_front_insert
        else:
            show eve b_front_insert_anal
        show eve_sex_front_face_mc normal_down
        with dissolve
        eve "!!!"
        pause
        eve "{i}*Whimper*{/i}"
        pause
        $ anim_toggle = True
        $ animated = True
        $ M_eve.set('sex speed', .12)
        hide eve
        hide eve_sex_front_face_mc
        if M_eve.get("biggus_dickus"):
            show expression AnimatedImage("eve_sex_front_alt", [1,2,3,4,5,6], M_eve) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
        else:
            show expression AnimatedImage("eve_sex_front_anal", [1,2,3,4,5,6], M_eve) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
        with dissolve
        pause
        eve "Fuuuuck!"
        eve "You're so deep inside my ass!"
        pause
        eve "Harder {b}[firstname]{/b}!"
        anon "Hmm?"
        eve "Fuck me harder!"
    jump eve_sex_front_loop

label eve_sex_back_first_intro:
    scene expression "backgrounds/location_tattoo_bedroom_sex_back.jpg" with None
    show eve b_back_pre
    if M_eve.get("biggus_dickus"):
        show eve_overlay_sex_back o_pre_alt
    with dissolve
    eve "Just go slow, okay?"
    anon "Y-yeah, okay."
    show eve b_back_insert
    hide eve_overlay_sex_back
    with dissolve
    eve "!!!"
    eve "Holy sh-"
    anon "Are you alright?"
    eve "Yeah, it's just-"
    eve "You're so big!"
    anon "Sorry."
    anon "I can stop if you-"
    eve "NO!"
    eve "... Just give me a second."
    pause
    eve "Phew."
    pause
    eve "Okay, you can start moving... Slowly."
    anon "Alright."
    hide eve
    hide eve_overlay_sex_back
    $ M_eve.set('sex speed', .08)
    if M_eve.get("biggus_dickus"):
        show expression AnimatedImage("eve_sex_back_alt", [1,2,3,4,5,6,7,8,9], M_eve) as eve_sex_back at Position(xalign = 0.0, yoffset = 0)
    else:
        show expression AnimatedImage("eve_sex_back", [1,2,3,4,5,6,7,8,9], M_eve) as eve_sex_back at Position(xalign = 0.0, yoffset = 0)
    with dissolve
    pause
    eve "{i}*Whimper*{/i}"
    pause
    anon "{b}Eve{/b}?"
    eve "I'm okay."
    if M_eve.get("biggus_dickus"):
        eve "Fuck this hurts!"
        eve "Oooowww!"
    else:
        eve "You're stretching me so much!"
        eve "Ngghhh!"
    eve "Try going faster."
    $ M_eve.set('sex speed', .06)
    pause
    eve "{i}*Whimper*{/i}"
    pause
    anon "Is it feeling any better?"
    eve "Y-yeah, I think so."
    if M_eve.get("biggus_dickus"):
        eve "My ass is on fire!"
    else:
        eve "It's so deep!"
    $ M_eve.set('sex speed', .04)
    eve "!!!"
    anon "You're so tight!"
    pause
    $ anim_toggle = True
    $ animated = True
    jump eve_sex_back_loop

label eve_sex_front_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_eve.get("biggus_dickus"):
                    show expression AnimatedImage("eve_sex_front_alt", [1,2,3,4,5,6], M_eve) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
                elif M_eve.get("sex_front_anal"):
                    show expression AnimatedImage("eve_sex_front_anal", [1,2,3,4,5,6], M_eve) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression AnimatedImage("eve_sex_front", [1,2,3,4,5,6], M_eve) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("eve_sex_front_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6]
            $ poses_done = []
            while poses_done != pose_list:
                if M_eve.get("biggus_dickus"):
                    show expression "eve_sex_front_alt {}".format(pose_list[pose_counter]) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
                elif M_eve.get("sex_front_anal"):
                    show expression "eve_sex_front_anal {}".format(pose_list[pose_counter]) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression "eve_sex_front {}".format(pose_list[pose_counter]) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("eve_sex_front_hscene_dialog")
        $ animcounter += 1
    call screen eve_sex_front_options

label eve_sex_front_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        eve "Haah, fuck me!{p=1}{nw}"
    if animcounter == 1 and randomizer() > 50 and (M_eve.get("sex_front_anal") or M_eve.get("biggus_dickus")):
        eve "Fuck my ass, {b}[firstname]{/b}!{p=2}{nw}"
    if animcounter == 2 and randomizer() < 50:
        eve "Ahhhh!{p=1}{nw}"
    if animcounter == 3 and randomizer() > 50:
        eve "I'm getting close...{p=2}{nw}"
    return

label eve_sex_front_cum_inside:
    eve "Don't stop!"
    anon "I can't-"
    pause
    eve "I'm going to cum!"
    anon "Me too!"
    pause
    eve "{b}[firstname]{/b}!"
    eve "Don't-"
    hide eve_sex_front
    show eve b_front_cum
    if M_eve.get("biggus_dickus"):
        show eve_overlay_sex_front o_cumshot_alt
    elif M_eve.get("sex_front_anal"):
        show eve_overlay_sex_front o_cum_anal
    '{color=ff69b4}[character.eve] & [character.anon]{/color}' "NGGHHH!!!" with flash
    if not M_eve.get("biggus_dickus") and not M_eve.get("sex_front_anal"):
        show xray_eve_front:
            align (0,0)
    pause
    hide xray_eve_front
    if M_eve.get("sex_front_anal"):
        show eve b_front_after_anal
        show eve_overlay_sex_front o_pullout_anal
    else:
        show eve b_front_after
        show eve_overlay_sex_front o_pullout
    show eve_sex_front_face_mc normal
    with dissolve
    pause
    if not M_eve.get("sex_front_anal"):
        show eve_overlay_sex_front o_creampie with dissolve
    pause
    if not M_eve.get("biggus_dickus") and not M_eve.get("sex_front_anal"):
        call call_pregnancy_minigame ("eve_sex_front_cum_end", M_eve)
    jump eve_sex_front_cum_end

label eve_sex_front_cum_outside:
    eve "Don't stop!"
    anon "I can't-"
    pause
    eve "I'm going to cum!"
    anon "Me too!"
    eve "{b}[firstname]{/b}!"
    eve "Don't-"
    hide eve_sex_front
    if M_eve.get("sex_front_anal"):
        show eve b_front_after_anal
    else:
        show eve b_front_after
    show eve_sex_front_face_mc cum
    show eve_overlay_sex_front o_cumshot
    show eve_sex_front_face_mc normal_down
    anon "HNNGGG!!!" with flash
    show eve_overlay_sex_front o_cumshot3
    eve "NGGHHH!!!"
    pause
    jump eve_sex_front_cum_end

label eve_sex_front_cum_end:
    show eve_sex_front_face_mc normal_talk
    anon "Haah... Haah..."
    pause
    anon "You alright?"
    show eve_sex_front_face_mc normal
    eve "Hehehe!"
    if M_eve.get("biggus_dickus"):
        eve "I'm a mess!"
        show eve_sex_front_face_mc normal_talk
        anon "Hehe!"
        show eve_sex_front_face_mc normal
    else:
        eve "That was incredible!"
        show eve_sex_front_face_mc normal_talk
        anon "Y-yeah, it was."
        show eve_sex_front_face_mc normal
        if M_eve.get("sex_front_1st_time"):
            eve "We'll have to do that again, for sure!"
    scene expression player.location.background_closeup
    show eve b_onbed_cuddle_naked f_happy_closed o_dick
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with fade
    pause
    if M_eve.get("sex_front_1st_time"):
        eve "I can't believe how good it feels when you fuck my ass like that..."
        anon "I'm glad you like it."
        eve "Hehe, I bet you are!"
        $ M_eve.set("sex_front_1st_time", False)
    else:
        eve "Mmm, we are getting pretty good at that."
        anon "Yeah, I'd say so."
        eve "Hehe!"
    pause
    if randomizer() > 50:
        eve "Mmm, I don't wanna move."
        anon "..."
    else:
        eve "Mmm, this feels wonderful."
        anon "It does."
    pause
    $ renpy.end_replay()
    $ persistent.cookie_jar["Eve"]["unlocked"] = True
    $ persistent.cookie_jar["Eve"]["gallery"]["05_unlocked"] = True
    jump eve_sex_true_end

label eve_sex_front_switcheroo:
    if M_eve.get("sex_front_anal"):
        hide eve_sex_front
        jump eve_girl_anal_front
    else:
        hide eve_sex_front
        jump eve_girl_vag_front

label eve_sex_back_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_eve.get("biggus_dickus"):
                    show expression AnimatedImage("eve_sex_back_alt", [1,2,3,4,5,6,7,8,9], M_eve) as eve_sex_back at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression AnimatedImage("eve_sex_back", [1,2,3,4,5,6,7,8,9], M_eve) as eve_sex_back at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("eve_sex_back_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                if M_eve.get("biggus_dickus"):
                    show expression "eve_sex_back_alt {}".format(pose_list[pose_counter]) as eve_sex_back at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression "eve_sex_back {}".format(pose_list[pose_counter]) as eve_sex_back at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("eve_sex_back_hscene_dialog")
        $ animcounter += 1
    call screen eve_sex_back_options

label eve_sex_back_hscene_dialog:
    if animcounter == 0 and randomizer() > 50:
        eve "Oh my god!{p=1}{nw}"
    if animcounter == 1 and randomizer() > 50:
        eve "{b}[firstname]{/b}, don't stop!{p=2}{nw}"
    if animcounter == 2 and randomizer() > 50:
        eve "Haah, it feels good!{p=1}{nw}"
        eve "Don't stop!{p=1}{nw}"
    if animcounter == 3 and randomizer() > 50:
        eve "Fuck me!{p=1}{nw}"
        eve "Fuck me, {b}[firstname]{/b}!{p=1}{nw}"
    return

label eve_sex_back_cum_inside:
    if randomizer() > 50:
        eve "Don't stop!"
        anon "I can't-"
        pause
    eve "I'm going to cum!"
    anon "Me too!"
    eve "Don't stop!"
    eve "Don't-"
    eve "NGGHHH!!!"
    pause
    hide eve_sex_back
    show eve b_back_cum
    anon "HNNGGG!!!" with flash
    if not M_eve.get("biggus_dickus"):
        show xray_eve_back:
            align (0,0)
    pause
    hide xray_eve_back
    show eve b_back_insert
    show eve_overlay_sex_back o_pullout
    with dissolve
    pause
    show eve b_back_after
    if M_eve.get("biggus_dickus"):
        show eve_overlay_sex_back o_after_alt
    else:
        hide eve_overlay_sex_back
        call call_pregnancy_minigame ("eve_sex_back_end", M_eve)
    jump eve_sex_back_end

label eve_sex_back_cum_outside:
    eve "I'm going to cum!"
    anon "Me too!"
    eve "Don't stop!"
    eve "Don't-"
    eve "NGGHHH!!!"
    pause
    hide eve_sex_back
    show eve b_back_cumshot
    if M_eve.get("biggus_dickus"):
        show expression "characters/eve/eve_overlay_sex_back_pre_o_alt.png"
    show eve_overlay_sex_back o_cumshot
    anon "HNNGGG!!!" with flash
    show eve_overlay_sex_back o_cumshot3
    pause
    jump eve_sex_back_end

label eve_sex_back_end:
    anon "Haah... Haah..."
    pause
    anon "You alright?"
    eve "Hehehe!"
    if M_eve.get("biggus_dickus"):
        eve "My poor little butthole..."
    else:
        eve "That was awesome!"
    anon "Hehe!"
    scene expression player.location.background_closeup
    show eve b_onbed_cuddle_naked f_happy_closed o_dick
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with fade
    if M_eve.get("sex_back_1st_time"):
        eve "Mmm, we are definitely doing that again!"
        anon "Heh, okay."
        pause
        if M_eve.get("biggus_dickus"):
            eve f_happy "I think I'm going to be walking funny tomorrow..."
            anon "Heh, I thought you enjoyed it?"
            eve "Oh, I loved it!"
            eve "... But you did fuck my ass really hard, you big brute!"
            anon "Well, I'll be more careful next time."
            eve "Psh, I hope not!"
            anon "Hmm?"
            eve "It felt wonderful!"
        else:
            anon "I thought there was supposed to be blood your first time?"
            eve "Hmm?"
            anon "You know, down there..."
            eve "Oh, right."
            eve "My hymen broke in my parents car accident."
            anon "I see."
            eve f_happy "Sorry."
            anon "N-no, there's nothing to be sorry about!"
            anon "I was just surprised, that's all..."
    else:
        eve "Mmm, we are getting pretty good at that."
        anon "Yeah, I'd say so."
        eve "Hehe!"
    show eve f_happy_closed
    eve "Mmm, this feels wonderful."
    anon "It does."
    pause
    if M_eve.get("sex_back_1st_time"):
        eve "Thank you, for being my first, {b}[firstname]{/b}."
        anon "Hehe, no problem."
        pause
        $ M_eve.set("sex_back_1st_time", False)
    $ renpy.end_replay()
    $ persistent.cookie_jar["Eve"]["unlocked"] = True
    $ persistent.cookie_jar["Eve"]["gallery"]["06_unlocked"] = True
    jump eve_sex_true_end

label eve_sex_true_end:
    scene expression player.location.background_blur with None
    show eve b_undies f_happy
    show anon
    with dissolve
    eve "I wish you could stay."
    anon "Yeah, me too."
    pause
    anon "I'll see you tomorrow, okay?"
    eve "Y-yeah, okay."
    hide anon
    show eve b_undies_kiss
    with dissolve
    pause
    show anon
    show eve b_undies f_happy
    with dissolve
    eve "Good night, {b}[firstname]{/b}."
    anon @ a_wave "Good night, {b}Eve{/b}."
    hide anon with dissolve
    $ game.timer.tick()
    $ player.go_to(L_map)
    $ game.main()

label eve_69:
    if _in_replay:
        $ player.go_to(L_tattooparlor_bedroom)
        if persistent.eve_bulge_unlocked:
            show screen popup_trap with dissolve
            call screen empty()
            if _return:
                $ M_eve.set('biggus_dickus', '_alt')
            else:
                $ M_eve.set('biggus_dickus', '')
            hide screen popup_trap with dissolve
        else:
            $ M_eve.set('biggus_dickus', '')
    if player.location == L_tattooparlor_tent:
        scene expression "backgrounds/location_tattoo_tent_sex_front.jpg"
    else:
        scene expression "backgrounds/location_tattoo_bedroom_sex_bj.jpg"
    show eve_sex_bj_mc_body
    show eve_sex_bj_mc_face pre
    if M_eve.get("biggus_dickus"):
        show eve b_sex_bj_pre o_pre_alt
    else:
        show eve b_sex_bj_pre
    with fade
    pause
    if randomizer() > 50:
        eve "You sure you're ready for this?"
        anon "As ready as I'll ever be!"
    else:
        eve "Are you ready?"
        anon "Yup!"
    eve "Hehe, okay."
    eve "Here I come."
    show eve b_sex_bj_talking o_empty
    hide eve_sex_bj_mc_body
    hide eve_sex_bj_mc_face
    with dissolve
    pause
    eve "!!!"
    if M_eve.get("biggus_dickus") and M_eve.get("69_1st_time"):
        eve "Wow, you took it all!"
        anon "{b}Glllkkch{/b}!"
    elif M_eve.get("69_1st_time"):
        eve "Oh my god, that feels amazing!"
        anon "Ddddthh iddd?"
    else:
        eve "!!!"
        eve "{i}*Gasp*{/i}"
        pause
        eve "You are so good at this!"
    eve "Ahh!"
    $ anim_toggle = True
    $ animated = True
    $ M_eve.set('sex speed', .12)
    hide eve
    show expression AnimatedImage("eve_sex_bj", [1,2,3,4,5,6,7,8,9,10], M_eve) as eve_sex_bj at Position(xalign = 0.0, yoffset = 0)
    anon "!!!"
    jump eve_sex_bj_loop

label eve_sex_bj_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("eve_sex_bj", [1,2,3,4,5,6,7,8,9,10], M_eve) as eve_sex_bj at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("eve_sex_bj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "eve_sex_bj {}".format(pose_list[pose_counter]) as eve_sex_bj at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("eve_sex_bj_hscene_dialog")
        $ animcounter += 1
    call screen eve_sex_bj_options

label eve_sex_bj_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        eve "Mmm.{p=1}{nw}"
    if animcounter == 1 and randomizer() > 50:
        anon "{i}*Slurp*{/i}{p=1}{nw}"
    if animcounter == 2 and randomizer() < 50:
        eve "{i}*Gluullggh*{/i}{p=1}{nw}"
    if animcounter == 3 and randomizer() > 50:
        eve "{i}*Sluuurrp*{/i}{p=1}{nw}"
    return

label eve_sex_bj_cum:
    if M_eve.get("biggus_dickus"):
        anon "Mmm!"
        eve "Mmm."
        pause
        anon "Mmmm!!"
        eve "Mmhmm."
    else:
        anon "Eervve!"
        anon "Mmy grrn krrrwwws!!"
        pause
        anon "Eervve!!!"
    pause
    anon "MMMMM!!!"
    eve "Mmm?"
    anon "HrrrNNGGG!!!" with flash
    hide eve_sex_bj
    show eve b_sex_bj_cum
    eve "!!!"
    pause
    show eve b_sex_bj_talking o_empty a_after f_after
    hide eve_sex_bj_mc_body
    hide eve_sex_bj_mc_face
    with dissolve
    pause
    eve f_swallow_after @ f_swallow -m_talk "{i}*Gulp*{/i}"
    eve "Fuuuuuck!"
    eve "NGGHHH!!!" with flash
    pause
    show eve f_normal
    eve "Haah... That was-"
    eve "Oh my god..."
    anon "Mmmm!!"
    pause
    eve f_after "Oh, crap!"
    show eve_sex_bj_mc_body
    if M_eve.get("biggus_dickus"):
        show eve_sex_bj_mc_face after_alt
        show eve b_sex_bj_pre o_after_alt zorder 1
        with dissolve
        anon "!!!"
    else:
        show eve_sex_bj_mc_face after
        show eve b_sex_bj_pre zorder 1
        with dissolve
        anon "{i}*GASP*{/i}"
    eve "Oh, I'm sorry!"
    anon "{i}*Gulp*{/i}"
    show eve_sex_bj_mc_face after
    anon "Haaah... Haaah..."
    eve "Are you alright?!"
    anon "I think so."
    if M_eve.get("biggus_dickus"):
        eve "Hehe, you came a lot!"
        anon "Y-yeah, you did too!"
    else:
        eve "Hehe, you're a mess!"
        anon "Y-yeah, you too!"

    if player.location == L_tattooparlor_tent:
        scene expression player.location.background_blur
    else:
        scene expression player.location.background_closeup
    show eve b_onbed_cuddle_naked f_happy_closed o_dick
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with fade
    if M_eve.get("69_1st_time"):
        eve "Mm, I can't believe we just did that..."
    else:
        eve "Mm, that was wonderful!"
    pause
    eve f_happy "Did you like it?"
    if randomizer() > 50:
        anon "Yeah, did you?"
        eve "Oh, I loved it!"
    else:
        anon "Of course!"
        eve f_happy_closed "Hehe!"
    pause
    if M_eve.get("69_1st_time"):
        eve f_happy_closed "We'll have to do it again sometime..."
        $ M_eve.set("69_1st_time", False)
    pause
    anon "It's getting late."
    anon "I'll need to head home soon."
    eve f_happy @ f_thinking_down "Aww, I don't want to get up yet!"
    eve "Can't you stay just a little bit longer?"
    anon "Y-yeah, okay, but just a little bit."
    eve f_happy_closed "Mmm."
    eve "I love it when you hold me like this..."
    pause
    $ renpy.end_replay()
    $ persistent.cookie_jar["Eve"]["unlocked"] = True
    $ persistent.cookie_jar["Eve"]["gallery"]["04_unlocked"] = True
    $ M_eve.trigger(T_eve_had_sixtynine)
    jump eve_HJ_end

label eve_sex_jerk_intro:
    $ player.go_to(L_tattooparlor_tent)
    scene expression player.location.background_blur with None
    if _in_replay:
        if persistent.eve_bulge_unlocked:
            show screen popup_trap with dissolve
            call screen empty()
            if _return:
                $ M_eve.set('biggus_dickus', '_alt')
            else:
                $ M_eve.set('biggus_dickus', '')
            hide screen popup_trap with dissolve
        else:
            $ M_eve.set('biggus_dickus', '')
        $ game.timer.tick(2)
    show anon b_onbed_sit f_laugh
    show eve b_onbed_dressed f_nervous
    with dissolve
    pause
    eve "So..."
    eve f_sexy "Here we are, in {b}Tuuku{/b}'s tent again..."
    anon f_normal @ -m_talk "Mmhmm."
    pause
    eve f_happy @ f_laugh "I really hope {b}Odette{/b} seals the deal this time!"
    anon f_confused "You do?"
    eve "Yeah."
    pause
    eve "Hehe, I suppose that is a weird thing to say, huh?"
    eve @ f_eyeroll "Jeez, I really hope {b}Odette{/b} nails my sister tonight..."
    anon @ f_laugh "Haha!"
    anon "No, it's okay... I get what you mean."
    anon "You just want {b}Grace{/b} to be happy."
    eve "Yeah, that..."
    pause
    eve @ f_laugh "... But also, an end to this whole being exiled to the roof bullshit!"
    anon "Hehe, it's not so bad..."
    eve "Pfft, it would be so much better downstairs, with a TV and a bed..."
    pause
    eve "... And heat."
    anon f_flirt "I can think of a few ways to warm you up..."
    eve f_sexy "Oh, yeah?"
    anon "Yeah."
    eve f_sexy @ f_laugh "Mmm, hehe!"
    pause
    eve a_remove1 "You know, it was really sweet, the way you helped {b}Odette{/b} and my sister today..."
    anon "Y-yeah?"
    show eve f_normal_down b_onbed_topless a_remove2 with dissolve
    eve @ -m_talk "Mmhmm."
    show eve f_sexy b_onbed_topless a_idle with dissolve
    eve "I think..."
    eve "That you, deserve a reward."
    anon "{i}*Gulp*{/i} O-okay."
    show eve f_normal_down b_onbed_tanktop_remove1 with dissolve
    pause
    show eve b_onbed_tanktop_remove2 with dissolve
    show anon f_surprised
    pause
    show eve f_sexy b_onbed_tanktop with dissolve
    eve @ f_laugh "You know, this is A LOT more fun now that I know you're okay with everything."
    anon f_flirt "Uh-huh."
    anon "D-definitely having fun..."
    eve @ f_laugh "Hehehe!"
    eve @ f_sexy "Shall I continue?"
    menu:
        "Yes.":
            anon "Yes, please."
        "HELL YES!":
            anon f_skeptical "Was that a serious question?"
            eve @ f_eyeroll "No."
    show eve b_onbed_top_remove3 with dissolve
    pause
    show eve f_sexy b_onbed_panties with dissolve
    anon "!!!"
    eve "You like?"
    anon "Oh, me like."
    anon "Me like very much!"
    eve @ f_laugh "Hehe!"
    pause
    eve "Hmm, I probably don't need these panties either, huh?"
    anon "Nuh-uh."
    eve "Hehe!"
    show eve b_onbed_top_remove4 with dissolve
    pause
    show eve f_sexy b_onbed_nude with dissolve

    if M_eve.biggus_dickus:
        anon "Mmm, is that for me?"
        eve "Yes."
        eve "It's all for you, {b}[firstname]{/b}!"
    else:
        anon "Mmm, that scar is so sexy!"
        eve "Yeah?"
        eve "Maybe you should come take a closer look?"
    anon "!!!"
    anon "Give me a second!"
    show anon b_onbed_sit_changing3 with fastdissolve
    pause .5
    show eve b_onbed_cuddle_naked f_happy o_dick
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with dissolve
    eve "That was quick!"
    show anon f_laugh
    pause
    hide anon
    show eve b_onbed_cuddle_naked_kiss
    with dissolve
    eve "Mmm."
    show eve b_onbed_cuddle_naked f_happy
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with dissolve
    eve "God I love kissing you!"
    anon "Likewise."
    eve "Hehe!"
    show eve b_onbed_cuddle_naked_kiss
    hide anon
    with dissolve
    pause
    pause
    show eve b_onbed_cuddle_naked
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with dissolve
    eve "You were right."
    eve "I'm feeling much warmer now."
    anon "Hehe."
    eve f_thinking_down "Hmm, I think somebody wants to come out and play..."
    anon @ -m_talk "Mmhmm."
    show eve a_jerk1 o_empty with dissolve
    eve "It's so big, {b}[firstname]{/b}..."
    pause
    anon "You still scared of it?"
    eve "A little."
    pause
    anon "That's okay."
    anon "Why don't you let me take care of you instead?"
    eve f_happy @ -m_talk "Hmm?"
    jump eve_handjob

label eve_handjob:
    anon "Come here."

    if player.location == L_tattooparlor_tent:
        scene location_tattoo_tent_sex_front
    else:
        scene expression player.location.background_closeup
    show eve b_front_pre
    show eve_sex_front_face_mc normal
    with fade
    eve "!!!"
    if M_eve.get("HJ_1st_time"):
        eve "W-what are you-"
        eve "Nobodies ever-"
    else:
        eve "A-are you sure-"
    show eve_sex_front_face_mc normal_talk
    anon "Shh."
    anon "It's alright."
    show eve_sex_front_face_mc normal_down
    eve "{i}*Gulp*{/i}"
    $ anim_toggle = True
    $ animated = True
    if M_eve.biggus_dickus:
        $ M_eve.set('sex speed', .08)
        show eve b_sex_jerk_alt
        show expression AnimatedImage("eve_sex_jerk_alt", [1,2,3,4,5,6,7,8,9,10,11], M_eve) as eve_sex_jerk at Position(xalign = 0.0, yoffset = 0)
    else:
        $ M_eve.set('sex speed', .09)
        show eve b_sex_jerk
        show expression AnimatedImage("eve_sex_jerk", [1,2,3,4,5,6], M_eve) as eve_sex_jerk at Position(xalign = 0.0, yoffset = 0)
    eve "{i}*Gasp*{/i}"
    pause
    show eve_sex_front_face_mc normal_talk
    anon "Does that feel okay?"
    if M_eve.get("HJ_1st_time"):
        anon "Should I keep going?"
        show eve_sex_front_face_mc normal
        eve "Y-yes!"
    else:
        show eve_sex_front_face_mc normal
        eve "S-so good!"
    show eve_sex_front_face_mc normal_down
    jump eve_sex_jerk_loop

label eve_sex_jerk_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_eve.biggus_dickus:
                    show eve b_sex_jerk_alt
                    show expression AnimatedImage("eve_sex_jerk_alt", [1,2,3,4,5,6,7,8,9,10,11], M_eve) as eve_sex_jerk at Position(xalign = 0.0, yoffset = 0)
                else:
                    show eve b_sex_jerk
                    show expression AnimatedImage("eve_sex_jerk", [1,2,3,4,5,6], M_eve) as eve_sex_jerk at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("eve_sex_jerk_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            if M_eve.biggus_dickus:
                $ pose_list = [1,2,3,4,5,6,7,8,9,10,11]
            else:
                $ pose_list = [1,2,3,4,5,6]
            $ poses_done = []
            while poses_done != pose_list:
                if M_eve.biggus_dickus:
                    show eve b_sex_jerk_alt
                    show expression "eve_sex_jerk_alt {}".format(pose_list[pose_counter]) as eve_sex_jerk at Position(xalign = 0.0, yoffset = 0)
                else:
                    show eve b_sex_jerk
                    show expression "eve_sex_jerk {}".format(pose_list[pose_counter]) as eve_sex_jerk at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("eve_sex_jerk_hscene_dialog")
        $ animcounter += 1
    call screen eve_sex_jerk_options

label eve_sex_jerk_hscene_dialog:
    if animcounter == 0 and randomizer() > 75:
        eve "Nnngghh, faster!{p=1}{nw}"
    elif animcounter == 0 and randomizer() > 50:
        eve "Oh god, faster!{p=1}{nw}"
    if animcounter == 1 and randomizer() > 50:
        eve "Oh my god...{p=1}{nw}"
    if animcounter == 2 and randomizer() < 50:
        eve "This feels so good, {b}[firstname]{/b}!{p=2}{nw}"
    if animcounter == 3 and randomizer() < 50:
        eve "Ahh!{p=1}{nw}"
    if animcounter == 4 and randomizer() < 50:
        eve "Nnngghh, don't stop!!"
    return

label eve_sex_jerk_cum:
    eve "Oh, fuck!"
    eve "I'm getting close!"
    show eve_sex_front_face_mc normal
    anon "Cum for me!"
    show eve_sex_front_face_mc normal_down
    pause
    eve "{b}[firstname]{/b}!!!"
    pause
    hide eve_sex_jerk
    if M_eve.biggus_dickus:
        show eve b_sex_jerk_cum_alt
        show eve_sex_jerk_cumshot
    else:
        show eve b_sex_jerk_cum
    eve "NNGGGHHH!!!" with flash
    pause
    eve "Haah... Haah..."
    eve "Holy shit."
    pause
    if player.location == L_tattooparlor_bedroom:
        scene expression player.location.background_closeup
    else:
        scene expression player.location.background_blur
    $ M_eve.set('sex speed', .4)
    if M_eve.biggus_dickus:
        show eve b_onbed_cuddle_naked f_happy o_dick
    else:
        show eve b_onbed_cuddle_naked f_surprised o_dick
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with fade
    if M_eve.biggus_dickus:
        if M_eve.get("HJ_1st_time"):
            eve "I made a mess..."
        else:
            eve "I made another mess..."
        anon "Heh, that's okay."
        eve "Hehe!"
    else:
        if M_eve.get("HJ_1st_time"):
            eve "I've never-"
            pause
            eve "Cum that hard before..."
        else:
            eve "T-that was-"
            pause
            eve "Amazing..."
    show eve f_happy a_jerk1 o_empty with dissolve
    eve "Now it's my turn."

    if M_eve.get("HJ_1st_time") and not _in_replay:
        anon "You don't have to..."
        eve "N-no, I want to!"

        label eve_jerk_me_off_scotty:
        show eve a_jerk
        anon @ -m_talk "Mmm."
        pause
        eve "Does that feel good?"
        anon "It feels really good!"
        eve "Hehe!"
        pause
        if M_eve.get("HJ_1st_time"):
            anon "Your hands are so soft and tiny..."
            eve "No, your dick is just fucking huge!"
            eve "How do you walk around with this thing?"
            pause
        else:
            eve "I love playing with your dick, {b}[firstname]{/b}."
            anon "Y-you do?"
            eve "Yes, very much!"
            pause
            anon "Heh, I think he likes it too."
            eve "Hehe!"
        show anon f_hurt
        eve "Are you getting close?"
        anon @ f_disgusted_wince "Y-yes."
        pause
        eve "Cum for me, {b}[firstname]{/b}!"
        eve "I wanna see it!"
        pause
        jump eve_sex_mc_jerk_loop
    else:

        menu:
            "Yes, please.":
                jump eve_jerk_me_off_scotty
            "No, thanks.":

                anon "You don't have to..."
                eve "No?"
                anon "Let's cuddle for a while."
                eve "Y-you're sure?"
                eve "I like to do it."
                anon "Yeah, it's alright."
                anon "Just laying here with you is fine."
                eve f_happy_closed "Mmm, okay."
                jump eve_HJ_end

label eve_sex_mc_jerk_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show eve a_jerk
                $ animated = True
            pause 5
        else:
            show eve a_jerk1
            pause
            show eve a_jerk2
            pause
        call expression game.dialog_select("eve_sex_mc_jerk_hscene_dialog")
        $ animcounter += 1
    call screen eve_sex_mc_jerk_options

label eve_sex_mc_jerk_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        anon @ f_disgusted_wince "Oh my god, this feels amazing!{p=2}{nw}"
    if animcounter == 1 and randomizer() > 50:
        anon @ f_disgusted_wince "Ahh!!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 50:
        anon @ f_disgusted_wince "I'm getting close...{p=1}{nw}"
    return

label eve_sex_mc_jerk_cum:
    anon @ f_disgusted_wince "I'm gonna-"
    pause
    anon f_cough "Here it comes!"
    pause
    show eve a_jerk1 f_surprised o_cum
    anon f_disgusted_wince "HNNGGG!!!" with flash
    show anon f_flirt_low
    show eve f_happy o_cum3
    pause
    eve "Holy shit..."
    anon "Haah... Haah..."
    eve "That's a lot of cum..."
    anon "S-sorry."
    eve "No, it's fine."
    pause
    show eve a_taste o_dick
    show expression "characters/eve/eve_overlay_onbed_cuddle_naked_o_cum3.png"
    with dissolve
    anon @ f_surprised_low "!!!"
    show eve a_chest with dissolve
    if M_eve.get("HJ_1st_time"):
        anon "D-did you just-"
        eve "Hehe!"
        eve "I was curious."
        anon "And?"
        show eve f_thinking_lip
        pause
        eve f_thinking_down "It's very... Salty."
        anon @ f_laugh "Haha!"
        eve f_happy_closed "Haha!"
        pause
        show eve f_happy
        anon "I'm going to have to get going soon."
        eve "Mmm, I wish you could stay."
        anon "I know, me too."
        anon "It's getting late though."
        pause
        anon "I wonder how {b}Odette{/b} and your sister are getting on?"
        eve "Who cares?"
        anon @ f_laugh "Hehe!"
        anon "Oh, you know you're curious!"
        eve "Maybe a little..."
        pause
        eve "I don't wanna move though!"
        anon @ f_laugh "Hehe!"
        eve @ f_happy_closed "Hehe!"
        pause
        eve f_thinking_down "{i}*Sigh*{/i} I suppose all good things must come to an end."
        anon "There's always next time."
        eve f_happy "I'm holding you to that!"
        anon "No problem."
        eve "Alright, let's get dressed and check on {b}Odette{/b} and {b}Grace{/b}."
        eve "Then I'll walk you out."
        anon "Okay."
        scene black with fade
        pause
        $ M_eve.set("HJ_1st_time",False)
    else:
        anon "!!!"
        eve "Hehe!"
        show eve f_thinking_lip

        label eve_HJ_end:
        pause
        scene black with fade
        pause
        if player.location == L_tattooparlor_tent:
            $ player.go_to(L_tattooparlor_roof)
        scene expression player.location.background_blur with None
        show eve f_happy
        if player.location == L_tattooparlor_bedroom and game.timer.is_dark():
            show eve b_pajamas
        show anon
        with dissolve
        anon "That was nice."
        eve "Really nice!"
        eve "I wish you could stay longer, I sleep like a baby when I'm in your arms."
        anon "Heh, I noticed."
        eve @ f_laugh "Hehe!"
        anon "Anyways, I should probably get going."
        eve "Yeah, okay."
        hide anon
        if player.location == L_tattooparlor_bedroom and game.timer.is_dark():
            show eve b_pajamas_kiss:
                xoffset -400
        else:
            show eve b_dressed_kiss:
                xoffset -400
        with dissolve
        anon "!!!"
        if player.location == L_tattooparlor_bedroom and game.timer.is_dark():
            show eve b_pajamas:
                xoffset -200
        else:
            show eve b_dressed:
                xoffset -200
        show anon
        with dissolve
        eve "Come back and see me soon, okay?"
        anon "I will."
        hide anon with dissolve
        $ renpy.end_replay()
        $ game.timer.tick()
        $ player.go_to(L_map)
        $ game.main()
    $ persistent.cookie_jar["Eve"]["unlocked"] = True
    $ persistent.cookie_jar["Eve"]["gallery"]["03_unlocked"] = True
    $ renpy.end_replay()
    if M_eve.is_state(S_eve_make_up_dress_table):
        jump eve_sex_mc_jerk_cum_continued
    else:
        $ game.main()

label eve_sex_mc_jerk_cum_continued:
    $ player.go_to(L_tattooparlor_fire_escape)
    scene expression player.location.background_blur with None
    show anon
    show eve f_happy
    with dissolve
    eve "I hope they're not fucking in my bed or something..."
    anon @ f_surprised a_salute "!!!"
    anon "N-nope."
    anon "Not in your bed."
    eve @ f_surprised "!!!"

    scene location_tattoo_apartment_cutscene02
    show text _ ("It seemed our plan had worked, {b}Odette{/b} had finally won {b}Grace{/b}'s heart.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... Or at the very least, she'd won her way into {b}Grace{/b}'s bed for the evening.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Either way, I viewed it as a success.") as caption with dissolve
    pause

    scene expression player.location.background_blur
    show anon f_flirt_grin
    show eve f_surprised
    with fade
    anon @ -m_talk "..."
    eve @ -m_talk "..."
    pause
    anon f_flirt "So, uhh..."
    eve f_normal "Y-yeah."
    anon "We probably shouldn't be watching this, huh?"
    eve f_sexy "You really think they'd care?"
    anon @ a_thinking f_thinking "W-well, {b}Odette{/b} probably wouldn't..."
    eve @ f_eyeroll "Yeah, my sister wouldn't either, trust me."
    anon "Does this mean you're sleeping in the tent tonight?"
    eve f_angry a_hip "Fuck that!"
    eve f_normal "I'll just sneak in there and go to my room."
    eve "I mean, look at them... They probably won't even notice me."
    anon "Y-yeah."
    anon "... Look at them."
    pause
    eve "Perv!"
    anon @ -m_talk "Hmm?"
    eve @ f_laugh "Haha!"
    anon "S-sorry."
    eve "It's okay."
    hide anon
    show eve b_dressed_kiss:
        xoffset -400
    anon "!!!"
    show eve b_dressed f_normal:
        xoffset 0
    show anon a_behind_head
    with dissolve
    eve "Thanks again for everything today."
    anon "It's no problem."
    eve "I'll see you soon, okay?"
    anon a_idle "Yeah."
    eve f_sexy "Don't stand out here all night watching them either!"
    anon "N-no, I won't."
    anon "I'm leaving."
    eve @ f_laugh "Hehe!"
    anon @ a_wave "Good night, {b}Eve{/b}."
    eve @ a_wave "Good night."
    scene black with fade
    pause
    $ player.go_to(L_tattooparlor)
    scene expression player.location.background_blur with None
    show anon f_flirt with dissolve
    anon @ -m_talk "( Wow, what a night! )"
    anon @ -m_talk "( So much happened and it sounds like things are definitely going to change for the better around here. )"
    pause
    anon @ -m_talk "( I'm too tired to think about that now though, I should get home. )"
    hide anon with dissolve
    $ M_eve.trigger(T_eve_dressed_table)
    $ game.timer.tick(3)
    $ player.go_to(L_map)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

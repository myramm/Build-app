label dianes_dialogue_breastfeed:
    if store._in_replay:
        scene expression player.location.background_blur
    show player 14 at left
    show diane b_naked a_idle f_smirk
    if store._in_replay:
        with fade
    player_name "Could I sample some more of your milk?"
    show player 13
    diane @ f_laugh "Heh, you want another dose straight from the tap?"
    show player 17
    player_name "Yes, please!"
    show player 13
    diane "Hmm, alright."
    diane "Just remember not to drink too much, okay?"
    show player 14
    player_name "Yup, I remember!"
    hide player
    hide diane
    with dissolve
    if M_diane.is_set("first boobjob"):
        jump diane_first_breastfeed
    jump diane_repeatable_breastfeed

label diane_repeatable_breastfeed:
    if L_diane_shed.is_here(M_diane):
        scene expression "backgrounds/location_diane_shed_hay_stack.jpg"
    else:
        scene expression "backgrounds/location_barn_hay_stack.jpg"
    if M_diane.outfit.get == "shirtless":
        $ M_diane.outfit.is_naked = 0
    show diane b_hay_feeding a_stroke f_explain
    with dissolve
    diane "Mmm, that warm mouth feels so good after a day of pumping."
    show diane f_lip_bite
    pause
    show diane f_explain
    diane "Ahh, how's it taste today, stud?"
    show diane f_smirk_down
    player_name "Mmhmm!"
    show diane f_laugh
    diane "Hehehe!"
    show diane f_smirk_down
    pause
    show diane f_explain
    diane "We shouldn't be doing this but for some reason..."
    diane "... That just makes me wanna do it even more!"
    show diane f_lip_bite
    pause
    show diane b_hay_feeding1 with dissolve
    diane "Ngghh!"
    show diane f_shamed_look
    diane "Alright, we'd better stop before you drink me dry, stud."
    show diane f_smirk_down
    player_name "Aww."
    show diane f_explain
    diane "I know..."
    show diane f_shamed_look
    diane "We'll do it again another day, alright?"
    show diane f_smirk_down
    player_name "Yeah, alright."
    show playersex 1 at right
    if M_diane.outfit.get == "shirtless":
        show diane f_smirk_front b_hay_undress1
    else:
        show diane f_smirk_front b_hay_sit
    with dissolve
    pause
    if M_diane.is_set("first cucumber"):
        $ M_diane.set("first cucumber", False)
        if M_diane.outfit.get == "shirtless":
            $ M_diane.outfit.is_naked = 1

        show diane f_smirk_front
        diane "Are you still hard?"
        if M_diane.outfit.get == "shirtless":
            show diane b_hay_dressed with dissolve
        player_name "Uh huh."
        diane "Why don't you take that big dick out for me?"
        player_name "O-okay."
        show playersex 2 with dissolve
        show diane f_down_front
        pause
        show playersex 4 with dissolve
        pause 1
        show playersex 3 with dissolve
        pause
        show diane f_smirk_front
        diane "Wonderful!"
        if M_diane.outfit.get == "shirtless":
            diane "My turn."
            show diane f_smirk_down b_hay_undress1 with dissolve
            pause
            show diane b_hay_undress2 with dissolve
            pause
            show diane b_hay_naked with dissolve
        diane "Now let me just-"
        hide playersex
        show diane b_hay_rub f_lip_bite
        player_name "!!!" with hpunch
        player_name "Oh, god!"
        pause
        pause
        show diane b_hay_sit f_smirk_front
        show playersex 3
        with dissolve
        player_name "Do you think we could do that thing again?"
        player_name "You know, with your boobs and my... Uhh..."
        diane "You want another boobjob?"
        player_name "Yeah, boobjob!"
        diane @ f_laugh "Hehe."
        diane "Well, we could..."
        pause
        diane "... Or, maybe, you could take care of my needs today?"
        player_name "Huh?"
        player_name "O-okay, sure."
        diane "Good boy!"
        player_name "What do you need me to do?"
        diane "Well, let's see..."
        show diane f_thinking
        pause
        show diane f_smirk_front
        diane "Oh, I know!"
        show diane b_hay_cucumber1 with dissolve
        player_name "Uhh, a cucumber?"
        diane "Oh, c'mon, don't play dumb."
        diane "I know you saw me in the kitchen that day."
        player_name "Y-yeah, but you want me to-"
        diane @ f_laugh "Mmhmm!"
        pause
        player_name "Alright."
        show diane b_hay_cucumber2 with dissolve
        pause
        show diane b_hay_behind_talk
        show playersex 18
        with dissolve
        diane "Be gentle, okay?"
        show diane b_hay_behind
        player_name "Okay."
        show diane b_hay_behind_pre with dissolve
        pause
        hide playersex
        show diane b_hay_insert1
        with dissolve
        player_name "Like this?"
        diane "Mmm, just like that!"
        hide diane
        jump diane_cucumber_start
    else:

        if M_diane.outfit.get == "shirtless":
            show diane b_hay_dressed with dissolve

        menu:
            "Boobjob.":
                show playersex 1 at right
                show diane f_smirk_front
                with dissolve
                player_name "Do you think you we could do that boobjob thing again?"
                diane "Sure, we can do that."
                diane "Get those pants off and sit up here."
                show playersex 2
                if M_diane.outfit.get == "shirtless":
                    show diane f_smirk_down b_hay_undress1
                with dissolve
                pause
                show playersex 4 with dissolve
                pause 1
                if M_diane.outfit.get == "shirtless":
                    show diane b_hay_undress2 f_down_front
                show playersex 3
                with dissolve
                pause
                if M_diane.outfit.get == "shirtless":
                    show diane b_hay_naked with dissolve
                    pause
                hide diane
                hide playersex

                scene expression "backgrounds/location_barn_floor_boobjob.jpg"
                if M_diane.outfit.get == "shirtless":
                    $ M_diane.outfit.is_naked = 1
                show diane_sex_boobjob 2
                show diane_sex_boobjob_look talk
                with dissolve
                diane "You really like this, huh?"
                hide diane_sex_boobjob_look

                jump diane_boobjob_start
            "Cucumber.":

                show playersex 1 at right
                show diane f_smirk_front
                with dissolve
                player_name "Would you like to use the cucumber again?"
                diane "Oh, definitely!"
                show playersex 2
                if M_diane.outfit.get == "shirtless":
                    show diane f_smirk_down b_hay_undress1
                else:
                    show diane f_down_front
                with dissolve
                pause
                show playersex 4 with dissolve
                pause 1
                if M_diane.outfit.get == "shirtless":
                    show diane b_hay_undress2 f_down_front
                show playersex 3
                with dissolve
                pause
                if M_diane.outfit.get == "shirtless":
                    show diane b_hay_naked with dissolve
                    pause
                    $ M_diane.outfit.is_naked = 1
                show diane f_smirk_front b_hay_cucumber1 with dissolve
                diane "Just be gentle, okay?"
                show playersex 18
                show diane b_hay_behind
                with dissolve
                player_name "I will."
                show diane b_hay_behind_pre with dissolve
                player_name "Here it comes..."
                hide playersex
                show diane b_hay_insert1
                with dissolve
                pause
                hide diane
                jump diane_cucumber_start
            "I better get back to work.":

                if store._in_replay is None:
                    scene expression player.location.background_blur with None
                else:
                    scene expression L_diane_shed.background_blur with None
                if M_diane.outfit.get == "shirtless":
                    $ M_diane.outfit.is_naked = 1

                    show diane b_shirtless f_smirk
                else:
                    show diane b_naked f_smirk
                show player 13 at left
                with dissolve
                diane "Now get your cute butt back to work!"
                show player 14
                player_name "Yes, ma'am!"
                hide player
                hide diane
                with dissolve
                $ renpy.end_replay()
    $ game.main()

label diane_cucumber_start:
    $ animated = True
    $ anim_toggle = True
    $ M_diane.set('sex speed', .4)
    show expression AnimatedImage("diane_hay_insert", [1,2], M_diane) as diane_hay_insert at Position(xalign = 0.0, yoffset = 0)
    diane "Ahhh!!"
    player_name "Wow, you're really wet, {b}Diane{/b}!"
    jump diane_cucumber_loop

label diane_cucumber_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("diane_hay_insert", [1,2], M_diane) as diane_hay_insert at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("diane_cucumber_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "diane_hay_insert {}".format(pose_list[pose_counter]) as diane_hay_insert at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("diane_cucumber_hscene_dialog")
        $ animcounter += 1
    call screen diane_cucumber_options

label diane_cucumber_cum:
    diane "I'm almost there!"
    if randomizer() < 50:
        diane "Don't stop!"
    else:
        diane "Fuck me!"
    pause
    diane "NGGHHH!!!" with flash
    hide diane_hay_insert
    show diane b_hay_insert1
    with dissolve
    diane "Haah... Haah..."
    show playersex 18
    show diane b_hay_behind_pre
    with dissolve
    pause
    show diane b_hay_behind_talk with dissolve
    diane "Oh, that was wonderful {b}[firstname]{/b}!"
    show diane b_hay_behind
    if randomizer() < 50:
        player_name "Hehe, you came really hard!"
        show diane b_hay_behind_talk
        diane "I did, hehe!"
    else:
        player_name "Hehe, yeah, that was fun!"
        player_name "You were shaking like crazy at the end there."
        show diane b_hay_behind_talk
        diane "Hehe!"
    diane "That's because you took such good care of me."
    show diane b_hay_behind
    pause
    show diane b_hay_behind_talk
    diane "Thank you for that, by the way."
    show diane b_hay_behind
    player_name "No problem."
    show diane b_hay_behind_talk
    diane "Haah... I need to rest for a moment."
    diane "You okay going back to work?"
    show diane b_hay_behind
    player_name "S-sure."
    show diane b_hay_behind_talk
    diane "Good boy."
    show diane b_hay_behind
    hide playersex with dissolve
    pause
    show diane b_hay_behind_pre with dissolve
    diane "Phew!"
    diane "That was intense!"
    hide diane with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["05_unlocked"] = True
    $ renpy.end_replay()
    $ game.timer.tick()
    if game.timer.is_night():
        $ player.go_to(L_map)
    else:
        if player.location is L_diane_barn_interior:
            $ player.go_to(L_diane_barn)
        else:
            $ player.go_to(L_diane_garden)
    $ game.main()

label diane_cucumber_hscene_dialog:
    if animcounter == 0 and randomizer() < 25:
        diane "Oh, god!{p=1}{nw}"
    if animcounter == 0 and randomizer() < 25:
        diane "Ahh!{p=1}{nw}"
    if animcounter == 1 and randomizer() > 75:
        diane "Yes!{p=1}{nw}"
    if animcounter == 1 and randomizer() > 75:
        diane "Mmm, that's it {b}[firstname]{/b}!{p=1}{nw}"
        diane "Fuck me with that cucumber!{p=2}{nw}"
    if animcounter == 2 and randomizer() < 25:
        diane "Deeper, {b}[firstname]{/b}!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 25:
        diane "You naughty boy!{p=1}{nw}"
        player_name "Heh.{p=1}{nw}"
    if animcounter == 3 and randomizer() > 75:
        diane "Ahhh!!{p=1}{nw}"
        diane "I'm almost there...{p=2}{nw}"
    if animcounter == 3 and randomizer() > 75:
        diane "Faster!{p=1}{nw}"
        if M_diane.get("sex speed") > 0.21:
            $ M_diane.set("sex speed", M_diane.get("sex speed") - 0.1)
        diane "Ahh!!{p=1}{nw}"
    return

label diane_first_breastfeed:
    scene expression "backgrounds/location_diane_shed_hay_stack.jpg"
    show diane b_hay_feeding a_stroke f_explain
    with dissolve
    diane "Mmm, that warm mouth feels so good after a day of pumping."
    show diane f_lip_bite
    pause
    show diane f_explain
    diane "Ahh, how's it taste today, stud?"
    show diane f_smirk_down
    player_name "Mmhmm!"
    show diane f_laugh
    diane "Hehehe!"
    show diane f_smirk_down
    pause
    show diane f_explain
    diane "We shouldn't be doing this but for some reason..."
    diane "... That just makes me wanna do it even more!"
    show diane f_lip_bite
    pause
    show diane b_hay_feeding1 with dissolve
    diane "Ngghh!"
    show diane f_shamed_look
    diane "Alright, we'd better stop before you drink me dry, stud."
    show diane f_smirk_down
    player_name "Aww."
    show diane f_explain
    diane "I know..."
    show diane f_shamed_look
    diane "We'll do it again another day, alright?"
    show playersex 1 at right
    if M_diane.outfit.get == "shirtless":
        show diane f_smirk_down b_hay_undress1
    else:
        show diane f_smirk_front b_hay_sit
    with dissolve
    player_name "Isn't there anything else we can do?"
    if M_diane.outfit.get == "shirtless":
        show diane b_hay_dressed f_smirk_front with dissolve
    diane "Like what?"
    player_name "I dunno..."
    player_name "... I'm just so horny!"
    diane @ f_laugh "Hehe, I know handsome, me too..."
    pause
    diane "Alright, why don't you take it out for me?"
    diane "Let me get a good look at it."
    pause
    player_name "O-okay."
    show playersex 2 with dissolve
    show diane f_down_front
    pause
    show playersex 4 with dissolve
    pause 1
    show playersex 3 with dissolve
    pause
    show diane f_surprised_front
    diane "Mmm, good lord..."
    diane "That is something really special!"
    player_name "Y-yeah?"
    show diane f_smirk_front
    diane @ -m_talk "Mmmhmm."
    pause
    if M_diane.outfit.get == "shirtless":
        $ M_diane.outfit.is_naked = 1
        diane "I guess it's my turn now, huh?"
        show diane f_smirk_down b_hay_undress1 with dissolve
        pause
        show diane b_hay_undress2 with dissolve
        player_name "Wow!"
        show diane b_hay_naked f_laugh with dissolve
        diane "Hehehe, you like?"
        show diane f_smirk_front
    player_name "You're so beautiful, {b}Diane{/b}!"
    diane "Oh, I'm not THAT beautiful..."
    player_name "Yes you are!"
    diane "Tsk, such a charmer..."
    player_name "So what are we going to do?"
    hide playersex
    show diane b_hay_rub f_lip_bite
    player_name "!!!" with hpunch
    player_name "Oh, god!"
    pause
    pause
    if M_diane.outfit.get == "shirtless":
        player_name "Can I put it inside, {b}Diane{/b}?"
        show playersex 3 at right
        show diane b_hay_naked f_shamed_front
        with dissolve
        diane "Ngh, no..."
        player_name "How come?"
        diane "{b}[firstname]{/b}, you know why..."
        diane "We can't..."
        player_name "{i}*Sigh*{/i} But I want to, so bad!"
        diane "I know, handsome..."
        pause
        show diane f_smirk_front
    else:
        show playersex 3 at right
        show diane b_hay_sit f_smirk_front
        with dissolve
    diane "Come sit here."
    player_name "Hmm?"
    diane "Come on."
    diane "I'm gonna take care of this for you."
    player_name "O-okay..."
    hide diane
    hide playersex
    scene expression "backgrounds/location_barn_floor_boobjob.jpg"
    if M_diane.outfit.get == "shirtless":
        $ M_diane.outfit.is_naked = 1
    show diane_sex_boobjob 2
    show diane_sex_boobjob_look talk
    with dissolve
    diane "You like my breasts, don't you?"
    show diane_sex_boobjob_look
    player_name "Of course!"
    show diane_sex_boobjob_look talk
    diane "I'm gonna show you something special..."
    show diane_sex_boobjob_look
    player_name "What are you-"
    hide diane_sex_boobjob_look
    jump diane_boobjob_start

label diane_boobjob_start:
    $ animated = True
    $ anim_toggle = True
    $ M_diane.set('sex speed', .25)
    show expression AnimatedImage("diane_sex_boobjob", [1,2,3,2], M_diane) as diane_sex_boobjob at Position(xalign = 0.0, yoffset = 0)
    player_name "Haah!" with hpunch
    diane "You like that?"
    player_name "Y-yes!!"
    label diane_boobjob_loop:
        show screen sex_anim_buttons
        pause
        hide screen sex_anim_buttons
        $ animcounter = 0
        while animcounter < 4:
            if anim_toggle:
                if not animated:
                    show expression AnimatedImage("diane_sex_boobjob", [1,2,3,2], M_diane) as diane_sex_boobjob at Position(xalign = 0.0, yoffset = 0)
                    $ animated = True
                pause 5
                call expression game.dialog_select("diane_boobjob_hscene_dialog")
                pause 3
            else:

                $ pose_counter = 0
                $ pose_list = [1,2,3,2]
                $ poses_done = []
                while poses_done != pose_list:
                    show expression "diane_sex_boobjob {}".format(pose_list[pose_counter]) as diane_sex_boobjob at Position(xalign = 0.0, yoffset = 0)
                    pause
                    $ poses_done.append(pose_list[pose_counter])
                    $ pose_counter += 1
                call expression game.dialog_select("diane_boobjob_hscene_dialog")
            $ animcounter += 1
        call screen diane_boobjob_options

label diane_boobjob_hscene_dialog:
    $ renpy.dynamic(rng=randomizer())
    if animcounter == 0:
        if rng > 90:
            player_name "Oh my god, this feels amazing!{p=2}{nw}"
            diane "Hehehe!{p=1}{nw}"
    elif animcounter == 1:
        if rng > 95:
            player_name "Where did you learn to do this?{p=2}{nw}"
            diane "Hmm?{p=1}{nw}"
            diane "Oh, umm... Actually, it was {b}[deb_name]{/b} who showed me how to do this...{p=2}{nw}"
            diane "Back when we were young and wild.{p=2}{nw}"
            player_name "What?!{p=1}{nw}"
            player_name "{b}[deb_name]{/b} taught you this?!{p=2}{nw}"
            diane "Hehe, what?{p=1}{nw}"
            diane "You didn't think {b}[deb_name]{/b} was a virgin, did you?{p=2}{nw}"
            player_name "Well, no.{p=1}{nw}"
            player_name "I just didn't...{p=1}{nw}"
            player_name "Ahh!!{p=1}{nw}"
        elif rng > 80:
            player_name "Mmm, this is so hot!{p=2}{nw}"
    elif animcounter == 2:
        if rng > 90:
            diane "You really like fucking my boobs, don't you handsome?{p=2}{nw}"
            player_name "Y-yeah!{p=1}{nw}"
            diane "Hehe!{p=1}{nw}"
        elif rng > 80:
            diane "You like the way my tits feel wrapped around your cock?{p=2}{nw}"
            player_name "Y-yes!{p=1}{nw}"
        elif rng > 70:
            diane "I love feeling that big hard cock of yours in between my tits...{p=2}{nw}"
            player_name "Me too!{p=1}{nw}"
    elif animcounter == 3:
        if rng > 90:
            player_name "I'm getting close...{p=2}{nw}"
    return

label diane_boobjob_cum:
    player_name "I'm getting close, {b}Diane{/b}!"
    diane "That's alright, handsome."
    diane "Let it out."
    pause
    show diane_sex_boobjob cum
    show diane_sex_boobjob_cum
    player_name "HNNGGG!!!" with flash
    show diane_sex_boobjob 2
    show diane_sex_boobjob_look talk
    with dissolve
    diane "Good boy!"
    show diane_sex_boobjob_look
    pause
    player_name "Haah... Haah..."
    pause
    show diane_sex_boobjob_look talk
    diane "Hehehe!"
    scene black with fade
    hide diane_sex_boobjob_look
    hide diane_sex_boobjob
    scene expression player.location.background_blur with None
    if M_diane.is_set("first boobjob"):
        $ M_diane.set("first boobjob", False)
        show player 261bf at left
        show diane b_naked f_down_front o_boob_cum
        with dissolve
        pause
        show player 14 with dissolve
        show diane f_smirk
        player_name "That was awesome!"
        show player 13
        diane "You feel better now?"
        show player 17
        player_name "Definitely!"
        show player 13
        show diane a_touch_cum f_down_front with dissolve
        pause
        show diane a_lick_cum f_lick_finger with dissolve
        show player 11
        player_name "!!!"
        show diane f_smirk a_idle with dissolve
        show player 10
        player_name "Did you just-"
        show player 5
        show diane f_laugh
        diane "Hehehe!"
        show diane f_smirk
        diane "You've been drinking my milk, it's only fair I get to try yours."
        show player 14
        player_name "... Well?"
        show player 13
        diane "It's not bad."
        pause
        diane "I don't think we're gonna get any orders for it though..."
        show diane f_cheese
        show player 17
        player_name "Haha!"
        show player 14
        player_name "Yeah, probably not."
        show player 13
        show diane f_smirk
        diane "Alright, we really should get back to work."
        diane "... And I need to clean myself up!"
        show player 14
        player_name "Yeah, okay {b}Diane{/b}."
        player_name "I'll be in the garden if you need me."
        show player 13
        diane "Thanks, {b}[firstname]{/b}."
        hide player with dissolve
        pause
        show diane a_touch_cum f_down_front with dissolve
        pause
        show diane a_lick_cum f_lick_finger with dissolve
        diane @ -m_talk "Mmm!"
        hide diane with dissolve
    else:
        if M_diane.outfit.get == "shirtless":
            $ M_diane.outfit.is_naked = 1
        show player 261bf at left
        show diane b_naked f_down_front o_boob_cum
        with dissolve
        pause
        show player 14
        show diane f_smirk
        player_name "Phew!"
        player_name "Thanks, {b}Diane{/b}."
        player_name "I really needed that."
        show player 13
        diane "My pleasure, stud."
        diane "Now get back to work, will ya?"
        show player 14
        player_name "Y-yeah, okay."
        hide player with dissolve
        pause
        show diane a_touch_cum f_down_front with dissolve
        pause
        show diane a_lick_cum f_lick_finger with dissolve
        diane @ -m_talk "Mmm, delicious!"
        show diane a_idle f_cheese with dissolve
        diane "Hehe!"
        hide diane with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["04_unlocked"] = True
    $ renpy.end_replay()
    $ game.timer.tick()
    if game.timer.is_night():
        $ player.go_to(L_map)
    else:
        if player.location is L_diane_barn_interior:
            $ player.go_to(L_diane_barn)
        else:
            $ player.go_to(L_diane_garden)
    $ game.main()

label diane_sex_breed_start:
    $ diane_sex_position = "back"
    $ anim_toggle = True
    $ animated = True
    $ M_diane.set('sex speed', 0.09)
    show expression AnimatedImage("diane_sex_back", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
    if store._in_replay:
        with fade
    jump diane_sex_breed_loop

label diane_sex_breed_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_diane.get("change angle"):
                    scene expression "backgrounds/location_barn_sex_front_day.jpg"
                    show expression AnimatedImage("diane_sex_front", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
                    with dissolve
                else:
                    scene expression "backgrounds/location_barn_sex_back_day.jpg"
                    show expression AnimatedImage("diane_sex_back", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
                    with dissolve
                $ animated = True
            pause 5
            call expression game.dialog_select("diane_sex_breed_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                if M_diane.get("change angle"):
                    scene expression "backgrounds/location_barn_sex_front_day.jpg"
                    show expression "diane_sex_front {}".format(pose_list[pose_counter]) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
                else:
                    scene expression "backgrounds/location_barn_sex_back_day.jpg"
                    show expression "diane_sex_back {}".format(pose_list[pose_counter]) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("diane_sex_breed_hscene_dialog")
        $ animcounter += 1
    call screen diane_sex_breed_options

label diane_sex_breed_hscene_dialog:
    if animcounter == 0 and randomizer() < 25:
        if randomizer() > 50:
            diane "Oh yes!{p=1}{nw}"
            diane "It's so deep!{p=1}{nw}"
        else:
            if M_diane.pregnancy.number_of_babies>0:
                diane "Oh, I want another baby so bad, {b}[firstname]{/b}.{p=2}{nw}"
            else:
                diane "Oh, I want your baby so bad, {b}[firstname]{/b}.{p=2}{nw}"
            diane "Put it inside me, please!{p=2}{nw}"
    if animcounter == 0 and randomizer() > 90:
        diane "Yes, {b}[firstname]{/b}!{p=1}{nw}"
        diane "Fuck me like an animal!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 25:
        diane "My bull!{p=1}{nw}"
        diane "My big strong bull!{p=2}{nw}"
    if animcounter == 1 and randomizer() < 25:
        if randomizer() > 50:
            diane "Oh, it's so good!{p=1}{nw}"
        else:
            diane "You're so big, {b}[firstname]{/b}!{p=1}{nw}"
    if animcounter == 2 and randomizer() > 75:
        if randomizer() > 50:
            player_name "Phew, this feels amazing {b}Diane{/b}!{p=2}{nw}"
            diane "Mmmhmm!{p=1}{nw}"
        else:
            diane "Yes!{p=1}{nw}"
            diane "Oh god, yes!{p=1}{nw}"
    if animcounter == 3 and randomizer() > 90:
        player_name "Moo for me.{p=1}{nw}"
        diane "What?{p=1}{nw}"
        pause 1
        player_name "You want to be fucked like an animal, don't you?{p=2}{nw}"
        diane "Oh, god yes!{p=1}{nw}"
        player_name "Then moo for me.{p=1}{nw}"
        pause 1
        diane "... Moo?{p=1}{nw}"
        player_name "You can do better than that...{p=2}{nw}"
        if M_diane.get("sex speed") > 0.031:
            $ M_diane.set("sex speed", M_diane.get("sex speed") - 0.03)
        diane "Moo!{p=1}{nw}"
        player_name "Louder, {b}Diane{/b}!{p=1}{nw}"
        diane "Moo!!{p=1}{nw}"
        player_name "Louder!{p=1}{nw}"
        if M_diane.get("sex speed") > 0.031:
            $ M_diane.set("sex speed", M_diane.get("sex speed") - 0.03)
        diane "Oh, shit!{p=1}{nw}"
        player_name "Moo for me!{p=1}{nw}"
        diane "MOO!!!{p=1}{nw}"
        pause 1
        diane "MOOOOOOO!!!{p=1}{nw}"
    if animcounter == 3 and randomizer() > 75:
        if randomizer() > 50:
            diane "That's it!{p=1}{nw}"
            diane "Fuck me, stud!{p=1}{nw}"
        if M_diane.get("sex speed") > 0.031:
            $ M_diane.set("sex speed", M_diane.get("sex speed") - 0.03)
        if randomizer() > 50:
            diane "Ohh! Oooh!!{p=1}{nw}"
            pause 1
            diane "OOOOH, GOD!!!{p=1}{nw}"
        else:
            diane "Aaahhh!!!{p=1}{nw}"
    if animcounter == 4 and randomizer() < 25:
        if randomizer() < 50:
            diane "It's so good!{p=1}{nw}"
            pause 1
            diane "Oh, it's so fucking good!{p=1}{nw}"
        else:
            diane "Fill me up, stud!{p=1}{nw}"
    if animcounter == 4 and randomizer() > 75:
        if randomizer() > 50:
            player_name "Wow, {b}Diane{/b}, you're so wet!{p=1}{nw}"
            pause 1
            diane "I know!{p=1}{nw}"
            diane "My body loves your cock!{p=1}{nw}"
        else:
            diane "Do it, {b}[firstname]{/b}!{p=1}{nw}"
            diane "Breed me!{p=1}{nw}"
    return

label diane_sex_breed_cum_pre:
    player_name "{b}Diane{/b} I'm gonna cum!"
    diane "Ah, meeee toooo!!!"
    pause
    if randomizer() < 50:
        diane "Cum in me, {b}[firstname]{/b}!"
        if M_diane.pregnancy.number_of_babies>0:
            diane "I want another baby inside me!"
        else:
            diane "I want your baby inside me!"
    else:
        diane "Cum inside me, {b}[firstname]{/b}!"
        diane "I want all of it!"
    player_name "Oh god!"
    pause
    if store._in_replay is None:
        $ M_diane.trigger(T_diane_brought_outfit_package)
    call screen diane_cum_breed_options

label diane_sex_breed_cum_out:
    player_name "I don't..."
    $ M_diane.set('sex speed', 0.09)
    pause
    player_name "I can't..."
    pause
    diane "AAAAHHHH!!!"
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show diane_sex_breed after
    show diane_sex_breed_mc cumshot 2
    player_name "HNNGGG!!!" with flash
    show diane_sex_breed_mc cumshot 1
    show diane_sex_flying_cum 1
    with dissolve
    pause 1
    show diane_sex_flying_cum 2
    with dissolve
    pause
    player_name "Haah... Haah..."
    diane "Wha-"
    pause

    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 368 at left
    show diane b_naked f_sad
    with fade
    if randomizer() < 50:
        diane "... What happened?"
        diane "{b}[firstname]{/b}, you were supposed to cum inside me..."
        show player 367
        player_name "I know."
        show player 368
        pause
        show player 367
        player_name "I know."
        player_name "I'm sorry."
        player_name "The moment came and I just kinda..."
        show player 368
        pause
        show player 367
        player_name "... Phew, I dunno."
        player_name "I'll cum inside you next time, okay?"
        show player 368
        pause
        if M_diane.pregnancy.number_of_babies>0:
            show diane f_shamed_smile
            diane "Alright..."
        else:
            diane "You have to remember, there's a reason we're doing this..."
            show diane f_shamed
            show player 367
            player_name "I know."
            show player 368
        show diane f_normal
        diane "That WAS incredible though!"
    else:
        diane "You pulled out!"
        show player 367
        player_name "I know."
        show player 368
        diane "Why did you-"
        diane "{b}[firstname]{/b}, I can't get pregnant if you cum on my back!"
        show player 367
        player_name "I'm sorry."
        player_name "I just, couldn't this time."
        show player 368
        pause
        diane "Oh, it's alright."
        diane "I'm not mad."
        if M_diane.pregnancy.number_of_babies>0:
            show player 367
        else:
            diane "You just have to remember why we're doing this."
            pause
            diane @ f_normal "Don't get me wrong, I REALLY like fucking you, {b}[firstname]{/b}..."
            diane "... But if I don't get pregnant then the business will suffer."
            show player 367
            player_name "I know."
        player_name "I'm sorry."
        hide player
        show diane b_kiss_both_naked:
            xoffset -217
        with dissolve
        player_name "!!!"
        pause
        show player 366 at left
        show diane b_naked f_normal
        with dissolve
        diane "Don't apologize."
        show diane f_smirk
        if M_diane.pregnancy.number_of_babies>0:
            diane "Just next time, put another baby in me!"
        else:
            diane "Just next time, put a baby in me!"
        diane "Okay?"
        show player 365
        player_name "Okay..."
        show player 366
        diane "Now, let's start milking."
        show player 365
        player_name "Yes, ma'am."
        show player 366
        diane "Just be gentle, {b}[firstname]{/b}."
        hide player
        hide diane
        with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["05_unlocked"] = True
    $ renpy.end_replay()
    jump milking_game_pre_after_sex

label diane_sex_breed_cum_in:
    player_name "Ooh!"
    pause
    player_name "Here it comes!"
    diane "Fill me up, {b}[firstname]{/b}!!"
    pause
    diane "AAAAHHHH!!!"
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    $ M_diane.set("sex speed",0.4)
    show diane_sex_breed creampie zorder 0
    show xray_diane_back zorder 1 at Position (align=(0,0))
    player_name "HNNGGG!!!" with flash
    hide xray_diane_back
    show diane_sex_breed creampie_pullout
    with dissolve
    diane "NGGHHH!!!"
    show diane_sex_breed insert_and_pullout
    show diane_sex_dick_cum 2 zorder 3
    with dissolve
    pause
    show diane_sex_breed after
    show diane_sex_cum zorder 1
    show diane_sex_breed_mc zorder 2
    show diane_sex_dick_cum 1
    with dissolve
    pause
    show diane_sex_breed after_spread
    show diane_sex_cum spread
    with dissolve
    player_name "Haah... Haah..."
    pause
    diane "Oh, GOD!"
    pause
    diane "So much..."
    pause
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["06_unlocked"] = True
    $ renpy.end_replay()
    call call_pregnancy_minigame (return_label="diane_sex_breed_cum_in_after_minigame", machine=M_diane)

label diane_sex_breed_cum_in_after_minigame:
    if M_diane.is_state(S_diane_milk_production_increase):
        $ M_diane.trigger(T_diane_breeding)

    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 366 at left
    show diane b_naked f_smirk
    with fade
    if randomizer() < 50 or M_diane.is_set("breed first time"):
        diane "That was so much cum, {b}[firstname]{/b}!"
        show player 365
        player_name "S-sorry."
        show player 366
        diane "No, it's wonderful!"
    else:
        diane "Mmm, I love your huge loads, {b}[firstname]{/b}."
        show player 365
        player_name "Y-yeah?"
        show player 366
        show diane f_laugh
        diane "They feel so wonderful!"
    show diane f_smirk
    show player 365
    player_name "Heh."
    show player 366
    pause
    show player 365
    if M_diane.pregnancy.number_of_babies>0:
        player_name "Do you think you're, you know... pregnant again?"
    else:
        player_name "Do you think you're, you know... pregnant?"
    show player 366
    show diane f_laugh
    diane "Haha, it's too early to know."
    show diane f_smirk
    diane "I hope so."
    pause
    show player 365
    player_name "You might have my baby inside you, right now!"
    show player 366
    diane "Hehe, I know!"
    diane "It's so exciting!"
    diane "Oh, stud... You were so good!"
    jump milking_game_pre_after_sex

label diane_debbie_sex_start:
    if store._in_replay:
        scene expression "backgrounds/location_home_debbiebed_sex.jpg"
        $ M_diane.set('sex speed', 0.09)
    $ anim_toggle = True
    if not M_diane.is_set("3way first time"):
        $ M_diane.set('sex speed', 0.09)
    if not animated:
        show expression AnimatedImage("diane_debbie_sex_bed", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_debbie_sex_bed at Position(xalign = 0.0, yoffset = 0)
        $ animated = True

label diane_debbie_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("diane_debbie_sex_bed", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_debbie_sex_bed at Position(xalign = 0.0, yoffset = 0) with dissolve
                $ animated = True
            pause 5
            call expression game.dialog_select("diane_debbie_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "diane_debbie_sex_bed {}".format(pose_list[pose_counter]) as diane_debbie_sex_bed at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("diane_debbie_sex_hscene_dialog")
        $ animcounter += 1
    call screen diane_debbie_sex_options

label diane_debbie_sex_hscene_dialog:
    if not M_diane.get("change partner"):
        if animcounter == 0 and randomizer() < 25:
            diane "OH MY GOD!{p=1}{nw}"
            diane "Don't stop!!{p=1}{nw}"
        if animcounter == 1 and randomizer() < 25:
            diane "Oh, shit!{p=1}{nw}"
            diane "Ahhh!{p=1}{nw}"
        if animcounter == 2 and randomizer() < 10:
            debbie "Hehe, I love this view!{p=2}{nw}"
            diane "Sorry, if I leak on you...{p=2}{nw}"
            debbie "It's okay, I don't mind.{p=2}{nw}"
        elif randomizer() < 25:
            diane "Oh my god, it's so deep!{p=2}{nw}"
            debbie "My boy has the best cock, doesn't he?!{p=2}{nw}"
            diane "Yes!!{p=1}{nw}"
        if animcounter == 3 and randomizer() < 25:
            player_name "I'm getting close!{p=1}{nw}"
            diane "Ahh, me too!{p=1}{nw}"
            debbie "That's okay sweetie, you go right ahead!{p=2}{nw}"
    else:
        if animcounter == 0 and randomizer() < 25:
            diane "C'mon, {b}[firstname]{/b}!{p=1}{nw}"
            diane "Fuck her harder!{p=1}{nw}"
            if M_diane.get("sex speed") > 0.31:
                $ M_diane.set("sex speed", M_diane.get("sex speed") - 0.03)
            debbie "Oh, god!{p=1}{nw}"
        elif randomizer() < 50:
            debbie "AHHH!!{p=1}{nw}"
            diane "That's it, stud!{p=1}{nw}"
        if animcounter == 1 and randomizer() < 25:
            debbie "Ahh!{p=1}{nw}"
        if animcounter == 2 and randomizer() < 25:
            diane "How is it so easy for you?!{p=2}{nw}"
            debbie "Hmm?{p=1}{nw}"
            diane "You take that huge cock like it's nothing!{p=2}{nw}"
            debbie "Mmm, I dunno...{p=1}{nw}"
            debbie "... It just feels so wonderful!{p=1}{nw}"
        if animcounter == 3 and randomizer() < 25:
            player_name "I'm getting close!{p=1}{nw}"
            debbie "Ahh, me too!{p=1}{nw}"
            diane "Go ahead, handsome.{p=1}{nw}"
            diane "Show {b}[deb_name]{/b} how much you love her.{p=2}{nw}"
    return

label diane_debbie_sex_cum:
    player_name "Here it comes!"
    pause
    if M_diane.get("cum inside"):
        show diane_debbie_sex_bed cumpie
        if not M_diane.get("change partner"):
            show xray_diane_debbie_sex at Position (align=(0,0))
        else:
            show xray_diane_debbie_sex at Position (xpos=190,ypos=420)
    else:
        show diane_debbie_sex_bed base
        show diane_debbie_sex_bed_cumshot_mc
    player_name "HNNGGG!!!" with flash
    if not M_diane.get("change partner"):
        diane "NGGHHH!!!"
    else:
        debbie "OHHH!!!"
    hide xray_diane_debbie_sex with dissolve
    pause
    player_name "Haah... Haah..."
    hide diane_debbie_sex_bed_cumshot_mc

    if not M_diane.get("change partner"):
        show diane_debbie_sex_bed diane_after_talk
        with dissolve
        diane "Oh, wow..."
        if M_diane.get("cum inside"):
            diane "He came so much in me."
            show diane_debbie_sex_bed debbie_after_talk
            debbie "Hehe, that's my boy!"
            show diane_debbie_sex_bed diane_after_talk
            diane "Mmm."
        else:
            show diane_debbie_sex_bed debbie_after_talk
            debbie "There's so much!"
            show diane_debbie_sex_bed diane_after_talk
            diane "Sheesh, I'm covered!"
            diane "Haha!"
    else:
        show diane_debbie_sex_bed debbie_after_talk
        with dissolve
        debbie "Oh, my..."
        if M_diane.get("cum inside"):
            debbie "I feel so full."
            show diane_debbie_sex_bed diane_after_talk
            diane "Hehe, that's my big sexy stud!"
            show diane_debbie_sex_bed debbie_after_talk
            debbie "Mmm."
        else:
            show diane_debbie_sex_bed diane_after_talk
            diane "There's so much!"
            show diane_debbie_sex_bed debbie_after_talk
            debbie "Hehe!"
            debbie "Oh, I love feeling it on me!"

    if M_diane.is_set("3way first time"):
        show diane_debbie_sex_bed diane_after_talk
        diane "I'm so glad this happened!"
        show diane_debbie_sex_bed debbie_after_talk
        debbie "It was wonderful, wasn't it?"
        player_name "It was so awesome!"
        show diane_debbie_sex_bed diane_after_talk
        diane "Hehehe!"
        show diane_debbie_sex_bed debbie_after_talk
        debbie "Hehehe!"
        player_name "Can we do this again?!"
        show diane_debbie_sex_bed diane_after_talk
        diane "I'm down!"
        show diane_debbie_sex_bed debbie_after_talk
        debbie "Of course, we can do it whenever you want, {b}[firstname]{/b}."
        pause
        show diane_debbie_sex_bed debbie_after_talk
        debbie "Right now, I just want you to come and lay with us."
        show diane_debbie_sex_bed debbie_lounge_after_talk with dissolve
        debbie "I'm worn out!"
        show diane_debbie_sex_bed diane_lounge_after_talk
        diane "Hah, yeah... Me too!"
        show diane_debbie_sex_bed player_lounge_after_talk
        player_name "Hehe."
        show diane_debbie_sex_bed debbie_lounge_after_talk
        debbie "C'mere sweetie!"
        debbie "Lie here between us."
        show diane_debbie_sex_bed player_lounge_after_talk
        player_name "O-okay."
    else:

        show diane_debbie_sex_bed diane_after_talk
        diane "Phew."
        diane "I'm so exhausted now..."
        show diane_debbie_sex_bed debbie_after_talk
        debbie "Ugh, me too."
        debbie "There's two of us, and we still can't keep up with him!"
        show diane_debbie_sex_bed diane_after_talk
        diane "Haha!"
        player_name "Whatever."
        show diane_debbie_sex_bed player_lounge_after_talk with dissolve
        player_name "I'm tired too!"
        show diane_debbie_sex_bed debbie_lounge_after_talk
        debbie "That's alright, sweetie."
        debbie "You just lay here and rest."
        show diane_debbie_sex_bed diane_lounge_after_talk
        diane "Aww, I love you guys!"
        show diane_debbie_sex_bed debbie_lounge_after_talk
        debbie "Hehe, we love you too."

    scene black with fade
    hide diane_debbie_sex_bed

    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["07_unlocked"] = True
    $ renpy.end_replay()
    $ M_diane.trigger(T_diane_debbie_3way)
    if M_diane.get("cum inside") and not M_diane.get("change partner"):
        call call_pregnancy_minigame ("diane_debbie_sleeping", M_diane)
    jump diane_debbie_sleeping

label diane_debbie_sleeping:
    call expression game.dialog_select("diane_debbie_sleeping_pre")
    call sleep_lock_check
    if M_player.is_set("just wokeup"):
        $ renpy.call(game.dialog_select("player_just_wokeup"), woke_with = M_diane)
    $ game.main()

label diane_debbie_sleeping_pre:
    scene location_home_debbiebedroom_night_sleep_trio with fade
    call popup ('sleep')
    return

label diane_debbie_sleepover_wakeup_first:
    scene expression "backgrounds/location_home_debbiebedroom_day_blur.jpg" with fade
    show player 7 with dissolve
    pause
    show player 8 with dissolve
    pause
    show player 5 with dissolve
    player_name "Hmm?"
    show player 10
    player_name "Where'd everybody go?"
    show player 9 at Position (xoffset=40) with dissolve
    pause
    show player 17 with dissolve
    player_name "{i}*Sniff*{/i} Something smells great!"
    show player 14
    player_name "{b}[deb_name]{/b} must be cooking {b}in the kitchen{/b}."
    player_name "I should {b}go check it out{/b}."
    hide player with dissolve
    return

label diane_debbie_sleepover_wakeup_repeat:
    scene expression "backgrounds/location_home_debbiebedroom_day_blur.jpg" with fade
    show player 7 with dissolve
    pause
    show player 8 with dissolve
    pause
    show player 14 with dissolve
    player_name "Looks like {b}Diane{/b} and {b}[deb_name]{/b} are already up."
    hide player with dissolve
    return

label diane_debbie_pre_sex_loop:
    if not animated:
        show diane_debbie_sex_bed prev_insert
    if not M_diane.get("change partner"):
        if randomizer() > 50:
            if animated:
                show diane_debbie_sex_bed player_talk
            player_name "I think it's time that {b}Diane{/b} had a turn."
            if animated:
                show diane_debbie_sex_bed debbie_talk
            debbie "If that's what you want, sweetie."
            debbie "Go ahead."
            if animated:
                show diane_debbie_sex_bed diane_talk
            diane "Mmhmm, bring that big dick over here."
            show diane_debbie_sex_bed insert with dissolve
            debbie "Hehe!"
            diane "C'mon stud, show me what you got!"
            show diane_debbie_sex_bed 7
            diane "!!!" with hpunch
        else:
            if animated:
                show diane_debbie_sex_bed player_talk
            player_name "{b}Diane{/b}, you're up next!"
            if animated:
                show diane_debbie_sex_bed diane_talk
            diane "Mmm, lucky me!"
            show diane_debbie_sex_bed insert with dissolve
            diane "C'mon stud, show me what you got!"
            show diane_debbie_sex_bed 7
            diane "!!!" with hpunch
    else:
        if randomizer() > 50:
            if animated:
                show diane_debbie_sex_bed player_talk
            player_name "Ready, {b}[deb_name]{/b}?"
            if animated:
                show diane_debbie_sex_bed debbie_talk
            debbie "Mmm!"
            show diane_debbie_sex_bed insert with dissolve
            debbie "That's it sweetie!"
            debbie "Let me show a thing or two, {b}[firstname]{/b}!"
            player_name "Uh huh!"
            show diane_debbie_sex_bed 7
            diane "Oh!" with hpunch
        else:
            if animated:
                show diane_debbie_sex_bed player_talk
            player_name "It's {b}[deb_name]{/b}'s turn!"
            if animated:
                show diane_debbie_sex_bed diane_talk
            diane "Ahh, good idea..."
            diane "I need a break!"
            if animated:
                show diane_debbie_sex_bed debbie_talk
            debbie "Hehe!"
            show diane_debbie_sex_bed insert with dissolve
            player_name "Here it comes, {b}[deb_name]{/b}."
            debbie "I'm ready!"
            show diane_debbie_sex_bed 7
            debbie "Oh! That's it sweetie!" with hpunch
    $ animated = False
    jump diane_debbie_sex_loop


label diane_cookiejar:
    return


label diane_cookiejar.paizuri:
    $ M_diane.reset()
    $ M_diane.outfit.outfits = {}
    $ player.location = L_diane_shed
    $ game.timer._tod = 2

    scene location_diane_shed_hay_stack

    menu:
        "Overalls":
            $ M_diane.outfit.set_default_outfit_schedule('shirtless')
        "Cowsuit":

            $ M_diane.outfit.set_default_outfit_schedule('cow')
        "Naked":

            $ M_diane.outfit.is_naked = True

    jump dianes_dialogue_breastfeed


label diane_cookiejar.cucumber:
    $ M_diane.reset()
    $ M_diane.set('first boobjob', False)
    $ player.location = L_diane_barn_interior

    scene location_barn_hay_stack

    menu:
        "Cowsuit":
            $ M_diane.outfit.set_default_outfit_schedule('cow')
        "Naked":

            $ M_diane.outfit.is_naked = True

    jump dianes_dialogue_breastfeed


label diane_cookiejar.breed:
    $ M_diane.reset()

    scene location_barn_hay_stack

    menu:
        "Cowsuit":
            $ M_diane.outfit.set_default_outfit_schedule('cow')
        "Naked":

            $ M_diane.outfit.is_naked = True

    scene location_barn_sex_back_day
    jump diane_sex_breed_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label garage_car_mom_mall_outing:
    scene location_car_cutscene01
    show text _ ("So we hopped in the car and made our way to the mall.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("I found that time passed quickly when I was with {b}[deb_name]{/b}...") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("... Her pleasant company and infectious smile never failed to brighten my mood.") as caption with dissolve
    pause

    scene black with dissolve
    return

label garage_car_mom_check_car:
    show anon f_worried with dissolve
    anon @ -m_talk "( She's right. The car doesn't want to start. )"

    anon @ -m_talk "( I'd better check the engine. )"

    if game.timer.is_dark():
        anon @ -m_talk "( It sure is dark in here. )"

    return

label garage_car_seen:
    show anon f_thinking with dissolve
    anon @ -m_talk "Hmm..."

    anon "I don't need to use {b}[deb_name]{/b}'s car."

    hide anon with dissolve
    return

label garage_car_not_seen:
    show anon with dissolve
    anon "{b}[deb_name]{/b}'s car... Wish I had a reason to drive it..."

    hide anon with dissolve
    return

label engine_broken:
    call expression game.dialog_select("engine_broken_dialogue")
    $ M_debbie.trigger(T_debbie_check_engine)
    $ player.go_to(L_home_garage)
    $ game.main()
    return

label engine_broken_dialogue:
    scene expression background(512, 400, 1.6, l=L_home_garage) as stage
    show anon f_surprised with dissolve
    anon @ -m_talk "( !!! )"
    anon @ -m_talk "( What the hell?! It looks like someone worked it over with a hammer! )"

    pause
    anon @ a_thinking f_thinking -m_talk "( Who could have- )"

    anon f_worried @ -m_talk "( Oh, man... I bet those Russian assholes did this! )"

    anon @ -m_talk "( {i}*Sigh*{/i} There's no way I can fix this! )"

    anon f_sad_down @ -m_talk "( We'll have to take it to a mechanic. )"

    anon @ -m_talk "( I should probably {b}let [deb_name] know the bad news{/b}... )"

    hide anon with dissolve
    return

label lawnmower_dialogue:
    $ player.go_to(L_home_garage)
    if M_debbie.is_state(S_debbie_fill_mower) and not player.has_item("gas_can"):
        if not game.timer.is_dark():
            call expression game.dialog_select("garage_mom_fill_mower_no_gas")
        else:
            call expression game.dialog_select("garage_mom_fill_mower_night")

    elif M_debbie.is_state(S_debbie_fill_mower) and player.has_item("gas_can"):
        if not game.timer.is_dark():
            call expression game.dialog_select("garage_mom_fill_mower_success")

            $ player.remove_item("gas_can")
            $ M_debbie.trigger(T_debbie_filled_mower)
            jump expression game.dialog_select("home_front_dialogue")
        else:

            call expression game.dialog_select("garage_mom_fill_mower_night")
    else:
        call expression game.dialog_select("garage_lawnmower_not_needed")
    $ game.main()

label garage_mom_fill_mower_night:
    scene expression game.timer.image("home_garage{}")
    show anon f_thinking with dissolve
    anon @ -m_talk "( Why would I use the lawn mower at night? I should return during the day... )"

    hide anon with dissolve
    return

label garage_mom_fill_mower_no_gas:
    scene home_garage_closeup
    show player 428f at right
    player_name "( I haven't used a lawn mower in years... Do I even remember how to use one? )"

    player_name "( {b}Dad{/b} used to pull the cord and it would start. Let me try that. )"

    scene home_garage_closeup
    show player 197
    with dissolve
    pause
    show player 200 at Position (xpos=566)
    pause
    show player 197 at center
    scene home_garage
    show player 35f
    with dissolve
    player_name "( It must be out of gas. It barely started, so at least I know it's running. )"

    show player 2f
    player_name "( Well it's not going to start without gas. I should probably {b}get some from Consum-R{/b}. )"

    return

label garage_mom_fill_mower_success:
    scene home_garage_closeup
    show player 202 at Position (xpos=521) with dissolve
    player_name "( I finally have some gas for the mower. )"

    show player 201 at Position (xpos=509)
    player_name "( That should be enough. )"

    show player 196 at Position (xpos=521)
    player_name "Hope this works. I don't know what else to do after this..."

    show player 197 at center
    pause
    show player 200 at Position (xpos=566)
    pause
    show player 197 at center
    pause
    show player 200 at Position (xpos=566)
    pause
    show player 199 at center
    player_name "Hmm... It's not working. I'll try pulling it a bit harder..."

    show player 200 at Position (xpos=566)
    pause
    show player 198 at center
    player_name "It worked!"

    return

label garage_lawnmower_not_needed:
    scene expression game.timer.image("home_garage{}")
    show anon f_thinking with dissolve
    anon @ -m_talk "( Why would I use the lawn mower? The grass looks fine... )"

    hide anon with dissolve
    return

label garage_use_workbench_night:
    scene expression player.location.background_blur
    show player 3 with dissolve
    player_name "( Damn! I can't see a thing! )"

    show player 4 with dissolve
    player_name "( And the light fixture is broken! )"

    player_name "( I should come back and work on this during the {b}day{/b}... )"

    hide player with dissolve
    return

label garage_dewitt_drill:
    call expression game.dialog_select("garage_dewitt_drill_dialogue")
    $ player.get_item("drill")
    $ game.main()

label garage_dewitt_drill_dialogue:
    scene expression game.timer.image("home_garage{}")
    show player 14 with dissolve
    player_name "Here is an old drill!"

    player_name "The batteries are still charged too."

    show player 12
    player_name "Now, I just need to {b}look for a fallen tree branch{/b}."

    hide player with dissolve
    return

label garage_dewitt_make_new_flute:
    scene home_garage_cs1
    show text _ ("You know, it was oddly satisfying, building this flute by hand.\nI'm actually pretty excited to play this thing now!") as caption
    with fade
    pause

    scene expression game.timer.image("home_garage{}")
    show player 566
    with fade
    player_name "Di sana!"

    player_name "Doesn't look all that bad!"

    show player 567
    pause
    show player 566
    player_name "Let's see what it does when I put my lips on it and blow..."

    show player 567d with dissolve
    pause
    show player 566 with dissolve
    player_name "Hey, this thing sounds pretty good!"

    player_name "I bet {b}Miss Dewitt{/b} is gonna freak out when she sees I built a flute from scratch!"

    hide player with dissolve
    return

label garage_dewitt_find_paint:
    scene expression game.timer.image("home_garage{}")
    show player 32 at Position (xoffset=68) with dissolve
    player_name "I don't see any paint in here..."

    pause
    show player 10 with dissolve
    player_name "Maybe {b}[deb_name]{/b} knows where it went."

    hide player with dissolve
    return

label garage_dewitt_make_replacement_guitar:
    scene home_garage_cs2
    show text _ ("You know, I'm really starting to dig all this woodworking.\nPerhaps I should look into becoming a carpenter someday.") as caption
    with fade
    pause

    scene expression game.timer.image("home_garage{}")
    show player 575
    with fade
    player_name "Yikes! Then again, maybe I'm not as talented as I thought."

    player_name "I hope this is good enough to fool {b}Mrs. Johnson{/b}."

    hide player with dissolve
    return

label garage_build_easels:
    scene location_home_garage_cutscene03
    show text _ ("Yeah, I think that looks right.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("I hope {b}Miss Ross{/b} likes it!") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("I really don't want to let her down...") as caption with dissolve
    pause

    scene black with dissolve
    return

label garage_workbench_not_needed:
    scene expression game.timer.image("home_garage{}")
    show anon f_worried with dissolve
    anon @ -m_talk "( I have no reason to use this right now. )"

    hide anon with dissolve
    return

label debbie_car_sex_pre:
    scene car_interior
    show player car 2d
    show player_arms car 1
    show old_debbie car 4 at right
    show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_debbie) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
    show xtra 30 at right
    with dissolve
    return

label debbie_car_sex_pre_first_time:
    pause
    show old_debbie car 4b
    debbie "You know, I really wasn't expecting you to bring me to the car."

    show old_debbie car 5g
    debbie "I was skeptical at first but now that we're sitting here..."

    show player car 3
    debbie "... It's kinda turning me on."

    debbie "Imagine if we were parked out in public somewhere?!"

    debbie "Hmm..."

    debbie "I'm getting wet just thinking about it!"

    show old_debbie car 5f
    show player car 4g
    player_name "I'd be down to try something like that..."

    show player car 5
    player_name "... You wouldn't be embarrassed?"

    show player car 5b
    show old_debbie car 5c
    show debbie_arms_car 5 at Position(xalign = 0.357, yalign = 0.558)

    debbie "..."
    show old_debbie car 5g
    debbie "Heh, I dunno... I would probably be mortified if we got caught!"

    debbie "... But..."

    debbie "... That's what makes it so exciting, you know?!"

    debbie "Well, at least it gets me excited..."

    debbie "I'm getting wet just thinking about it!"

    show old_debbie car 5f
    show player car 4h
    player_name "..."
    show player car 5
    player_name "You are?"

    show player car 5b
    show old_debbie car 3b
    debbie "Hehe, ya..."

    debbie "So, what are we gonna do about this big, hard cock here?"

    show old_debbie car 3
    show player car 2d
    return

label debbie_car_sex_pre_repeat:
    show old_debbie car 4b
    show debbie_arms_car 5c at Position(xalign = 0.357, yalign = 0.558)
    debbie "I like feeling this big guy stiffen up in my hand."

    show old_debbie car 4
    pause
    show player car 4b
    show old_debbie car 3b
    show debbie_arms_car 5 with dissolve
    debbie "Young cocks sure do get hard fast."

    show old_debbie car 4
    pause
    show player car 2d
    show old_debbie car 5b with dissolve
    debbie "It looks so... Delicious!"

    show old_debbie car 3b
    debbie "Want me to take you in my mouth?"

    show old_debbie car 3
    return

label debbie_car_sex_jerk_off:
    show player car 2c
    player_name "Just keep doing what you're doing!"

    show player car 2d
    show old_debbie car 3b
    debbie "Alright, sweetie."

    show old_debbie car 4
    return

label debbie_car_sex_bj:
    show player car 2c
    player_name "Would you... Use your mouth?"

    show player car 2d
    show old_debbie car 3b
    debbie "Sangat!"

    scene car_interior bj
    show player car 4c
    show player_arms car 1
    show debbie_car_bj 11 at right
    show xtra 30 zorder 2 at right
    with dissolve
    pause
    show debbie_car_bj 12 with dissolve
    pause
    show debbie_car_bj 7
    show player_boner car 3
    with dissolve
    pause
    hide player_boner
    show debbie_car_bj 8 zorder 1 at Position(xalign = 0.93, yalign = 1.0)
    with dissolve
    pause
    show player car 4c
    return

label debbie_car_sex_leave:
    show player car 5
    player_name "I think I'm good for now."

    player_name "That felt good."

    show player car 5b
    show old_debbie car 5g
    debbie "Benar-benar?"

    debbie "But you haven't even cum yet?"

    show old_debbie car 5f
    show player car 2
    player_name "Tidak apa-apa."

    show player car 5b
    show old_debbie car 5g
    debbie "Did I do something wrong?"

    show old_debbie car 5f
    show player car 2c
    player_name "It was good {b}[deb_name]{/b}! Don't worry."

    player_name "I have to get going is all."

    show player car 5b
    debbie "..."
    show old_debbie car 5g
    debbie "Baiklah..."

    return

label debbie_car_sex:
    $ M_debbie.set("sex speed", .175)
    $ animated = False
    call expression game.dialog_select("debbie_car_sex_pre")
    if not M_debbie.is_set("car sex"):
        call expression game.dialog_select("debbie_car_sex_pre_first_time")
        $ M_debbie.set("car sex", True)
    else:

        call expression game.dialog_select("debbie_car_sex_pre_repeat")
    menu:
        "Jerk me off.":
            $ M_debbie.set("car jerk", True)
            call expression game.dialog_select("debbie_car_sex_jerk_off")
            jump expression game.dialog_select("car_mom_sex_loop")
        "Seks oral.":

            $ M_debbie.set("car jerk", False)
            call expression game.dialog_select("debbie_car_sex_bj")
            jump expression game.dialog_select("car_mom_sex_loop")

        "Pergi." if store._in_replay == None:
            call expression game.dialog_select("debbie_car_sex_leave")
    scene black with fade
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["05_unlocked"] = True
    $ player.go_to(L_home_garage)
    $ game.timer.tick()
    $ game.main()

label car_mom_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_debbie.is_set("car jerk"):
                    show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_debbie) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
                else:
                    show expression AnimatedImage("debbie_car_bj", [8,"8b","8c","8d","8e","8f","8g"], M_debbie) as debbie_car_bj zorder 1 at Position(xalign = 0.93, yalign = 1.0)
                $ animated = True
            pause 4
            if animcounter in [1,3]:
                call expression game.dialog_select("car_mom_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            if M_debbie.is_set("car jerk"):
                $ pose_list = [5,"5b","5c","5b"]
            else:
                $ pose_list = [8,"8b","8c","8d","8e","8f","8g"]
            $ poses_done = []
            while poses_done != pose_list:
                if M_debbie.is_set("car jerk"):
                    show expression "debbie_arms_car {}".format(pose_list[pose_counter]) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
                else:
                    show expression "debbie_car_bj {}".format(pose_list[pose_counter]) as debbie_car_bj zorder 1 at Position(xalign = 0.93, yalign = 1.0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("car_mom_hscene_dialog")
        $ animcounter += 1
    call screen car_mom_sex_options

label car_mom_hscene_dialog:
    if M_debbie.is_set("car jerk"):
        if animcounter == 3:
            if randomizer() <= 50:
                show old_debbie car 4b
                show player car 5b
                debbie "I can't believe your cock is so big!{p=2}{nw}"

                debbie "I love how soft it feels.{p=2}{nw}"

                show old_debbie car 4
            else:

                show old_debbie car 5b
                show player car 5b
                debbie "I just love your big cock!{p=2}{nw}"

                debbie "Cum for me, {b}[firstname]{/b}!{p=2}{nw}"

                show player car 4b
                pause 1
                show old_debbie car 4
                show player car 4c
                player_name "Okay...{p=2}{nw}"

                show player car 4h
    else:
        if animcounter == 1:
            debbie "Mmmm...{p=1}{nw}"


        elif animcounter == 3:
            player_name "Oh...{p=1}{nw}"

            show player car 4d
            player_name "Right there, {b}[deb_name]{/b}.{p=2}{nw}"

            show player car 4c
    return

label car_mom_faster_dialogue:
    show player car 4c
    player_name "Faster, {b}[deb_name]{/b}."

    show player car 4h
    jump expression game.dialog_select("car_mom_sex_loop")

label car_mom_slower_dialogue:
    show player car 4c
    player_name "Go slower..."

    show player car 4h
    jump expression game.dialog_select("car_mom_sex_loop")

label car_mom_sex_cum:
    if M_debbie.is_set("car jerk"):
        call expression game.dialog_select("car_mom_jerk_cum")
    else:
        call expression game.dialog_select("car_mom_bj_cum")
    scene black with fade
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["05_unlocked"] = True
    $ player.go_to(L_home_garage)
    $ game.timer.tick()
    $ game.main()

label car_mom_jerk_cum:
    show player car 4c
    pause
    show player car 4d
    show player_arms car 2
    show debbie_arms_car 5d at Position(xalign = 0.357, yalign = 0.558)
    with dissolve
    player_name "( !!! )"
    show old_debbie car 4b
    debbie "Whoa!!!"

    show old_debbie car 5b
    debbie "Oh, sweetie!"

    show player car 2b
    show player_arms car 1 with dissolve
    debbie "I always forget just how big your loads are!"

    show old_debbie car 4b
    debbie "At least we didn't get any on the car..."

    show old_debbie car 3
    show player car 2c
    player_name "That was great..."

    scene car_interior kiss
    show old_debbie car 6 at right
    show player_boner car 1b
    show xtra 30 at right
    with dissolve
    pause
    scene car_interior
    show player car 2c
    show player_arms car 1
    show player_boner car 1b
    show old_debbie car 3 at right
    show debbie_arms_car 1
    show xtra 30 at right
    with dissolve
    player_name "Terima kasih, {b}[deb_name]{/b}."

    show player car 2d
    show old_debbie car 3b
    debbie "You're welcome, sweetie."

    show old_debbie car 4b
    debbie "Let's head back inside before {b}[jen_name]{/b} starts wondering where we snuck off to."

    show old_debbie car 3b
    debbie "I don't want her to find out what we're doing out here!"

    return

label car_mom_bj_cum:
    show player_arms car 2
    show player car 4d
    player_name "{b}[deb_name]{/b}, I'm gonna..."

    player_name "( !!! )"
    show debbie_car_bj 9
    show player_arms car 2
    with flash
    debbie "Mmmmph!!"

    scene car_interior
    show player car 4d
    show player_arms car 1
    show player_boner car 2
    show debbie_car_bj 10 at right
    show xtra 30 at right
    with dissolve
    pause
    show player car 2d
    debbie "{i}*Meneguk*{/i}"

    debbie "... {i}*Gulp*{/i}"

    show old_debbie car 2 at right
    hide debbie_arms_car
    hide debbie_car_bj
    show debbie_arms_car 1
    hide xtra
    show xtra 30 at right
    with dissolve
    pause
    show old_debbie car 3b
    debbie "Wow! That was so much!"

    debbie "Phew... I guess I won't have much of an appetite at dinner tonight."

    show old_debbie car 3
    show player car 2c
    player_name "That was awesome! You're so good at that!"

    show player car 2d
    show old_debbie car 3b
    debbie "Hehe, well, I'm glad you enjoy it, {b}[firstname]{/b}. 'Cause I love sucking your cock!"

    show old_debbie car 3b
    debbie "Let's head back inside before {b}[jen_name]{/b} starts wondering where we snuck off to."

    show old_debbie car 3
    show player car 5
    player_name "Baiklah."

    player_name "Just let me clean myself up first..."

    show player car 3
    show old_debbie car 3b
    debbie "I'll see you in there, sweetie!"

    show player car 5b
    show old_debbie car 4b
    debbie "Don't take too long..."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

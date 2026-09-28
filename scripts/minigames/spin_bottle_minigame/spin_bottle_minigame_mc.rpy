label spin_bottle_minigame_mc:
    if M_roxxy.get("roxxy locker sex"):
        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_roxxy")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_missy")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_becca")
            call expression game.dialog_select("spin_bottle_minigame_final_spin")

        elif M_player.get("beach bottle spins") == 4:
            if not M_player.get("mc beach sex"):
                call expression game.dialog_select("spin_bottle_minigame_mc_4some_intro_pre_first")
            else:
                call expression game.dialog_select("spin_bottle_minigame_mc_4some_intro_pre_repeat")
            $ anim_toggle = True
            $ animated = False
            $ M_roxxy.set("sex speed", .09)
            $ M_missy.set("sex speed", .09)
            $ M_becca.set("sex speed", .09)
            $ M_player.set("left of 4some", M_becca)
            call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_roxxy")
            call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop") pass (character_machine=M_roxxy)
    else:

        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_roxxy")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_missy")
            call expression game.dialog_select("spin_bottle_minigame_last_spin")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_becca")
            $ game.timer.tick()
            $ game.main()
    call screen spin_bottle_minigame

label beach_mc_4some_roxxy_replay:
    call expression game.dialog_select("beach_mc_4some_dialogue_replay")
    $ M_player.set("left of 4some", M_becca)
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_roxxy")
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop") pass (character_machine=M_roxxy)

label beach_mc_4some_missy_replay:
    call expression game.dialog_select("beach_mc_4some_dialogue_replay")
    $ M_player.set("left of 4some", M_roxxy)
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_missy")
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop") pass (character_machine=M_missy)

label beach_mc_4some_becca_replay:
    call expression game.dialog_select("beach_mc_4some_dialogue_replay")
    $ M_player.set("left of 4some", M_missy)
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_becca")
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop") pass (character_machine=M_becca)

label beach_mc_4some_dialogue_replay:
    $ game.timer.tick(2)
    call expression game.dialog_select("beach_mc_4some_dialogue_replay_intro")
    call expression game.dialog_select("button_roxxy_beach_spin_bottle")
    call expression game.dialog_select("button_roxxy_beach_spin_bottle_sex_repeat")
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_intro_pre_repeat")
    $ anim_toggle = True
    $ animated = False
    $ M_roxxy.set("sex speed", .09)
    $ M_missy.set("sex speed", .09)
    $ M_becca.set("sex speed", .09)
    return

label beach_mc_4some_dialogue_replay_intro:
    scene expression game.timer.image("backgrounds/location_beach_water{}_blur.jpg")
    show player 13f at right
    show old_becca bikini 9 at Position (xpos=315)
    show old_missy bikini 2 at left
    show old_roxxy bikini 1f at Position (xpos=500)
    with dissolve
    return

label spin_bottle_minigame_mc_4some_intro_pre_first:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show old_roxxy sitting 2 zorder 1 at right
    show old_becca sitting 8b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show old_missy sitting 6b at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    missy "Whoa, wait a second..."
    missy "What happens now?"
    show old_missy sitting 6
    show old_becca sitting 8c
    becca "Yeah, I never even thought about it landing on {b}[firstname]{/b}..."
    show old_becca sitting 8b
    show player_sitting 3b
    show old_roxxy sitting 3
    roxxy "Oh, well, this means {b}[firstname]{/b} wins."
    show old_roxxy sitting 2
    show old_becca sitting 7
    becca "Huh?"
    show old_becca sitting 8
    show player_sitting 3
    show old_missy sitting 3
    missy "So what, he is taking himself to the changing room for a special reward?"
    show old_missy sitting 2
    show old_becca sitting 5
    show old_roxxy sitting 5
    roxxy "Hahaha, nope."
    show old_roxxy sitting 3
    show player_sitting 3b
    roxxy "This means we're all going!"
    show old_roxxy sitting 2
    show player_sitting 5
    show old_becca sitting 8b
    becca "!!!"
    show old_missy sitting 6b
    missy "Seriously?!"
    show old_missy sitting 6
    show old_roxxy sitting 3
    roxxy "Yup!"
    show old_roxxy sitting 2
    show old_becca sitting 9
    becca "..."
    show old_missy sitting 5
    missy "AWESOME!"
    player_name "..."
    show player_sitting 3b
    show old_roxxy sitting 3
    roxxy "You're going to love this, {b}[firstname]{/b}."
    show old_roxxy sitting 2
    show player_sitting 3
    show old_becca sitting 8
    show old_missy sitting 3
    missy "Look how nervous {b}Becca{/b} is!!"
    show old_missy sitting 5
    show old_becca sitting 8b
    missy "Hahaha!"
    show old_becca sitting 8
    show old_roxxy sitting 5
    roxxy "Hahaha!"
    show old_becca sitting 7b
    becca "Shut up, skanks!"
    hide old_becca
    hide old_missy
    hide old_roxxy
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show old_becca bikini 20 at right
    show old_roxxy bikini 27 at Position (xpos=400)
    with dissolve
    roxxy "Are you ready for this, {b}[firstname]{/b}?"
    hide old_roxxy
    hide old_becca
    with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 10 at left
    show old_roxxy bikini 5 at right
    show old_becca bikini 1 at Position (xpos=575)
    show old_missy bikini 1 at Position (xpos=375)
    with dissolve
    player_name "So, are we going to-"
    show old_roxxy bikini 6 with dissolve
    show player 428
    player_name "!!!"
    show old_roxxy bikini 7 with dissolve
    pause .15
    show old_roxxy bikini 8 with dissolve
    pause .15
    show player 426
    show old_roxxy bikini 9 with dissolve
    pause .15
    show old_roxxy bikini usa 5 with dissolve
    pause .15
    show old_roxxy 22 with dissolve
    pause .15
    show old_roxxy 24 with dissolve
    roxxy "C'mon girls, time's wasting!"
    show old_roxxy 23
    show old_becca bikini 13
    show old_missy bikini 3 with dissolve
    pause .25
    show old_becca bikini 16
    show old_missy bikini 4 with dissolve
    pause .25
    show old_becca bikini 3
    show old_missy bikini 4b
    with dissolve
    pause .2
    show old_becca bikini 4
    show old_missy bikini 5
    with dissolve
    pause .15
    show old_becca bikini 5
    show old_missy bikini 7b
    with dissolve
    pause .15
    show old_becca bikini 5b
    show old_missy naked 1
    with dissolve
    pause .15
    show old_becca naked 1 with dissolve
    show player 427
    player_name "Okay, not that I'm complaining or anything..."
    show player 12
    player_name "... But what exactly is going on?!"
    show player 5
    show old_roxxy 24
    roxxy "We're going to be sharing you tonight."
    show old_roxxy 23
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "{i}*Gulp*{/i} Y-you mean-"
    show player 5
    show old_roxxy 24
    roxxy "That's right!"
    roxxy "Get undressed, {b}[firstname]{/b}."
    show old_roxxy 23
    player_name "..."
    show player 10
    player_name "Okay..."
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player 430 with dissolve
    pause
    hide player
    hide old_becca
    hide old_missy
    show old_roxxy 109 at center
    with dissolve
    roxxy "I'll start us off..."
    pause
    show old_roxxy 109c
    roxxy "Wanna make sure you all remember who's the {i}alpha bitch{/i} here!"
    hide old_roxxy with dissolve
    return

label spin_bottle_minigame_mc_4some_intro_pre_repeat:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show old_roxxy sitting 5 zorder 1 at right
    show old_becca sitting 8b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show old_missy sitting 6 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    roxxy "{b}[firstname]{/b} wins!"
    show player_sitting 3
    show old_roxxy sitting 2
    show old_missy sitting 2
    show old_becca sitting 3
    becca "That means we all go, right?"
    show old_becca sitting 2
    show old_roxxy sitting 3
    roxxy "That's right."
    show old_roxxy sitting 2
    show old_becca sitting 9
    show old_missy sitting 5
    missy "Yes!!!"
    player_name "..."
    show old_missy sitting 2
    show old_roxxy sitting 3
    show player_sitting 3b
    roxxy "You're going to love this, {b}[firstname]{/b}."
    show old_roxxy sitting 2
    show player_sitting 3
    show old_missy sitting 3
    missy "Look how nervous {b}Becca{/b} is!!"
    show old_missy sitting 5
    show old_becca sitting 8b
    missy "Hahaha!"
    show old_becca sitting 8
    show old_roxxy sitting 5
    roxxy "Hahaha!"
    show old_becca sitting 7b
    becca "Shut up, skanks!"
    hide old_roxxy
    hide old_missy
    hide old_becca
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show old_becca bikini 20 at right
    show old_roxxy bikini 27 at Position (xpos=400)
    with dissolve
    roxxy "Are you ready for this, {b}[firstname]{/b}?"
    hide old_roxxy
    hide old_becca
    with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 13 at left
    show old_roxxy bikini 5 at right
    show old_becca bikini 1 at Position (xpos=575)
    show old_missy bikini 1 at Position (xpos=375)
    with dissolve
    pause .15
    show old_roxxy bikini 6 with dissolve
    show player 426
    pause .15
    show old_roxxy bikini 7 with dissolve
    pause .15
    show old_roxxy bikini 8 with dissolve
    pause .15
    show old_roxxy bikini 9 with dissolve
    pause .15
    show old_roxxy bikini usa 5 with dissolve
    pause .15
    show old_roxxy 22 with dissolve
    pause .15
    show old_roxxy 24 with dissolve
    roxxy "C'mon girls, time's wasting!"
    show old_roxxy 23
    show old_becca bikini 13
    show old_missy bikini 3 with dissolve
    pause .25
    show old_becca bikini 16
    show old_missy bikini 4 with dissolve
    pause .25
    show old_becca bikini 3
    show old_missy bikini 4b
    with dissolve
    pause .2
    show old_becca bikini 4
    show old_missy bikini 5
    with dissolve
    pause .15
    show old_becca bikini 5
    show old_missy bikini 7b
    with dissolve
    pause .15
    show old_becca bikini 5b
    show old_missy naked 1
    with dissolve
    pause .15
    show old_becca naked 1 with dissolve
    show old_missy naked 2
    missy "Mmm, can I go first this time?!"
    show old_missy naked 1
    show old_becca naked 2
    becca "No, {b}Roxxy{/b} goes first. You know the rules!"
    show old_roxxy 24
    roxxy "That's right!"
    roxxy "Get undressed, {b}[firstname]{/b}."
    show old_roxxy 23
    show player 429
    player_name "Alright."
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player 430 with dissolve
    pause
    hide player
    hide old_becca
    hide old_missy
    show old_roxxy 109c at center
    with dissolve
    roxxy "I'll start us off..."
    pause
    roxxy "Wanna make sure you all remember who's the {i}alpha bitch{/i} here!"
    hide old_roxxy with dissolve
    return

label spin_bottle_minigame_mc_4some_loop_pre(current_character_machine, next_character_machine):
    $ anim_toggle = True
    $ animated = False
    $ M_roxxy.set("sex speed", .09)
    $ M_missy.set("sex speed", .09)
    $ M_becca.set("sex speed", .09)
    if current_character_machine == M_roxxy:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_from_roxxy")

    elif current_character_machine == M_missy:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_from_missy")

    elif current_character_machine == M_becca:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_from_becca")

    if next_character_machine == M_roxxy:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_to_roxxy")
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_roxxy")

    elif next_character_machine == M_missy:
        $ M_missy.once('taken_dick')
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_to_missy")
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_missy")

    elif next_character_machine == M_becca:
        $ M_becca.once('taken_dick')
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_to_becca")
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_becca")
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop") pass (character_machine=next_character_machine)

label spin_bottle_minigame_mc_4some_loop_pre_change_from_roxxy:
    show roxxys_beach 13 at Position (xalign = 0.5) with dissolve
    pause .4
    show roxxys_beach 11 with dissolve
    return

label spin_bottle_minigame_mc_4some_loop_pre_change_from_missy:
    show missys_beach 13 at Position (xalign = 0.5) with dissolve
    pause .4
    show missys_beach 11 with dissolve
    return

label spin_bottle_minigame_mc_4some_loop_pre_change_from_becca:
    show beccas_beach 13 at Position (xalign = 0.7) with dissolve
    pause .4
    show beccas_beach 11 with dissolve
    return

label spin_bottle_minigame_mc_4some_loop_pre_change_to_roxxy:
    player_name "Alright, {b}Roxxy{/b}. Ready for another round?"
    roxxy "Oh, I'm always ready for you, {b}[firstname]{/b}."
    return

label spin_bottle_minigame_mc_4some_loop_pre_change_to_missy:
    player_name "Alright, {b}Missy{/b}, your turn."
    missy "Yes, finally!"
    return

label spin_bottle_minigame_mc_4some_loop_pre_change_to_becca:
    player_name "{b}Becca{/b}, you want a turn?"
    becca "Y-yeah... Okay."
    return

label spin_bottle_minigame_mc_4some_loop_pre_roxxy:
    scene expression "backgrounds/location_beach_cabin_sex_foursome.jpg"
    if M_player.get("left of 4some") == M_becca:
        show beccas_beach_side at Position (xpos = 50)
        show missys_beach_side at Position (xpos = 925)
    else:

        show missys_beach_sidef at Position (xpos = 150)
        show beccas_beach_sidef at Position (xpos = 975)
    show roxxys_beach 12 at Position (xalign = 0.5)
    with dissolve
    roxxy "Now pay close attention, girls..."
    roxxy "I'll show you how it's done!"
    show roxxys_beach 11
    missy "Can you really take the entire thing?"
    show roxxys_beach 13 with dissolve
    roxxy "Heh, yeah. It's a piece of ca-"
    show roxxys_beach 14
    roxxy "-aaAAAAKE!" with hpunch
    show expression AnimatedImage("roxxys_beach", [1,2,3,4,5,6,7,8,9,10], M_roxxy) as roxxys_beach at Position (xalign = 0.5)
    pause
    return

label spin_bottle_minigame_mc_4some_loop_pre_missy:
    scene expression "backgrounds/location_beach_cabin_sex_foursome.jpg"
    if M_player.get("left of 4some") == M_becca:
        show beccas_beach_side at Position (xpos = 50)
        show roxxys_beach_side at Position (xpos = 950)
    else:

        show roxxys_beach_sidef at Position (xpos = 50)
        show beccas_beach_sidef at Position (xpos = 975)
    show missys_beach 12 at Position (xalign = 0.5)
    with dissolve
    missy "I'm gonna blow your mind, {b}[firstname]{/b}!"
    show missys_beach 11
    becca "Hahah, yeah right!"
    becca "Like you have the first clue what you're doing..."
    show missys_beach 13 with dissolve
    missy "Hey shut up, I know exactly what I'm-"
    show missys_beach 14
    missy "{i}*Gasp*{/i}" with hpunch
    pause
    player_name "Oh, she's really tight!"
    show expression AnimatedImage("missys_beach", [1,2,3,4,5,6,7,8,9,10], M_missy) as missys_beach at Position (xalign = 0.5)
    pause
    return

label spin_bottle_minigame_mc_4some_loop_pre_becca:
    scene expression "backgrounds/location_beach_cabin_sex_foursome.jpg"
    if M_player.get("left of 4some") == M_roxxy:
        show roxxys_beach_sidef at Position (xpos = 50)
        show missys_beach_side at Position (xpos = 925)
    else:

        show missys_beach_sidef at Position (xpos = 150)
        show roxxys_beach_side at Position (xpos = 950)
    show beccas_beach 11 at Position (xalign = 0.7)
    with dissolve
    becca "Just be careful, I'm not used to something this big..."
    show beccas_beach 12
    roxxy "Oh please! Her pussy's so wet!"
    show beccas_beach 13 with dissolve
    roxxy "It's gonna slide right in."
    show beccas_beach 14
    becca "Haaah!" with hpunch
    roxxy "See..."
    becca "That's so fucking deep!"
    show expression AnimatedImage("beccas_beach", [1,2,3,4,5,6,7,8,9,10], M_becca) as beccas_beach at Position (xalign = 0.7)
    pause
    return

label spin_bottle_minigame_mc_4some_loop(character_machine):
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if character_machine == M_roxxy:
                    show expression AnimatedImage("roxxys_beach", [1,2,3,4,5,6,7,8,9,10], M_roxxy) as roxxys_beach at Position (xalign = 0.5)

                elif character_machine == M_missy:
                    show expression AnimatedImage("missys_beach", [1,2,3,4,5,6,7,8,9,10], M_missy) as missys_beach at Position (xalign = 0.5)

                elif character_machine == M_becca:
                    show expression AnimatedImage("beccas_beach", [1,2,3,4,5,6,7,8,9,10], M_becca) as beccas_beach at Position (xalign = 0.7)
                $ animated = True
            pause 5
            call expression game.dialog_select("spin_bottle_minigame_mc_4some_hscene_dialog") pass (character_machine=character_machine)
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                if character_machine == M_roxxy:
                    show expression "roxxys_beach {}".format(pose_list[pose_counter]) as roxxys_beach at Position (xalign = 0.5)

                elif character_machine == M_missy:
                    show expression "missys_beach {}".format(pose_list[pose_counter]) as missys_beach at Position (xalign = 0.5)

                elif character_machine == M_becca:
                    show expression "beccas_beach {}".format(pose_list[pose_counter]) as beccas_beach at Position (xalign = 0.3)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("spin_bottle_minigame_mc_4some_hscene_dialog") pass (character_machine=character_machine)
        $ animcounter += 1
    call screen spin_bottle_minigame_mc_4some_options(character_machine)

label spin_bottle_minigame_mc_4some_hscene_dialog(character_machine):
    if animcounter == 0:
        if randomizer() < 25:
            if character_machine == M_roxxy:
                roxxy "AAHHH! Fuck!{p=1}{nw}"
                missy "Haha!{p=1}{nw}"

            elif character_machine == M_missy:
                player_name "Ngghhh, holy crap!{p=2}{nw}"
                missy "Ohmygod, ohmygod, ohmygod!!!{p=1}{nw}"

            elif character_machine == M_becca:
                becca "Ahhh!{p=1}{nw}"
                missy "Wow, {b}Becca{/b} looks so cute when she's getting railed by that big dick...{p=3}{nw}"
                roxxy "I know, right?!{p=2}{nw}"
        else:

            if character_machine == M_missy:
                missy "It's so fucking thick!!{p=2}{nw}"

    elif animcounter == 1:
        if randomizer() < 25:
            if character_machine == M_roxxy:
                becca "Mmm, I love watching her tits bounce...{p=2}{nw}"
                missy "Yeah, it is kinda hypnotic.{p=2}{nw}"
                pause 1
                missy "Boingy, boingy, boingy!{p=1}{nw}"
                becca "Hahaha!{p=1}{nw}"
                roxxy "Oh, my god shut up!{p=2}{nw}"
                roxxy "I'm trying to enjoy th-{p=2}{nw}"
                if M_roxxy.get("sex speed") > .031:
                    $ M_roxxy.set("sex speed", M_roxxy.get("sex speed") - 0.03)
                roxxy "-iiIIISSS!!!{p=1}{nw}"

            elif character_machine == M_missy:
                roxxy "Harder, {b}[firstname]{/b}!{p=1}{nw}"
                roxxy "Fuck some smarts into that dumb bitch!{p=2}{nw}"
                if M_missy.get("sex speed") > .031:
                    $ M_missy.set("sex speed", M_missy.get("sex speed") - 0.03)
                missy "Oh, GOD!!{p=1}{nw}"
                becca "Wow, he's really giving it to her!{p=2}{nw}"
                roxxy "I know.{p=1}{nw}"
                roxxy "My man is a monster in the sack!{p=2}{nw}"

            elif character_machine == M_becca:
                becca "Oh my god, this is so good!{p=2}{nw}"
                roxxy "C'mon {b}[firstname]{/b}, do it harder!{p=2}{nw}"
                missy "Yeah, fuck those dumb freckles off her face!{p=2}{nw}"
                becca "Shut up, {b}Missy{/b}!{p=2}{nw}"
                if M_becca.get("sex speed") > .031:
                    $ M_becca.set("sex speed", M_becca.get("sex speed") - 0.03)
                becca "AAAHHHH!!!{p=1}{nw}"
                pause 1
                roxxy "Yeah, that's more like it!{p=2}{nw}"

    elif animcounter == 2:
        if randomizer() < 25:
            if character_machine == M_roxxy:
                roxxy "Holy shit!{p=1}{nw}"

            elif character_machine == M_missy:
                missy "I'm-{p=1}{nw}"
                missy "AAAAHHH!!{p=1}{nw}"
                becca "Mmm, I can't believe how much this is turning me on...{p=2}{nw}"
                roxxy "I know, right?!{p=1}{nw}"

            elif character_machine == M_becca:
                becca "Haah! FUCK!!{p=1}{nw}"
                missy "Oh, she's getting close!{p=2}{nw}"

    elif animcounter == 3:
        if randomizer() < 25:
            if character_machine == M_roxxy:
                roxxy "I'm gonna cum!{p=1}{nw}"
                roxxy "Oh my god!{p=1}{nw}"
                roxxy "I'm gonna-{p=1}{nw}"
                pause 1
                roxxy "NGGHHH!!!{p=1}{nw}"

            elif character_machine == M_missy:
                missy "Nggghh!!{p=1}{nw}"
                missy "HAAAAAAAHHH!!!{p=1}{nw}"

            elif character_machine == M_becca:
                becca "AAAHHH!!{p=1}{nw}"
                becca "{i}*Whimper*{/i}{p=1}{nw}"
                pause 1
                roxxy "God, she's so fucking adorable when she cums!{p=2}{nw}"
    return

label spin_bottle_minigame_mc_4some_cum(character_machine):
    if character_machine == M_roxxy:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_roxxy_cum_dialogue")

    elif character_machine == M_missy:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_missy_cum_dialogue")

    elif character_machine == M_becca:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_becca_cum_dialogue")

    call expression game.dialog_select("spin_bottle_minigame_mc_4some_after_cum_dialogue")
    $ renpy.end_replay()
    if character_machine == M_roxxy:
        $ unlock_scene('Roxxy', '08_unlocked')
    elif character_machine == M_becca:
        $ unlock_scene('becca', '02_unlocked')
    elif character_machine == M_missy:
        $ unlock_scene('missy', '02_unlocked')
    $ M_player.machine_trigger(T_mc_beach_sex)
    $ game.timer.tick()
    $ game.main()

label spin_bottle_minigame_mc_4some_roxxy_cum_dialogue:
    player_name "{b}Roxxy{/b}, I'm getting close!"
    roxxy "Don't stop, {b}[firstname]{/b}!"
    roxxy "I want all of it inside me!"
    pause
    show roxxys_beach 14_15 at Position (xalign = 0.5)
    player_name "HNNGGG!!!" with flash
    roxxy "AAAHHHH!!!"
    show roxxys_beach 15
    show xray_roxxy_3some_beach at Position (align=(0,0))
    missy "Awesome!"
    pause
    hide xray_roxxy_3some_beach
    show roxxys_beach 16
    with dissolve
    roxxy "Oh my god that felt so good!"
    show roxxys_beach 17 with dissolve
    pause
    becca "Holy shit, look at that huge load!"
    missy "I'm so jelly right now..."
    return

label spin_bottle_minigame_mc_4some_missy_cum_dialogue:
    player_name "I'm gonna blow!"
    roxxy "Don't stop, {b}[firstname]{/b}."
    roxxy "Fill that dumb bitch up!"
    missy "Oh yess!!!"
    missy "Thank you, thank you, THANK YOU!!"
    pause
    show missys_beach 14_15 at Position (xalign = 0.5)
    player_name "HNNGGG!!!" with flash
    missy "{i}*Gasp*{/i}"
    show missys_beach 15
    show xray_missy_3some_beach at Position (align=(0,0))
    pause
    hide xray_missy_3some_beach
    show missys_beach 16
    with dissolve
    missy "Haah... Haah..."
    show missys_beach 17
    missy "That was epic!"
    show missys_beach 18
    becca "Yeah, he totally wrecked you!"
    roxxy "That was really hot..."
    return

label spin_bottle_minigame_mc_4some_becca_cum_dialogue:
    player_name "I can't hold it much longer..."
    becca "Oh, can I have it {b}Roxxy{/b}?!"
    becca "Please!"
    roxxy "{i}*Sigh*{/i} Alright, fine..."
    missy "Aww, but I wanted it!"
    roxxy "Shut up, {b}Missy{/b}!"
    pause
    player_name "Here it comes!"
    show beccas_beach 14_15 at Position (xalign = 0.7)
    player_name "HNNGGG!!!" with flash
    becca "{i}*Whimper*{/i}"
    show beccas_beach 15
    show xray_becca_3some_beach at Position (align=(0,0))
    pause
    hide xray_becca_3some_beach
    show beccas_beach 16
    with dissolve
    pause
    show beccas_beach 17 with dissolve
    becca "Oh my god, that was amazing..."
    show beccas_beach 18
    missy "Whoa, that's so much cum!"
    roxxy "You owe me big time, {b}Becca{/b}!"
    return

label spin_bottle_minigame_mc_4some_after_cum_dialogue:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 366f at right
    show old_becca naked 4 at Position (xpos=315)
    show old_roxxy 106 at Position (xpos=600)
    show old_missy naked 5 at left
    with dissolve
    missy "That was by far the coolest thing we've ever done!"
    show old_missy naked 4
    show old_becca naked 5
    becca "You are such a dork, {b}Missy{/b}..."
    show old_becca naked 4
    show old_missy naked 5
    missy "What?!"
    missy "I'm serious!"
    missy "We should totally do this again next week!"
    show old_missy naked 4
    becca "..."
    show old_roxxy 107
    roxxy "{i}*Sigh*{/i}"
    roxxy "We'll see..."
    show old_roxxy 106
    show old_missy naked 5
    missy "Yaaay!!!"
    show old_missy naked 4
    show old_becca naked 5
    becca "C'mon, stupid..."
    becca "Let's give these lovebirds some alone time."
    show old_becca naked 4
    missy "Hmm?"
    show old_missy naked 5
    missy "Oh..."
    missy "Okay."
    missy "Thanks for fucking us, {b}[firstname]{/b}!!!"
    show old_missy naked 4
    becca "!!!" with hpunch
    show old_missy naked 5
    missy "It was REALLY good!"
    missy "Byeee!!"
    hide old_missy with dissolve
    show old_becca naked 5
    becca "I..."
    becca "She shouldn't have..."
    show old_becca naked 4
    becca "..."
    show old_becca naked 5
    becca "Hehe, uhh..."
    becca "Bye {b}[firstname]{/b}."
    hide old_becca with dissolve
    show old_roxxy 108
    roxxy "Well, that was smooth..."
    show old_roxxy 106
    show player 365f
    player_name "I think they're adorable."
    show player 366f
    show old_roxxy 107f at Position (xpos=500) with dissolve
    roxxy "Yeah, but don't let them know that."
    roxxy "I trust you enjoyed that?"
    show old_roxxy 106f
    show player 365f
    player_name "Y-yeah!"
    show player 367f
    player_name "You sure you're okay with all this?"
    show player 368f
    show old_roxxy 107f
    roxxy "So long as it only happens when I'm present."
    show old_roxxy 108f
    roxxy "... Yeah!"
    show player 366f
    show old_roxxy 107f
    roxxy "I actually think it's REALLY sexy."
    roxxy "Watching you fuck them."
    show old_roxxy 106f
    show player 365f
    player_name "Wow, you're like the best girlfriend ever, {b}Roxxy{/b}!"
    show player 366f
    show old_roxxy 107f
    roxxy "I know, right?!"
    roxxy "Now, c'mon!"
    show old_roxxy 108f
    roxxy "I wanna go skinny dipping!"
    hide old_roxxy with dissolve
    show player 365f
    player_name "Heh, wait up!"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

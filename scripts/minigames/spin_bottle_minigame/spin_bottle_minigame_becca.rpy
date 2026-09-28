label spin_bottle_minigame_becca:
    if M_roxxy.get("roxxy locker sex"):
        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_becca")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_becca_missy")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_becca")
            call expression game.dialog_select("spin_bottle_minigame_final_spin")

        elif M_player.get("beach bottle spins") == 4:
            if not M_becca.get("becca beach sex"):
                call expression game.dialog_select("spin_bottle_minigame_becca_solo_intro_pre_first")
            else:
                call expression game.dialog_select("spin_bottle_minigame_becca_solo_intro_pre_repeat")
            call expression game.dialog_select("spin_bottle_minigame_becca_solo_intro")
            $ anim_toggle = True
            $ animated = False
            $ M_becca.set("sex speed", .09)
            $ M_becca.once('taken_dick')
            call expression game.dialog_select("spin_bottle_minigame_becca_solo_intro_after")
            jump expression game.dialog_select("spin_bottle_minigame_becca_solo_loop")
    else:

        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_becca")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_becca_missy")
            call expression game.dialog_select("spin_bottle_minigame_last_spin")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_becca")
            $ game.timer.tick()
            $ game.main()
    call screen spin_bottle_minigame

label beach_becca_solo_replay:
    $ M_player.set("beach bottle spins", 4)
    $ M_roxxy.set("roxxy locker sex", 1)
    jump expression game.dialog_select("spin_bottle_minigame_becca")

label spin_bottle_minigame_becca_solo_intro_pre_first:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show old_roxxy sitting 2 zorder 1 at right
    show old_becca sitting 8b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show old_missy sitting 6 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "!!!"
    show player_sitting 3
    show old_becca sitting 8
    show old_missy sitting 7
    missy "What?! NO!!"
    show old_missy sitting 8
    show old_becca sitting 8b
    show old_roxxy sitting 5
    roxxy "Hehe, looks like it's {b}Becca{/b}'s lucky night..."
    show old_roxxy sitting 2
    show old_becca sitting 8c
    becca "I don't-"
    show old_becca sitting 10b
    becca "I mean, are you-"
    show old_becca sitting 8b
    show old_roxxy sitting 3
    roxxy "Aww, look how shy she is..."
    show old_roxxy sitting 2
    show old_becca sitting 10b
    becca "I'm not!"
    show old_becca sitting 10
    show old_roxxy sitting 6
    roxxy "Isn't she just adorable?"
    show old_roxxy sitting 2
    show old_becca sitting 9
    becca "..."
    hide old_roxxy
    hide old_becca
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show old_roxxy bikini 26 with dissolve
    roxxy "You're going to like this..."
    hide old_roxxy with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 13 at left
    show old_roxxy bikini 22 at right
    show old_becca bikini 1
    with dissolve
    roxxy "I can't wait for you to fuck her adorable little brains out!"
    show old_roxxy bikini 21
    show player 11
    player_name "!!!" with hpunch
    show old_becca bikini 13
    show player 10
    player_name "Are you for real?!"
    show old_becca bikini 1
    show player 11
    roxxy "Mmmhmm..."
    show old_roxxy bikini 22
    roxxy "What did you think the special reward was?!"
    show old_roxxy bikini 21
    show player 29 with dissolve
    player_name "I dunno, more kissing?!"
    show player 3
    show old_becca bikini 15
    show old_roxxy bikini 23
    roxxy "Hahaha!"
    show old_roxxy bikini 22
    roxxy "C'mon, {b}Becca{/b}..."
    roxxy "Get that bikini off!"
    show old_roxxy bikini 21
    show old_becca bikini 6
    becca "I uhh..."
    show old_becca bikini 18
    becca "O-okay."
    show old_becca bikini 3 with dissolve
    pause
    show old_becca bikini 4 with dissolve
    pause
    show old_becca bikini 5
    show player 428
    with dissolve
    pause
    show old_becca bikini 5b with dissolve
    pause
    show old_becca naked 1 with dissolve
    player_name "..."
    show old_roxxy bikini 22
    roxxy "Daaamn!"
    show player 426
    roxxy "Isn't she sexy, {b}[firstname]{/b}?"
    show old_roxxy bikini 21
    show player 429
    player_name "Y-yeah..."
    show player 426
    show old_roxxy bikini 22
    roxxy "Don't you just wanna ravage her?!"
    show old_roxxy bikini 21
    show player 429
    player_name "Y-yeah..."
    show player 426
    show old_roxxy bikini 22
    roxxy "Hehehe!"
    roxxy "What about you, {b}Becca{/b}?!"
    roxxy "Don't you want it?"
    show old_roxxy bikini 21
    show old_becca naked 2
    becca "... Yes."
    show old_becca naked 1
    show old_roxxy bikini 23
    roxxy "C'mon, you can do better than that!"
    show old_roxxy bikini 22
    roxxy "I want you to beg for it!"
    show old_roxxy bikini 21
    show player 11
    show old_becca naked 3
    becca "!!!"
    becca "..."
    show old_becca naked 2
    becca "Please..."
    show old_becca naked 1
    show old_roxxy bikini 23
    roxxy "Please what?"
    show old_roxxy bikini 21
    show old_becca naked 2
    becca "Please, {b}Roxxy{/b}..."
    becca "I want {b}[firstname]{/b} to fuck me!"
    show old_becca naked 1
    show old_roxxy bikini 22
    roxxy "Hahaha!"
    roxxy "Alright."
    roxxy "Get over there and fuck her, {b}[firstname]{/b}!"
    show old_roxxy bikini 21
    show player 429
    player_name "O-okay..."
    hide player
    hide old_becca
    hide old_roxxy
    with dissolve
    return

label spin_bottle_minigame_becca_solo_intro_pre_repeat:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show old_roxxy sitting 2 zorder 1 at right
    show old_becca sitting 8b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show old_missy sitting 6 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "!!!"
    show player_sitting 3
    show old_missy sitting 7
    missy "What?! NO!!"
    show old_missy sitting 8
    show old_roxxy sitting 3
    show player_sitting 3b
    roxxy "Hehe, looks like it's {b}Becca{/b}'s lucky night..."
    show player_sitting 3
    show old_roxxy sitting 2
    show old_becca sitting 8c
    becca "I don't-"
    show old_becca sitting 10b
    becca "I mean, are you-"
    show old_becca sitting 8b
    show old_roxxy sitting 3
    roxxy "Aww, look how shy she is..."
    show old_roxxy sitting 2
    show old_becca sitting 8c
    becca "I'm not!"
    show old_becca sitting 9
    show old_roxxy sitting 6
    roxxy "Isn't she just adorable?"
    show old_roxxy sitting 2
    becca "..."
    hide old_becca
    hide old_roxxy
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show old_roxxy bikini 26 with dissolve
    roxxy "You're going to like this..."
    hide old_roxxy with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 13 at left
    show old_roxxy bikini 22 at right
    show old_becca bikini 1
    with dissolve
    roxxy "C'mon, {b}Becca{/b}..."
    roxxy "Get that bikini off!"
    show old_roxxy bikini 21
    show old_becca bikini 6
    becca "I uhh..."
    show old_becca bikini 18
    becca "O-okay."
    show old_becca bikini 3 with dissolve
    pause
    show old_becca bikini 4 with dissolve
    pause
    show old_becca bikini 5
    show player 428
    with dissolve
    pause
    show old_becca bikini 5b with dissolve
    pause
    show old_becca naked 1 with dissolve
    player_name "..."
    show old_roxxy bikini 22
    roxxy "Daaamn!"
    show player 426
    roxxy "Isn't she sexy, {b}[firstname]{/b}?"
    show old_roxxy bikini 21
    show player 429
    player_name "Y-yeah..."
    show player 426
    show old_roxxy bikini 22
    roxxy "Don't you just wanna ravage her?!"
    show old_roxxy bikini 21
    show player 429
    player_name "Y-yeah..."
    show player 426
    show old_roxxy bikini 22
    roxxy "Hehehe!"
    roxxy "What about you, {b}Becca{/b}?!"
    roxxy "Don't you want it?"
    show old_roxxy bikini 21
    show old_becca naked 2
    becca "... Yes."
    show old_becca naked 1
    show old_roxxy bikini 23
    roxxy "C'mon, you can do better than that!"
    show old_roxxy bikini 22
    roxxy "I want you to beg for it!"
    show old_roxxy bikini 21
    show player 11
    show old_becca naked 3
    becca "!!!"
    becca "..."
    show old_becca naked 2
    becca "Please..."
    show old_becca naked 1
    show old_roxxy bikini 23
    roxxy "Please what?"
    show old_roxxy bikini 21
    show old_becca naked 2
    becca "Please, {b}Roxxy{/b}..."
    becca "I want {b}[firstname]{/b} to fuck me!"
    show old_becca naked 1
    show old_roxxy bikini 22
    roxxy "Hahaha!"
    roxxy "Alright."
    roxxy "Get over there and fuck her, {b}[firstname]{/b}!"
    show old_roxxy bikini 21
    show player 429
    player_name "O-okay..."
    hide player
    hide old_becca
    hide old_roxxy
    with dissolve
    return

label spin_bottle_minigame_becca_solo_intro:
    scene expression "backgrounds/location_beach_cabin_sex_becca.jpg"
    show beccas_solo 1
    with dissolve
    pause
    show beccas_solo 2 with dissolve
    pause
    show beccas_solo 3
    becca "!!!" with hpunch
    becca "Holy shit!"
    roxxy "Hahaha!"
    roxxy "I know, right?!"
    becca "It's so big!"
    roxxy "C'mon, {b}[firstname]{/b}. She can take it!"
    show beccas_solo 4 with dissolve
    becca "AAhhh!!"
    return

label spin_bottle_minigame_becca_solo_intro_after:
    show expression AnimatedImage("beccas_solo", [7,8,9,10,11,12,13,14,15,16], M_becca) as beccas_solo
    with dissolve
    pause
    return

label spin_bottle_minigame_becca_solo_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("beccas_solo", [7,8,9,10,11,12,13,14,15,16], M_becca) as beccas_solo
                $ animated = True
            pause 5
            call expression game.dialog_select("spin_bottle_minigame_becca_solo_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [7,8,9,10,11,12,13,14,15,16]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "beccas_solo {}".format(pose_list[pose_counter]) as beccas_solo
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("spin_bottle_minigame_becca_solo_hscene_dialog")
        $ animcounter += 1
    call screen spin_bottle_minigame_solo_sex_options(M_becca)

label spin_bottle_minigame_becca_solo_hscene_dialog:
    if animcounter == 0:
        if randomizer() < 25:
            becca "Oh my god!{p=2}{nw}"
            becca "OH MY GOD!!{p=2}{nw}"
            roxxy "Hahaha!{p=1}{nw}"

    elif animcounter == 1:
        if randomizer() < 25:
            roxxy "That's it, {b}[firstname]{/b}!{p=2}{nw}"
            roxxy "Fuck her brains out!{p=2}{nw}"

    elif animcounter == 2:
        if randomizer() < 25:
            becca "AAAHH!!{p=1}{nw}"
            becca "I'm cumming!{p=1}{nw}"
            becca "{i}*Whimper*{/i}{p=1}{nw}"
            pause
            roxxy "Hahaha, that was fast!{p=2}{nw}"
            roxxy "She is making the most adorable faces!{p=2}{nw}"
            roxxy "Keep going, {b}[firstname]{/b}!{p=2}{nw}"

    elif animcounter == 3:
        if randomizer() < 25:
            becca "Ngghh!!{p=1}{nw}"
            pause 1
        else:

            becca "{i}*Whimper*{/i}{p=1}{nw}"
    return

label spin_bottle_minigame_becca_solo_cum:
    call expression game.dialog_select("spin_bottle_minigame_becca_solo_cum_dialogue")
    $ renpy.end_replay()
    $ unlock_scene('becca', '01_unlocked')
    $ M_becca.machine_trigger(T_becca_beach_sex)
    $ M_becca.trigger(T_bec00_solo)
    $ game.timer.tick()
    $ game.main()

label spin_bottle_minigame_becca_solo_cum_dialogue:
    player_name "I'm getting close!"
    becca "Finish inside me!"
    roxxy "Excuse me?!"
    becca "..."
    roxxy "That didn't sound like begging to me..."
    becca "{i}*Whimper*{/i}"
    pause
    becca "Ngghhh!!!"
    becca "Please, {b}Roxxy{/b}!!!"
    becca "AAhhh!!! Please, please, please!"
    roxxy "Hahaha!"
    roxxy "Alright, {b}[firstname]{/b}..."
    roxxy "Give it to her!"
    pause
    becca "OH MY GOD!!!"
    show beccas_solo 3_4
    player_name "HNNGGG!!!" with flash
    show beccas_solo 4
    show xray_becca_1o1_beach at Position (align=(0,0))
    pause
    hide xray_becca_1o1_beach
    show beccas_solo 5
    with dissolve
    player_name "Haaah... Haaah..."
    becca "{i}*Whimper*{/i}"
    show beccas_solo 6 with dissolve
    roxxy "Haha, wow you really did a number on her..."
    roxxy "That was so fucking hot!"

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 365 at left
    show old_becca naked 4
    show old_roxxy bikini 21 at right
    with dissolve
    player_name "You alright, {b}Becca{/b}?"
    show player 366
    show old_becca naked 5
    becca "Mmmhmm, I just can't... Exactly... Feel my legs..."
    show old_becca naked 4
    show old_roxxy bikini 22
    roxxy "Hehe, I think you exhausted her."
    show old_roxxy bikini 21
    pause
    show player 365
    player_name "I feel kinda bad for {b}Missy{/b}."
    player_name "Out there all by herself..."
    show player 366
    show old_roxxy bikini 23
    roxxy "Psh, screw that greedy bitch."
    roxxy "Besides, she's been at the door watching almost the entire time..."
    roxxy "Haven't you, {b}Missy{/b}?!"
    show old_roxxy bikini 21
    pause
    missy "... No."
    show old_roxxy bikini 2 with dissolve
    show player 365
    roxxy "Hahaha!"
    player_name "Hahaha!"
    hide player
    hide old_roxxy
    hide old_becca
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

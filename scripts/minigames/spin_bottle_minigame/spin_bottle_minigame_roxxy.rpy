label spin_bottle_minigame_roxxy:
    if M_roxxy.get("roxxy locker sex"):
        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_roxxy")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_missy")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_becca")
            call expression game.dialog_select("spin_bottle_minigame_final_spin")

        elif M_player.get("beach bottle spins") == 4:
            call expression game.dialog_select("spin_bottle_minigame_roxxy_solo_intro_pre")
            call expression game.dialog_select("spin_bottle_minigame_roxxy_solo_intro")
            $ anim_toggle = True
            $ animated = False
            $ M_roxxy.set("sex speed", .09)
            call expression game.dialog_select("spin_bottle_minigame_roxxy_solo_intro_after")
            jump expression game.dialog_select("spin_bottle_minigame_roxxy_solo_loop")
    else:

        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_roxxy")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_missy")
            call expression game.dialog_select("spin_bottle_minigame_last_spin")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_becca")
            $ game.timer.tick()
            $ game.main()
    call screen spin_bottle_minigame

label beach_roxxy_solo_replay:
    $ M_player.set("beach bottle spins", 4)
    $ M_roxxy.set("roxxy locker sex", 1)
    jump expression game.dialog_select("spin_bottle_minigame_roxxy")

label spin_bottle_minigame_roxxy_solo_intro_pre:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show old_roxxy sitting 2 zorder 1 at right
    show old_becca sitting 10 at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show old_missy sitting 7 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    missy "What?! NO!!"

    show player_sitting 3b
    show old_missy sitting 8
    show old_roxxy sitting 5
    roxxy "Hehe, sorry bitches."

    show old_roxxy sitting 3
    roxxy "He's all mine tonight."

    show old_roxxy sitting 2
    show player_sitting 3
    show old_becca sitting 10b
    becca "Aduh..."

    show old_becca sitting 10
    show old_missy sitting 7
    missy "Tidak bisakah kita-"

    show old_missy sitting 6
    show old_roxxy sitting 6
    show player_sitting 3b
    roxxy "NO!!!"

    show old_roxxy sitting 2
    show old_missy sitting 8
    missy "..."
    show old_missy sitting 7
    missy "This sucks!"

    hide old_roxxy
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show old_roxxy bikini 25 with dissolve
    roxxy "This way lucky..."

    hide old_roxxy with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 13 at left
    show old_roxxy bikini 22 at right
    with dissolve
    roxxy "I'm so glad I get you all to myself tonight."

    show old_roxxy bikini 21
    show player 14
    player_name "Heh, yeah. Me too."

    hide player
    show old_roxxy bikini 17 at left
    with dissolve
    pause
    show old_roxxy bikini 23 at center
    show player 13 at left
    with dissolve
    roxxy "Ugh, those bitches will probably be at the door watching us in a couple minutes."

    show old_roxxy bikini 21
    show player 14
    player_name "Well, we can take this back to your place if you want?"

    show player 13
    show old_roxxy bikini 1 with dissolve
    roxxy "..."
    show old_roxxy bikini 2
    roxxy "Nah, screw it!"

    show old_roxxy bikini 5 with dissolve
    show player 426
    pause
    show old_roxxy bikini 6 with dissolve
    pause
    show old_roxxy bikini 7 with dissolve
    pause
    show old_roxxy bikini 8 with dissolve
    pause
    show old_roxxy bikini 9 with dissolve
    pause
    show old_roxxy bikini usa 5 with dissolve
    pause
    show old_roxxy 22 with dissolve
    pause
    show old_roxxy 23b with dissolve
    roxxy "Let them watch."

    show old_roxxy 24
    show player 13
    roxxy "I want you right now!"

    show old_roxxy 23
    show player 14
    player_name "B-baiklah."

    hide player
    hide old_roxxy
    with dissolve
    return

label spin_bottle_minigame_roxxy_solo_intro:
    scene expression "backgrounds/location_beach_cabin_sex_roxxy.jpg"
    show roxxys_solo 1
    with dissolve
    roxxy "Mmm, berikan padaku {b}[firstname]{/b}..."

    show roxxys_solo 2 with dissolve
    pause
    show roxxys_solo 3 with dissolve
    roxxy "Aahhh..."

    return

label spin_bottle_minigame_roxxy_solo_intro_after:
    show expression AnimatedImage("roxxys_solo", [7,8,9,10,11,12,13,14,15,16], M_roxxy) as roxxys_solo
    with dissolve
    pause
    return

label spin_bottle_minigame_roxxy_solo_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("roxxys_solo", [7,8,9,10,11,12,13,14,15,16], M_roxxy) as roxxys_solo
                $ animated = True
            pause 5
            call expression game.dialog_select("spin_bottle_minigame_roxxy_solo_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [7,8,9,10,11,12,13,14,15,16]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "roxxys_solo {}".format(pose_list[pose_counter]) as roxxys_solo
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("spin_bottle_minigame_roxxy_solo_hscene_dialog")
        $ animcounter += 1
    call screen spin_bottle_minigame_solo_sex_options(M_roxxy)

label spin_bottle_minigame_roxxy_solo_hscene_dialog:
    if animcounter == 0:
        if randomizer() < 25:
            roxxy "Yes!!{p=1}{nw}"


    elif animcounter == 1:
        if randomizer() < 25:
            roxxy "Ohh, it's so deep!{p=2}{nw}"


    elif animcounter == 2:
        if randomizer() < 25:
            roxxy "Aaahhh!!{p=1}{nw}"

            roxxy "Oh god!{p=1}{nw}"


    elif animcounter == 3:
        if randomizer() < 25:
            roxxy "{b}[firstname]{/b}!!!{p=1}{nw}"

            pause 1
            roxxy "Oh, fuck me harder!{p=2}{nw}"

    return

label spin_bottle_minigame_roxxy_solo_cum:
    call expression game.dialog_select("spin_bottle_minigame_roxxy_solo_cum_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Roxxy"]["unlocked"] = True
    $ persistent.cookie_jar["Roxxy"]["gallery"]["07_unlocked"] = True
    $ M_roxxy.trigger(T_roxxy_beach_sex)
    $ game.timer.tick()
    $ game.main()

label spin_bottle_minigame_roxxy_solo_cum_dialogue:
    roxxy "aku akan keluar!"

    player_name "Ya, aku juga!"

    pause
    roxxy "Aahhh, FUCK!!!"

    show roxxys_solo 3_4
    player_name "HNNGGG!" with flash
    show roxxys_solo 4
    show xray_roxxy_1o1_beach at Position (align=(0,0))
    pause
    hide xray_roxxy_1o1_beach
    show roxxys_solo 5
    with dissolve
    player_name "Haaah... Haaah..."

    show roxxys_solo 6 with dissolve
    roxxy "Itu luar biasa!"

    player_name "Hehe, ya..."

    pause

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 366 at left
    show old_roxxy 108 at right
    with dissolve
    roxxy "Hehe, well, I bet that was quite a show!"

    show old_roxxy 107
    roxxy "I can barely stand..."

    show old_roxxy 106
    show player 365
    player_name "Yeah, you think they enjoyed it?"

    show player 366
    roxxy "Hmm..."

    show old_roxxy 107
    roxxy "What do you say, bitches? Did you enjoy that?"

    show old_roxxy 106
    pause
    scene expression "backgrounds/location_beach_cutscene06.jpg" with fade
    missy "Ya..."

    roxxy "Ha ha ha!"

    player_name "Ha ha ha!"

    hide player
    hide old_roxxy
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

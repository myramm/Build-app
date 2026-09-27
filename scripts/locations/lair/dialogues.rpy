label lair_aqua_lair:
    scene expression player.location.background_blur
    show player 25
    player_name "{i}*Cough*{/i} Oh man... I thought I was done for."

    show player 113
    pause
    show player 10
    player_name "Whoa, this place is spooky!"

    player_name "It's like something out of a comic book..."

    show player 113
    player_name "... Or one of {b}Erik{/b}'s computer games."

    show player 10
    player_name "..."
    show player 12
    player_name "... But that weird fish lady has to be here somewhere!"

    player_name "If she thinks she's keeping my lure, well, she's got another thing coming!"

    show player 16
    hide player with dissolve
    return

label seasucc_dialogue:
    scene lair_seasucc
    if M_aqua.is_state(S_aqua_seasucc_intro):
        call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_intro")
        $ M_aqua.trigger(T_aqua_seasucc)

    elif M_aqua.is_state(S_aqua_seasucc_mushroom) and not player.has_item("mushroom"):
        call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_no_mushroom")

    elif M_aqua.is_state(S_aqua_seasucc_mushroom) and player.has_item("mushroom"):
        $ player.remove_item("mushroom")
        call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_mushroom_intro")
        jump expression game.dialog_select("seasucc_loop")
    else:

        label aqua_succ_replay:
            call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_mushroom_repeat_intro")
        if not store._in_replay == None:
            jump expression game.dialog_select("succ_replay_jump")
        menu:
            "Ya.":
                label succ_replay_jump:
                    call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_mushroom_repeat_yes")
                jump expression game.dialog_select("seasucc_loop")
            "Tidak.":

                call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_mushroom_repeat_no")
    hide aqua
    hide player
    hide player_boner
    hide seasucc
    hide seasucc_bg_01
    hide seasucc_bg_02
    with dissolve
    $ game.main()

label seasucc_dialogue_aqua_seasucc_intro:
    show aqua 19
    show seasucc_bg_01
    show seasucc_bg_02
    show seasucc 1
    show player 10 at left
    with dissolve
    player_name "Hey, {b}Aqua{/b}?"

    show player 5
    show aqua 20
    aqua "Yesss?"

    show aqua 19
    show player 10
    player_name "Umm, what's this strange looking thing?"

    show player 5
    show aqua 20
    aqua "Is not thing. Is {b}SsseaSucc{/b}!"

    show aqua 19
    show player 12
    player_name "Hmm, and what does this {b}SeaSucc{/b} do?"

    show player 5
    show aqua 20
    aqua "It is used for giving pleasuresss."

    show aqua 19
    show player 12
    player_name "It gives you pleasure?"

    show player 5
    show aqua 20
    aqua "Yesss, it gives pleasure to all."

    show aqua 19
    show player 10
    player_name "So, {b}SeaSucc{/b} would give me pleasure, too?"

    show player 5
    show aqua 20
    aqua "Yesss, if you make friends."

    show aqua 19
    show player 10
    player_name "How do I make friends with a chair?"

    show player 5
    show aqua 20
    aqua "You must {b}feed it ssspecial food, Falicum mushroom{/b}. {b}Falicum{/b}."

    show aqua 19
    show player 12
    player_name "Feed it?"

    player_name "How do you feed a chair?"

    player_name "And I've never heard of {b}Falicum mushrooms{/b} before..."

    show player 10
    player_name "... Where can I find some?"

    show player 5
    show aqua 20
    aqua "It grows on land."

    aqua "{b}Deep in forest{/b}."

    aqua "{b}Aqua{/b} no like going there!"

    show aqua 19
    show player 12
    player_name "Hmm, in the {b}forest{/b}, huh?"

    show player 14
    player_name "I could go try and find some."

    show player 13
    show aqua 20
    aqua "Yesss, You go get {b}Falicum{/b}..."

    aqua "... Make friends with {b}SeaSucc{/b}."

    aqua "Then we enjoy pleasure together."

    return

label seasucc_dialogue_aqua_seasucc_no_mushroom:
    show aqua 19
    show seasucc_bg_01
    show seasucc_bg_02 zorder 1
    show seasucc 1 zorder 2
    show player 12 zorder 3 at left
    with dissolve
    player_name "What did you say {b}SeaSucc{/b} needed?"

    show player 5
    show aqua 20
    aqua "You must {b}feed it ssspecial food, Falicum mushroom{/b}... {b}Falicum{/b}!"

    show aqua 19
    show player 10
    player_name "Where can I find some?"

    show player 5
    show aqua 20
    aqua "It grows on land."

    aqua "{b}Deep in forest{/b}."

    show aqua 19
    show player 14
    player_name "Alright! I'll take a look."

    return

label seasucc_dialogue_aqua_seasucc_mushroom_intro:
    show aqua 19
    show seasucc_bg_01
    show seasucc_bg_02 zorder 1
    show seasucc 1 zorder 2
    show player 14 zorder 3 at left
    with dissolve
    player_name "{b}Aqua{/b}!"

    player_name "I think I found something."

    show player 239_240 with dissolve
    player_name "..."
    show player 500 with dissolve
    player_name "Melihat?"

    show player 499
    show aqua 20
    aqua "Yesss, you bring {b}Falicum{/b}!"

    show aqua 19
    show player 500
    player_name "Is this what {b}SeaSucc{/b} needs?"

    show player 499
    show aqua 20
    aqua "Yesss, {b}SeaSucc{/b} likes {b}Falicum{/b}."

    aqua "Sssit and feed."

    aqua "Become friendsss."

    show aqua 19
    show player 10 with dissolve
    player_name "Baiklah."

    hide player
    show player seasucc 1 zorder 3 with dissolve
    pause
    show aqua 21
    hide player
    show player seasucc 5 behind seasucc_bg_02
    show player_pants seasucc 2 behind seasucc_bg_02
    with dissolve
    pause
    show player seasucc 6 with dissolve
    pause
    show player seasucc 9 with dissolve
    player_name "Here you go {b}SeaSucc{/b}."

    show seasucc 2 with dissolve
    show player seasucc 8
    player_name "..."
    show seasucc 3
    show player seasucc 10
    with dissolve
    player_name "!!!" with hpunch
    show seasucc 4
    show player seasucc 5
    with dissolve
    show aqua 22
    aqua "Mmm, {b}SsseaSucc{/b} likesss {b}Falicum{/b}."

    show aqua 21
    show seasucc 1
    show player seasucc 7
    with dissolve
    player_name "You must have been really hungry!"

    show player seasucc 3 with dissolve
    show aqua 22
    aqua "You try {b}SeaSucc{/b} now, yesss?"

    show aqua 21
    show player seasucc 7 with dissolve
    player_name "Uhh, I just sit on it?"

    show player seasucc 5 with dissolve
    show aqua 22
    aqua "Yesss, Ssshow {b}SeaSucc{/b} big eel."

    show aqua 21
    show player seasucc 6 with dissolve
    player_name "..."
    show player seasucc 7
    player_name "Baiklah."

    hide player_pants
    show player seasucc 11 with dissolve
    pause
    show player seasucc 3
    show player_boner seasucc 2b
    with dissolve
    show aqua 25
    aqua "Ahh, good morning big eel."

    show aqua 21
    show seasucc 5
    show player seasucc 7
    with dissolve
    player_name "Are you sure this is-"

    show aqua 24
    show player seasucc 5
    show seasucc 6
    with dissolve
    pause
    show seasucc 7 with dissolve
    player_name "!!!"
    hide player_boner
    show seasucc 8 at Position(xalign = 0.35, yalign = 0.0)
    with dissolve
    pause
    show seasucc 8b
    pause
    show seasucc 8c
    pause
    show seasucc 8d
    pause
    show seasucc 8e
    show player seasucc 12
    player_name "Wah!"

    $ M_aqua.set("sex speed", 0.175)
    show expression AnimatedImage("seasucc", [8,"8b","8c","8d","8e","8f","8g","8h","8i"], M_aqua) as seasucc at Position(xalign = 0.35, yalign = 0.0)
    pause
    pause
    show player seasucc 13
    player_name "This feels amazing!!"

    show player seasucc 14
    show aqua 23
    aqua "Yesss, {b}SeaSucc{/b} gives best pleasuress!"

    show aqua 24
    pause
    return

label seasucc_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("seasucc", [8,"8b","8c","8d","8e","8f","8g","8h","8i"], M_aqua) as seasucc at Position(xalign = 0.35, yalign = 0.0)
                $ animated = True
            pause 4
            call expression game.dialog_select("seasucc_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [8,"8b","8c","8d","8e","8f","8g","8h","8i"]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "seasucc {}".format(pose_list[pose_counter]) as seasucc at Position(xalign = 0.35, yalign = 0.0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("seasucc_hscene_dialog")
        $ animcounter += 1
    call screen seasucc_options

label seasucc_hscene_dialog:
    if animcounter == 0:
        show player seasucc 13
        if randomizer() <= 50:
            player_name "Ohh...{p=1}{nw}"

        else:
            player_name "Uhh!{p=1}{nw}"

        show player seasucc 14
    elif animcounter == 2 and randomizer() <= 50:
        show aqua 23
        aqua "Sssuck {b}SsseaSucc{/b}!{p=2}{nw}"

        show aqua 24

    elif animcounter == 3 and randomizer() <= 50:
        show player seasucc 13
        pause 2
        show player seasucc 14
    return

label seasucc_cum:
    call expression game.dialog_select("seasucc_cum_pre")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Aqua"]["unlocked"] = True
    $ persistent.cookie_jar["Aqua"]["gallery"]["02_unlocked"] = True
    $ game.timer.tick()
    $ M_aqua.trigger(T_aqua_seasucc_fuck)
    $ game.main()

label seasucc_cum_pre:
    show player seasucc 13
    show aqua 23
    aqua "Give {b}SsseaSucc{/b} ssseeds."

    aqua "Cum for {b}SsseaSucc{/b}!!!"

    show aqua 24
    pause
    hide player
    hide seasucc
    show seasucc 9 behind seasucc_bg_02
    with flash
    pause
    show seasucc 3
    show player seasucc 14 behind seasucc_bg_02
    show player_boner seasucc 15 behind seasucc_bg_02
    with dissolve
    pause
    show seasucc 4 with dissolve
    pause
    show seasucc 1 with dissolve
    show player seasucc 3
    show aqua 25
    if M_aqua.is_state(S_aqua_seasucc_mushroom):
        aqua "Now that {b}SeaSucc{/b} taste mate ssseed, it remembersss."

        aqua "You friendsss now!"

        aqua "It give pleasure alwaysss."

        call popup ('scene', 'seasucc')
    else:
        aqua "{b}SsseaSucc{/b} likesss ssseed from big eel!"

    return

label seasucc_dialogue_aqua_seasucc_mushroom_repeat_intro:
    scene lair_seasucc
    show aqua 20
    show seasucc_bg_01
    show seasucc_bg_02 zorder 1
    show seasucc 1 zorder 2
    show player 13 zorder 3 at left
    with dissolve
    aqua "Back for moresss?"

    show aqua 19
    return

label seasucc_dialogue_aqua_seasucc_mushroom_repeat_yes:
    show player 4 with dissolve
    player_name "..."
    show player 26 with dissolve
    player_name "Ya."

    show player 13
    show aqua 20
    aqua "{b}SsseaSucc{/b} isss good!"

    aqua "Sssit and feed {b}SsseaSucc{/b}."

    show aqua 19
    hide player
    show player seasucc 1 zorder 3
    with dissolve
    pause
    show aqua 21
    hide player
    show player seasucc 5 behind seasucc_bg_02
    show player_pants seasucc 2 behind seasucc_bg_02
    with dissolve
    pause
    show aqua 22
    aqua "Ssshow {b}SsseaSucc{/b} big eel."

    show aqua 21
    hide player_pants
    show player seasucc 11 with dissolve
    pause
    show player seasucc 3
    show player_boner seasucc 2b
    with dissolve
    show aqua 25
    aqua "Ahh, good morning big eel."

    show aqua 21
    show seasucc 5
    with dissolve
    show aqua 24
    show player seasucc 5
    show seasucc 6
    with dissolve
    pause
    show seasucc 7 with dissolve
    player_name "!!!"
    hide player_boner
    show seasucc 8 at Position(xalign = 0.35, yalign = 0.0)
    with dissolve
    pause
    show seasucc 8b
    pause
    show seasucc 8c
    pause
    show seasucc 8d
    pause
    show seasucc 8e
    show player seasucc 12
    player_name "Wah!"

    $ M_aqua.set("sex speed", 0.175)
    show expression AnimatedImage("seasucc", [8,"8b","8c","8d","8e","8f","8g","8h","8i"], M_aqua) as seasucc at Position(xalign = 0.35, yalign = 0.0)
    pause
    pause
    show player seasucc 13
    player_name "This thing feels amazing!!"

    show player seasucc 14
    show aqua 23
    aqua "Yesss, {b}SeaSucc{/b} gives best pleasuress!"

    show aqua 24
    return

label seasucc_dialogue_aqua_seasucc_mushroom_repeat_no:
    show player 14
    player_name "Mungkin nanti."

    return

label aqua_lure_steal:
    call expression game.dialog_select("aqua_lure_steal_pre")
    $ player.remove_item("special_lure")
    $ M_aqua.trigger(T_aqua_lure_steal)
    label follow_aqua:
        call expression game.dialog_select("aqua_lure_steal_after")
    menu:
        "Dive!":
            call expression game.dialog_select("aqua_lure_steal_dive_pre")
            $ playSound()
            call expression game.dialog_select("aqua_lure_steal_dive_after")
            $ M_aqua.trigger(T_aqua_dive)

            call combat ('squid', gui=flip, level=6, skill=player.stats._dex, transition=(combat.wipeccw, combat.wipeccw2))


            if _return:
                $ M_aqua.trigger(T_aqua_squid_defeated)
                call squid_pass
                call screen lair_entrance
                return

            $ M_aqua.trigger(T_aqua_chase_fail)
            $ game.timer.tick()
            call squid_fail
        "Belum.":

            call expression game.dialog_select("aqua_lure_steal_not_yet")
    $ game.main()

label aqua_lure_steal_pre:
    scene location_pier_dock_cutscene
    show text _ ("When that line snapped, my heart sank. I thought my lure was lost...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... But suddenly, something breached the surface of the water!") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Or should I say, someone...") as caption with dissolve
    pause

    scene location_pier_minigame06b
    show player 472 at Position(xpos=0.715,ypos=.9425)
    show aqua 16 at Position (xpos=0.4175,ypos=1.0)
    with fade
    aqua "Shiiiny..."

    show player 473
    show aqua 15
    player_name "!!!"
    player_name "W-what are you?!"

    show player 472
    show aqua 18
    aqua "Aku?"

    aqua "Me {b}Aqua{/b}... what you?"

    show player 473
    show aqua 17
    player_name "Hah?"

    show player 472
    show aqua 18
    aqua "You the human sssteals all {b}Aqua{/b} fishiesss?!"

    show player 473
    show aqua 17
    player_name "Fishies?"

    show player 472
    show aqua 16b
    aqua "Yesss, fishiesss!"

    aqua "You use ssshiny to sssteal my fishiesss!"

    show player 473
    show aqua 15b
    player_name "N-no, I just got the umm... \"Shiny\"?"

    player_name "{b}Captain Terry{/b} just gave it to me."

    show player 472
    show aqua 16b
    aqua "{b}Caplan Terry{/b}?"

    show player 473
    show aqua 15b
    player_name "Yeah, {b}Captain Terry{/b}."

    show player 472
    show aqua 16
    aqua "Hmm, {b}Aqua{/b} thinks you lie..."

    show aqua 16b
    aqua "... better take ssshiny and keep fishesss sssafe."

    show player 474
    show aqua 17
    player_name "Wait, no..."

    player_name "... Please, I worked really hard to get that!"

    show player 475
    show aqua 16b
    aqua "Too bad, it belong to {b}Aqua{/b} now!"

    hide aqua with dissolve
    show player 474
    player_name "Hai!!"


    show player 476
    player_name "Crap!"

    player_name "..."
    call popup ('take', 'special_lure')
    return

label aqua_lure_steal_after:
    player_name "!!!"
    player_name "( Damn! I'll have to go after her if I want that lure back. )"

    player_name "( It could be dangerous though. )"

    player_name "( I'd better make sure I'm ready first. )"

    return

label aqua_lure_steal_dive_pre:
    player_name "Screw it, I worked too hard for that lure!"

    player_name "I'm not going to let it go without a fight!"

    show player 477
    return

label aqua_lure_steal_dive_after:
    scene location_lair_dive
    show text _ ("I went straight after her...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... Diving headfirst into the dark blue water.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("I was determined to get my lure back!") as caption with dissolve
    pause

    scene location_lair_ocean_look with fade
    player_name "( She has to be around here somewhere. )"

    player_name "..."
    player_name "( Grr, where did she go?! )"


    scene location_lair_ocean_prefight
    player_name "( !!! )" with hpunch
    player_name "( What the- )"

    player_name "( A giant squid?!?! )"

    return

label aqua_lure_steal_not_yet:
    show player 476b
    player_name "( I... I can't just dive in after her. )"

    player_name "( There's no telling what's down there. )"

    player_name "( Maybe later. )"

    return

label squid_pass:
    scene location_lair_ocean
    with fade
    player_name "( Ah hah, she must be in that cave! )"

    player_name "( I'll need to find her quickly... )"

    player_name "( ... Before I run out of air! )"

    return

label squid_fail:
    scene location_lair_fail_squid
    show text _ ("The fight just wasn't going my way...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("The beast was too strong and the water was stifling.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("I waited for my opening and made a mad dash to the surface") as caption with dissolve
    pause

    scene location_pier_minigame06b with fade
    show player 478 at Position (xpos=0.644,ypos=1.0) with dissolve
    player_name "{i}*Cough*{/i}"

    player_name "I couldn't do it."

    show player 479 at Position (xpos=0.663,ypos=1.0) with dissolve
    player_name "..."
    player_name "I need to make sure I'm better prepared next time."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

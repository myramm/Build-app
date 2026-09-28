label hospital_elevator_dialogue:
    if M_priya.is_state(S_priya_roz_camera_check):
        call expression game.dialog_select("elevator_priya_check_pregnax")
        $ player.go_to(L_hospital_basement)
        $ M_priya.trigger(T_priya_helped_roz_with_camera)

    $ game.main()
    return

label elevator_priya_check_pregnax:
    $ player.go_to(L_hospital_elevator)
    scene expression player.location.background_closeup
    show old_roz 21 at left
    show player 13f at right
    with dissolve
    roz "Here you go."
    show old_roz 20
    pause
    show old_roz 7
    show player 696 at Position (xoffset=-9)
    with dissolve
    roz "It's supposed to take a picture when I press the button but nothing happens."
    roz "Stupid thing is broken!"
    show old_roz 6
    show player 700 at Position (xoffset=-2) with dissolve
    player_name "Hmm."
    player_name "Oh, here we go!"
    show player 701 at Position (xoffset=-36) with dissolve
    pause
    show player 700 at Position (xoffset=-2) with dissolve
    player_name "You just need to open up the flash bar here to turn the camera on."
    player_name "I think that should-"
    show player 702
    player_name "!!!" with flash
    show player 703 at Position (xoffset=-36) with dissolve
    player_name "Ack!"
    player_name "Yeah, it's definitely working now..."
    pause
    show old_roz 23 with vpunch
    show player 10f with dissolve
    player_name "Whoa, did you just stop the elevator?"
    show player 5f
    show old_roz 7 with dissolve
    roz "I'm just making sure we won't be disturbed."
    show old_roz 6
    show player 12f
    player_name "Huh?"
    player_name "Why would-"
    show old_roz 10 with dissolve
    pause
    show old_roz 8
    show player 6f
    player_name "!!!" with hpunch
    player_name "Agh, what are you doing?!?!"
    show old_roz 9
    roz "Gettin' ready for my close up."
    show old_roz 8
    player_name "Yeah, I don't know what that means..."
    show old_roz 9
    roz "Well, now that you got it workin', I want you to snap a few photos of me."
    roz "For the fellas down at the home."
    show old_roz 8
    show player 113f with dissolve
    player_name "Why me?!"
    show player 114f
    show old_roz 9
    roz "You wanna go to the basement don'tcha, kiddo?"
    show old_roz 8
    show player 113f
    player_name "Y-yeah..."
    show player 114f
    show old_roz 9
    roz "Well then, I suggest you quit yappin' and start snappin'."
    show old_roz 8
    show player 24f
    player_name "..."
    show old_roz 9
    roz "You gotta scratch my back if you want me to scratch yours."
    show old_roz 8
    show player 37f with dissolve
    player_name "Ugh, damn it."
    show player 24f with dissolve
    show old_roz 9
    roz "Make sure you get my good side!"

    if Game.is_halloween():
        scene location_hospital_cutscene01_halloween
    else:
        scene location_hospital_cutscene01
    show text _ ("... And here I thought this was going to be easy.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("How am I constantly getting myself into these situations?!") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("These pills had better be worth it.") as caption with dissolve
    pause

    scene expression player.location.background_closeup
    show old_roz 22 at left
    show player 24f at right
    with fade
    roz "Oh, yeah!"
    roz "This is gonna drive the fellas wild!"
    show old_roz 20 with dissolve
    show player 10f
    player_name "Are we done?"
    show player 5f
    roz "Hmm?"
    show player 10f
    player_name "I really need to speak with {b}Doctor Singh{/b}."
    show player 5f
    show old_roz 23 with dissolve
    roz "Oh, right."
    show old_roz 7
    roz "Sheesh, you kids these days have no patience!" with vpunch
    show old_roz 6
    player_name "..."
    show old_roz 7
    roz "... And don't go tellin' nobody it was me who brought you down here!"
    show old_roz 6
    show player 10f
    player_name "Uh huh. I won't tell a soul about any... Of this."
    show player 5f
    show old_roz 7
    roz "Good."
    roz "Now scram!"
    hide player with dissolve
    $ player.go_to(L_hospital_basement)
    scene expression player.location.background_blur
    show player 24 with dissolve
    player_name "( Ugh, what a day! )"
    player_name "( At least it got me down to the {b}basement{/b}. )"
    player_name "( I should {b}take a look around{/b} and see if I can find this {b}Doctor Singh{/b} guy. )"
    player_name "( Maybe I can find some bleach for my eyes, while I'm at it... )"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Roz"]["unlocked"] = True
    $ persistent.cookie_jar["Roz"]["gallery"]["02_unlocked"] = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

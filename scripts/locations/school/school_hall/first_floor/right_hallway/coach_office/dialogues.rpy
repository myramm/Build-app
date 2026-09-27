label coach_locker_dialogue:
    if player.has_picked_up_item("master_key"):
        if M_bissette.is_state(S_bissette_roxxy_pom_poms):
            if player.has_item("pompoms"):
                jump expression game.dialog_select("coachs_office_locker_peeking")
            else:

                call expression game.dialog_select("coachs_locker_bissette_roxxy_pom_poms")
        python:
            for image in renpy.get_showing_tags():
                renpy.hide(image)
        call screen coachs_locker
    else:

        if M_bissette.is_state(S_bissette_roxxy_pom_poms):
            call expression game.dialog_select("coachs_locker_locked_bissette_roxxy_pom_poms")
        else:

            call expression game.dialog_select("coachs_locker_locked")
    $ game.main()

label coachs_locker_bissette_roxxy_pom_poms:
    show coach_locker
    player_name "There they are!"

    return

label coachs_locker_locked_bissette_roxxy_pom_poms:
    show expression game.timer.image("coach_office{}_b")
    show player 12 with dissolve
    player_name "I bet they're in that locker."

    player_name "Looks like I'll need a key to get in."

    hide player with dissolve
    return

label coachs_locker_locked:
    show expression game.timer.image("coach_office{}_b")
    show player 1 with dissolve
    player_name "{b}Coach Bridget{/b}'s locker is locked. I can't open it as I don't have the key."

    hide player with dissolve
    return

label coachs_office_roxxy_pom_poms_right_time:
    show player 30 with dissolve
    player_name "Alright, she's not in here."

    show player 14
    player_name "This is my chance to {b}find those pom-poms{/b}!"

    show player 3f with dissolve
    player_name "..."
    show player 38 at Position (xoffset=41) with dissolve
    player_name "Now, where could they be?"

    hide bridget
    hide player
    with dissolve
    return

label coachs_office_roxxy_pom_poms_wrong_time:
    show bridget a_sides f_normal
    show player 23 at left
    with dissolve
    player_name "Oh crap! She's in here!"

    show player 22
    bridget @ f_suspicious "Can I help you?"

    show player 10
    player_name "Err, umm..."

    show player 11
    bridget @ f_suspicious "Ya?"

    show player 21
    player_name "No, I was just..."

    show player 27
    bridget @ f_suspicious_right "..."
    show player 29
    show xtra 21 at left
    with dissolve
    player_name "Excuse me, I need to use the restroom!"

    hide player
    hide xtra
    with dissolve
    bridget @ f_suspicious "What a weirdo..."

    hide bridget
    hide player
    with dissolve
    return

label coachs_office_roxxy_pom_poms:
    scene expression game.timer.image("coach_office{}_b")
    if game.timer.is_morning():
        call expression game.dialog_select("coachs_office_roxxy_pom_poms_right_time")
    else:

        call expression game.dialog_select("coachs_office_roxxy_pom_poms_wrong_time")
        $ player.go_to(L_school_righthallway)
    return

label coach_locker_pom_poms:
    show coach_locker
    player_name "Luar biasa!"

    call expression game.dialog_select("coach_locker_pom_poms_dialogue")
    $ player.get_item("pompoms")

    $ player.location.call_screen(False)

label coach_locker_pom_poms_dialogue:
    call popup ('give', 'pompoms')
    scene expression game.timer.image("coach_office{}_b")
    show player 14 with dissolve
    player_name "Now, I just need to {b}get these back to Rox{/b}-"

    show player 11
    bridget "Yeah, yeah! Just head to the track and I'll meet you there."

    bridget "I need to change first."

    show player 22
    player_name "!!!" with hpunch
    show player 23
    player_name "Oh crap! She's coming!"

    player_name "I'm so dead! What am I gonna do?!"

    player_name "I gotta hide somewhere!"

    hide player with dissolve
    return

label coachs_office_locker_hide_fail:
    call expression game.dialog_select("coachs_office_locker_hide_fail_dialogue")

    $ M_bissette.trigger(T_bissette_bridget_pompoms_steal)
    $ player.go_to(L_school_righthallway)
    $ game.main()

label coachs_office_locker_hide_fail_dialogue:
    scene expression game.timer.image("coach_office{}_b")
    show bridget a_crossed f_angry
    show player 22 at left
    with dissolve
    bridget "Apa yang kamu lakukan di sini?"

    show player 23
    player_name "I... Uh..."

    show player 29 with dissolve
    player_name "This... Isn't the restroom?"

    show player 22 with dissolve
    bridget @ f_angry_yell "Get your scrawny ass out of here!"

    show player 23
    player_name "On my way!"

    hide player with dissolve
    bridget a_sides f_suspicious "Weirdo."

    hide bridget with dissolve
    return

label coachs_office_locker_peeking:
    call expression game.dialog_select("coachs_office_locker_peeking_dialogue")

    $ M_bissette.trigger(T_bissette_bridget_pompoms_steal)
    $ game.main()

label coachs_office_locker_peeking_dialogue:
    scene expression game.timer.image("coach_office{}_b")
    show player 10 with dissolve
    player_name "This is the only place to hide!"

    player_name "I just have to hope she doesn't look in here."

    hide player with dissolve

    scene coach_locker_cs1
    show text _ ("It was a tight fit but I managed to get inside the locker and close the door.\nJust in time too, {b}Coach Bridget{/b} had almost caught me!") as caption
    with fade
    pause

    scene coach_locker_cs2
    show text _ ("All I could do now was keep quiet and hope she didn't find me.") as caption
    with fade
    pause

    scene coach_locker_peek
    show bridget a_crossed
    show coach_locker_peek_overlay
    with fade
    player_name "( There she is! )"

    player_name "( Please don't look in here... )"

    pause
    bridget "Man, it sure is cookin' out there."

    bridget "I'm sweating like a whore in church!"

    show bridget b_undress with dissolve
    player_name "( She's undressing! )"

    player_name "( I am so dead if she finds me! )"

    show bridget b_lingerie a_undress_top with dissolve
    pause
    bridget a_hips f_pleased_down "Mmm, I hope you're paying attention!"

    player_name "( Does she know?! )"

    pause
    bridget a_flex f_pleased_down_left "I'd hate for you to miss the gun show!"

    player_name "( ... )"
    pause
    bridget "Damn girl!"

    bridget "Better put those away before they hurt somebody."

    show bridget a_undress_top with dissolve
    player_name "( What a weirdo... )"

    show bridget b_undress with dissolve
    pause
    show bridget b_dressed a_sides f_suspicious_right with dissolve
    pause
    bridget f_suspicious "Huh. Thought I heard something."

    bridget "Must have been my imagination..."

    hide bridget with dissolve
    pause
    pause
    player_name "( I think she's gone. )"

    hide player with dissolve
    return

label coach_locker_pantie_collection:
    scene expression player.location.background_blur with None
    if player.location.is_here(M_bridget):
        show anon f_surprised_teeth with dissolve
        anon @ -m_talk "( Not on your nelly! No one would even find my body! )"

    else:
        show anon f_shy_down a_panties_bridget1 with dissolve
        anon @ -m_talk "( These are {b}Coach Bridget{/b}'s panties. )"

        anon @ -m_talk "( She must have hung these up after an intense workout... )"

        pause
        if M_somrak.finished_state(S_somrak_start):
            anon f_grin "( I bet {b}Master Somrak{/b} would like these. )"

            $ player.get_item("bridget_panties")
        else:
            anon f_shy_down @ -m_talk "( They're a bit ripe, I'll just leave them here. )"

        hide anon with dissolve
    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

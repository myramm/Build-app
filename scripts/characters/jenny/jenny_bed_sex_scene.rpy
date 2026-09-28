label jenny_bed_night_button:
    $ player.go_to(L_home_sisbedroom)
    if not M_jenny.finished_state(S_jenny_give_cunni):
        call expression game.dialog_select("jenny_bed_night_pre_j17")
        $ player.go_to(L_home_hallway)
        $ game.main()
    elif M_jenny.between_states(S_jenny_give_cunni, S_jenny_night_time_sex):
        call expression game.dialog_select("jenny_bed_night_j17_j20")
        $ player.go_to(L_home_hallway)
        $ game.main()
    elif M_jenny.pregnancy:
        call jenny_bed_night_pregnant
    else:
        call expression game.dialog_select("jenny_bed_night_sex_intro")
    $ game.main()

label jenny_bed_night_pre_j17:
    scene expression player.location.background_blur with None
    show anon f_surprised_teeth with dissolve
    anon "( There's no way I'm bothering her! )"
    anon "( She'll kill me! )"
    hide anon with dissolve
    return

label jenny_bed_night_j17_j20:
    scene expression player.location.background_blur with None
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( You know, we have been getting along better recently... )"
    anon @ -m_talk "( Maybe she wouldn't mind? )"
    show anon f_grin
    menu:
        "Do it.":
            call expression game.dialog_select("jenny_bed_night_do_it_j17")
        "I'd better not.":
            call expression game.dialog_select("jenny_bed_night_better_not")
    return

label jenny_bed_night_do_it_j17:
    scene expression "backgrounds/location_home_jennybedroom_bed.jpg" with None
    show jenny b_sleep_side o_sleep_blanket a_side f_sleep_side_rolleye with None
    show anon b_sleep_climb
    with dissolve
    pause
    show anon b_sleep_side f_sleep_side_shy o_sleep_side_boxers
    show expression "characters/anon/anon_arms_sleep_side_a_normal.png"
    show jenny o_empty
    show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png"
    with dissolve
    pause
    show anon b_sleep_cuddle o_empty
    hide expression "characters/anon/anon_arms_sleep_side_a_normal.png"
    with dissolve
    pause
    show jenny f_sleep_side_wake
    jenny "Hmm?"
    show jenny b_sleep_turn a_turn f_sleep_turn_angry o_sleep_panties with dissolve
    jenny "What the-"
    anon "H-hi."
    pause
    show jenny a_turn_push
    show anon b_sleep_side o_sleep_side_boxers a_react f_sleep_side_shock
    jenny "WHAT THE FUCK?!" with hpunch
    scene expression player.location.background_blur
    show anon f_surprised_teeth b_underwear
    show jenny f_angry a_crossed
    with fade
    jenny "Seriously, what the fuck is wrong with you?!"
    anon f_sad "I'm sorry... I-"
    jenny "You don't just sneak into a woman's bed while she's sleeping, {b}[firstname]{/b}!"
    jenny "That is so creepy!"
    anon "I just thought that maybe-"
    show anon f_depressed
    jenny "No, you obviously didn't think!"
    jenny "Eugh, just get the fuck out!"
    anon f_sad @ -m_talk "..."
    hide anon with dissolve
    show jenny f_eyeroll
    jenny "Fucking loser..."
    scene black with fade
    pause
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with None
    show anon f_sad_down with dissolve
    anon @ -m_talk "( Well, that was awful... )"
    anon @ -m_talk "( Why did I think that was a good idea? )"
    anon @ -m_talk "( {i}*Sigh*{/i} I hope she doesn't tell {b}[deb_name]{/b} about this... )"
    hide anon with dissolve
    return

label jenny_bed_night_better_not:
    show anon f_worried a_idle with dissolve
    anon @ -m_talk "( Yeah, no... )"
    anon @ -m_talk "( It's not worth pissing her off. )"
    hide anon with dissolve
    return

label jenny_bed_night_sex_intro:
    if store._in_replay is not None:
        $ player.location = L_home_sisbedroom
        $ game.timer.tick(3)
    scene expression player.location.background_blur with None
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( Surely she won't get mad at me now, right? )"
    anon @ -m_talk "( I mean, she's been climbing into MY bed in the middle of the night... Why can't I do the same? )"
    show anon f_grin
    menu:
        "Do it.":
            call expression game.dialog_select("jenny_bed_night_sex_do_it")
        "I'd better not." if store._in_replay is None:
            call expression game.dialog_select("jenny_bed_night_better_not")
    return

label jenny_bed_night_sex_do_it:
    if store._in_replay is not None or M_jenny.get("bed_sex_first_time"):
        $ M_jenny.set("bed_sex_first_time", False)
        scene expression "backgrounds/location_home_jennybedroom_bed.jpg" with None
        show jenny b_sleep_side o_sleep_blanket a_side f_sleep_side_sleeping with None
        show anon b_sleep_climb
        with dissolve
        pause
        show anon b_sleep_side f_sleep_side_shy o_sleep_side_boxers
        show expression "characters/anon/anon_arms_sleep_side_a_normal.png"
        show jenny o_empty
        show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png" zorder 3
        with dissolve
        pause
        show anon b_sleep_cuddle f_sleep_side_shy o_empty
        hide expression "characters/anon/anon_arms_sleep_side_a_normal.png"
        with dissolve
        pause
        show jenny f_sleep_side_wake
        jenny "Hmm?"
        show jenny b_sleep_turn a_turn f_sleep_turn_angry o_sleep_panties with dissolve
        jenny "{b}[firstname]{/b}?"
        anon "H-hi."
        pause
        jenny "What the fuck are you doing?"
        anon "Uhh, going to bed?"
        jenny "Go get in your own bed, loser!"
        anon "Aww, c'mon {b}[jen_name]{/b}... You climb into my bed all the time!"
        jenny "Yeah, because I wanna fuck... Not to cuddle up and slobber all over you while you're trying to sleep."
        anon "I don't slobber..."
        show jenny b_sleep_side a_side f_sleep_side_tired with dissolve
        jenny "Yeah, right."
        show jenny f_sleep_side_sleeping
        pause
        show jenny b_sleep_turn a_turn f_sleep_turn_normal with dissolve
        jenny @ -m_talk "..."
        jenny "Fine, just hurry it up!"
        anon @ -m_talk "Hmm?"
        jenny "I'm tired, {b}[firstname]{/b}!"
        jenny "So, if you're going to fuck me then hurry up and do it already... Otherwise, get the fuck out!"
        show jenny b_sleep_side a_side f_sleep_side_sleeping with dissolve
        show anon f_sleep_side_shock
        menu:
            "Okay.":
                anon f_sleep_side_shy "O-okay."
                pause
                anon "Umm..."

                label jenny_bed_night_grope_in_bed:
                    show anon f_sleep_side_kiss b_empty_sleep_cuddle
                    show jenny b_empty
                    show jenny_arms_a_sleep_side_grope as anim_arms
                    show jenny b_sleep_side_grope a_empty f_empty as anim_body behind jenny
                    with dissolve
                    pause
                    jenny "Mmm."
                    show anon b_sleep_side f_sleep_side_shy o_sleep_side_boxers_boner
                    show expression "characters/anon/anon_arms_sleep_side_a_normal.png"
                    hide anim_arms
                    hide anim_body
                    show jenny b_sleep_turn a_turn_remove_top1 f_sleep_turn_normal
                    with dissolve
                    pause
                    show jenny b_sleep_turn_shirtup a_turn_remove_top2
                    with dissolve
                    anon "..."
                    show jenny b_sleep_side_shirtup a_side f_sleep_side_normal with dissolve
                    pause
                    show anon f_sleep_side_kiss b_empty_sleep_cuddle o_empty
                    hide expression "characters/anon/anon_arms_sleep_side_a_normal.png"
                    show jenny b_empty f_sleep_side_enjoy
                    show jenny_arms_a_sleep_side_grope as anim_arms
                    show jenny b_sleep_side_grope_shirtup a_empty f_empty as anim_body behind jenny
                    with dissolve
                    pause
                    jenny "Okay, that feels really good..."
                    show jenny f_sleep_side_rolleye
                    show jenny_arms_a_sleep_side_grope as anim_arms
                    show jenny b_sleep_side_grope_hump_shirtup as anim_body
                    with dissolve
                    jenny "Ngghhh!"
                    pause
                    anon f_sleep_side_shy "You glad I woke you up yet?"
                    show jenny f_sleep_side_tired
                    jenny "Shut up..."
                    show anon f_sleep_side_kiss
                    show jenny f_sleep_side_enjoy
                    pause
                    menu jenny_bed_night_whatcha_do:
                        "Go further.":
                            jump jenny_bed_night_go_further
                        "Continue.":
                            pause
                            jump jenny_bed_night_whatcha_do

            "Forget it." if store._in_replay is None:
                show anon b_sleep_leave
                hide anim_arms
                hide anim_body
                show jenny b_sleep_turn a_turn f_sleep_turn_normal o_sleep_blanket
                hide expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png"
                with dissolve
                anon "Fine, just forget it..."
                hide anon with dissolve
                jenny "Gladly."
                $ player.go_to(L_home_hallway)
                $ game.main()
    else:
        scene expression "backgrounds/location_home_jennybedroom_bed.jpg" with None
        show jenny b_sleep_side o_sleep_blanket a_side f_sleep_side_sleeping with None
        show anon b_sleep_climb
        with dissolve
        pause
        show anon b_sleep_cuddle f_sleep_side_shy
        show jenny o_empty
        show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png" zorder 3
        with dissolve
        show jenny f_sleep_side_wake
        jenny "Hmm?"
        show jenny b_sleep_turn a_turn f_sleep_turn_angry o_sleep_panties with dissolve
        jenny "{b}[firstname]{/b}?"
        anon "H-hi."
        pause
        jenny "This shit again?"
        anon "I thought you liked it?"
        jenny "What the fuck gave you that idea?"
        anon "S-so, you didn't like it?"
        jenny "That's not-"
        pause
        jenny "Never mind, just hurry it up, would you?!"
        show jenny b_sleep_side a_side f_sleep_side_sleeping with dissolve
        jump jenny_bed_night_grope_in_bed


label jenny_bed_night_go_further:
    show anon b_sleep_side f_sleep_side_shy o_sleep_side_boxers_boner
    show expression "characters/anon/anon_arms_sleep_side_a_normal.png"
    hide anim_arms
    hide anim_body
    show jenny b_sleep_turn_shirtup o_sleep_panties f_sleep_turn_normal a_turn
    with dissolve
    jenny "Alright, that's enough foreplay."
    show jenny a_turn_remove1 o_empty with dissolve
    pause
    show anon a_remove1_boner f_sleep_side_normal o_empty zorder 1
    show jenny a_turn_remove2 zorder 2
    with dissolve
    pause
    show anon b_sleep_side a_remove2
    show jenny a_turn o_sleep_panties_down
    with dissolve
    pause
    show anon a_insert o_sleep_side_boxers_down with dissolve
    pause
    scene expression "backgrounds/location_home_jennybedroom_sex_sleep.jpg"
    show jenny_sleeping_sex default
    show jenny_sleeping_sex_face normal_talk
    show player_jenny_sleeping_sex pre
    show jenny_sex_sleep_blanket
    with fade
    jenny "Put it inside me."
    hide jenny_sleeping_sex_face
    show jenny_sleeping_sex insert
    hide player_jenny_sleeping_sex
    with dissolve
    anon "Alright."
    show jenny_sleeping_sex 1 with dissolve
    jenny "Fuuuuck..."
    $ anim_toggle = True
    $ animated = True
    $ M_jenny.set('sex speed', .12)
    show expression AnimatedImage("jenny_sleeping_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_sleeping_sex at Position(xalign = 0.0, yoffset = 0)
    jump jenny_jenny_bed_sex_loop

label jenny_jenny_bed_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_sleeping_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_sleeping_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_jenny_bed_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_sleeping_sex {}".format(pose_list[pose_counter]) as jenny_sleeping_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_jenny_bed_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_jenny_bed_sex_options

label jenny_jenny_bed_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 25:
        jenny "Mmm, that feels good...{p=1}{nw}"
    if animcounter == 1 and randomizer() < 25:
        anon "Mmhmm.{p=1}{nw}"
    if animcounter == 2 and randomizer() < 25:
        jenny "Ahhh!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 25:
        jenny "Oh, right there!{p=1}{nw}"
        jenny "Yeah!{p=1}{nw}"
    return

label jenny_jenny_bed_sex_cum_outside:
    $ M_jenny.set("jenny_bed_cum_inside", False)
    jenny "Don't stop!"
    anon "I'm going to cum!"
    jenny "DON'T STOP!!"
    show jenny_sleeping_sex insert with dissolve
    jenny "DON'T-"
    show jenny_sleeping_sex default
    show jenny_sleeping_sex_face cum
    show player_jenny_sleeping_sex cum
    anon "HNNGGG!!!" with flash
    show jenny_sleeping_sex_face angry_talk
    jenny "Oh, what the fuck, {b}[firstname]{/b}!"
    scene expression "backgrounds/location_home_jennybedroom_bed.jpg"
    show jenny b_sleep_after f_sleep_turn_angry
    show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png" zorder 1
    show anon f_sleep_side_shy b_empty_sleep_cuddle
    with fade
    anon @ -m_talk "Hmm?"
    jenny "Eugh, it's fucking everywhere!"
    jenny "How am I supposed to sleep now?"
    anon "S-sorry..."
    jenny "For fuck's sake..."
    pause
    jenny "Get out!"
    anon "What?!"
    anon "Are you serious?"
    jenny "Yes, you're disgusting!"
    jump jenny_bed_sex_night_end

label jenny_jenny_bed_sex_cum_inside:
    $ M_jenny.set("jenny_bed_cum_inside", True)
    jenny "Don't stop!"
    anon "I'm going to cum!"
    jenny "DON'T STOP!!"
    jenny "NGGHHH!!!"
    show jenny_sleeping_sex cum
    anon "HNNGGG!!!" with flash
    show xray_jenny_jenny_bed at Position (align=(0,0))
    show jenny_sleeping_sex cum2
    with dissolve
    pause
    hide xray_jenny_jenny_bed
    show jenny_sleeping_sex pullout
    with dissolve
    jenny "Oh, wow!"
    show jenny_sleeping_sex default
    show jenny_sleeping_sex_face normal
    show player_jenny_sleeping_sex after
    with dissolve
    anon "Haah... Haah..."
    call call_pregnancy_minigame ("jenny_bed_sex_cum_inside_post_pregnancy", M_jenny)

label jenny_bed_sex_cum_inside_post_pregnancy:
    scene expression "backgrounds/location_home_jennybedroom_bed.jpg"
    show jenny b_sleep_after f_sleep_turn_angry
    show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png" zorder 1
    show anon f_sleep_side_shy b_empty_sleep_cuddle
    with fade
    jenny "Did you fucking cum inside me?"
    anon "Yeah."
    jenny "Goddamnit, {b}[firstname]{/b}!"
    anon "You did say not to stop..."
    jenny "You know that's not what I meant!"
    anon "Well, I'm sorry..."
    anon "We were just really into it and everything felt so good, I-"
    jenny "{i}*Sigh*{/i} For fuck's sake..."
    jenny "Just get out!"
    anon "What?!"
    anon "Are you serious?"
    jenny "Yes, you're disgusting!"
    jump jenny_bed_sex_night_end

label jenny_bed_sex_night_end:
    if M_jenny.get("dominance") > 0:
        show anon f_sleep_side_normal
        anon "Would you just chill out?"
        if M_jenny.get("jenny_bed_cum_inside"):
            anon "Everything will be fine."
        else:
            anon "It's not like you've never had my semen on you before..."
        jenny "..."
        anon "Just shut up and go to sleep, we can deal with it in the morning."
        show jenny f_sleep_turn_angry
        jenny "Fine."
        jenny "... Asshole."
    else:
        show anon f_sleep_side_shy
        anon "C'mon, {b}[jen_name]{/b}..."
        anon "Can't we just sleep?"
        show jenny f_sleep_turn_angry
        jenny "I don't want you snoring in my ear all night!"
        anon "You're the one who snores!!!"
        jenny "Fuck you!"
        pause
        jenny "Fine."
        jenny "You big fucking baby!"
        anon "Thank you!"
        jenny "Eugh..."
    scene location_home_jennybedroom_night_sleep with fade
    if _in_replay:
        pause
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["17_unlocked"] = True
    call popup ('sleep')
    jump jenny_bed_sex_sleeping

label jenny_bed_sex_sleeping:
    call sleep_lock_check
    if M_player.is_set("just wokeup"):
        $ renpy.call(game.dialog_select("player_just_wokeup"), woke_with = M_jenny)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label jenny_couch_sex:
    if M_jenny.get("dominance") <= 0:
        hide jenny_couch_dick_rub
        show jenny a_dick3 f_sexy
        jenny "Alright, I'm bored of this..."
        show anon f_couch_sit_right
        anon @ -m_talk "Hmm?"
        show anon a_boner zorder 1
        show jenny b_couch_remove zorder 0
        with dissolve
        pause
        show jenny b_couch_sit f_sexy a_rest o_couch_teasing with dissolve
        jenny "Get over here and fuck me."
        anon "What?!"
        jenny "You heard me."
        anon "B-but, {b}[deb_name]{/b} is right in there!"
        jenny "I know, it's exciting! Isn't it?"
        anon "N-no?"
        show jenny f_eyeroll
        jenny "{i}*Sigh*{/i} Yes, it is!"
        show jenny f_sexy
        anon @ -m_talk "..."
        jenny "Don't be a pussy."
        show jenny f_sexy_down
        jenny "I want that big dick!"
    else:
        show jenny f_sexy_down
        jenny "Are you getting close?"
        anon f_couch_sit_down "Y-yes."
        show anon f_couch_sit_right
        hide jenny_couch_dick_rub
        show jenny a_dick3 f_sexy_down
        pause
        anon "What are you doing?!"
        show jenny f_sexy
        jenny "I'm bored of this..."
        pause
        jenny "Let's fuck!"
        anon "Huh?!"
        jenny "You heard me."
        show anon a_boner zorder 1
        show jenny b_couch_remove zorder 0
        with dissolve
        pause
        show jenny b_couch_sit f_sexy a_rest o_couch_teasing with dissolve
        jenny "I want you inside me."
        anon "B-but, {b}[deb_name]{/b} is right in there!"
        jenny "So?"
        jenny "I can be quiet."
        anon "Yeah, right."
        show jenny f_upset
        jenny "C'mon, please?"
        anon @ f_couch_sit_down_surprised "!!!"
        anon "Did you just say, please?"
        show jenny f_eyeroll
        jenny "... Maybe."
        show jenny f_sexy
        anon "Wow, you really do want it."
        show jenny f_sexy_down
        jenny "Mmhmm!"
    anon "Fine."
    show anon b_couch_remove
    with dissolve
    pause
    show anon b_couch_jump
    show jenny b_couch_jump o_empty
    with dissolve
    jenny "Oh, fuuuuck!"
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .09)
    hide jenny
    scene expression "backgrounds/location_home_livingroom_couch_sex.jpg"
    show expression AnimatedImage("jenny_couch_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_couch_sex at Position(xalign = 0.0, yoffset = 0)
    with fade
    anon "Shhh!"
    anon "{b}[deb_name]{/b} will freak out if she finds us!"
    jenny "I know!"
    jenny "It's just so deep, I can't-"
    jump jenny_couch_sex_loop

label jenny_couch_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_couch_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_couch_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_couch_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_couch_sex {}".format(pose_list[pose_counter]) as jenny_couch_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_couch_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_couch_sex_options

label jenny_couch_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jenny "Ahh!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jenny "I love your dick so much!{p=2}{nw}"
        jenny "Oh, god!!{p=1}{nw}"
        jenny "I love it, I love it, I LOVE IT!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jenny "FUUUCK, YES!{p=1}{nw}"
        anon "Shh!!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        jenny "C'mon, {b}[firstname]{/b}!{p=1}{nw}"
        jenny "Fuck me harder!{p=1}{nw}"
        anon "Stop pulling on me!{p=2}{nw}"
        if M_jenny.get("sex speed") > 0.061:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.03)
        jenny "Oh, right there!{p=1}{nw}"
    return

label jenny_couch_sex_cum_outside:
    anon "I'm going to cum!"
    jenny "Me too!"
    jenny "NGGHHH!!!"
    show jenny_couch_sex cumshot
    anon "HNNGGG!!!" with flash
    pause
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show jenny b_couch_after3
    show anon b_couch_sit_naked f_couch_sit_right a_naked_after
    with fade
    anon "Wow..."
    show jenny b_couch_after4
    jenny "Haah... Haah..."
    show jenny b_couch_after3
    anon "That was intense!"
    show jenny b_couch_after4
    jenny "You came all over me!"
    show jenny b_couch_after3
    anon "Would you rather I had cum inside of you?"
    show jenny b_couch_after4
    jenny "No... But you could have-"
    show jenny b_couch_after3
    pause
    show jenny b_couch_after4
    jenny "{i}*Sigh*{/i} Never mind."
    show jenny b_couch_remove with dissolve
    jenny "I'm going to go take a shower."
    show jenny b_couch_transition with dissolve
    pause 1
    hide jenny with dissolve
    jenny "Later, loser."
    anon "Yeah, see ya."
    pause
    anon f_couch_sit_down_surprised "( Phew, I guess we're just fucking whenever now... )"
    anon "( Awesome! )"
    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["08_unlocked"] = True
    $ M_jenny.set("couch_sex_first", False)
    $ M_jenny.set("had_couch_sex", True)
    $ game.timer.tick()
    $ game.main()

label jenny_couch_sex_cum_inside:
    anon "I'm going to cum!"
    jenny "Me too!"
    anon "Let go of me!"
    jenny "NGGHHH!!!"
    anon "{b}[jen_name]{/b} I can't-"
    show jenny_couch_sex cum
    anon "HNNGGG!!!" with flash
    jenny "AHHHH!!!"
    show jenny_couch_sex cum 2
    show xray_jenny_couch at Position (align=(0,0))
    pause
    hide xray_jenny_couch
    show jenny_couch_sex pullout 1
    with dissolve
    anon "Holy crap..."
    show jenny_couch_sex pullout 2 with dissolve
    jenny "Haah... Haah..."
    call call_pregnancy_minigame ("jenny_couch_sex_cum_inside_post_pregnancy", M_jenny)

label jenny_couch_sex_cum_inside_post_pregnancy:
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show jenny b_couch_after2
    show anon b_couch_sit_naked f_couch_sit_right a_naked_after
    with fade
    show jenny b_couch_after1
    jenny "Oh my god, did you cum inside me?!"
    show jenny b_couch_after2
    anon "I tried pulling out but you wouldn't let go of me!"
    show jenny b_couch_after1
    jenny "Well, I was focused on cumming!"
    show jenny b_couch_after2
    pause
    show jenny b_couch_after1
    jenny "FUCK!"
    jenny "You are so dead if I get pregnant!"
    show jenny b_couch_after2
    anon "M-me?!"
    anon "You're the one who held me there!"
    show jenny b_couch_after1
    jenny "Shut up!"
    show jenny b_couch_remove with dissolve
    jenny "Grr, I'm getting in the shower!"
    show jenny b_couch_transition_mad with dissolve
    pause 1
    hide jenny with dissolve
    jenny "Asshole..."
    anon "Oh, so it's all my fault, huh?!"
    pause
    anon "( She's gone... )"
    pause
    anon f_couch_sit_down_surprised "( Phew, I guess we're just fucking whenever now... )"
    anon "( Awesome! )"
    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["09_unlocked"] = True
    $ M_jenny.set("had_couch_sex", True)
    $ M_jenny.set("couch_sex_first", False)
    $ game.timer.tick()
    $ game.main()

label jenny_shower_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_shower_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_shower_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_shower_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_shower_sex {}".format(pose_list[pose_counter]) as jenny_shower_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_shower_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_shower_sex_options

label jenny_shower_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jenny "Ahh!!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jenny "It's so deep!{p=1}{nw}"
        jenny "Oh, fuck me!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jenny "FUUUUUCK!!!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        anon "Uhh!{p=1}{nw}"
    return

label jenny_shower_sex_cum_inside:
    jenny "I'm cumming! I'm cumming!"
    jenny "NGGHHH!!!"
    anon "Yeah, I'm getting close too."
    pause
    anon "{b}[jen_name]{/b}?"
    show jenny_shower_sex cum
    anon "HNNGGG!!!" with flash
    jenny "AAAHHHH!!!"
    show jenny_shower_sex cum 2
    show xray_jenny_shower at Position (align=(0,0))
    pause
    call call_pregnancy_minigame ("jenny_mc_shower_sex_cum_inside_post_pregnancy_minigame", M_jenny)

label jenny_mc_shower_sex_cum_inside_post_pregnancy_minigame:
    call scene_shower_with_vfx
    show anon b_naked f_tired od_naked_dick1
    show jenny b_shower_back a_push
    with fade
    anon "Haah... Haah..."
    show jenny a_butt f_surprised with dissolve
    anon f_normal "Holy crap!"
    show jenny b_shower_back_creampie with dissolve
    jenny "Did you cum in me?!"
    anon f_worried "Y-yeah, a little..."
    show anon f_surprised
    show jenny b_naked a_crossed f_angry with dissolve
    jenny "A LITTLE?!"
    jenny "THAT'S A LOT YOU MORON!"
    anon f_worried "I'm sorry."
    anon "I guess I got a little carried away there at the end..."
    jenny "What if I get pregnant?!"
    anon "I didn't-"
    jenny "Damn it, {b}[firstname]{/b}!"
    jenny "Get the fuck out!"
    anon "Alright, alright..."
    anon "I said I was sorry, sheesh."
    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["14_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_hallway)
    $ game.main()

label jenny_shower_sex_cum_outside:
    jenny "I'm cumming! I'm cumming!"
    jenny "NGGHHH!!!"
    anon "Yeah, I'm getting close too."
    pause
    anon "{b}[jen_name]{/b}?"
    hide jenny_shower_sex
    show jenny b_shower_cumshot f_shower_cumshot
    show anon b_side_naked_forward od_side_naked_forward_cum1 f_side_react a_up_clench
    anon "HNNGGG!!!" with flash
    show anon od_side_naked_forward_cum2 o_side_naked_forward_cum3 with dissolve
    pause
    show anon b_naked a_idle f_tired od_naked_dick1 o_empty
    show jenny b_naked a_sides f_sexy_down
    with dissolve
    anon "Haah... Haah..."
    show anon f_normal
    show jenny f_sexy
    jenny "Haah... Holy shit!"
    show jenny f_sexy_down
    jenny "I think-"
    jenny "I need to go lie down for a bit."
    show jenny f_sexy
    anon f_worried "You alright?"
    jenny "Y-yeah, it's just the steam and the sex and..."
    show anon f_normal
    show jenny f_laugh
    jenny "Fuck, I can barely walk!"
    show jenny f_sexy
    anon @ f_grin -m_talk "Heh."
    anon "Here, I'll help you."
    show anon f_worried
    show jenny f_upset a_hips with dissolve
    jenny "No, fuck off!"
    jenny "I'm fine!"
    anon "Alright, sheesh."
    anon "I'm just trying to be considerate..."
    jenny "Well, cut it out!"
    hide jenny with dissolve
    pause
    anon @ -m_talk "( She's so weird sometimes... )"
    anon f_grin @ -m_talk "( Oh well, that was awesome! )"
    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["14_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_hallway)
    $ game.main()

label bj_shower_repeat_sub:
    show anon f_worried_low
    anon "Arf!"
    show jenny f_grin
    jenny "Heh, more!"
    anon "{i}*Sigh*{/i}"
    anon f_shock "Arf! Arf! Arf!"
    show anon f_worried_low
    show jenny f_laugh
    jenny "Hahahaah!!"
    show anon b_side_naked a_react f_side_shy_down od_side_naked_dick3
    show jenny b_shower_kneeling f_shower_kneeling
    with dissolve
    if randomizer() > 50:
        jenny "Good doggy!"
    else:
        jenny "There's a good boy!"
    call scene_shower_with_vfx_zoom
    show jenny_shower_bj_mc
    show jenny_shower_bj pre_talk
    with fade
    jenny "Now you get a reward!"

label bj_shower_repeat_dom:
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .14)
    show expression AnimatedImage("jenny_shower_bj", [1,2,3,4,5,6,7], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
    anon "!!!" with hpunch

    if M_jenny.get('first_time_deep_bj'):
        $ M_jenny.set('first_time_deep_bj', False)
        anon "{i}*Gasp*{/i}"
        pause
        anon "Wow, okay..."
        anon "Ahh!"
        pause
        anon "Mm, that feels so good!"
        jenny "Mmhrmm."
        pause
        show jenny_shower_bj_mc
        show jenny_shower_bj pre_talk
        with dissolve
        jenny "Alright, I'm going to try something now..."
        show jenny_shower_bj pre_look
        anon "Hmm?"
        show jenny_shower_bj pre_talk
        jenny "My fans have been asking me for something and I'm going to test it out on you."
        show jenny_shower_bj pre_look
        anon "What is it?"
        show jenny_shower_bj pre_talk
        jenny "You'll see."
        jenny "Just try and stay still!"
        show expression AnimatedImage("jenny_shower_bj", [1,2,3,4,5,6,7], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
        anon "You're not going to do anything weird, are you?"
        pause
        anon "{b}[jen_name]{/b}?"
    else:
        anon "Mmm."
        pause
        anon "Very nice!"
        jenny "Shrmmup!!"
        anon "Ohh!"
        pause
        anon "Mm, that feels so good!"
        jenny "Mmhrmm."
        pause

    $ M_jenny.set('sex speed', .4)
    show expression AnimatedImage("jenny_shower_bj_deep", [1,2], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
    $ M_jenny.set("jenny_bj_deep", True)
    anon "!!!" with hpunch
    anon "Oh my god!!"
    pause
    anon "That feels incredible!!!"
    jenny "{i}*Gllrrkkk*{/i}"
    pause
    jenny "{i}*Bllgghhh*{/i}"
    anon "{b}[jen_name]{/b}, I can't-"

    label jenny_shower_bj_loop:
        show screen sex_anim_buttons
        pause
        hide screen sex_anim_buttons
        $ animcounter = 0
        while animcounter < 4:
            if anim_toggle:
                if not animated:
                    if M_jenny.get("jenny_bj_deep"):
                        $ M_jenny.set('sex speed', .4)
                        show expression AnimatedImage("jenny_shower_bj_deep", [1,2], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0) with dissolve
                    else:
                        $ M_jenny.set('sex speed', .14)
                        show expression AnimatedImage("jenny_shower_bj", [1,2,3,4,5,6,7], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0) with dissolve
                    $ animated = True
                pause 5
                call expression game.dialog_select("jenny_shower_bj_hscene_dialog")
                pause 3
            else:

                $ pose_counter = 0
                if M_jenny.get("jenny_bj_deep"):
                    $ pose_list = [1,2]
                else:
                    $ pose_list = [1,2,3,4,5,6,7]
                $ poses_done = []
                while poses_done != pose_list:
                    if M_jenny.get("jenny_bj_deep"):
                        show expression "jenny_shower_bj_deep {}".format(pose_list[pose_counter]) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
                    else:
                        show expression "jenny_shower_bj {}".format(pose_list[pose_counter]) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
                    pause
                    $ poses_done.append(pose_list[pose_counter])
                    $ pose_counter += 1
                call expression game.dialog_select("jenny_shower_bj_hscene_dialog")
            $ animcounter += 1
        call screen jenny_shower_bj_options

label jenny_shower_bj_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        anon "Mmm.{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        anon "Very nice!{p=1}{nw}"
        jenny "Shrmmup!!{p=1}{nw}"
        anon "Ohh!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        anon "{i}*Gasp*{/i}"
    if animcounter == 3 and randomizer() < 10:
        anon "Wow, okay..."
        anon "Ahh!"
    if animcounter == 3 and randomizer() < 10:
        anon "Mm, that feels so good!"
        jenny "Mmhrmm."
    return

label jenny_shower_bj_cum:
    anon "I'm getting close!"
    jenny "{i}*Sluuuuurp*{/i}"
    pause
    anon "{b}[jen_name]{/b}!"
    pause
    show jenny_shower_bj cum
    anon "HNNGGG!!!" with flash
    jenny "!!!"
    show jenny_shower_bj after with dissolve
    pause
    call scene_shower_with_vfx
    show jenny b_naked a_hips f_cheeks_surprised
    show anon b_naked f_normal od_naked_dick1
    with fade
    if M_jenny.get("first_shower_time"):
        $ M_jenny.set("first_shower_time", False)
        anon "Phew, that was-"
        anon "I mean, I wasn't expecting you to-"
        show anon f_surprised
        show jenny f_cheeks_swallow a_shocked with dissolve
        anon @ -m_talk "!!!"
        show jenny f_normal
        jenny "Damn, that was a lot of cum!"
        show jenny a_hips with dissolve
        anon f_worried "You swallowed it!"
        show anon f_surprised
        jenny "Yeah, so?"
        anon f_normal "I thought you didn't like doing that?!"
        show jenny f_upset
        jenny "When did I ever say that?"
        anon f_skeptical "When you blew me on stream!"
        anon "You said you only swallowed because your fans pay extra for it!"
        show jenny f_normal
        jenny "Oh, right..."
        anon "They can't see us in here, {b}[jen_name]{/b}!"
        show jenny f_upset
        jenny "Maybe I didn't wanna make a mess, you ever think of that?!"
        anon f_worried "You didn't wanna make a mess... In the shower?"
        jenny @ -m_talk "..."
        jenny "Oh my god, just-"
        jenny "Whatever."
        show jenny f_eyeroll
        jenny "{i}*Sigh*{/i} I like it, okay?"
        show jenny f_upset
        anon f_surprised @ -m_talk "..."
        jenny "I like swallowing your cum..."
        jenny "Are you fucking happy now?!"
        anon f_normal "Heh, I can't believe you just said that..."
        show jenny f_eyeroll a_crossed with dissolve
        jenny "Ugh..."
        show jenny f_upset
        jenny "Don't get any ideas, loser!"
        jenny "Just because I like your cum and your big cock, it doesn't mean I like you!"
        anon f_worried @ -m_talk "..."
        jenny "Now go away and let me finish my shower!"
        anon "Alright."
        anon f_normal "Thanks for the-"
        show anon f_surprised
        show jenny f_angry
        jenny "Get out!!"
        hide anon with dissolve
        jenny "For fuck's sake!"
        show jenny f_angry_pouting

        $ player.go_to(L_home_hallway)
        scene expression player.location.background_blur
        show anon f_grin with dissolve
        anon @ -m_talk "( That was so awesome! )"
        anon @ -m_talk "( Does this mean {b}I can join her in the shower whenever I want{/b}? )"
        show anon f_thinking a_thinking with dissolve
        pause
        anon f_grin @ -m_talk "( I think it does! )"
    else:
        anon "Phew..."
        anon "You're getting really good at that!"
        show jenny f_cheeks_swallow a_shocked with dissolve
        pause
        show jenny f_grin
        jenny "Pfft, was I ever not good at it?"
        anon "Heh, good point."
        pause
        show jenny f_normal
        jenny "Alright, beat it so I can finish my shower."
        anon "Yeah, okay."
        anon "Thanks for the blowjob!"
        show anon f_grin
        show jenny f_eyeroll a_crossed with dissolve
        jenny "Oh my god."
        show jenny f_upset
        jenny "Get out!"
    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["13_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_hallway)
    $ game.main()

label jenny_mc_room_sex_on_sleep:
    if store._in_replay is not None:
        $ player.location = L_home_bedroom
    $ game.timer.tick(3)
    scene expression "backgrounds/location_home_bedroom_cutscene18.jpg"
    jenny "Psst!"
    jenny "{b}[firstname]{/b}, you awake?"
    scene expression "backgrounds/location_home_bedroom_cutscene17.jpg"
    anon "Mmm."
    pause
    scene expression "backgrounds/location_home_bedroom_sex01c.jpg"
    show anon b_visit f_visit_sleep
    show jenny b_visit_sit a_down f_visit_sexy with dissolve
    if M_jenny.is_state(S_jenny_night_time_sex):
        jenny "{b}[firstname]{/b}?"
        anon "Nnnhhh."
        pause
        jenny "C'mon, wake up."
        anon "NNNHHH!"
        show jenny f_visit_sexy_down a_reach with dissolve
        anon f_visit_normal "Damn it, {b}[jen_name]{/b}..."
        anon "It's the middle of the night!"
        show anon b_visit_up2 f_visit_up_tired
        show jenny a_pull
        with dissolve
        jenny "Oh, shut up."
        show jenny f_visit_sexy_down a_up with dissolve
        show jenny a_up2 with dissolve
        pause
        show jenny a_stroke with dissolve
        anon "What are you doing, {b}[jen_name]{/b}?"
        anon "I'm trying to slee-"
        show jenny f_visit_sexy_down
        jenny "What does it look like I'm doing?!"
        show jenny b_visit_remove1
        show jenny_arms_visit_a_dick
        with dissolve
        show anon f_visit_up_surprised
        pause
        show jenny b_visit_remove2 with dissolve
        anon f_visit_up_tired "We really have to do this, right now?!"
        hide jenny_arms_visit_a_dick
        show jenny b_visit_climb
        with dissolve
        jenny "Yes, I'm fucking horny and I want it right now!"

        scene expression "backgrounds/location_home_bedroom_sex05.jpg"
        show jenny_mc_room_sex insert
        with fade
        anon "!!!"
        anon "Damn it {b}[jen_name]{/b}, I'm tired..."
        jenny "Oh, for fuck's sake... All you have to do is lay there!"
        jenny "I'm the one doing all the work!"
        show jenny_mc_room_sex 1 with dissolve
        jenny "{i}*Gasp*{/i}"
        jenny "God, I love your dick!"
        jump jenny_mc_room_sex_start
    else:
        jenny "Wake up, {b}[firstname]{/b}."
        show jenny f_visit_sexy
        anon f_visit_normal "{b}[jen_name]{/b}?"
        show jenny a_reach with dissolve
        jenny "C'mon, I need it."
        show anon b_visit_up2 f_visit_up_tired
        show jenny f_visit_sexy_down a_pull
        with dissolve
        pause
        show jenny a_up with dissolve
        show jenny a_up2 with dissolve
        pause
        show jenny a_stroke with dissolve
        menu:
            "Right now?":
                anon f_visit_up_tired "Right now?"
                show jenny b_visit_remove1
                show jenny_arms_visit_a_dick
                with dissolve
                show anon f_visit_up_surprised
                pause
                show jenny b_visit_remove2 with dissolve
                pause
                hide jenny_arms_visit_a_dick
                show jenny b_visit_climb
                with dissolve
                jenny "Yes, I want it right now."

                scene expression "backgrounds/location_home_bedroom_sex05.jpg"
                show jenny_mc_room_sex insert
                with fade
                anon "!!!"
                anon "O-okay."
                jenny "God, I can't get this dick out of my head!"
                anon "Wow, you're really wet..."
                show jenny_mc_room_sex 1 with dissolve
                jenny "{i}*Gasp*{/i}"
                jenny "Ohh, fuck."
                jump jenny_mc_room_sex_start
            "Not tonight." if store._in_replay is None:
                if M_jenny.get("dominance") <= 0:
                    anon f_visit_up_tired "Not right now, {b}[jen_name]{/b}."
                    show jenny f_visit_sexy_down
                    jenny "C'mon, you know you want it..."
                    anon "Let's just do it tomorrow, okay?"
                    show jenny f_visit_sexy
                    jenny "I don't want it tomorrow, I want it now!"
                    show jenny f_visit_sexy_down
                    anon "Ahhh, I'm tiiiiired..."
                    show jenny f_visit_angry a_up2 with dissolve
                    jenny "Seriously?!"
                    jenny "You've got a mega hot girl stroking you cock right now and you're saying no?!"
                    anon "{i}*Sigh*{/i} I'm sorry... I didn't-"
                    jenny "Just forget it!"
                    anon "N-no, we can if you really want to-"
                    jenny "I'm not in the mood anymore!"
                    hide jenny
                    show jenny_arms_visit_a_dick
                    with dissolve
                    jenny "You are such a little bitch sometimes, I swear!"
                    anon "{b}[jen_name]{/b}, I'm sorry, I-"
                    anon @ -m_talk "..."
                else:
                    anon "Not right now, {b}[jen_name]{/b}."
                    show jenny f_visit_sexy_down
                    jenny "C'mon, you know you want it..."
                    anon "No, I just wanna sleep... Okay?"
                    show jenny f_visit_sexy
                    jenny "Please, {b}[firstname]{/b}?"
                    anon "I said no!"
                    show jenny f_visit_angry a_up2 with dissolve
                    jenny "Seriously?!"
                    jenny "I'm trying to be nice here, the way you like it... I even said please!"
                    anon "I'm just not in the mood, okay?"
                    jenny @ -m_talk "..."
                    jenny "FINE!"
                    hide jenny
                    show jenny_arms_visit_a_dick
                    with dissolve
                    jenny "I don't know why I waste my time on you..."
                    anon "Whatever."
                jump resume_sleeping_bedroom

label jenny_mc_room_sex_start:
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    show expression AnimatedImage("jenny_mc_room_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
    jenny "Ahh!"
    pause
    anon "Okay, that feels really good..."
    if M_jenny.is_state(S_jenny_night_time_sex):
        jenny "See, and you were all whining about it!"
        anon "Well, we could have done this tomorrow!"
        jenny "Yeah, and we probably will..."
        anon "R-really?"
        jenny "Uhh, yeah... Camshows, dummy."
        anon "Oh, right."
        jenny "Just shut up and let me enjoy this!"
    else:
        jenny "Ahh!"
        pause
        anon "Okay, that feels really good..."
        jenny "Yeah, it does!"
    pause
    jenny "Ahh, fuuuuck!"
    pause
    jenny "Mmm, I'm gonna cum all over that big dick of yours, {b}[firstname]{/b}!"
    if M_jenny.get("dominance") <= 0:
        jenny "You'd like that, wouldn't you?!"
        anon "Y-yes."
        if M_jenny.get("sex speed") > 0.061:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.03)
        jenny "Ahh!"
        jenny "C'mon, say it!"
        jenny "Say you want me to cum on your big dick!"
        anon "I want you to cum on my big dick!"
        if not M_jenny.is_state(S_jenny_night_time_sex):
            jenny "I think you can do better..."
            pause
            jenny "Tell me I'm a sex goddess!"
            anon "Y-you're a sex goddess!"
            jenny "Come on, bitch!"
            jenny "I can't hear you!"
            anon "You're a sex goddess!!!"
            jenny "You worship this pussy, don't you?!"
            anon "Y-yes!"
        jenny "Hahahaah!!"
    else:
        anon "Then do it!"
        if M_jenny.get("sex speed") > 0.061:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.03)
        jenny "Ahh, shit!"
        anon "Tell me you want it!"
        jenny "Mmm, I want it!"
        pause
        anon "C'mon {b}[jen_name]{/b}, faster!"
        jenny "Oh my god!"
        pause
        if M_jenny.is_state(S_jenny_night_time_sex):
            jenny "Ahh, fuck me!!"
        else:
            anon "Beg me to give it to you!"
            jenny "Ahh!"
            jenny "Please!!"
            pause
            anon "C'mon, you can do better!"
            jenny "Fuuuuck!"
            jenny "Please, {b}[firstname]{/b}!!"
            jenny "Give it to me!!!"

    anon "Shh!"
    anon "You're gonna wake up {b}[deb_name]{/b}..."
    jenny "I don't fucking care!"
    pause
    jenny "Ahh, I'm so close!"

label jenny_mc_room_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_mc_room_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_mc_room_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_mc_room_sex {}".format(pose_list[pose_counter]) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_mc_room_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_mc_room_sex_options

label jenny_mc_room_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jenny "Ahh, fuuuuck!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jenny "Fuuuuck!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jenny "Hahahaah!!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        anon "Oh my god!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jenny "Ahh, fuck me!!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        anon "I'm getting close...{p=1}{nw}"
    return

label jenny_mc_room_sex_cum_inside:
    jenny "Oh my god, oh my god, OH MY GOD!"
    pause
    jenny "I'm cumming! I'm cumming!"
    anon "Me too!"
    jenny "AAAHHH, FUCK!!!"
    anon "{b}[jen_name]{/b}, get off!"
    jenny "NGGHHH!!!"
    anon "Ah, crap!"
    $ M_jenny.set('sex speed', .4)
    show expression AnimatedImage("jenny_mc_room_sex cum", [1,2], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
    anon "HNNGGG!!!" with flash
    show jenny_mc_room_sex cum 2
    show xray_jenny_mcbedroom:
        align (0,0)
    pause
    call call_pregnancy_minigame ("jenny_mc_room_sex_cum_inside_post_pregnancy_minigame", M_jenny)

label jenny_mc_room_sex_cum_inside_post_pregnancy_minigame:
    scene expression "backgrounds/location_home_bedroom_sex05.jpg"
    show jenny_mc_room_sex pullout
    with fade
    anon "Haah... Haah..."
    hide jenny_mc_room_sex
    show jenny b_visit_after f_visit_after_angry_down o_visit_after_creampie
    with dissolve
    jenny "Oh my god..."
    pause
    show jenny f_visit_after_angry
    jenny "Did you cum in me?!"
    anon "I told you to get off me!"
    jenny "Goddamnit, {b}[firstname]{/b}!"
    anon "What?!"
    jenny "I could get pregnant you moron!"
    anon "Well, I'm sorry but I did warn you..."
    jenny "Ugh, whatever."
    show jenny f_visit_after_angry_down
    pause
    show jenny f_visit_after_normal
    jenny "{i}*Sigh*{/i} Fuck it..."
    jenny "Heh, my legs are shaking like crazy!"
    if M_jenny.get('girlfriend_in_progress'):
        jump jenny_mc_room_sex_end_girlfriend_experience
    else:
        jump jenny_mc_room_sex_end

label jenny_mc_room_sex_cum_outside:
    jenny "Oh my god, oh my god, OH MY GOD!"
    pause
    jenny "I'm cumming! I'm cumming!"
    jenny "NGGHHH!!!"
    pause
    anon "Me too!"
    show jenny_mc_room_sex cumshot
    anon "HNNGGG!!!{p=1}{nw}" with flash
    show jenny o_visit_cumshot f_empty a_empty b_empty
    pause
    hide jenny_mc_room_sex
    show jenny b_visit_after f_visit_after_normal o_visit_cumshot2
    with dissolve
    anon "Haah... Haah..."
    jenny "Phew, that was awesome..."
    pause
    jenny "Hahaha, you're a fucking mess!"
    anon "Heh, I don't even care... I'm so exhausted."
    jenny "{i}*Snort*{/i} Hehehe!"
    jenny "You should clean yourself up, you look ridiculous..."
    if M_jenny.get('girlfriend_in_progress'):
        jump jenny_mc_room_sex_end_girlfriend_experience
    else:
        jump jenny_mc_room_sex_end

label jenny_mc_room_sex_end_girlfriend_experience:
    scene expression "backgrounds/location_home_bedroom_bed.jpg"
    show jenny b_sleep_side_naked a_side f_sleep_side_tired:
        flip
        xoffset 500
    show anon b_sleep_side f_sleep_side_normal a_poke o_sleep_side_dick2
    show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent2.png"
    with fade
    if M_jenny.get("jenny_girlfriend_first_time"):
        anon "Tonight was a lot of fun!"
        show jenny f_sleep_side_tired
        jenny "I'm glad you enjoyed yourself."
        anon "... And I'm really happy you're not rushing off this time."
        jenny "Well, you did pay me not to, remember?"
        anon "Yeah."
        jenny "Hahahaah!"
        anon "You had fun too, didn't you?"
        show jenny f_sleep_side_rolleye
        jenny "Yes, {b}[firstname]{/b}..."
        show jenny f_sleep_side_tired
        jenny "Now can you shut up and let me sleep?"
        show jenny f_sleep_side_sleeping
        anon "Sorry..."
        show anon f_sleep_side_kiss
    else:
        anon "Hehe, I'm really enjoying the nights we do this..."
        show jenny f_sleep_side_tired
        jenny "Yeah, me too."
        jenny "I'm glad I came up with the idea."
        anon "Uhh, you know, this was technically MY idea..."
        jenny "Oh, shut up!"
        anon "I'm just saying..."
        jenny "Yeah, I know what you're saying... Now zip it!"
        jenny "You're ruining my post-coital bliss."
        anon "Sorry."
        show jenny f_sleep_side_rolleye
        jenny "Go to sleep."
        show jenny f_sleep_side_sleeping
        show anon f_sleep_side_kiss
    $ M_jenny.set('had_sex_bedroom', True)
    jump resume_sleeping_bedroom

label jenny_mc_room_sex_end:
    show jenny f_visit_after_normal
    if M_jenny.is_state(S_jenny_night_time_sex):
        anon "You staying?"
    else:
        anon "You leaving again?"
    jenny "Hmm?"
    if M_jenny.is_state(S_jenny_night_time_sex):
        anon "Do you wanna sleep here with me tonight?"
        jenny "Eww, no!"
        jenny "I'm not your fucking girlfriend, doofus..."
    else:
        anon "You can sleep here, you know?"
        jenny "For fuck's sake..."
        jenny "Didn't we go over this already?"

    if store._in_replay is not None:
        $ player.location = L_home_bedroom

    scene expression player.location.background_blur with None
    show jenny b_naked a_sides f_normal o_empty:
        xoffset -400
    show anon b_underwear f_skeptical at flip
    with dissolve
    if M_jenny.is_state(S_jenny_night_time_sex):
        anon "Wait!"
    else:
        anon "Alright, fine... Whatever."
    show anon f_worried
    hide jenny
    if M_jenny.is_state(S_jenny_night_time_sex):
        $ M_jenny.trigger(T_jenny_didnt_sleep_much)
        show jenny b_naked a_crossed f_upset at flip
        with dissolve
        jenny "What, {b}[firstname]{/b}?!"
        anon "I wasn't trying to-"
        anon "{i}*Sigh*{/i} Just, explain this to me..."
        anon @ f_skeptical "So, we can have sex whenever we want but you won't sleep in my bed?"
        show jenny f_eyeroll
        jenny "Umm, no... We can have sex whenever {i}I{/i} want..."
        show jenny f_upset
        jenny "... So long as it doesn't interfere with my camshows."
        pause
        jenny "... And no, I won't sleep in your bed!"
        jenny "I'm not your fucking girlfriend, and you're sure as hell not my boyfriend!!!"
        jenny "Get that through your thick skull, dummy!"
        anon f_skeptical "I don't get you at all..."
        jenny "Yeah, well... You don't have to {i}get{/i} me."
        jenny "That's just the way things are."
        jenny "Deal with it."
        anon @ -m_talk "..."
    else:
        show jenny b_naked a_crossed f_upset at flip
        with dissolve
        anon f_skeptical "Just forget I said anything."
        jenny "Gladly."
        pause
    show jenny f_upset
    jenny "Now go to sleep!"
    show jenny f_grin
    jenny "My fans are expecting a good show tomorrow."
    hide jenny with dissolve
    pause
    anon f_worried @ -m_talk "..."
    scene black with fade
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["12_unlocked"] = True
    jump resume_sleeping_bedroom

label jenny_sex_intro_repeat:
    show anon f_worried
    anon "Sex. Please."
    show jenny f_upset
    jenny "Hurry up."
    show jenny f_grin_down b_pull1 with dissolve
    pause
    show jenny b_pull2 with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show anon f_surprised
    pause
    show jenny b_panties a_hips f_upset with dissolve
    jenny "Well?"
    anon @ -m_talk "Hmm?"
    jenny "Get those clothes off!"
    show jenny b_naked f_grin_down a_panties_remove with dissolve
    anon f_worried "R-right..."
    show anon b_dressed_changing
    show jenny b_cheer_dress1
    with dissolve
    pause
    show jenny b_cheer_dress3 f_grin_down with dissolve
    pause
    show jenny b_cheer_dress2 with dissolve
    show anon f_worried b_shorts with dissolve
    anon "You're going to wear that again?"
    show jenny b_cheer a_hips f_sexy with dissolve
    jenny "Of course!"
    jenny "My fans like it."
    show anon b_dressed_changing2 with dissolve
    anon "..."
    show anon b_underwear f_worried with dissolve
    jenny "Get on the bed."
    hide anon with dissolve
    pause
    jenny "... And put your mask on!"
    label finger_blasting_sex:
    scene black with fade
    pause
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show anon b_bed_jenny_sit f_shy_down of_mask
    show jenny o_under_body_laptop o_naked_bed_belly_cheer b_naked_bed_bellytype f_sexy_down
    with dissolve
    pause
    jenny "You boys ready for another show?"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    show jenny f_laugh
    jenny "Hehehe!"
    show jenny f_sexy_down
    jenny "Alright, let me get things ready..."
    show jenny b_bed_climbing o_cheer_bed_climbing
    show anon b_bed_jenny_laying_undies_arms of_bed_jenny_laying_undies_arms_mask_X
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick7.png" zorder 2
    show expression "characters/jenny/layeredimage/jenny_overlay_o_laptop.png"
    with dissolve
    jump jenny_cheer_sex_intro_prepare

label jenny_cheer_sex_intro_prepare:
    anon "Are we really going to-"
    jenny "Shh!"
    pause
    show jenny b_bed_back_sit o_cheer_bed_back
    show expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_handcuffs.png" zorder 1
    with dissolve
    anon "Aww, c'mon {b}[jen_name]{/b}!"
    anon "You know I hate these things..."
    show jenny a_sit_tie
    hide expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_handcuffs.png"
    show expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_tie.png" zorder 1
    show anon oh_bed_jenny_laying_undies_handcuffs
    with dissolve
    jenny "Shut your mouth!"
    if M_jenny.get("dominance") <= 0:
        anon "..."
        pause
        show jenny a_sit_hips
        hide expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_tie.png"
        show expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_hips.png" zorder 1
        with dissolve
        if M_jenny.finished_inclusive(S_jenny_end) or store._in_replay:
            jenny "And if you hate them that much, quit moaning about them and do something."
            jenny "They're only plastic, I'm sure the boys would love to see you try and {b}break free{/b}!"
        else:
            jenny "Good."
        jenny "Now, beg for it."
        anon "What?!"
        jenny "You want me to take that big cock of yours for a ride, don't you?"
        anon "Y-yes..."
        jenny "Then you're going to beg me for it, in front of my fans!"
        anon "..."
        jenny "Go on!"
        anon "Please..."
        jenny "Princess!"
        anon "..."
        anon "Please, {b}Princess [jen_name]{/b}..."
        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
        jenny "HAHAHAAH!"
        show jenny b_bed_front_sit a_pull1 f_sexy_down o_cheer_bed_front_sit2
        hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick7.png"
        hide expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_hips.png"
        with dissolve
        pause
        show jenny a_pull2 o_cheer_bed_front_sit3 with dissolve
        jenny "You boys ready?"
    else:
        anon "I don't like them!"
        jenny "HOLD STILL!"
        anon "Grr!"
        jenny "I'm in charge here, not you!"
        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
        show jenny a_hips
        hide expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_tie.png"
        show expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_hips.png" zorder 1
        with dissolve
        jenny "There!"
        jenny "Sheesh, I don't know what you're complaining about..."
        show jenny b_bed_front_sit a_pull1 f_sexy_down o_cheer_bed_front_sit2
        hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick7.png"
        hide expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_hips.png"
        with dissolve
        jenny "Here I am, offering to fuck your brains out, and you're whining about stupid handcuffs!"
        show jenny a_pull2 o_cheer_bed_front_sit3 with dissolve
        jenny "You boys wouldn't put up a fight, would you?!"
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick6.png"
    show jenny a_sides f_sexy_down o_cheer_bed_front_sit
    with dissolve
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    jenny "Heh, they're excited..."
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg"
    show jenny_cheer_sex tied insert
    with fade
    jenny "( Here we go, {b}[firstname]{/b}... The moment you've been dreaming of! )"
    jenny "Ohh!"
    jenny "Holy shit!"
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .09)
    show expression AnimatedImage("jenny_cheer_sex_tied_mask", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
    jenny "Oh my god, you guys..."
    jenny "This is a REALLY big dick!"
    jump jenny_cheer_sex_loop_tied

label jenny_cheer_sex_loop_tied:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_jenny.get("cam show mask"):
                    show expression AnimatedImage("jenny_cheer_sex_tied_mask", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression AnimatedImage("jenny_cheer_sex_tied", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_cheer_sex_hscene_dialog_tied")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
            $ poses_done = []
            while poses_done != pose_list:
                if M_jenny.get("cam show mask"):
                    show expression "jenny_cheer_sex_tied_mask {}".format(pose_list[pose_counter]) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression "jenny_cheer_sex_tied {}".format(pose_list[pose_counter]) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_cheer_sex_hscene_dialog_tied")
        $ animcounter += 1
    call screen jenny_cheer_sex_options_tied

label jenny_cheer_sex_hscene_dialog_tied:
    if animcounter == 0 and randomizer() < 10:
        jenny "Ahh!{p=1}{nw}"
    if animcounter == 0 and randomizer() < 10:
        jenny "This is so fucking good!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jenny "Oh, fuck!{p=1}{nw}"
        jenny "I'm gonna squirt all over that big dick!{p=2}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jenny "Mmm, fuck!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jenny "It's so good!!{p=1}{nw}"
        anon "I'm getting close!{p=1}{nw}"
        jenny "SO FUCKING GOOD!!{p=1}{nw}"
        anon "{b}[jen_name]{/b}!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        anon "You're really good at this!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 5:
        jenny "You like that, don't you?!{p=1}{nw}"
        anon "Y-yeah.{p=1}{nw}"
        jenny "Tell me you like it!{p=1}{nw}"
        anon "I like it!{p=1}{nw}"
        jenny "Tell me you love my pussy!{p=1}{nw}"
        anon "Ahh, I love it!{p=1}{nw}"
        jenny "Hahahaah!{p=1}{nw}"
        if M_jenny.get("sex speed") > 0.031:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.03)
        jenny "Mmm, yeah!{p=1}{nw}"
    return

label jenny_cheer_sex_cum_inside_tied:
    if M_jenny.is_state(S_jenny_cheerleader_sex):
        anon "I can't hold it!"
    else:
        anon "Get off!"
    pause
    anon "{b}[jen_name]{/b}!!!"
    jenny "NGGHHH!!!"
    anon "I can't-"
    pause
    show jenny_cheer_sex tied cum
    anon "HNNGGG!!!" with flash
    show jenny_cheer_sex tied cum 2
    show xray_jenny_cheer_bedroom:
        align (0,0)
    pause
    call call_pregnancy_minigame ("jenny_cheer_sex_cum_inside_tied_post_pregnancy", M_jenny)

label jenny_cheer_sex_cum_inside_tied_post_pregnancy:
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg"
    show jenny_cheer_sex tied pullout 1
    with fade
    jenny "Haah... Haaah..."
    show jenny_cheer_sex tied pullout 2 with dissolve
    jenny "Fuuuck, that was incredi-"
    show jenny_cheer_sex tied pullout 3 with dissolve
    jenny "!!!"
    show jenny_cheer_sex tied pullout 4 with dissolve
    if M_jenny.is_state(S_jenny_cheerleader_sex):
        jenny "Did you cum inside me?!"
        anon "Y-you told me not to stop..."
        jenny "Yeah, but I didn't say to finish inside me you idiot!"
        anon "I'm sorry, I didn't mean to-"
        jenny "What if I get pregnant?!"
        anon "..."
    else:
        jenny "Did you cum inside me?!"
        anon "I warned you!"
        jenny "I didn't hear anything!"
        anon "Well, what do you want me to do?!"
        anon "I'm handcuffed to your bed!"
        jenny "I could get pregnant you moron!"
        anon "Then you should have gotten off when I warned you!"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    jenny "Oh for fuck's sake..."
    jump jenny_cheer_sex_aftermath

label jenny_cheer_sex_cum_outside_tied:
    anon "I'm going to cum!"
    jenny "Hold it!"
    anon "W-what?! It doesn't work like that!"
    jenny "I'm so close!"
    anon "{b}[jen_name]{/b}!!!"
    jenny "FUCK!!"
    show jenny_cheer_sex tied cumshot
    show jenny_cheer_sex_mc tied cumshot initial
    anon "HNNGGG!!!" with flash
    show jenny_cheer_sex_mc tied cumshot
    pause
    anon "Haah... Haah..."
    jenny "You couldn't have lasted another ten seconds?!"
    if randomizer() > 50:
        anon "S-sorry."
    else:
        anon "It's difficult when I'm handcuffed to the bed!"
    jenny "Whatever..."
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    jenny "Oh for fuck's sake..."
    jump jenny_cheer_sex_aftermath

label jenny_cheer_sex_break_free:
    if player.has_required_str(7) or store._in_replay is not None:
        $ display.toast(str_pass)
        show jenny_cheer_sex free break
        jenny "!!!" with hpunch
        $ animated = True
        $ anim_toggle = True
        $ M_jenny.set('sex speed', .08)
        if M_jenny.get("cam show mask"):
            show expression AnimatedImage("jenny_cheer_sex_free_mask", [1,2,3,4,5], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
        else:
            show expression AnimatedImage("jenny_cheer_sex_free", [1,2,3,4,5], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
        jenny "OH FUCK!!{p=1}{nw}"
        pause 1
        jenny "OHMYGOD, OHMYGOD, OHMYGOD!!!{p=1}{nw}"
        pause 1
        jenny "AHHH!!!{p=1}{nw}"
        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}{p=1}{nw}"
        pause 1
        jenny "FUUUUCK MEEEE!!!{p=1}{nw}"

        label jenny_cheer_sex_loop_free:
            show screen sex_anim_buttons
            pause
            hide screen sex_anim_buttons
            $ animcounter = 0
            while animcounter < 4:
                if anim_toggle:
                    if not animated:
                        if M_jenny.get("cam show mask"):
                            show expression AnimatedImage("jenny_cheer_sex_free_mask", [1,2,3,4,5], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                        else:
                            show expression AnimatedImage("jenny_cheer_sex_free", [1,2,3,4,5], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                        $ animated = True
                    pause 5
                    call expression game.dialog_select("jenny_cheer_sex_hscene_dialog_free")
                    pause 3
                else:

                    $ pose_counter = 0
                    $ pose_list = [1,2,3,4,5]
                    $ poses_done = []
                    while poses_done != pose_list:
                        if M_jenny.get("cam show mask"):
                            show expression "jenny_cheer_sex_free_mask {}".format(pose_list[pose_counter]) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                        else:
                            show expression "jenny_cheer_sex_free {}".format(pose_list[pose_counter]) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                        pause
                        $ poses_done.append(pose_list[pose_counter])
                        $ pose_counter += 1
                    call expression game.dialog_select("jenny_cheer_sex_hscene_dialog_free")
                $ animcounter += 1
            call screen jenny_cheer_sex_options_free

        label jenny_cheer_sex_hscene_dialog_free:
            if animcounter == 0 and randomizer() < 30:
                jenny "OH FUCK!!{p=1}{nw}"
            if animcounter == 1 and randomizer() < 10:
                jenny "FUCK ME!{p=.5}{nw}"
                jenny "FUCK ME!{p=.5}{nw}"
                jenny "FUUUUCK MEEEE!!!{p=1}{nw}"
            if animcounter == 2 and randomizer() < 30:
                jenny "AHHH!!!{p=1}{nw}"
            return
    else:

        $ display.toast(str_fail)
        jenny "Oh my god!{p=1}{nw}"
        pause 1
        jenny "Fuck me!{p=1}{nw}"
        pause 1
        jenny "FUCK ME!!{p=1}{nw}"
        jump jenny_cheer_sex_loop_tied

label jenny_cheer_sex_cum_inside_free:
    anon "I'm getting close!"
    pause
    jenny "Don't stop!"
    anon "{b}[jen_name]{/b}, I can't-"
    jenny "DON'T STOP!"
    pause
    jenny "NGGHHH!!!"
    show jenny_cheer_sex free cum
    anon "HNNGGG!!!" with flash
    show jenny_cheer_sex free cum 2
    show xray_jenny_cheer_bedroom:
        align (0,0)
    pause
    call call_pregnancy_minigame ("jenny_cheer_sex_cum_inside_free_post_pregnancy", M_jenny)

label jenny_cheer_sex_cum_inside_free_post_pregnancy:
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg"
    show jenny_cheer_sex free pullout 1
    with fade
    jenny "Haah... Haaah..."
    show jenny_cheer_sex free pullout 2 with dissolve
    jenny "Fuuuck, that was incredi-"
    show jenny_cheer_sex free pullout 3 with dissolve
    jenny "!!!"
    show jenny_cheer_sex free pullout 4 with dissolve
    jenny "Did you cum inside me?!"
    anon "You told me not to stop..."
    jenny "I didn't mean for you to cum inside me, idiot!"
    anon "Don't start in with the name-calling..."
    jenny "What if I get pregnant!!"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    jenny "Oh for fuck's sake..."
    jump jenny_cheer_sex_aftermath

label jenny_cheer_sex_cum_outside_free:
    anon "I'm getting close!"
    pause
    jenny "Don't stop!"
    anon "{b}[jen_name]{/b}, I can't-"
    jenny "DON'T STOP!"
    pause
    jenny "NGGHHH!!!"
    show jenny_cheer_sex free cumshot
    show jenny_cheer_sex_mc tied cumshot initial
    anon "HNNGGG!!!" with flash
    show jenny_cheer_sex_mc tied cumshot
    pause
    anon "Haah... Haah..."
    jenny "What the fuck, I told you not to stop!!"
    anon "What, do you want me to cum inside you?!"
    jenny "N-no, it just... Felt really good and-"
    jenny "{i}*Sigh*{/i} Never mind..."
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    jenny "Oh for fuck's sake..."
    jenny "Show's over, pervs!"
    jenny "Tune in next time!"
    jump jenny_cheer_sex_aftermath

label jenny_cheer_sex_aftermath:
    scene expression game.timer.image("backgrounds/location_home_jennybedroom{}.jpg")
    show jenny f_upset b_cheer a_hips
    show anon b_underwear
    with dissolve
    anon "That was awesome!"
    show jenny f_eyeroll
    jenny "Yeah, whatever."
    show jenny f_upset
    jenny "You were alright."
    show anon f_worried
    jenny "Now, get out!"
    anon "Can't we just-"
    show jenny a_hips_money
    jenny "No, take your stupid money and get out!"
    hide jenny with dissolve
    anon "Alright, sheesh..."
    hide anon with dissolve
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with None
    show anon f_grin with dissolve
    anon @ -m_talk "( I just had sex with {b}[jen_name]{/b}... )"
    anon @ -m_talk "( On camera in front of hundreds of people! )"
    pause
    anon @ -m_talk "( How crazy is that?! )"
    anon @ -m_talk "( I hope we do it again. )"
    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["11_unlocked"] = True
    call popup ('earn', 200)
    $ M_jenny.trigger(T_jenny_had_cheerleader_sex)
    $ player.get_money(200)
    $ game.timer.tick()
    $ player.go_to(L_home_hallway)
    $ game.main()

label jenny_cunni_intro_repeat:
    show anon f_worried
    anon "So no camshow today?"
    show jenny f_upset
    jenny "No, I'm not in the mood..."
    anon "What?!"
    anon "You're always in the mood."
    jenny "To be gawked at, asshole!"
    jenny "I'm not in the mood to be gawked at!"
    anon f_laugh "Oh heh. Gotcha."
    show anon f_normal
    jenny "I need a day off..."
    show anon f_grumpy:
        flip
        xoffset -500
    with dissolve
    anon "I'll leave you to it then."
    jenny "Wait."
    hide anon
    show anon f_normal
    with dissolve
    anon @ -m_talk "..."
    show jenny f_grin
    jenny "Since you're already here..."
    anon f_worried @ -m_talk "Hmm?"
    jenny "C'mon."

    label finger_blasting_cunni:
    scene location_home_hallway_cutscene
    with fade
    anon "Where are we going?!"
    jenny "I think you need more practice..."
    anon "W-why are we going to my room?!"
    jenny "Oh, shut up!"

    $ player.go_to(L_home_bedroom)
    scene expression player.location.background_blur
    show anon f_worried
    show jenny b_dressed_panties_remove_down
    with fade
    pause
    show jenny b_pantieless a_hips f_grin with dissolve
    anon "What are you doing?"
    jenny "You're going to lick my pussy."
    if M_jenny.get("dominance") <= 0:
        anon "I am?"
        jenny "Yup."
        jenny "C'mon, loser!"
        jenny "I'm going to cum all over that idiot face of yours!"
    else:
        anon "Oh really?"
        jenny "Yup."
        anon "Maybe if you ask me nicely."
        show jenny f_upset
        jenny "Ugh, you're still hung up on that shit?!"
        show anon f_skeptical
        if randomizer() > 50:
            anon "If you wanna go back to masturbating, suit yourself..."
        else:
            anon "I'm not your little whipping boy, {b}[jen_name]{/b}..."
        jenny "Grr, you are such a pain in the ass!"
        jenny "Fine."
        show jenny f_angry_pouting a_crossed with dissolve
        pause
        show jenny f_upset
        jenny "{b}[firstname]{/b}, would you please lick my pussy?"
        anon @ f_laugh "Haha, sure!"
        show jenny f_eyeroll
        jenny "Just, c'mon!"
    jump jenny_cunni_repeat


label jenny_cunni_repeat:
    scene bedroom_sex2
    if M_jenny.is_state(S_jenny_give_cunni):
        show jennysex 135 at right
    else:
        show jennysex 137 at right
    show jennysex_cunnilingus_player at right
    with fade
    if M_jenny.is_state(S_jenny_give_cunni):
        jenny "Hehe, remember that cum you shot all over my comforter?!"
        jenny "It's payback time, bitch!"
        show jennysex 134
        anon "Hey, I washed it for you!"
        show jennysex 135
        jenny "Hahaha!"
        show jennysex 137 with dissolve
    pause
    show jennysex 137b
    jenny "Well, what are you waiting for, an invitation?!"
    jenny "Lick my puss-"
    $ M_jenny.set('sex speed', .3)
    show expression AnimatedImage("jenny_lick_shirt", [1,2,3,4], M_jenny) as jennysex at Position(xalign = 0.0, yoffset = 0)
    hide jennysex_cunnilingus_player
    with fastdissolve
    jenny "EEyyyy!!!"
    pause
    jenny "Fuuuuuck!"
    pause
    jenny "Mmm, your tongue feels amazing!"
    jenny "Ahh!"
    pause
    show jennysex 135
    show jennysex_cunnilingus_player at right
    with dissolve
    jenny "Focus on my clit more, dummy!"
    jenny "... And play with my tits too!"
    show jennysex 134
    if M_jenny.get("dominance") <= 0:
        anon "Alright."
        show jennysex 135
        jenny "{i}*Ahem*{/i} Alright, what?"
        show jennysex 134
        anon "{i}*Sigh*{/i} Alright, {b}Princess [jen_name]{/b}..."
        show jennysex 135
        jenny "Hahaha!"
        jenny "That's right, loser!"
    else:
        anon "Ask nicely or I'm stopping..."
        show jennysex 135
        jenny "What?!"
        jenny "Oh my god, you can't stop now!"
        show jennysex 134
        anon "Watch me."
        show jennysex 135
        jenny "No, no, no!"
        show jennysex 134
        jenny "Grr!"
        show jennysex 135
        jenny "Please, play with my tits, {b}[firstname]{/b}..."
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .2)
    show expression AnimatedImage("jenny_lick", [1,2,3,4], M_jenny) as jennysex at Position(xalign = 0.0, yoffset = 0)
    hide jennysex_cunnilingus_player
    with dissolve
    jump jenny_lick_loop

label jenny_lick_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_lick", [1,2,3,4], M_jenny) as jennysex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_lick_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_lick {}".format(pose_list[pose_counter]) as jennysex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_lick_hscene_dialog")
        $ animcounter += 1
    call screen jenny_lick_options

label jenny_lick_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jenny "!!!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jenny "Right there!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jenny "Just like that.{p=1}{nw}"
        jenny "Yesss!!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        jenny "Mmm, I'm getting close!{p=2}{nw}"
    return

label jenny_lick_cum:
    jenny "I'm gonna-"
    jenny "Oh fuck!"
    pause
    show jennysex 143
    jenny "NGGHHH!!!" with flash
    show jennysex 135c
    show jennysex_cunnilingus_player at right
    with dissolve
    jenny "Haah... Haah..."
    show jennysex 134c
    anon "Sheesh, you soaked me."
    pause
    show jennysex 135c
    jenny "Psh, you like it!"
    show jennysex 134c
    anon "Yeah, right..."
    show jennysex 135c
    jenny "Hehehe!"
    hide jennysex
    hide jennysex_cunnilingus_player
    with dissolve
    scene expression player.location.background_blur with None
    show jenny f_normal b_pantieless
    show anon f_worried
    with dissolve
    jenny "Phew, alright... That was pretty good."
    anon "Yeah, for you."
    show jenny f_laugh
    jenny "Hahaha!"
    show jenny f_normal
    jenny "Don't worry, I'll take care of you later."
    show jenny f_grin
    jenny "Maybe..."
    pause
    jenny "... If you're a good boy."
    anon "C'mon, {b}[jen_name]{/b}..."
    show jenny f_upset
    jenny "No."
    show jenny f_grin
    jenny "Besides, don't you have some laundry to do?!"
    anon f_grumpy @ -m_talk "..."
    show jenny a_panties with dissolve
    jenny "Later, loser!"
    hide jenny with dissolve
    jenny "Hahahaah!"
    anon f_unimpressed "{i}*Sigh*{/i}"
    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["10_unlocked"] = True
    $ player.go_to(L_home_bedroom)
    $ game.timer.tick()
    $ M_jenny.trigger(T_jenny_gave_cunni)
    $ game.main()


label jenny_bj_intro_repeat:
    show anon f_worried
    anon "Oral."
    show jenny f_upset
    jenny "Hurry up."
    show jenny f_grin_down b_pull1 with dissolve
    pause
    show jenny b_pull2 with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show anon f_surprised
    pause
    show jenny b_panties a_hips f_upset with dissolve
    jenny "Well?"
    anon @ -m_talk "Hmm?"
    jenny "Get those clothes off!"
    show jenny f_grin_down b_naked a_panties_remove with dissolve
    anon f_worried "R-right..."
    show jenny b_naked_panties_remove_down with dissolve
    pause

    label finger_blasting_bj:
    scene expression "backgrounds/location_home_jennybedroom_cutscene05.jpg"
    with fade
    jenny "You know the drill."
    jenny "Mask on and keep your mouth shut."
    anon "Yeah, I remember."
    jenny "I'll handle the rest."

    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg"
    $ M_jenny.set('cam show mask', True)
    show anon b_bed_jenny_sit f_shy_down of_mask
    show jenny o_under_body_laptop b_naked_bed_bellytype f_sexy_down
    with fade
    jenny "Hi again, everybody!"
    jenny "I brought my boy toy back to give you guys another show."
    pause
    show jenny f_laugh
    jenny "Hehe, of course!"
    show jenny b_bed_climbing
    show anon b_bed_jenny_laying_undies_arms of_bed_jenny_laying_undies_arms_mask_X od_bed_jenny_laying_dick1
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick1.png"
    with dissolve
    pause
    show jenny b_bed_back_sit a_sit_handcuffs with dissolve
    anon "Handcuffs again?!"
    show jenny a_sit_tie
    show anon oh_bed_jenny_laying_undies_handcuffs
    with dissolve
    jenny "Shh!"
    hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick1.png"
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick7.png"
    with dissolve
    anon "{b}[jen_name]{/b}, I don't wanna-"
    jenny "Shut up!"
    show jenny b_bed_back_look a_up f_normal with dissolve
    jenny "There."
    jenny "Let's see if our friend is awake yet, hmm?"
    show jenny b_bed_front_sit a_sides f_sexy_down with dissolve
    hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick7.png"
    show jenny a_pull1
    with dissolve
    pause
    show jenny a_pull2 with dissolve
    jenny "!!!"
    jenny "Hello, big fella."
    hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick6.png"
    show anon od_bed_jenny_laying_dick6
    show jenny b_bed_front_laying
    with dissolve
    jenny "You boys ready to have some fun?"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    anon "What are we going-"
    show jenny b_bed_pussy1
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick6.png"
    anon "!!!" with hpunch
    anon "Mrphmmmll-"
    jenny "What was that, boy toy?"
    jenny "We can't hear you... Hahahaah!"
    show anon od_empty
    show jenny b_bed_pussy
    with dissolve
    pause
    jenny "Mmm, fuck yeah!"
    pause
    show jenny f_nipple2
    jenny "Ahh!"
    show jenny f_nipple3
    pause
    show jenny f_nipple2
    jenny "You're so fucking good at this!"
    show jenny f_nipple3
    anon "Errmmhnnn!"
    show jenny f_nipple2
    jenny "Hahaha!"
    show jenny f_nipple3
    pause
    show jenny f_nipple2
    jenny "I'm getting close!"
    show jenny f_nipple3
    pause
    show jenny f_nipple2
    jenny "Oh, god!"
    jenny "Right there!!"
    show jenny f_nipple3
    pause
    show jenny b_bed_pussy1 f_nipple2
    jenny "NGGHHH!!!" with flash
    pause
    hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick6.png"
    show jenny b_bed_front_laying
    show anon od_bed_jenny_laying_dick6
    with dissolve
    jenny "Haah... Haaah..."
    anon "{i}*Gasp*{/i}"
    anon "{i}*Cough* *Sputter* *Cough*{/i}"
    anon "Damn it, {b}[jen_name]{/b}!"
    anon "You know I can't breathe when you do that!"
    show jenny f_laugh
    jenny "Hehehe!"
    show jenny f_sexy_down
    anon "It's not funny!"
    jenny "Oh, shut up..."
    jenny "My fans don't wanna hear your bitching."
    pause
    jenny "Oh, really?"
    pause
    show jenny f_eyeroll
    jenny "{i}*Sigh*{/i} Again?!"
    show jenny f_sexy_down
    pause
    jenny "Well, I'm not going to do it unless you guys-"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    show jenny f_surprised_down
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    jenny "For fuck's sake..."
    show jenny f_sexy_down
    anon "Now what's happening?"
    jenny "You're about to get your cock sucked again."
    anon "R-really?"
    anon "That's awe-"
    show jenny b_bed_pussy1
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick6.png"
    with dissolve
    anon "Srrrmmmph!"
    jenny "Shut up!"
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg" with None
    show expression AnimatedImage("jenny_bj", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_bj at Position(xalign = 0.0, yoffset = 0)
    anon "Nnnrrrmmph-" with hpunch
    jenny "{i}*Gluullggh*{/i}"
    jump jenny_bj_loop

label jenny_bj_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_bj", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_bj at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_bj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_bj {}".format(pose_list[pose_counter]) as jenny_bj at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_bj_hscene_dialog")
        $ animcounter += 1
    call screen jenny_bj_options

label jenny_bj_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        jenny "Mmm.{p=1}{nw}"
    if animcounter == 1 and randomizer() > 50:
        jenny "{i}*Slurp*{/i}{p=1}{nw}"
    if animcounter == 2 and randomizer() < 50:
        anon "...{p=1}{nw}"
    if animcounter == 3 and randomizer() > 50:
        jenny "{i}*Slurrrrrp*{/i}{p=1}{nw}"
    return

label jenny_bj_cum:
    if jen_name == 'Jenny':
        anon "Jrrnnnneeeee!"
    else:
        anon "Hhhrreeeee!"
    anon "Mmy grrn krrrwwws!!"
    pause
    if jen_name == 'Jenny':
        anon "Jrrnnnneeeee!!!"
    else:
        anon "Hrrrmmmmmphhhh!!!"
    pause
    show jenny_bj cum
    anon "HrrrNNGGG!!!" with flash
    jenny "!!!"
    pause
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    show anon b_bed_jenny_laying_undies_arms of_bed_jenny_laying_undies_arms_mask_X oh_bed_jenny_laying_undies_handcuffs od_bed_jenny_laying_dick3
    show jenny b_bed_front_sit a_shocked f_cheeks_surprised o_laptop
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick3.png"
    with dissolve
    jenny "{i}*Gulp*{/i}"
    show jenny f_cheeks_angry
    jenny "{i}*Cough* *Sputter* *Cough*{/i}"
    if M_jenny.is_state(S_jenny_start_camshow_blowjob):
        show jenny b_bed_back_sit a_sit_hips with dissolve
        jenny "Goddamnit!!"
        jenny "You came right down my fucking throat!"
        show jenny b_bed_climbing with dissolve
        jenny "Eugh, I swallowed a bunch of it!"
        show jenny b_bed_side f_angry a_laptop with dissolve
        anon "I tried to warn you..."
        jenny "Bullshit, I didn't hear anything!"
        anon "Yeah, probably because you were humping my face!"
        jenny "Tch, whatever..."
        show jenny b_bed_side_laptop f_gross_down with dissolve
        pause
        jenny "Grr, it's not funny!"
        jenny "It's disgusting!"
        pause
        jenny "Ugh, you're all assholes!"
        jenny "Shows over!"
        scene black with fade
        pause
        scene expression player.location.background_blur with None
        show jenny b_naked a_hips f_angry
        show anon f_surprised b_underwear
        with dissolve
        jenny "Unbelievable!"
        anon f_worried "I really did try to warn-"
        jenny "I don't wanna hear it!"
        jenny "Just shut up!"
        show jenny f_gross_down
        jenny "Eugh, I gotta go brush my fucking teeth!"
        hide jenny with dissolve
        pause
        anon "Hey, what about my money?!"
        pause
        anon @ -m_talk "( Hmm, I guess I'll just ask her about it tomorrow. )"
        hide anon with dissolve
        $ M_jenny.trigger(T_jenny_done_camshow_blowjob)
    else:
        show jenny b_bed_back_sit a_sit_hips with dissolve
        jenny "Phew, happy now?"
        anon "I warned you again!"
        jenny "I know."
        pause
        jenny "I just wasn't expecting so much..."
        show jenny b_bed_climbing with dissolve
        anon "W-wait, so you-"
        show jenny b_bed_side_laptop f_sexy_down a_laptop with dissolve
        jenny "Shows over boys!"
        jenny "Thanks for tuning in!"
        pause
        jenny "Hehe, we'll see you next time!"
        scene black with fade
        pause
        scene expression player.location.background_blur with None
        show jenny b_naked a_hips f_normal
        show anon b_underwear f_surprised
        with dissolve
        anon "Y-you swallowed on purpose?"
        show jenny f_upset
        jenny "Yeah?"
        anon f_surprised_teeth "!!!"
        jenny "Don't get any ideas, it's just what the fans want to see..."
        anon f_worried "O-oh."
        show jenny a_money with dissolve
        jenny "Here's your cut."
        show jenny a_sides with dissolve
        anon f_normal "Thanks."
        show jenny f_angry
        jenny "Now get the fuck out!"
        show anon f_surprised
        hide jenny with dissolve
        jenny "Eugh, I need some mouth wash!"
        anon f_grin "..."
        hide anon with dissolve
        call popup ('earn', 100)
        $ player.get_money(100)
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["09_unlocked"] = True
    $ player.go_to(L_home_hallway)
    $ game.timer.tick()
    $ game.main()

label jenny_couch_fj_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_couch_dick_rub", [1,2,3], M_jenny) as jenny_couch_dick_rub at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_couch_fj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_couch_dick_rub {}".format(pose_list[pose_counter]) as jenny_couch_dick_rub at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_couch_fj_hscene_dialog")
        $ animcounter += 1
    call screen jenny_couch_fj_options

label jenny_couch_fj_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        show jenny f_sexy_down
        jenny "Does it feel good?{p=1}{nw}"
        show anon f_couch_sit_down
        anon "Yes.{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        show jenny f_sexy_down
        jenny "Are you getting close?{p=1}{nw}"
        show anon f_couch_sit_down
        anon "Y-yes.{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        show anon f_couch_sit_right
        if randomizer() > 50:
            anon "You're really good at this!{p=2}{nw}"
        else:
            anon "Holy crap!{p=1}{nw}"
        show anon f_couch_sit_down
        show jenny f_laugh
        jenny "Hehehe!{p=1}{nw}"
        show jenny f_sexy_down
    return

label jenny_couch_fj_cum:
    if M_jenny.finished_state(S_jenny_catch_her_jilling):
        show anon f_couch_sit_down_surprised
        anon "Here it comes!"
        pause
    show anon f_couch_sit_down_surprised
    hide jenny_couch_dick_rub
    show jenny a_dick3
    anon "HNNGGG!!!" with flash
    show jenny_player_couch_cum zorder 3 with dissolve
    show anon f_couch_sit_down
    pause
    show anon f_couch_sit_right
    show jenny f_laugh
    jenny "Pfft, hahaha!"
    hide jenny_player_couch_cum
    show anon a_boner
    show jenny a_after2 f_sexy_down
    with dissolve
    if M_jenny.is_state(S_jenny_catch_her_jilling):
        $ M_jenny.trigger(T_jenny_gave_footjob)
        jenny "I just made you cum with my feet!"
        jenny "I'm like, a total sex goddess!!"
        show jenny a_after1 f_sexy_down with dissolve
        anon "That was amazing!"
        jenny "I know, right?"
        jenny "You're welcome, loser."
        show jenny b_couch_transition zorder 0 with dissolve
        anon "Where are you going?"
        show jenny b_couch_sit a_rest f_sexy with dissolve
        jenny "Umm, to wash my feet?"
        show jenny a_after2 with dissolve
        jenny "Unless you wanna clean them with your tongue?"
    else:
        jenny "Sheesh, look at the mess you made of my pretty little feet!"
        jenny "You sure you don't wanna clean them up with your tongue?!"
    show jenny f_sexy a_after1 with dissolve
    if M_jenny.get("dominance") <= 0:
        anon "Please, don't make me do that..."
        show jenny f_laugh
        jenny "Hahaha!"
        show jenny f_sexy
        jenny "Don't ask stupid questions then."
    else:
        anon "Eugh, no way!"
        show jenny f_laugh
        jenny "Hahaha!"
        show jenny f_sexy
        jenny "Aww, c'mon..."
        show jenny a_after2 with dissolve
        jenny "Lick my toes, {b}[firstname]{/b}!"
        anon "Forget it!"
        show jenny f_laugh
        jenny "Hahaha!"
        show jenny f_sexy
        jenny "Fine."
    jenny "I'm going to go take a shower."
    jenny "See ya, perv."
    hide jenny with dissolve
    show anon f_couch_sit_down
    anon @ -m_talk "( Phew, that was awesome! )"
    show anon b_couch_sit_watching f_couch_sit_watching_straight with dissolve
    anon "( I should turn this off and get to bed before {b}[deb_name]{/b} hears it. )"
    hide anon with dissolve
    $ renpy.end_replay()
    $ game.timer.tick()
    $ game.main()

label jenny_computer_video_ec:
    scene expression "backgrounds/location_home_jennybedroom_cam1.jpg"
    show jenny b_cam_intro a_cover f_cam_intro_normal
    show expression "characters/jenny/layeredimage/jenny_webcam_border.png"
    with dissolve
    jenny "Sorry boys... This next part is for subscribers only."
    jenny "You'd better pay quickly if you don't wanna miss out!!"
    pause
    show jenny a_reveal with dissolve
    jenny "Hehe, alright. Who's ready to get naughty?"
    show jenny a_electro f_cam_intro_normal_left with dissolve
    jenny "I've got a nice new toy here... Just for you guys!"
    jenny "Mmm, I can't wait to tease my clit with this..."
    pause
    show jenny f_cam_intro_normal
    jenny "Why don't you guys give me a little incentive?"
    show jenny f_cam_intro_normal_down
    "{i}*PING*{/i}"
    "{i}*PING*{/i}"
    jenny "Oh, c'mon now... You can do better than that, can't you?"
    jenny "My pussy's absolutely aching for some attention..."
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    "{i}*PING*{/i} {i}*PING*{/i}"
    jenny "Hehe, that's better!"
    pause
    show jenny b_cam_electro_talk with dissolve
    jenny "Ah, I'm so wet..."
    hide jenny
    show expression AnimatedImage("jenny_electro", [1,2,3,4], M_jenny) as jenny_toy
    with dissolve
    jenny "Oh, yes!"
    pause
    jenny "It's so good!"
    pause
    jenny "Mmm, c'mon boys, I need more love!"
    "{i}*PING*{/i} {i}*PING*{/i}"
    jenny "That's it! I'm getting closer!"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    hide jenny_toy
    show jenny b_cam_electro_insert
    jenny "Ahh!!" with hpunch
    pause
    show jenny b_cam_electro_talk with dissolve
    jenny "Hehe! How was that?!"
    scene expression game.timer.image("backgrounds/location_home_bedroom_desk_cam{}.jpg") as cutscene
    show player 311 at Position(xpos = 672)
    with dissolve
    jenny "Hmm, you want me to get something bigger next time?"
    pause
    jenny "Anal?!"
    jenny "You seriously want me to stick something up my ass, {b}sam9{/b}?"
    jenny "Tch, you guys are so demanding!"
    pause
    jenny "Hmm, if I get thirty more subscribers, I'll get something bigger, okay?"
    pause
    jenny "Yes, I promise."
    pause
    jenny "I don't know about the anal, {b}sam9{/b}... We'll see..."
    pause
    anon "( Wow, that was pretty hot! )"
    anon "( I should see what else she has... )"
    hide cutscene
    hide player
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["03_unlocked"] = True
    return

label jenny_computer_video_uv:
    scene expression "backgrounds/location_home_jennybedroom_cam1.jpg"
    show jenny b_cam_intro a_cover f_cam_intro_normal
    show expression "characters/jenny/layeredimage/jenny_webcam_border.png"
    with dissolve
    jenny "Sorry boys... This next part is for subscribers only."
    jenny "You can still get in and watch if you hurry!!"
    pause
    show jenny a_reveal with dissolve
    jenny "Hehe, alright. I made a promise to you guys, didn't I?"
    show jenny a_vibrate f_cam_intro_normal_left with dissolve
    jenny "What do you think of this big guy, huh?"
    jenny "I told you all I would get something bigger."
    show jenny f_cam_intro_normal_down
    pause
    show jenny a_back with dissolve
    jenny "No, {b}sam9{/b}... It's not going in my butt."
    jenny "Yes, yes... Maybe in the future, we'll see."
    pause
    jenny "Now, how about some incentive for your sex goddess?"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    "{i}*PING*{/i} {i}*PING*{/i}"
    jenny "Hehe, that's what I like to see!"
    jenny "Just a little bit more!"
    pause
    show jenny a_vibrate with dissolve
    jenny "Don't you wanna see me cum all over this toy?"
    "{i}*PING*{/i} {i}*PING*{/i}"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    jenny "There we go!"
    pause
    show jenny b_cam_vibrate_talk with dissolve
    jenny "Hehe, I don't know if it will fit inside my tight little pussy..."
    hide jenny
    show expression AnimatedImage("jenny_vibrate", [1,2,3,4], M_jenny) as jenny_toy
    with dissolve
    pause
    jenny "Oh, fuck..."
    pause
    jenny "Haah!"
    pause
    jenny "Mmm, c'mon boys, show me the money!"
    "{i}*PING*{/i} {i}*PING*{/i}"
    jenny "That's it! It feels so good!"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    jenny "I'm getting close!!"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    jenny "Oh fuck yes!!"
    hide jenny_toy
    show jenny b_cam_vibrate_cum1
    jenny "Ahh!!" with hpunch
    pause
    pause
    show jenny b_cam_vibrate_cum2 with dissolve
    jenny "Hehe, I think I made a mess..."
    scene expression game.timer.image("backgrounds/location_home_bedroom_desk_cam{}.jpg") as cutscene
    show player 311 at Position(xpos = 672)
    with dissolve
    anon "( Wow, did she just squirt?! )"
    jenny "I guess I'll have to wash my sheets..."
    pause
    jenny "What?!"
    jenny "I'm not sending you my sheets!"
    pause
    jenny "You'll pay me how much?"
    pause
    jenny "I'll think about it..."
    jenny "For now, I just wanna-"
    jenny "Hmm?"
    pause
    jenny "You guys want to see me with a real penis?"
    pause
    jenny "Maaaaybe..."
    pause
    jenny "Hah, {b}sam9{/b} wants to see me with a real penis, in my ass... Big surprise."
    pause
    jenny "You guys are dorks."
    anon "( Wow, I can see why she's making money doing this... )"
    jenny "I'll see you boys soon, okay?"
    anon "( Hmm, I guess that's it for that video. )"
    hide cutscene
    hide player
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["04_unlocked"] = True
    return

label jenny_computer_video_bm:
    scene expression "backgrounds/location_home_jennybedroom_cam1.jpg"
    show jenny b_cam_intro a_cover f_cam_intro_normal
    show expression "characters/jenny/layeredimage/jenny_webcam_border.png"
    with dissolve
    jenny "Sorry boys... This next part is for subscribers only."
    jenny "You guys should really pay up and join us today!"
    jenny "Spoiler alert!"
    show jenny a_monster f_cam_intro_normal_left with dissolve
    jenny "This thing is going inside me today!"
    jenny "I hope to see you there!"
    show jenny f_cam_intro_normal_down
    pause
    show jenny a_back with dissolve
    jenny "Hehe, alright. Let's wait just a second and see if anyone else joins..."
    pause
    jenny "Yes, I'm serious!"
    jenny "I'm gonna fuck myself silly on this monster!"
    show jenny f_cam_intro_normal
    pause
    jenny "Ugh, yeah... Alright, {b}sam9{/b}. I'll put it in."
    jenny "You see that guys?"
    jenny "I give {b}sam9{/b} what he wants because he's always so generous with his tips!"
    pause
    jenny "That's right, tip more and you'll get what you want too."
    show jenny f_cam_intro_normal_down
    pause
    jenny "Holy shit, we've got almost two hundred new subs in here for this show!"
    jenny "I guess you guys are thirsty for your sex goddess, huh?"
    pause
    show jenny f_cam_intro_normal
    jenny "Okay, first things first..."
    show jenny b_cam_monster_talk with dissolve
    jenny "This is for {b}sam9{/b}!"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    show jenny b_cam_monster_talk2 with dissolve
    jenny "NGGGHHH!!"
    jenny "Fucking Sam!"
    pause
    jenny "Yeah, I know... It's growing on me."
    pause
    jenny "I just said I like it, didn't I?!"
    jenny "Pay attention, dummy!"
    pause
    jenny "No, that doesn't mean I'm getting something bigger."
    pause
    jenny "Alright, enough with the anal stuff..."
    show jenny b_cam_monster_talk3 with dissolve
    jenny "It's time for the main event!"
    pause
    jenny "Are you boys ready?"
    "{i}*PING*{/i} {i}*PING*{/i}"
    jenny "I can't hear you!!"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    jenny "Hehe, here we go!"
    pause
    show jenny b_cam_monster_anim1 with dissolve
    jenny "Haah..."
    show jenny b_cam_monster_anim2 with dissolve
    jenny "Oh my god..."
    jenny "It's fucking huge!"
    pause
    show jenny b_cam_monster_anim3 with dissolve
    jenny "Holy shit!!!"
    pause
    jenny "Okay..."
    $ M_jenny.set("sex speed", 0.175)
    hide jenny
    show expression AnimatedImage("jenny_monster", [4,1,2,3], M_jenny) as jenny_toy
    with dissolve
    pause
    jenny "Ahh!!"
    pause
    jenny "Oh, yes, yes, YES!!!"
    pause
    jenny "Oh my god you guys, this is amazing!"
    "{i}*PING*{/i} {i}*PING*{/i}"
    pause
    jenny "AH FUCK!"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    jenny "I'm gonna cum!!"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    jenny "YES!!"
    $ M_jenny.set("sex speed", 0.6)
    show expression AnimatedImage("jenny_monster", [2,3], M_jenny) as jenny_toy
    jenny "Ngghhh!!!" with hpunch
    pause
    hide jenny_toy
    show jenny b_cam_monster_after
    with dissolve
    pause
    jenny "Haah... Haah..."
    jenny "Wow, that was-"
    pause
    scene expression game.timer.image("backgrounds/location_home_bedroom_desk_cam{}.jpg") as cutscene
    show player 311 at Position(xpos = 672)
    with dissolve
    anon "( Holy crap! )"
    jenny "Oh my god, look at how much I'm shaking..."
    pause
    jenny "Phew, just give me a second."
    pause
    jenny "Hahaha! I told you guys it was gonna be worth it."
    pause
    jenny "I know, right?"
    pause
    jenny "Yeah, I know you want to see me ride a real dick..."
    jenny "It's coming, okay?"
    jenny "Just have your wallets ready, 'cause I'm expecting a LOT of tips for that show."
    pause
    jenny "Hehe, yeah."
    pause
    jenny "You're welcome, {b}sam9{/b}."
    pause
    jenny "Yeah, I'll see you all next time."
    pause
    jenny "Buh bye, boys."
    anon "( Totally worth it. )"
    anon "( That was awesome! )"
    hide cutscene
    hide player
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["05_unlocked"] = True
    return

label jenny_hj_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_hj", [1,2,3,4,5,4,3,2], M_jenny) as jenny_hj at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_hj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,4,3,2]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_hj {}".format(pose_list[pose_counter]) as jenny_hj at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_hj_hscene_dialog")
        $ animcounter += 1
    call screen jenny_hj_options

label jenny_hj_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        anon "Holy crap!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        anon "Oh my god!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jenny "Mmm, I can feel it throbbing...{p=2}{nw}"
        "{i}*PING*{/i} {i}*PING*{/i}{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        anon "I'm getting close...{p=2}{nw}"
        if M_jenny.get("sex speed") > 0.051:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.025)
        anon "Oh my god!{p=1}{nw}"
    return

label jenny_hj_cum:
    if M_jenny.is_state(S_jenny_start_camshow_handjob):
        jenny "I wonder what else I shou-"
        hide jenny_hj
        show jenny_hj_mc cum
        anon "HNNGGG!!!{p=1}{nw}" with flash
        show jenny_hj_cum
        jenny "{i}*Gasp*{/i}"
        pause
        jenny "What the fuck!"
        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
        anon "Phew..."
        scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
        show anon b_bed_jenny_laying od_bed_jenny_laying_dick3 of_bed_jenny_laying_mask_X
        show jenny b_bed_side f_angry o_laptop a_cum
        with dissolve
        jenny "Why didn't you warn me!"
        show jenny f_angry
        anon "You didn't tell me to warn you..."
        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
        jenny "Well, I thought that was fucking obvious you moron!"
        jenny "Oh my god, it's everywhere!"
        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
        jenny "Ugh, okay... Stream's over!"
        anon "B-but they're still tipping-"
        jenny "GET THE FUCK OUT OF MY ROOM!"
        anon "Okay, okay..."
        hide anon with dissolve
        show jenny f_gross_down
        jenny "Eugh."
        pause
        show jenny b_bed_side_laptop f_gross_down with dissolve
        jenny "It's not funny!"
        scene black with fade
        pause
        $ game.timer.tick()
        $ M_jenny.trigger(T_jenny_gave_handjob)
        $ player.go_to(L_home_bedroom)
        scene expression player.location.background_blur with None
        show anon f_surprised with dissolve
        anon @ -m_talk "( Wow! )"
        anon f_flirt @ -m_talk "( I can't believe {b}[jen_name]{/b} just jerked me off... )"
        anon @ -m_talk "( That was so hot!! )"
        pause
        anon f_grin @ -m_talk "( Man, I hope I get to do that again! )"
        hide anon with dissolve
    else:
        anon "Here it comes!"
        jenny "Hmm?"
        hide jenny_hj
        show jenny_hj_mc cum
        anon "HNNGGG!!!{p=1}{nw}" with flash
        show jenny_hj_cum
        jenny "!!!"
        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
        scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
        show anon b_bed_jenny_laying od_bed_jenny_laying_dick3 of_bed_jenny_laying_mask_X
        show jenny b_bed_side f_angry o_laptop a_cum
        with hpunch
        jenny "Again?!"
        jenny "Goddamnit, you asshole!"
        anon "I warned you!"
        jenny "Well, I wasn't paying attention!"
        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
        show jenny f_gross_down
        jenny "Eugh."
        show jenny b_bed_side_laptop with dissolve
        jenny "Yeah, yeah... Very funny."
        jenny "Show's over pervs!"
        hide jenny
        hide anon
        with dissolve
        scene expression game.timer.image("backgrounds/location_home_jennybedroom{}.jpg")
        show anon f_surprised b_underwear
        show jenny b_naked f_upset a_hips
        with dissolve
        jenny "You're washing my sheets this time!"
        anon f_worried "Fine, whatever."
        jenny "I'm getting in the shower."
        show jenny a_money with dissolve
        jenny "Take this and get the fuck out!"
        hide jenny with dissolve
        pause
        anon f_normal "Sweet!"
        hide anon with dissolve
        call popup ('earn', 50)
        $ player.get_money(50)
        $ game.timer.tick()
        $ player.go_to(L_home_basement)
        scene expression player.location.background_blur
        show anon f_normal
        with fade
        anon "Phew!"
        anon "Alright, that's done."
        pause
        anon f_laugh "Totally worth it!"
        hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
    $ game.main()

label jenny_hj_intro_repeat:
    show jenny f_upset
    jenny "Hurry up."
    show jenny f_grin_down b_pull1 with dissolve
    pause
    show jenny b_pull2 with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show anon f_surprised
    pause
    show jenny b_panties a_hips f_upset with dissolve
    jenny "Well?"
    show jenny f_grin_down b_naked a_panties_remove with dissolve
    show anon f_worried
    anon @ -m_talk "Hmm?"
    show jenny b_naked_panties_remove_down with dissolve
    pause
    show jenny b_naked a_hips f_upset with dissolve
    jenny "Get those clothes off!"
    anon "R-right..."

    label finger_blasting_hj:
    scene location_home_jennybedroom_cutscene05
    with fade
    jenny "You know the drill."
    jenny "Mask on and keep your mouth shut."
    anon "Yeah, I remember."
    jenny "I'll handle the rest."

    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg"
    $ M_jenny.set('cam show mask', True)
    show anon b_bed_jenny_sit f_shy_down of_mask
    show jenny o_under_body_laptop b_naked_bed_bellytype f_sexy_down
    with fade
    jenny "Hi again, everybody!"
    show jenny b_naked_bed_belly with dissolve
    jenny "I brought my boy toy back to give you guys another show."
    pause
    show jenny f_laugh
    jenny "Hehe, of course!"
    show jenny f_sexy_down
    pause
    jenny "Well, let's find out, shall we?"
    show jenny o_laptop b_bed_side a_laptop
    show anon b_bed_jenny_laying od_bed_jenny_laying_dick1 of_bed_jenny_laying_mask_X
    with dissolve
    jenny "I bet he's good and ready this time."
    show jenny a_pull1 f_sexy_down with dissolve
    pause
    show anon od_empty
    show jenny a_pull2
    with dissolve
    pause
    show jenny a_point
    show anon od_bed_jenny_laying_dick4
    with fastdissolve
    show anon od_bed_jenny_laying_dick5 with fastdissolve
    show anon od_bed_jenny_laying_dick6 with fastdissolve
    jenny "!!!"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    pause
    show jenny b_bed_side_laptop f_sexy_down with dissolve
    jenny "Hehe, I know it's big!"
    jenny "I wouldn't settle for anything less, would I?"
    pause
    jenny "Yeah, I think I should too."
    $ M_jenny.set("sex speed",0.4)
    show jenny b_bed_side a_jerk with dissolve
    anon "!!!"
    pause
    anon "Oh, god!"
    jenny "Yeah, you like that, don't you?"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    pause
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg" with None
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .1)
    show jenny_hj_mc
    show expression AnimatedImage("jenny_hj", [1,2,3,4,5,4,3,2], M_jenny) as jenny_hj at Position(xalign = 0.0, yoffset = 0)
    with dissolve
    jenny "C'mon, boy toy!!"
    jenny "Tell everybody how much you love me stroking your big, hard cock..."
    anon "I love it!"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    jenny "Hahaha!"
    pause
    anon "{b}[jen_name]{/b}, I'm gonna-"
    jenny "You boys seeing this?!"
    jenny "Hehe, oh you like my big tits, huh?"
    "{i}*PING*{/i} {i}*PING*{/i}"
    jump jenny_hj_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

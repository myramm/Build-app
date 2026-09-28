label job_done_dialogue(earnings):
    $ renpy.checkpoint()
    if M_diane.between_states(S_diane_bug_infested_garden, S_diane_clear_bug_infested_garden):
        scene garden_dead
    elif M_diane.finished_state(S_diane_barn_news):
        scene expression "backgrounds/location_barn_garden_day_blur.jpg"
    else:
        scene garden

    if M_diane.is_state(S_diane_clean_garden):
        scene garden_dead
        show player 14 with dissolve
        player_name "Phew!"
        player_name "Alright, I think I finally got everything..."
        show player 31f with dissolve
        player_name "..."
        show player 32f
        player_name "Now, where did {b}Diane{/b} sneak off to?"
        player_name "She must have gone inside..."
        hide player with dissolve
        $ M_diane.trigger(T_diane_cleaned_garden)

    elif M_diane.is_state(S_diane_drunken_garden_work):
        call expression game.dialog_select("dianes_garden_diane_drunk_like_a_sailor")
        $ M_diane.trigger(T_diane_drunken_massage)
        $ game.timer.tick(3)
        $ player.go_to(L_map)

    elif M_diane.is_state(S_diane_get_bug_spray, S_diane_clear_bug_infested_garden) and player.has_item('annihilator'):
        scene location_diane_garden_cutscene03
        show text _ ("I began to spray the whole lot with green napalm...\nEmptied the entire can of spray on the nasty buggers...\nUntil nothing remained!") as caption
        with fade
        pause

        scene black with dissolve
        call popup ('bugs', True)
        $ player.remove_item('annihilator', 'eradicator', 'exterminator')
        $ M_diane.trigger(T_diane_use_bug_spray_on_garden)

        scene garden
        show diane a_blush
        show anon
        with dissolve
        diane "Phew, what a day!"
        show diane a_shovel with dissolve
        anon "Heh, I know... I'm exhausted."
        anon "We got it all finished though."
        diane "We sure did."
        show diane f_laugh
        diane "It'll be even better than it was before!"
        show diane a_finger with dissolve
        diane "You wait and see!"
        show diane f_normal a_shovel with dissolve
        anon "Hehe, I hope so."
        diane "Thanks for all your help today, stud."
        anon @ f_laugh "My pleasure!"
        show anon b_empty f_grin
        show diane b_kiss
        with dissolve
        pause
        show anon b_dressed f_normal
        show diane b_dressed
        with dissolve
        diane "Tell {b}[deb_name]{/b} hi for me."
        anon "Will do."
        hide anon
        hide diane
        with dissolve
        $ game.timer.tick(2)
        $ M_diane.trigger(T_diane_inform_diane)

    elif M_diane.is_state(S_diane_get_bug_spray, S_diane_clear_bug_infested_garden) and player.has_item('eradicator', 'exterminator'):
        scene garden
        show expression Transform('player 109', xzoom=-1) as player at center
        with dissolve
        player_name "( Huh? This spray didn't seem to affect the bugs at all... )"
        show player 34 with dissolve
        player_name "( Perhaps I should try another pesticide... )"
        hide player with dissolve
        call popup ('bugs', False)
        $ player.remove_item('exterminator', 'eradicator')

    elif M_diane.is_state(S_diane_work_on_garden):
        scene expression "backgrounds/location_diane_garden_closeup.jpg"
        show player 13 at right
        show diane a_shovel:
            flip
        with dissolve
        diane "Hey, that's looking great!"
        show player 22
        player_name "!!!" with hpunch
        show player 29f with dissolve
        player_name "H-hey, {b}Diane{/b}."
        show player 3f at Position (xoffset=-8)
        diane "I'm sorry I wasn't out here to greet you..."
        show diane f_thinking
        diane "... Something urgent came up that I had to take care of."
        show diane f_cheese
        show player 10f
        player_name "... Oh, y-yeah?"
        show player 14f
        show diane f_normal
        player_name "I mean... Heh, no worries!"
        show player 29f with dissolve
        player_name "I was just out here... Umm..."
        show player 3f at Position (xoffset=-8)
        pause
        show diane f_smirk
        diane "... Working?"
        show player 29f
        player_name "Y-yeah!"
        show player 3f at Position (xoffset=-8)
        show diane f_laugh
        diane "Heh?"
        show diane f_normal
        diane "What's got you so tongue-tied all of a sudden?"
        show player 29f
        player_name "N-nothing..."
        player_name "I was just... Umm..."
        show player 3f at Position (xoffset=-8)
        diane "Well, the garden really does look great."
        diane "I think it's even better than it was before the earwig fiasco!"
        show diane b_grab_cucumber with dissolve
        show player 428f with dissolve
        diane "Just look at these beauties."
        player_name "..."
        show diane b_dressed a_cucumber_touch with dissolve
        show player 11f
        diane "What a monster!"
        show diane a_cucumber_rub with dissolve
        diane "And all these wonderful ridges."
        show diane f_cheese
        show player 78f with dissolve
        pause
        show player 81f
        player_name "!!!" with hpunch
        show diane f_laugh a_cucumber_touch with dissolve
        diane "With vegetables like this, I might have to give you a raise."
        show diane f_surprised_down
        diane "{i}*Gasp*{/i}"
        diane "!!!"
        show diane f_surprised
        player_name "..."
        diane "..."
        show player 79f with dissolve
        player_name "I uhh..."
        show player 78f with dissolve
        show diane f_surprised_down
        diane "... Are you-"
        show diane f_surprised
        show player 83f
        player_name "I should go!!"
        show player 78f with dissolve
        show diane f_laugh
        diane "Wait!"
        show player 81f
        player_name "Later, {b}Diane{/b}!"
        hide player with dissolve
        pause
        show diane f_sad
        diane "{b}[firstname]{/b}?!"
        diane "..."
        hide diane with dissolve
        scene expression "backgrounds/location_diane_front_day_blur.jpg"
        show player 83 with dissolve
        player_name "Oh my god..."
        player_name "I can't believe I got a boner in front of {b}Diane{/b}!"
        player_name "That was so embarrassing!"
        player_name "I've gotta get outta here!"
        hide player with dissolve
        $ game.timer.tick(2)
        $ player.go_to(L_map)
        $ M_diane.trigger(T_diane_worked_on_garden)

    elif M_diane.is_state(S_dia01_work):
        $ game.timer.tick()
        scene black
        pause .5
        if earnings > 0:
            call expression game.dialog_select("garden_firsttime_pass")
        else:
            call expression game.dialog_select("garden_firsttime_fail")
        hide diane with dissolve
        pause 2
        show anon f_depressed a_rub with dissolve
        anon @ -m_talk "( Phew, gardening is hard work! )"
        anon f_tired a_idle @ -m_talk "( I'm exhausted. )"
        pause
        anon @ -m_talk "( {b}I should head home{/b} and get some sleep. )"
        hide anon with dissolve

    $ after_minigame = True
    if earnings > 0:
        $ player.get_money(earnings)
        call popup ('earn', earnings)

    if M_daisy.is_state(S_daisy_pizza_craving):
        call expression game.dialog_select("barn_front_daisy_pizza_craving")
        $ M_daisy.trigger(T_daisy_find_food)
        $ player.go_to(L_diane_barn)
    elif M_diane.is_state(S_dia01_work):
        $ M_diane.set("garden first time", False)
        $ M_diane.trigger(T_dia01_work)
    else:
        $ game.timer.tick()

    $ game.main()

label garden_firsttime_pass:
    scene location_diane_garden_cutscene01
    show text _ ("{b}Diane{/b} went to lie down as I began digging up her garden.\nIt was so hot outside and there were so many weeds and bugs!\nI grit my teeth and set myself to the task...\n... I hope she's planning to pay me well for all this physical labor!") as caption
    with fade
    pause

    scene location_diane_garden_cutscene02
    show text _ ("As I worked, I noticed {b}Diane{/b} was watching me intently...\nI suppose she was just trying to make sure I did a good job.\nWe exchanged a few words here and there but mostly just small talk.\nHer eyes seemed fixed upon me.") as caption
    with fade
    pause

    scene black with dissolve
    pause

    scene expression player.location.background_blur
    show anon
    show diane a_shovel
    with dissolve
    diane "Oh, wow! My garden looks absolutely gorgeous, {b}[firstname]{/b}!"
    show diane f_smirk
    anon "Yeah... I had to get rid of a lot of stuff..."
    show diane a_cucumber f_teasing_look with dissolve
    show anon f_surprised
    diane "Just look at that big, hard cucumber!"
    show diane f_smirk
    anon @ -m_talk "..."
    anon f_worried "Why do you only want the vegetables that are long and hard?"
    show diane f_shamed_smile
    diane "I err..."
    show diane f_shamed_look
    diane "Well, you see they... Umm..."
    show diane f_shamed
    anon "Do they sell better or something?"
    show diane f_laugh
    diane "Yes!! That's exactly it!"
    show diane f_teasing_look
    diane "They sell better."
    show diane f_smirk
    anon f_normal @ f_skeptical "Hmm, interesting."
    anon "I guess I have a lot to learn about vegetables..."
    show diane f_normal a_shovel with dissolve
    diane "Well, don't you worry, {b}[firstname]{/b}."
    diane "I can teach you everything there is to know about gardening."
    anon "How did you get into this stuff anyways?"
    diane "Oh, I've always had a bit of a green thumb. Even when I was a kid."
    anon "Really?"
    show diane f_laugh
    diane "You betcha!"
    show diane f_normal
    diane "You know, I used to dream about owning a farm of my own..."
    anon "Like a for real farm? With fields of crops and animals?"
    diane "That's right! I wanted the whole nine yards!"
    anon "You should totally do that, {b}Diane{/b}!"
    anon @ f_laugh "I'd help you!"
    show diane f_laugh
    diane "Haha, yeah well, thanks, {b}[firstname]{/b}... I'm afraid it's not as easy as all that."
    show diane f_normal
    anon "Yeah, I suppose you're right."
    show diane f_laugh
    diane "Thanks for your help today!"
    show diane f_normal
    diane "Why don't you come back tomorrow, and we'll continue where we left off?"
    anon "Alright, I'll see you tomorrow then."
    show diane f_smirk
    diane "Bye, handsome."
    return

label garden_firsttime_fail:
    scene expression player.location.background_blur
    show anon f_worried
    show diane f_sad a_shovel
    with dissolve
    diane "Hmm... There's some room for improvement."
    anon f_worried_low "Yeah... I didn't do too well. Sorry {b}Diane{/b}!"
    show diane f_shamed_smile
    diane "It's okay... You're new at this..."
    show anon f_normal
    show diane f_laugh
    diane "And I'm sure you'll get better at it!"
    show diane f_normal
    diane "I always need fresh vegetables..."
    anon "I guess so..."
    show diane f_smirk a_finger with dissolve
    diane "Just make sure you {b}only{/b} keep the vegetables that are {b}long{/b} and {b}hard{/b}!"
    show diane f_normal a_shovel with dissolve
    anon "I'll do better next time..."
    anon @ f_laugh "Thanks, {b}Diane{/b}!"
    return

label garden_listing:
    call screen garden_minigame
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

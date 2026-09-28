label milking_game_pre:
    scene expression background(320, 440, 2.5) as stage
    show diane a_milk_cups

    if M_diane.pregnancy.stage > 4:
        show diane b_casual
    else:
        show diane b_naked

    with fade
    show anon with {'master': dissolve}
    diane "You remember how everything works?"
    show anon a_sides
    with {'master': dissolve}
    anon "Yeah, of course."
    show anon f_normal_low
    show diane a_milk_cups_give f_smirk
    with {'master': dissolve}
    diane "Heh, I figured you would."
    show anon a_milk_cups f_looking_down
    show diane a_idle
    with {'master': dissolve}
    diane "Just remember to be gentle."
    hide diane
    with {'master': dissolve}
    anon f_shy "Y-yes, ma'am."

    $ M_diane.set("sex_pre_milking", False)
    show screen minigame_milk() with fade
    call screen empty()
    hide screen minigame_milk

    if _return:
        call milking_minigame_done
    else:
        call milking_minigame_fail
    return


label milking_game_pre_after_sex:
    show diane f_smirk b_naked a_idle
    show player 365
    player_name "Yeah?"
    show player 366
    diane "Mmmhmm!"
    diane "I've never been fucked like that, {b}[firstname]{/b}!"
    diane "Hehe, my legs are like jello right now..."
    show player 365
    player_name "Hehe."
    show player 366
    pause
    $ game.main()


label milking_game_pre_daisy:
    show screen minigame_milk('daisy') with fade
    call screen empty()
    hide screen minigame_milk

    if _return:
        call milking_minigame_done_daisy
    else:
        call milking_minigame_fail_daisy
    return


label milking_minigame_done_daisy:
    scene expression player.location.background_blur
    show player 17 at left
    show daisy f_down b_naked_shy
    with fade
    player_name "All done!"
    show player 1b
    daisy f_normal "Aww, already?"
    show player 14b
    player_name "Heh, I don't think you have anything left in there..."
    show player 1b
    daisy "Yeah, okay..."
    daisy "Can you milk me again later, {b}[firstname]{/b}?"
    show player 14b
    player_name "S-sure, if you want."
    show player 1b
    show daisy f_laugh b_naked a_up with dissolve
    daisy "Yes, please!"
    daisy "It feels so good when you do it."
    show daisy f_normal a_idle with dissolve
    pause
    hide player
    show daisy b_naked_hug
    with dissolve
    daisy "Thank you, {b}[firstname]{/b}!"
    daisy "You're the bestest man ever!"
    show player 14b at left
    show daisy b_naked
    with dissolve
    player_name "You're welcome."
    player_name "I should probably get started on my other work."
    show player 1b
    daisy "Okay, {b}[firstname]{/b}."
    show player 14b
    player_name "I'll see you soon, {b}Daisy{/b}."
    show player 1b
    show daisy f_laugh
    daisy "Byeeeee!"
    hide player with dissolve
    pause
    show daisy f_normal
    pause
    hide daisy with dissolve

    $ renpy.dynamic(earnings=bisect.bisect((0, 0, 2, 3, 5),
                                           M_daisy.pregnancy.stage) * 50)
    $ player.get_money(earnings)
    call popup ('earn', earnings)
    $ game.timer.tick()
    $ M_daisy.trigger(T_daisy_milked)
    $ game.main()


label milking_minigame_fail_daisy:
    scene expression player.location.background_blur
    show player 24 at left
    show daisy f_sad
    with fade
    daisy "Are you okay, {b}[firstname]{/b}?"
    player_name "Y-yeah."
    show player 10b
    player_name "I guess I'm just a little off my game today..."
    show player 5b
    daisy f_normal "Hehe, that's alright."
    show player 10b
    player_name "You should go and ask {b}Diane{/b} to finish you off."
    show player 5b
    daisy f_sad "I should?"
    show player 10b
    player_name "Yeah, I'm not having much luck..."
    show player 5b
    pause
    show player 10b
    player_name "Sorry, {b}Daisy{/b}."
    show player 5b
    daisy f_normal "Aww... It's okay."
    daisy "Byeeeee {b}[firstname]{/b}!"
    hide daisy
    hide player
    with dissolve
    $ game.timer.tick()
    $ game.main()


label milking_minigame_done:
    if M_diane.between_states(S_diane_return_production_book, S_diane_return_outfit_package):
        scene expression "backgrounds/location_barn_day_blur.jpg"
        show player 13 at left
        show diane f_laugh b_shirtless
        with fade
        diane "Phew!"
        diane "That feels so much better!"
        show diane f_cheese
        pause
        show diane f_normal
        diane "Thank you, {b}[firstname]{/b}."
        show player 17
        player_name "You're welcome."
        show player 13
        diane "I don't know if it's you or this new equipment, but that was the smoothest milking session I've ever had."
        diane "Just look at all that milk!"
        show player 14
        player_name "Yeah, you had a lot in there."
        show player 13
        show diane f_laugh
        diane "Hehe!"
        show diane f_normal
        diane "Keep this up, and we'll fill my orders no problem!"
        pause
        diane "I'm gonna go ahead and give you your cut now."
        show player 5
        player_name "Hmm?"
        show diane a_money with dissolve
        diane "Here ya go."
        show diane a_idle
        show player 640e
        with dissolve
        player_name "You're gonna pay me to do this?"
        show player 13 with dissolve
        diane "Well, of course."
        diane "It's a job after all."
        show player 14
        player_name "Yeah, but-"
        show player 13
        show diane f_smirk
        diane "Believe me, those magic hands of yours are worth every penny."
        show player 14
        player_name "You're sure?"
        show player 13
        diane "Yep."
        show diane f_normal
        diane "Just remember, you have a garden to tend as well."
        show player 14
        player_name "I remember."
        show player 13
        diane "Well, you'd best get to it then."
        show player 14
        player_name "Thanks, {b}Diane{/b}."
        show player 13
        diane "You're welcome, handsome."
        hide player with dissolve

    elif M_diane.pregnancy.stage > 1:
        call milking_game_post.pregnant
    else:

        call milking_game_post

    $ renpy.dynamic(earnings=bisect.bisect((0, 0, 2, 3, 5),
                                           M_diane.pregnancy.stage) * 50)
    $ player.get_money(earnings)
    call popup ('earn', earnings)
    $ game.timer.tick()
    $ game.main()


label milking_minigame_fail:
    scene expression background(320, 440, 2.5) as stage

    if M_diane.get("sex_pre_milking"):
        show player 368 at left
    else:
        show player 5 at left

    if M_diane.pregnancy.stage > 4:
        show diane b_casual
    else:
        show diane b_naked

    show diane f_sad
    with fade
    diane "Hmm, well, that was disappointing..."
    if M_diane.get("sex_pre_milking"):
        show player 367
    else:
        show player 10
    player_name "Sorry, {b}Diane{/b}."
    player_name "I don't know what happened."
    if M_diane.get("sex_pre_milking"):
        show player 368
    else:
        show player 5
    show diane f_shamed_smile
    diane "It's alright, handsome."
    diane "I'm probably just having an off day."
    show diane f_shamed
    pause
    show diane f_shamed_smile
    diane "We can try again later, okay?"
    show diane f_shamed
    if M_diane.get("sex_pre_milking"):
        show player 367
    else:
        show player 10
    player_name "Y-yeah, okay."
    hide player with dissolve
    $ game.timer.tick()
    $ game.main()


label milking_game_post:
    scene expression background(320, 440, 2.5) as stage
    show diane b_naked f_drunk
    show anon a_milk_cups f_shy o_boner
    with fade
    diane "Phew!"
    diane "That feels so much better..."
    show diane a_take
    with {'master': dissolve}
    pause
    show anon a_sides
    show diane a_milk_cups f_smirk
    with {'master': dissolve}
    diane "... You have the most magical hands, {b}[firstname]{/b}."
    show anon a_behind_head of_blush
    show diane a_take:
        xoffset 600
        xzoom -1
    with {'master': dissolve}
    anon "Heh, thanks!"
    show diane a_idle f_surprised_front:
        xoffset 0
        xzoom 1
    with {'master': dissolve}
    show diane f_reading_lip_bite
    pause
    show anon a_sides f_confused -of_blush
    with {'master': dissolve}
    diane f_smirk @ f_teasing "And something else is looking pretty magical too."
    anon @ -m_talk "Hmm?"
    diane @ f_teasing "I think all the milking got you a little excited, huh?"
    show anon f_looking_down
    pause
    show anon f_surprised_down
    show diane f_laugh
    anon @ -m_talk "!!!" with hpunch
    show anon a_cover_boner f_worried
    with {'master': dissolve}
    anon "Oh, uhh... yeah, I guess it did."
    show diane f_smirk
    anon f_shy "Heh, sorry."
    diane "It's alright, stud."
    diane @ f_teasing_look "You know, I could take care of it for you... if you want?"
    show anon a_surprised f_surprised
    with {'master': dissolve}
    anon "W-what, now?"
    diane @ f_reading_lip_bite -m_talk "Mhmm."
    diane "You up for a little post-milking breeding session?"
    show anon a_sides f_confused
    with {'master': dissolve}
    anon "Oh, I uhh..."

    menu:
        "Hell yeah!":
            jump milking_game_post.sex
        "Not today.":

            pass

    show anon f_worried -o_boner
    with {'master': dissolve}
    anon "... Actually, I don't really have time for that today..."
    diane f_sad "Oh?"
    show anon a_shy_neck
    with {'master': dissolve}
    anon "... Y-yeah, sorry."
    diane "Well, that's okay, {b}[firstname]{/b}."
    diane f_normal "Maybe next time?"
    show anon a_fists f_happy
    with {'master': dissolve}
    anon "Definitely!"
    show anon a_sides
    with {'master': dissolve}
    diane @ f_laugh "Hehe!"
    show anon a_wave
    with {'master': dissolve}
    anon "I'll see you later, {b}Diane{/b}."
    diane "Later, stud."
    hide anon with dissolve
    return


label milking_game_post.pregnant:
    scene expression background(320, 440, 2.5) as stage

    if M_diane.pregnancy.stage > 4:
        show diane b_casual
    else:
        show diane b_naked

    show diane f_drunk
    show anon a_milk_cups f_shy
    with fade
    diane "Phew!"
    diane "That feels so much better..."
    show diane a_take
    with {'master': dissolve}
    pause
    show anon a_sides f_shy_low
    show diane a_milk_cups
    with {'master': dissolve}

    if M_diane.pregnancy.stage > 4:
        diane "... They get so sore, with all the breastfeeding..."
        diane "... It's nice to feel your gentle touch on them."
    else:

        diane "... They get so swollen with your little one on board."

    show diane a_take:
        xoffset 600
        xzoom -1
    with {'master': dissolve}

    if M_diane.pregnancy.stage > 4:
        anon f_shy "I'm happy I can help!"
    else:
        anon f_shy "Yeah, you're producing a ton more now that you're pregnant."

    show diane a_idle:
        xoffset 0
        xzoom 1
    with {'master': dissolve}
    diane @ -m_talk "Mhmm."
    pause
    show diane f_tired
    with {'master': dissolve}
    diane "I think I might need to go lie down for a spell, {b}[firstname]{/b}."
    anon f_confused "Oh?"
    diane "Are you okay, cleaning up by yourself?"
    anon "S-sure."
    anon f_shy "No problem, {b}Diane{/b}."
    diane f_smirk "Thanks, stud."
    hide diane
    show anon a_wave:
        xoffset -500
        xzoom -1
    with {'master': dissolve}
    anon "You go and rest up!"
    hide anon with dissolve
    return


label milking_game_post.sex:
    anon f_happy "Absolutely!"
    hide anon
    show diane b_kiss_naked:
        xoffset -100
    with {'master': dissolve}
    diane @ -m_talk "Mmm."
    pause
    show anon a_sides f_flirt
    show diane b_naked:
        xoffset -200
    with {'master': dissolve}
    diane "C'mon."
    hide diane
    show anon f_confused:
        xoffset -500
        xzoom -1
    with {'master': dissolve}
    anon f_confused "Wait, we're doing it here?"
    diane "Mhmm."
    diane "Have a seat."
    anon "O-okay."

    call scene_diane_sex_milk.repeat (M_diane.outfit.get)
    $ unlock_scene('Diane', '08_unlocked', variant=M_diane.outfit.get)

    scene expression background() as stage
    show diane b_naked f_tired:
        xoffset -200
    show anon a_sides
    with fade
    diane "Ngh, I think I need to go lie down."
    anon "Yeah, go take a rest, {b}Diane{/b}."
    anon "I can clean up here."
    diane "Thanks, stud."
    hide anon
    show diane b_kiss_naked:
        xoffset -100
    with {'master': dissolve}
    diane @ -m_talk "Mmm."
    pause
    show anon a_sides f_flirt
    show diane b_naked f_tired:
        xoffset -200
    with {'master': dissolve}
    anon "No problem."
    hide diane
    show anon:
        xoffset -500
        xzoom -1
    with {'master': dissolve}
    pause
    show anon f_grin:
        xoffset 0
        xzoom 1
    with {'master': dissolve}
    pause
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

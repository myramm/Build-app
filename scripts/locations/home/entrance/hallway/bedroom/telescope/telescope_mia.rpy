label mia_bedroom:
    if M_jenny.is_state(S_jenny_spy_on_mia_telescope) and game.timer.is_morning():
        hide screen telescope
        hide screen telescope_fake
        call expression game.dialog_select("telescope_mia_sister_spying")
        $ persistent.cookie_jar["Mia"]["unlocked"] = True
        $ persistent.cookie_jar["Mia"]["gallery"]["02_unlocked"] = True
        $ M_jenny.trigger(T_jenny_spied_on_mia)
        jump expression game.dialog_select("bedroom_dialogue")
    else:
        call expression game.dialog_select(game.telescope.mia)

    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_mia_sister_spying:
    scene telescope_mia_masturbate with dissolve
    pause
    anon "She's probably just getting ready for-"

    anon "!!!"
    pause
    anon "Wah!!"

    scene expression "backgrounds/location_home_bedroom_caught_01.jpg" with dissolve
    anon "She's masturbating!"

    scene expression "backgrounds/location_home_bedroom_caught_02.jpg" with dissolve
    pause
    scene expression "backgrounds/location_home_bedroom_caught_03.jpg" with dissolve
    anon "I wonder what she's thinking about?"

    scene expression "backgrounds/location_home_bedroom_caught_04.jpg" with dissolve
    pause
    scene expression "backgrounds/location_home_bedroom_telescope_window.jpg"
    show anon b_telescope_peeking
    with dissolve
    pause
    show jenny b_telescope_standing f_grin zorder 1 with dissolve
    pause
    jenny "{i}*Ehem*{/i}"

    show anon b_telescope_peeking_caught
    anon "!!!" with hpunch
    show anon b_telescope f_surprised
    with dissolve
    jenny "Apa yang sedang kamu lakukan?"

    anon f_worried "N-nothing..."

    jenny "Are you perving on the neighbors?"

    anon f_surprised @ -m_talk "..."
    jenny "Let me see!"

    anon @ f_worried "Y-you don't have to-"

    jenny "Move!"

    show jenny b_telescope_look
    show anon b_telescope_laying_back f_surprised zorder 0
    with dissolve
    pause
    show jenny f_telescope_laugh b_telescope a_down with dissolve
    jenny "Heh, isn't that the super religious girl you're always hanging around with?"

    show jenny f_telescope_normal
    anon f_worried "{b}Mia{/b}'s not super religious..."

    show jenny b_telescope_look with dissolve
    pause
    anon "... Her parents are."

    jenny "Eh ya."

    pause
    jenny "I guess she isn't so goodie-goodie after all..."

    anon @ -m_talk "..."
    show jenny f_telescope_normal b_telescope a_down with dissolve
    jenny "... I bet this turns you on, huh?"

    anon "Apa?!"

    show anon f_surprised_teeth
    show jenny f_telescope_laugh
    jenny "You know, watching the little Bible-thumper rub her raspberry!"

    show jenny f_telescope_normal
    pause
    jenny "Does it get you hard?"

    if M_jenny.get("dominance") <= 0:
        anon f_worried "aku tidak-"

        anon "W-what are you talking about?"

        jenny "Tunjukkan padaku."

        anon "Y-you don't mean..."

        jenny "C'mon, I wanna see it!"

        anon "... R-really?"

        jenny "Tsk, you've seen me naked like a dozen times..."

        jenny "Quit being a loser and get it out!"

        anon "O-oke."

        show anon a_pull1 f_shy_down with dissolve
        pause
        show anon a_pull2 with dissolve
        pause
        show anon a_pull3 f_worried with dissolve
        show jenny f_telescope_surprised
        jenny "Good lord..."

        jenny "How do you walk around with that thing all day?"

        anon "Umm, I dunno."

        show jenny f_telescope_laugh a_up with dissolve
        jenny "It's like a little league baseball bat!"

        show jenny a_touch with dissolve
        anon "Apa yang kamu-"

        show jenny f_telescope_normal
        jenny "Oh, diamlah!"

        show jenny f_telescope_normal_down a_pushing
        show anon a_pushed f_shy_down
        with dissolve
        show jenny a_pushing_after
        show anon a_springing
        with dissolve
        pause
        show anon a_pull3 f_worried with dissolve
        show jenny f_telescope_laugh
        jenny "Hahahaah!"

        show jenny f_telescope_normal_down a_down with dissolve
        pause
        show jenny f_telescope_normal
        jenny "I can't believe you're equipped like this..."

        show jenny f_telescope_normal_down
        pause
        show jenny f_telescope_normal
        jenny "I guess I don't have to worry about you getting embarrassed in front of a camera."

        show jenny f_telescope_normal_down
        anon "Apa maksudmu?"

        pause
        show jenny f_telescope_normal
        jenny "You wanna do stuff with me, don't you?"

        show jenny f_telescope_angry
        anon "WHAT?!" with hpunch
        show anon f_surprised_teeth
        show jenny f_telescope_normal
        jenny "Don't deny it."

        jenny "Why else would you be perving on me in the shower or paying to see me naked?"

        anon f_worried "I-itu bukan-"

        anon "I mean, we can't-"

        jenny "Ugh, shut up!"

        jenny "I'll tell you what we can and cannot do."

        pause
        show jenny f_telescope_normal_down
        pause
        show jenny f_telescope_normal
        jenny "{i}*Sigh*{/i} Come to {b}my room this afternoon{/b}."

        show jenny b_telescope_standing f_grin with dissolve
        anon "Hah?"

        anon "W-what are you planning?"

        jenny "You'll find out."

        jenny "Just don't forget..."

        pause
        jenny "... And put that thing away. You look ridiculous."

        show anon f_surprised
        hide jenny with dissolve
        anon "..."
    else:
        anon f_skeptical "Did you really just ask me that?"

        show jenny f_telescope_normal
        jenny "Tunjukkan padaku."

        anon f_surprised @ -m_talk "..."
        anon f_worried "You want me to show you my dick?"

        jenny "Itu benar."

        anon "Why are you suddenly interested?"

        jenny "Who said I was interested?!"

        show anon f_squint
        pause
        anon f_skeptical "Well, if you aren't interested then why should I bother?"

        jenny "Alright, alright... damn you, I'm interested."

        jenny "Just fucking show me already, sheesh!"

        anon "Bagus."

        show anon a_pull1 f_shy_down with dissolve
        pause
        show anon a_pull2 with dissolve
        pause
        show anon a_pull3 f_worried with dissolve
        show jenny f_telescope_surprised
        jenny "Good lord..."

        jenny "How do you walk around with that thing all day?"

        anon "Umm, I dunno."

        show jenny f_telescope_laugh a_up with dissolve
        jenny "It's like a little league baseball bat!"

        show jenny a_touch with dissolve
        anon f_skeptical "Hey, who said you could touch?!"

        show jenny f_telescope_normal
        jenny "Pfft, I let you touch me..."

        anon f_worried "Not for free, you don't!"

        jenny "Oh, diamlah!"

        show jenny f_telescope_normal_down a_pushing
        show anon a_pushed f_shy_down
        with dissolve
        show jenny a_pushing_after
        show anon a_springing
        with dissolve
        pause
        show anon a_pull3 f_worried with dissolve
        show jenny f_telescope_laugh
        jenny "Hahahaah!"

        show jenny f_telescope_normal_down a_down with dissolve
        pause
        show jenny f_telescope_normal
        jenny "I can't believe you're equipped like this..."

        show jenny f_telescope_normal_down
        anon "Well, I am."

        show jenny f_telescope_normal
        jenny "I bet you wouldn't be shy about people seeing it, huh?"

        anon "I dunno, probably not..."

        anon "Mengapa?"

        pause
        jenny "You wanna do stuff with me, don't you?"

        show jenny f_telescope_angry
        anon "What kind of stuff?"

        show jenny f_telescope_normal
        jenny "Don't be dense, you know what I'm talking about!"

        anon "..."
        jenny "Why else would you be perving on me in the shower or paying to see me naked?"

        anon "Well, you do have a nice body... I'll give you that."

        jenny "You're damn right I do."

        jenny "And I suppose... your dick is pretty nice."

        show jenny f_telescope_normal_down
        anon @ f_skeptical "Did you just complement my penis?"

        show jenny f_telescope_laugh
        jenny "Too bad it's attached to a huge loser!"

        show jenny f_telescope_normal
        anon f_skeptical "... And there it is..."

        anon "... Always with the bitchy remarks."

        jenny "Apa pun."

        jenny "Just come to {b}my room this afternoon{/b}."

        jenny "I have a proposition for you."

        anon "Ya baiklah."

        show jenny f_telescope_normal_down
        pause
        show jenny f_telescope_normal
        jenny "Aku tidak percaya aku sedang mempertimbangkan ini..."

        pause
        show jenny b_telescope_standing f_grin with dissolve
        jenny "... And put that thing away. You look ridiculous."

        anon "Screw you."

        hide jenny with dissolve
        jenny "Haha!"

    scene expression game.timer.image("bedroom{}") with None
    show anon f_worried with dissolve
    anon @ -m_talk "( That was weird. )"

    anon @ -m_talk "( I can't believe she asked to see my dick. )"

    anon @ -m_talk "( Then she touched it! )"

    pause
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( Hmm, I wonder what she's planning in {b}her room{/b}? )"

    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Mia"]["unlocked"] = True
    $ persistent.cookie_jar["Mia"]["gallery"]["02_unlocked"] = True
    return

label telescope_mia_morning_1:
    scene windowmiamorning01
    if game.timer.dayOfWeek() == "Sun":
        player_name "( She's getting ready for church. )"

    elif game.timer.is_weekend():
        player_name "( I wonder what she's doing today? )"

    else:
        player_name "( She's getting ready for school. )"

    return

label telescope_mia_morning_2:
    scene windowmiamorning02
    player_name "( Too late... I always miss the best part! )"

    return

label telescope_mia_afternoon_1:
    scene windowmiaday 1
    player_name "( Her blinds are closed. She's probably not home. )"

    return

label telescope_mia_afternoon_2:
    scene windowmiaday 2
    player_name "( She's not home. )"

    return

label telescope_mia_night_1:
    scene windowmianight01
    player_name "( She's always reading or studying... )"

    return

label telescope_mia_night_2:
    if _in_replay or not M_mia.get("telescope teddy seen"):
        $ persistent.cookie_jar["Mia"]["unlocked"] = True
        $ persistent.cookie_jar["Mia"]["gallery"]["01_unlocked"] = True
        $ M_mia.set("telescope teddy seen", True)
        scene windowmianight03a_b
        player_name "( What's she doing? )"

        player_name "..."
        player_name "( She's... )"

        player_name "( ... Humping her teddy bear? )"

        player_name "( Wow... )"

        player_name "( That's really hot- )"

        scene windowmianight03c with hpunch
        player_name "!!!"
        scene windowmianight03d
        player_name "( Oh, crap! )"

        player_name "( I think she just got caught... )"

        player_name "( Her mom must be furious... She's always so strict with her... )"

        $ renpy.end_replay()
    else:
        call telescope_mia_night_3
    return

label telescope_mia_night_3:
    scene windowmianight02
    player_name "( She must be sleeping. )"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

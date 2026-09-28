label third_floor_okita_get_ingredients:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10 with dissolve
    player_name "Hmm, I need to {b}get into Mrs. Smith's office again to look for some kind of DNA sample{/b}..."
    player_name "I should go in when she's not there."
    return

label annie_enter_office_dialogue:
    $ player.go_to(L_school_floor3)
    if not M_okita.is_set("talked to annie"):
        call expression game.dialog_select("smith_office_annie_guarding")
        $ M_okita.set("talked to annie", True)
    else:

        call expression game.dialog_select("smith_office_annie_guarding_repeat")
        if player.has_required_chr(7):
            $ display.toast(chr_pass)
            call expression game.dialog_select("smith_office_annie_guarding_distract_pass")
            $ player.go_to(L_school_smithoffice)
            $ game.main()
        else:

            $ display.toast(chr_fail)
            call expression game.dialog_select("smith_office_annie_guarding_distract_fail")
    $ game.main()

label smith_office_annie_guarding_distract_pass:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 2 at left
    show old_annie 1 at right
    player_name "I just overheard your thief bragging downstairs near the boys' locker room..."
    show player 1
    show old_annie 3
    annie "What? Really?!"
    show player 2
    show old_annie 1
    player_name "Yup and if you hurry you might still catch him..."
    show player 1
    show old_annie 3
    annie "{b}Mrs. Smith{/b} will definitely reward me for that!"
    annie "Would you mind watching this door for me?"
    show player 2
    show old_annie 1
    player_name "Not at all. Go get him!"
    hide old_annie
    hide player
    show player 1f
    show old_annie 16 at left
    with dissolve
    annie "Ahahahahaah!"
    hide old_annie with dissolve

    show player 2f
    player_name "Well, that should keep her busy for a while..."
    player_name "Now to {b}search the office for something with Mrs. Smith's DNA on it{/b}."
    return

label smith_office_annie_guarding_distract_fail:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10 at left
    show old_annie 1 at right
    player_name "O-okay..."
    player_name "... I was just looking for {b}Mrs. Smith{/b}."
    show player 11
    show old_annie 3
    annie "Yeah, well, she isn't here."
    show old_annie 4
    annie "So beat it!"
    show player 12
    show old_annie 1
    player_name "Alright, sheesh! You don't have to get your panties in a bunch!"
    return

label smith_office_annie_guarding_repeat:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 11 at left
    show old_annie 3 at right
    with dissolve
    annie "Nobody is getting past me, {b}[firstname]{/b}!"
    return

label smith_office_annie_guarding:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10 at left
    show old_annie 1 at right
    with dissolve
    player_name "{b}Annie{/b}, what are you doing here?"
    show player 11
    show old_annie 3
    annie "I'm {b}guarding Mrs. Smith's office{/b} while she's away."
    show player 10
    show old_annie 1
    player_name "... Why?"
    show player 11
    show old_annie 3
    annie "Umm, because she asked me too? Duh."
    show old_annie 1
    player_name "..."
    show old_annie 3
    annie "She said someone keeps sneaking in and going through her stuff."
    show old_annie 5
    annie "You wouldn't happen to know anything about that, would you?!"
    show player 10
    show old_annie 6
    player_name "M-me? No, I don't know anything about that!"
    show player 11
    show old_annie 5
    annie "Uh huh..."
    show old_annie 3
    annie "Well, whoever it is, they aren't getting past {i}me{/i}!"
    show player 10
    player_name "Okay, well, good luck with that..."
    hide old_annie with dissolve
    hide player
    show player 5 with dissolve
    player_name "( I have to figure out into that office... )"
    show player 34
    player_name "( Perhaps I can {b}trick her{/b} somehow? )"
    return

label third_floor_roxxy_intro:
    scene expression game.timer.image("school_hall_third_floor{}_b")
    show anon f_skeptical with dissolve
    anon @ -m_talk "( ... )"
    anon @ -m_talk "( It looks like {b}Roxxy{/b} is arguing with some of the teachers... )"
    anon f_laugh @ -m_talk "( I should take a closer look! )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

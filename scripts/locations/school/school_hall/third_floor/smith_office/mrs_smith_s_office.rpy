label principal_smiths_office_dialogue:
    $ player.go_to(L_school_smithoffice)

    if M_diane.is_state(S_diane_delivery_3_fetch_invoice):
        call expression game.dialog_select("principals_office_delivery_invoice")
        $ M_diane.trigger(T_diane_delivery_3_got_invoice)

    elif M_dewitt.is_state([S_dewitt_paint_trail, S_dewitt_check_up]):
        call expression game.dialog_select("principals_office_dewitt_paint_trail")
        $ player.go_to(L_school_floor3)
        $ M_dewitt.trigger(T_dewitt_clue_dead_end)

    elif M_dewitt.is_state(S_dewitt_smith_office_trap):
        call expression game.dialog_select("principals_office_dewitt_smith_office_trap")
        $ player.remove_item("sticky_tape")
        $ player.go_to(L_map)

        $ game.timer.tick()
        $ M_dewitt.trigger(T_dewitt_trap_set)

    elif M_dewitt.is_state(S_dewitt_trap_check_up):
        call expression game.dialog_select("principals_office_dewitt_trap_check_up")
        $ player.go_to(L_school_floor3)
        $ M_dewitt.trigger(T_dewitt_trap_check_ok)

    elif M_dewitt.is_state(S_dewitt_office_night_visit_delay):
        call expression game.dialog_select("principals_office_dewitt_office_night_visit_delay")
        $ player.go_to(L_school_floor3)

    elif M_okita.is_state(S_okita_get_keycode) and game.timer.is_morning():
        call expression game.dialog_select("principals_office_okita_get_keycode_morning")
        $ player.go_to(L_school_floor3)
        $ game.main()

    elif M_okita.is_state(S_okita_get_keycode) and game.timer.is_afternoon():
        call expression game.dialog_select("principals_office_okita_get_keycode_afternoon")

    elif M_okita.is_state(S_okita_get_ingredients) and game.timer.is_morning():
        call expression game.dialog_select("principals_office_okita_get_ingredients_morning")
        $ player.go_to(L_school_floor3)
        $ game.main()

    elif M_latinas.is_state(S_latinas_caught):
        call expression game.dialog_select("principals_office_annie_trouble")
        $ persistent.cookie_jar["Annie"]["unlocked"] = True
        $ persistent.cookie_jar["Annie"]["gallery"]["01_unlocked"] = True
        $ M_latinas.trigger(T_latinas_annie_trouble)

    elif M_smith.is_state(S_smith_intro, S_smith_go_to_locker):
        $ pass

    elif M_eve.is_state(S_eve_school_dress_code):
        $ pass

    elif player.location.is_here(M_smith):
        if game.timer.is_dark():
            call expression game.dialog_select("principals_office_no_entry_night")
        else:
            call expression game.dialog_select("principals_office_no_entry")
        $ player.go_to(L_school_floor3)
        $ game.main()
    $ game.main()

label smith_office_smith_delivery_3_dialogue:
    scene expression "backgrounds/location_school_office_chair_closeup.jpg"
    show player 168b at left
    show titty 1f at right
    show principal 27 at Position (xpos=614)
    with dissolve
    smith "Stop gawking! Take {b}Ronda{/b} and get that delivery down to the cafeteria!"
    show principal 26
    show player 168c
    player_name "Y-yes, ma'am!"
    hide player
    hide titty
    hide principal
    with dissolve
    $ game.main()

label smith_office_ronda_delivery_3_dialogue:
    scene expression "backgrounds/location_school_office_chair_closeup.jpg"
    show old_annie 6 zorder 3 at right
    show ronda b_chair1 f_upset zorder 1
    show player 427f zorder 2 at Position (xpos=700)
    with dissolve
    player_name "H-hey, {b}Ronda{/b}..."
    show player 433f
    with dissolve
    ronda "Get me out of here!"
    show player 427f with dissolve
    player_name "Don't worry, I'll get you out of here."
    show ronda f_surprised_down
    show player 670bf at Position (xoffset=-140)
    with dissolve
    player_name "Let me just..."
    show ronda b_chair2 f_hurt_down
    show player 670d at Position (xoffset=-218)
    with dissolve
    pause
    show player 670b zorder 0 at Position (xoffset=-740) with dissolve
    with dissolve
    ronda f_surprised_down "... Thanks."
    ronda f_hurt_down "Ugh, this is so embarrassing..."
    show old_annie 5
    annie "Oh, don't be so dramatic!"
    show ronda f_upset
    annie "It's not that bad."
    show old_annie 6
    ronda @ f_upset_angry "You all are some messed-up people!"
    show old_annie 3
    annie "She can do a lot worse, you know..."
    show old_annie 5
    annie "... I would have recommended she gag you."
    show old_annie 6
    ronda "Creepy little bitch..."
    show old_annie 4
    annie "I heard that!"
    show old_annie 6
    ronda f_upset_angry "Oh, yeah?! You're lucky I'm tied up right now!"
    ronda "Otherwise, I'd knock that smug look right off your stupid face!"
    show ronda f_upset
    player_name "Would you both please shut up!"
    player_name "It's hard enough trying to untie this without you two distracting me!"
    ronda @ -m_talk "..."
    player_name "Got it!"
    show ronda b_chair3 with dissolve
    show player 433f at Position (xpos=700) with dissolve
    pause
    hide ronda
    show ronda b_shirt_on:
        flip
    with dissolve
    pause
    show ronda b_dressed a_box f_upset with dissolve
    show player 11f
    ronda "I'm out of here."
    ronda "You better pray my father doesn't find out about this!"
    smith "{i}*Snort*{/i} Like that fat simpleton can do anything!"
    show old_annie 7
    annie "Hahaha!"
    ronda "Grrr!!!!"
    hide ronda with dissolve
    pause
    show player 10f
    show old_annie 6
    player_name "{b}Ronda{/b}, wait up!"
    hide player with dissolve
    pause
    show old_annie 3f at center with dissolve
    annie "{b}Mrs. Smith{/b}, I'll make sure they deliver-"
    show old_annie 1f
    smith "Ah, ah, ah!"
    smith "You're not going anywhere until you've been properly punished for barging in here."
    show old_annie 10f
    annie "O-of course, ma'am."
    hide old_annie with dissolve
    scene expression "backgrounds/location_school_cafeteria_day_blur.jpg"
    show ronda a_box f_normal:
        flip
        xoffset -100
    show player 13f zorder 1 at right
    with dissolve
    ronda "Thanks again for getting me out of there, {b}[firstname]{/b}."
    show ronda a_idle with dissolve
    show player 14f
    player_name "Not a problem."
    show player 10f
    player_name "What did you do to end up in there anyways?"
    show player 5f
    ronda "Ugh, I was in {b}Coach Bridget{/b}'s office working out and {b}Mrs. Smith{/b} comes in yelling about whether I had permission to be there or not."
    ronda "I told her {b}Coach{/b} lets me use her equipment all the time, but she didn't believe me."
    ronda "Next thing I know, I'm tied up in her office and that psychopath is pulling my bra down!"
    show player 10f
    player_name "Yeah, she is pretty weird..."
    show player 12f
    player_name "Say, isn't your dad the police chief?!"
    show player 5f
    ronda "Yeah, so?"
    show player 12f
    player_name "So why don't you tell him about all the inappropriate stuff {b}Mrs. Smith{/b} does around here?!"
    player_name "Surely he could help-"
    show player 11f
    ronda "Nah, I don't wanna bother him with that."
    ronda "He has enough on his plate already, trust me."
    show player 4f with dissolve
    pause
    show player 10f with dissolve
    player_name "Oh."
    show player 401f
    player_name "O-okay..."
    show player 13f
    show old_kevin 9b zorder 0 at Position (xpos=600) with dissolve
    kevin "Sup, bros!"
    show old_kevin 19 at Position (xoffset=-95) with dissolve
    kevin "Is that the new milk for the cafeteria?"
    show old_kevin 23f at Position (xoffset=-50) with dissolve
    show player 14f
    player_name "Hey, {b}Kevin{/b}."
    player_name "Yup, this is it."
    show player 13f
    show old_kevin 40 at Position (xoffset=-58) with dissolve
    kevin "Right on!"
    show old_kevin 42 at Position (xoffset=-47) with dissolve
    pause
    show old_kevin 41 at Position (xoffset=-113) with dissolve
    kevin "Whoa, that's delicious!"
    show old_kevin 39 at Position (xoffset=-58) with dissolve
    show player 14f
    player_name "I know, right?"
    show player 13f
    show old_kevin 38 at Position (xoffset=-58)
    kevin "You tried this stuff?"
    show old_kevin 23
    show ronda a_milk
    with dissolve
    pause
    show ronda f_drink a_milk_drink with dissolve
    pause
    show ronda f_surprised a_milk with dissolve
    ronda "!!!"
    show ronda f_surprised_down
    ronda "Mmm!"
    ronda "Oh my god, that would be amazing in a protein shake!"
    show ronda f_drink a_milk_drink with dissolve
    show old_kevin 9b
    kevin "Totally!"
    show old_kevin 23
    show ronda f_normal a_milk with dissolve
    show player 14f
    player_name "So who's supposed to pay me for this?"
    show player 13f
    show old_kevin 9bf at Position (xoffset=-127) with dissolve
    kevin "I've got you."
    show old_kevin 43f zorder 2 at Position (xoffset=-50) with dissolve
    pause
    show old_kevin 23f zorder 0 at Position (xoffset=-127)
    show player 640ef at Position (xoffset=-9)
    with dissolve
    player_name "Thanks!"
    show player 13f
    show old_kevin 23
    with dissolve
    ronda "Can you get me more of this?"
    show player 14f
    player_name "Heh, you'll have to order it from my friend."
    player_name "She's the one who makes it."
    show player 13f
    show old_kevin 9b
    kevin "I've got her number in the kitchen."
    kevin "C'mon, I've gotta place the next order anyways."
    show old_kevin 23
    ronda "Right behind you."
    show player 14f
    player_name "I'll leave you all to it..."
    show player 13f
    show old_kevin 9bf at Position (xoffset=-127) with dissolve
    kevin "Bye!"
    show old_kevin 23f at Position (xoffset=-127)
    ronda a_milk_wave "See ya, {b}[firstname]{/b}."
    show player 14f
    player_name "See ya."
    hide ronda
    hide player
    hide old_kevin
    with dissolve
    $ player.remove_item("milk_9x9z2y")
    $ M_diane.trigger(T_diane_delivery_3_finished)
    $ player.go_to(L_school_cafeteria)
    $ game.unlock_ui()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

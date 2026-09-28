label okita_office_door:
    $ player.go_to(L_school_floor3)
    if M_okita.is_set("office locked"):
        if player.has_item("keycode_note"):
            call screen okita_keypad
        else:
            call expression game.dialog_select("okita_office_door_need_keycode")
    else:
        if M_okita.is_state(S_okita_tired_from_belt):
            call expression game.dialog_select("okita_office_door_okita_tired")
        else:
            jump okita_office_door_through
    $ game.main()

label okita_office_door_need_keycode:
    scene expression player.location.background_blur
    show player 10
    with dissolve
    player_name "Hmm, I guess {b}Miss Okita{/b} keeps her office locked when she's not inside?"
    player_name "It's got one of those automated keypad locks too."
    show player 11
    pause
    show player 10
    player_name "I'm definitely not getting in there without a {b}key code{/b}."
    return

label okita_office_door_okita_tired:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10
    with dissolve
    player_name "I should let her rest for now."
    return

label okita_office_unlock:
    $ M_okita.set("office locked", False)
    jump okita_office_door_through

label okita_office_locked:
    $ player.go_to(L_school_floor3)
    scene expression player.location.background_blur
    show player 10
    with dissolve
    player_name "Oops! That wasn't the right code..."
    show player 34
    player_name "Hmm, I'd better {b}double check that key code{/b} I got out of {b}Mrs. Smith{/b}'s desk before trying again."
    $ game.main()

label okita_office_door_through:
    $ player.location.hide_screen()
    $ player.go_to(L_school_okitaoffice)
    $ L_school_okitaoffice.call()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label treehouse_first_visit:
    scene expression player.location.background_blur
    show player 32 with dissolve
    player_name "Cool! Our old tree house is still holding up."
    hide player with dissolve
    return

label treehouse_closeup_first_visit:
    scene expression player.location.background
    player_name "( That doesn't look too safe... )"
    return

label treehouse_interior_first_visit:
    scene expression player.location.background_blur
    show player 2 with dissolve
    player_name "( Wow! It hasn't changed at all! )"
    player_name "( Let's have a look around... )"
    hide player with dissolve
    return

label treehouse_got_wood_pile:
    scene expression player.location.background_blur
    if M_ross.is_state(S_ross_get_easels):
        call expression game.dialog_select("treehouse_woodpile_ross_easels")

    elif M_dewitt.between_states(S_dewitt_garage_find_paint, S_dewitt_make_replacement_guitar):
        call expression game.dialog_select("treehouse_woodpile_dewitt_guitar")

    call expression game.dialog_select("treehouse_woodpile_after")
    $ player.get_item("wood_pile")
    $ game.main()

label treehouse_woodpile_ross_easels:
    show player 585 with dissolve
    player_name "These will work great!"
    show player 586
    pause
    show player 585
    player_name "I can {b}take these to Dad's old workbench at the house{/b} to build some easels."
    return

label treehouse_woodpile_dewitt_guitar:
    show player 585 with dissolve
    player_name "Yeah, this should work."
    player_name "With some tools and a little {b}paint{/b}, I can make a fake guitar no problem."
    return

label treehouse_woodpile_after:
    hide player with dissolve
    call popup ('give', 'wood_pile')
    return

label treehouse_got_controller:
    call expression game.dialog_select("treehouse_controller_dialogue")
    if _return:
        call popup ('give', 'controller')
        $ player.get_item("controller")
    $ game.main()

label treehouse_controller_dialogue:
    scene expression player.location.background_blur
    show player 502b
    with dissolve
    player_name "There it is!"
    player_name "Man, {b}Erik{/b} sure did love this thing..."

    if M_okita.is_state(S_okita_get_controller):
        player_name "It's nice of him to let me take it."
        show player 502
        player_name "I'd best get this to {b}June{/b}."
        hide player with dissolve
        return True

    player_name "I should speak to him about it, I don't want to just take it."
    hide player with dissolve
    return

label lure_02:
    call expression game.dialog_select("lure_02_dialogue")
    $ player.get_item("lure01")
    $ game.main()

label lure_02_dialogue:
    scene expression "backgrounds/location_treehouse_box.jpg"
    call popup ('give', 'lure01')
    return

label treehouse_box_binoculars_dialogue:
    scene expression player.location.background_blur
    show anon f_grin with dissolve
    anon @ -m_talk "( Alright, they're still here! )"
    anon @ -m_talk "( These should come in real handy. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

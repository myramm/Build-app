label treehouse_dialogue:
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if L_treehouse.first_visit:
        call expression game.dialog_select("treehouse_first_visit")
        $ L_treehouse.visited()
    $ game.main()
    return


label treehouse_ladder_dialogue:
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if L_treehouse_ladder.first_visit:
        call expression game.dialog_select("treehouse_closeup_first_visit")
        $ L_treehouse_ladder.visited()

    $ player.location.call_screen(False)
    return


label treehouse_interior_dialogue:
    if not game.timer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if L_treehouse_interior.first_visit:
        call expression game.dialog_select("treehouse_interior_first_visit")
        $ L_treehouse_interior.visited()
    $ game.main()
    return


label treehouse_box_binoculars:
    call treehouse_box_binoculars_dialogue
    $ player.get_item('binoculars')
    call popup ('give', 'binoculars')
    if M_anon.is_state(S_ano12_zoom):
        $ M_anon.trigger(T_ano12_zoom)

    $ game.main()
    return


label treehouse_dink:
    if M_anon.is_state(S_ano28_dink):
        if game.timer.is_day():
            call ano28_dink_dink
            $ player.get_item('money_bag')
            call popup ('give', 'money_bag')
            $ game.timer.tick()
            $ M_anon.trigger(T_ano28_dink)
        else:
            call ano28_dink_dink.late
    else:
        call treehouse_dink_dialogue

    $ game.main()
    return


label treehouse_window:
    call treehouse_window_dialogue

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

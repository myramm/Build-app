label hill_dialogue:
    $ player.go_to(L_hill)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 129>audio/ambience_ravenhill.ogg"):
            $ playSound("<loop 129>audio/ambience_ravenhill.ogg")
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if M_anon.is_state(S_ano27_init) and game.timer.is_evening():
        $ setrestorepoint()

    if L_hill.first_visit and not M_mia.is_state(S_mia_find_harold):
        call expression game.dialog_select("hill_first_visit")
        $ L_hill.visited()

    elif M_mia.is_state(S_mia_find_harold) and game.timer.is_day():
        call expression game.dialog_select("hill_mia_find_harold")

    elif M_mia.is_state(S_mia_find_harold):
        call expression game.dialog_select("hill_mia_find_harold_night")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

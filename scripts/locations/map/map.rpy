label town_map_dialogue:
    if M_erik.is_state(S_erik_bully_visit):
        $ player.go_to(L_home_entrance)
        jump entrance_dialogue

    $ player.go_to(L_map)

    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

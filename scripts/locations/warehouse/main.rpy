label warehouse_dialogue:
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if M_anon.is_state(S_ano12_dark):
        call ano12_dark_warehouse
        $ M_anon.trigger(T_ano12_dark)

    $ game.main()
    return


label warehouse_door:
    call ano12_oops_warehouse_door

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

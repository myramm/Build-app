label mias_house_dialogue:
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if game.timer.is_morning() and not game.timer.is_weekend() and not M_mia.between_states(S_mia_urgent_help, S_mia_harold_found_news):
        call expression game.dialog_select("mias_house_is_morning")

    elif M_mia.get_state() == S_mia_concerning_visit and game.timer.is_afternoon():
        call expression game.dialog_select("mias_house_mia_concerning_visit")
        $ M_mia.trigger(T_harold_leaves)

    $ game.main()

label mias_mailbox_dialogue:
    $ player.location.call_screen(False)

label mias_mailbox_item:
    scene expression player.location.background_blur

    if game.mail["mia"] == "m_pizza_pamphlet":
        call expression game.dialog_select("mailbox_pizza_pamphlet")

    elif game.mail["mia"] == "m_newspaper":
        call expression game.dialog_select("mailbox_newspaper")

    $ player.location.call_screen(False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

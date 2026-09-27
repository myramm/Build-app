label park_bushes_dialogue:
    $ player.go_to(L_park_bushes)

    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if player.has_picked_up_item("treasure_key") and not player.has_picked_up_item("stolen_goods"):
        scene expression game.timer.image("park_bushes{}_b")
        $ player.get_item('stolen_goods')
        call popup ('give', 'stolen_goods')

    if M_larry.is_state(S_larry_msg_done) or M_mia.is_state(S_mia_stolen_goods):
        call park_bushes_loot_located

    $ game.main()

label park_bushes_bag_dialogue:
    $ player.go_to(L_park_bushesbag)

    if M_larry.is_state(S_larry_msg_done) or M_mia.is_state(S_mia_stolen_goods):
        call park_bushes_loot_bag

    $ M_mia.trigger(T_harold_found_goods)
    $ M_mia.set('stolen goods recovered', True)
    $ player.location.call_screen(False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

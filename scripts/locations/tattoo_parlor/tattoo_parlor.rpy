label tattoo_parlor_dialogue:
    $ player.go_to(L_tattooparlor)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    if M_eve.is_state(S_eve_visit_tattoo_shop) and game.timer.is_evening():
        $ player.go_to(L_tattooparlor_interior)
        call expression game.dialog_select("tattoo_parlor_eve_visit_tattoo_shop")
        $ M_eve.trigger(T_eve_visited_tattoo_shop)
    elif M_eve.is_state(S_eve_ask_distract_grace) and not game.timer.is_night():
        $ player.go_to(L_tattooparlor_fire_escape)
        call expression game.dialog_select("tattoo_parlor_eve_distract_grace")
        $ M_eve.trigger(T_eve_distract_grace)
        $ player.go_to(L_tattooparlor_apartment)
        $ game.main()
    elif M_eve.is_state(S_eve_upset_pot) and game.timer.is_tick(0, 1, 2):
        $ player.go_to(L_tattooparlor_interior)
        call expression game.dialog_select("tattoo_parlor_eve_upset_pot")
        $ M_eve.trigger(T_eve_pot_cheerup)
        $ game.main()
    elif M_eve.is_state(S_eve_voyeurism_meetup) and game.timer.is_evening():
        call expression game.dialog_select("tattoo_parlor_eve_voyeurism_meetup")
        $ M_eve.trigger(T_eve_voyeurism_follow_roof)
        $ game.main()
    elif M_eve.is_state(S_eve_clients_tattooshop_crowd) and game.timer.is_day():
        call expression game.dialog_select("tattoo_parlor_eve_clients_tattooshop_crowd")
        $ M_eve.trigger(T_eve_tattoo_shop_crowded)
    elif M_eve.is_state(S_eve_party_start) and game.timer.is_evening() and game.timer.is_dow(5):
        call expression game.dialog_select("tattoo_parlor_eve_party_start")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

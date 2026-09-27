label living_room_dialogue:
    $ player.go_to(L_home_livingroom)

    if M_anon.is_state(S_ano21_news):
        call ano21_news_home_lounge
        $ game.timer.tick(3)
        $ player.go_to(L_home_entrance)
        $ M_anon.trigger(T_ano21_news)

    elif M_debbie.is_state(S_debbie_spy) and not game.timer.is_dark():
        call expression game.dialog_select("living_room_mom_spy")

    elif M_diane.is_state(S_diane_peeking) and game.timer.is_evening():
        call expression game.dialog_select("living_room_diane_peeking")
        $ M_diane.trigger(T_diane_gotta_jack_it)
        $ player.go_to(L_home_bedroom)
        $ game.lock_ui()

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

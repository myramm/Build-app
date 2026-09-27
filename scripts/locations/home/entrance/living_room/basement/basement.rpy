label basement_dialogue:
    $ player.go_to(L_home_basement)
    if M_debbie.is_state(S_debbie_wash_clothes):
        call expression game.dialog_select("basement_mom_wash_clothes")
        $ M_debbie.trigger(T_debbie_clean_clothes)
        $ player.go_to(L_home_bedroom)

        $ game.timer.tick()

    elif M_debbie.is_state(S_debbie_close_valve):
        call expression game.dialog_select("basement_mom_close_valve")

    elif M_debbie.is_state(S_debbie_lotion_adventure) and M_debbie.is_set("retrieved lotion"):
        jump expression game.dialog_select("mom_lotion_fun")

    elif M_debbie.is_state(S_debbie_give_laundry):
        call expression game.dialog_select("basement_mom_give_laundry")
        jump expression game.dialog_select("basement_mom_sex")
    $ game.main()

label basement_basket_debbie_panties:
    scene expression player.location.background_blur with None
    if M_somrak.finished_state(S_somrak_start):
        show player 724 with dissolve
        player_name "( These are {b}[deb_name]{/b}'s panties. )"

        player_name "( Man, they sure are soft... )"

        pause
        player_name "( I bet {b}Master Somrak{/b} would like these. )"

        hide player with dissolve
        $ player.get_item("debbie_panties")
    else:
        show player 10 with dissolve
        player_name "( Why would I try to steal {b}[deb_name]{/b}'s panties. )"

        player_name "( I have no use for them right now. )"

        hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

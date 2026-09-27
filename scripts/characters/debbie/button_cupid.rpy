label debbie_cupid_outing:
    scene expression player.location.background_blur
    if M_debbie.is_state(S_debbie_choose_gift):
        call expression game.dialog_select("mom_cupid_outing_choose_gift")

    elif M_debbie.is_state(S_debbie_show_necklace):
        $ player.remove_item("pearl_necklace")
        call expression game.dialog_select("mom_cupid_outing_show_necklace")
        $ M_debbie.trigger(T_debbie_give_necklace)
    hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

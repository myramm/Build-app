label pizzeria_storage_dialogue:
    if M_diane.is_state(S_dia03_stow):
        call dia03_stow_pizzeria_storage
        $ M_maria.set('met', True)
        $ player.remove_item('milk_2x2z1y')
        $ player.get_money(100)
        $ M_diane.trigger(T_dia03_stow)
        $ player.go_to(L_pizzeria_exterior)

    $ game.main()
    return


label pizzeria_storage_sack:
    if not game.timer.is_day():
        if L_pizzeria_storage.is_here(M_maria):
            jump maria_button_dialogue

        call ano08_sack_flour_late
        jump pizzeria_storage_sack.skip

    if player.stats.str() < 5:
        call ano08_sack_flour_fail
    else:
        call ano08_sack_flour_pass
        $ M_anon.trigger(T_ano08_sack)

    label pizzeria_storage_sack.skip:
    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

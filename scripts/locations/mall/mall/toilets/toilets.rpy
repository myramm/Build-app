label mall_toilets_dialogue:
    $ player.go_to(L_mall_toilets)

    if game.rump_n_cunt:
        call expression game.dialog_select("mall_toilets_rump_n_cunt")

    $ game.main()
    return


label mall_toilets_stall_dialogue:
    if game.rump_n_cunt:
        call rump_toilets_stall

    elif M_anon.is_state(S_ano07_find):
        call ano07_find_mall_toilet
    else:

        call mall_toilets_stall

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label tattoo_parlor_bathroom_dialogue:
    if player.location.is_here(M_eve) and M_eve.pregnancy.stage in (3, 4):
        call tattoo_parlor_bathroom_eve_shower

    elif M_eve.is_state(S_eve_bathroom_break):
        call expression game.dialog_select("tattoo_parlor_bathroom_eve_bathroom_break")
        $ M_eve.trigger(T_eve_bathroom_mishap)

    elif player.location.is_here(M_grace) and M_grace.pregnancy.stage in (3, 4):
        call tattoo_parlor_bathroom_grace_shower

    elif player.location.is_here(M_odette) and M_odette.pregnancy.stage in (3, 4):
        call tattoo_parlor_bathroom_odette_shower

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

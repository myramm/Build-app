label warehouse_bushes_dialogue:
    if M_anon.is_state(S_ano12_oops):
        $ game.timer.tick(3)
        call ano12_oops_warehouse_bushes
        $ player.go_to(L_home_hallway)
        $ M_anon.trigger(T_ano12_oops)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label iwanka_rumps_bedroom_dialogue:

    if M_iwanka.is_state(S_iwa02_init):
        call iwa02_init_rump_second
        if _return:
            $ player.go_to(L_boat_bridge)
        if game.timer._tod < 1:
            $ game.timer.tick(1)
        $ M_iwanka.trigger(T_iwa02_init)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

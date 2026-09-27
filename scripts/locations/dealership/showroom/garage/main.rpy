label dealership_garage_dialogue:

    if M_yoyo.is_state(S_yoy01_lewd):
        call yoy01_meet_dealership_garage
        $ M_yoyo.trigger(T_yoy01_lewd)
        $ game.timer.tick(3)
        $ player.go_to(L_map)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

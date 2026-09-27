label dianes_front_yard_dialogue:
    $ player.go_to(L_diane_yard)
    if M_diane.is_state(S_diane_seen_cucumber):
        call expression game.dialog_select("dianes_front_seen_cucumber")
        $ M_diane.trigger(T_diane_cucumber_aftermath)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

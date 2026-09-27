label tattoo_parlor_tent_dialogue:
    if M_eve.is_state(S_eve_voyeurism_follow_tent):
        call expression game.dialog_select("tattoo_parlor_tent_eve_voyeurism_follow_tent")
        $ M_eve.trigger(T_eve_trap_revealed)
        $ game.timer.tick()
        $ player.go_to(L_map)
        $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

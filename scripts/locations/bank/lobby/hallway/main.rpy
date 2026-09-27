label bank_hallway_dialogue:

    if M_anon.is_state(S_ano23_help):
        call ano23_help_bank_hallway
        $ player.go_to(L_bank)
        $ M_anon.trigger(T_ano23_help)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

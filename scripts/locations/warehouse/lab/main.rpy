label warehouse_lab_dialogue:

    if M_anon.is_state(S_ano27_free):
        call ano27_free_warehouse_lab
        $ M_anon.trigger(T_ano27_free)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

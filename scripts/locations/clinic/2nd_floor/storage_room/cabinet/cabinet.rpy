label hospital_storage_cabinet_dialogue:
    if M_erik.is_state(S_erik_learn_fetch, S_erik_learn_get_pills):
        call expression game.dialog_select("hospital_storage_cabinet_erik_learn_pills")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

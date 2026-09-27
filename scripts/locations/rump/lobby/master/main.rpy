label mayor_rumps_bedroom_dialogue:

    if M_anon.is_state(S_ano18_trap):
        call ano18_trap_rump_master

    elif M_melonia.is_state(S_mel01_init) and L_rump_master.is_here(M_melonia):
        call mel01_init_rump_master
        $ M_melonia.set('scare', True)
        $ player.go_to(L_rump_lobby)

    $ game.main()
    return


label rump_bedroom_bed:
    if M_anon.is_state(S_ano18_hide):
        call ano18_hide_bed
        $ M_anon.trigger(T_ano18_hide)

    $ game.main()
    return


label rump_bedroom_painting:
    call rump_bedroom_painting_dialogue

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label mayor_rumps_office_dialogue:
    if M_anon.is_state(S_ano20_oval):
        call ano20_oval_rump_office
        $ M_anon.trigger(T_ano20_oval)

    $ game.main()
    return


label rump_office_bobblehead:
    call ano20_open_bobblehead

    $ game.main()
    return


label rump_office_bookcase:
    call ano20_open_bookcase

    $ game.main()
    return


label rump_office_papers:
    call ano20_open_papers

    $ game.main()
    return


label rump_office_safe:
    call ano20_open_safe

    if M_anon.is_state(S_ano20_find):
        $ M_anon.trigger(T_ano20_find)

    if _return:
        $ player.get_item('evidence')
        call popup ('give', 'evidence')
        $ M_anon.trigger(T_ano20_open)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

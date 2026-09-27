init -1 python:
    M_svetlana = Machine(
        'svetlana',
        default_loc=[[L_warehouse_depot,
                      L_warehouse_depot,
                      L_warehouse_depot,
                      L_NULL]],
        vars={'sex speed': 1. / 12})


init -3 python:
    T_sve01_init = Trigger()
    T_sve01_lewd = Trigger()


init python:
    S_sve00_init = State()
    S_sve00_done = State()


    S_sve01_init = State(_("I wonder how Svetlana and Nadya are getting on with the new business."))
    S_sve01_wait = State(_("Was it just me or was Svetlana blushing..."))
    S_sve01_lewd = State(_("Maybe Nadya can help me get a better read on Svetlana."))
    S_sve01_done = State()


init python:
    S_sve00_init.add(T_nad01_lewd, S_sve00_done)
    S_sve00_done.add(T_all_sleep, S_sve01_init,
                     actions=('priority', 1))

    S_sve01_init.add(T_sve01_init, S_sve01_wait)
    S_sve01_wait.add(T_all_sleep, S_sve01_lewd,
                     actions=('location', ('nadya', {'tod': [0, 1], 'place': L_warehouse_office}),
                              'force', ('nadya', {'tod': [0, 1]})))
    S_sve01_lewd.add(T_sve01_lewd, S_sve01_done,
                     actions=('unforce', 'nadya',
                              'unforce', None))


init python:
    M_svetlana.add(
        S_sve00_init, S_sve00_done,
        S_sve01_init, S_sve01_wait, S_sve01_lewd, S_sve01_done)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

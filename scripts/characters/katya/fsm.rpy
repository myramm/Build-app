init -1 python:
    M_katya = Machine(
        'katya',
        default_loc=[[L_NULL, L_NULL, L_NULL, L_NULL]],
        vars={'sex speed': 1. / 12})


init -3 python:
    T_kat01_init = Trigger()


init python:
    S_kat00_init = State()
    S_kat00_done = State(delay=6)


    S_kat01_init = State(_("I hope Katya from the warehouse is doing okay. Maybe I can visit her after work."))
    S_kat01_done = State()


init python:
    S_kat00_init.add(T_nad01_lewd, S_kat00_done,
                     actions=('setdefaultloc', [[L_warehouse_office,
                                                 L_warehouse_office,
                                                 L_NULL, L_NULL]]))
    S_kat00_done.add(T_all_sleep, S_kat01_init,
                     actions=('priority', 1))

    S_kat01_init.add(T_kat01_init, S_kat01_done,
                     actions=('setdefaultloc', [[L_warehouse_office,
                                                 L_warehouse_office,
                                                 L_warehouse_depot,
                                                 L_NULL]]))


init python:
    M_katya.add(
        S_kat00_init, S_kat00_done,
        S_kat01_init, S_kat01_done)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

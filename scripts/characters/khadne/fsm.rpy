init -1 python:
    M_khadne = Machine(
        'khadne',
        default_loc=[[L_NULL, L_NULL, L_NULL, L_NULL]],
        vars={'sex speed': 1. / 12})


init -3 python:
    T_kha01_init = Trigger()
    T_kha01_lewd = Trigger()
    T_kha01_talk = Trigger()


init python:
    S_kha00_init = State()
    S_kha00_wait = State()
    S_kha00_done = State()


    S_kha01_init = State(_("Maybe it's time to speak to Nadya about that job offer..."))
    S_kha01_lewd = State(_("Nadya said I should help Khadne relieve some pressure in the lab."))
    S_kha01_talk = State(_("I should let Nadya know that Khadne's feeling more relaxed."))
    S_kha01_done = State()


init python:
    S_kha00_init.add(T_nad01_lewd, S_kha00_wait,
                     actions=('setdefaultloc', [[L_warehouse_lab,
                                                 L_warehouse_lab,
                                                 L_NULL, L_NULL]]))
    S_kha00_wait.add(T_kat01_init, S_kha00_done)
    S_kha00_done.add(T_all_sleep, S_kha01_init,
                     actions=('priority', 1))

    S_kha01_init.add(T_kha01_init, S_kha01_lewd)
    S_kha01_lewd.add(T_kha01_lewd, S_kha01_talk,
                     actions=('setdefaultloc', [[L_warehouse_lab,
                                                 L_warehouse_lab,
                                                 L_warehouse_depot,
                                                 L_NULL]]))
    S_kha01_talk.add(T_kha01_talk, S_kha01_done)


init python:
    M_khadne.add(
        S_kha00_init, S_kha00_wait, S_kha00_done,
        S_kha01_init, S_kha01_lewd, S_kha01_talk, S_kha01_done)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

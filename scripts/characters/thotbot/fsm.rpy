init -1 python:
    M_thotbot = Machine(
        'thotbot',
        default_loc=[[L_NULL] * 4],
        vars={})


init -3 python:
    T_bot01_init = Trigger()


init python:
    S_bot00_init = State()
    S_bot00_done = State()

    S_bot01_init = State(_("I wonder how the Rump's are getting on with the Thotbot..."))
    S_bot01_wait = State(_("Don't think about it. Nope. Nopenopenope."))
    S_bot01_done = State(_("Do not touch. D:"))


init python hide:

    S_bot00_init.add(T_con01_give, S_bot01_init)
    S_bot00_init.add(T_con01_skip, S_bot00_done)
    S_bot00_done.add(T_all_sleep, S_bot01_init)


    home = ('setdefaultloc', [[L_rump_lobby] * 4])
    S_bot01_init.add(T_bot01_init, S_bot01_wait,
                     actions=('condition', (
                        'M_consuela.finished_state(S_con01_skip)', home)))
    S_bot01_wait.add(T_all_sleep, S_bot01_done, actions=home)


init python:
    M_thotbot.add(
        S_bot00_init, S_bot00_done,
        S_bot01_init, S_bot01_wait, S_bot01_done)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

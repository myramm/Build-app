init -1 python:
    M_yoyo = Machine(
        'yoyo',
        default_loc=[[L_NULL] * 4],
        vars={'sex speed': 0.3})


init -3 python:
    T_yoy00_hook = Trigger()

    T_yoy01_init = Trigger()
    T_yoy01_meet = Trigger()
    T_yoy01_hold = Trigger()
    T_yoy01_lewd = Trigger()


init python:
    S_yoy00_hook = State()


    S_yoy01_init = State(_("I can't believe how like her brother she is. What has to happen in your life for you to end up like that?"))
    S_yoy01_wait = State(_("That's quite enough for one day. Maybe I'll try again later."))
    S_yoy01_meet = State(_("Maybe it's worth trying to speak to her again. Better psych myself up for it though."))
    S_yoy01_hold = State(_("Banana cream? I know it's probably a bad idea... but maybe I should take her up on it..."))
    S_yoy01_lewd = State(_("Kim's waiting with her tasty banana cream pie in the garage, I should get in there."))
    S_yoy01_done = State()


init python:
    S_yoy00_hook.add(T_yoy00_hook, S_yoy01_init,
                     actions=('priority', 1))

    S_yoy01_init.add(T_yoy01_init, S_yoy01_wait)
    S_yoy01_wait.add(T_all_sleep, S_yoy01_meet)
    S_yoy01_meet.add(T_yoy01_meet, S_yoy01_hold)
    S_yoy01_meet.add(T_yoy01_hold, S_yoy01_lewd,
                     actions=('location', {'place': L_dealership_garage},
                              'force', {'flag': True}))
    S_yoy01_hold.add(T_yoy01_hold, S_yoy01_lewd,
                     actions=('location', {'place': L_dealership_garage},
                              'force', {'flag': True}))
    S_yoy01_lewd.add(T_yoy01_lewd, S_yoy01_done,
                     actions=('unforce', None))


init python:
    M_yoyo.add(
        S_yoy00_hook,
        S_yoy01_init, S_yoy01_wait, S_yoy01_meet, S_yoy01_hold,
            S_yoy01_lewd, S_yoy01_done)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

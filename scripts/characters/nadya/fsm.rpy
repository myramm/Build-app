init -1 python:
    M_nadya = Machine(
        'nadya',
        default_loc=[[L_NULL] * 4],
        vars={},
        pregnancy_chance=0.2,
        can_birth_twins=False,
        default_pregnancy_schedule={
            '':                LocationSchedule([[L_warehouse_depot, L_warehouse_depot, L_warehouse_office, L_NULL]]),
            '_pregnant_bump':  LocationSchedule([[L_warehouse_depot, L_warehouse_depot, L_warehouse_office, L_NULL]]),
            '_pregnant_belly': LocationSchedule([[L_warehouse_depot, L_warehouse_depot, L_warehouse_office, L_NULL]]),
            '_baby_girl':      LocationSchedule([[L_warehouse_depot, L_warehouse_depot, L_warehouse_office, L_NULL]]),
            '_baby_boy':       LocationSchedule([[L_warehouse_depot, L_warehouse_depot, L_warehouse_office, L_NULL]])})


init -3 python:
    T_nad01_init = Trigger()
    T_nad01_thug = Trigger()
    T_nad01_meet = Trigger()
    T_nad01_find = Trigger()
    T_nad01_lewd = Trigger()


init python:
    S_nad00_init = State()
    S_nad00_done = State(delay=6)


    S_nad01_init = State()
    S_nad01_thug = State(_("Deb is in trouble! I need to get downstairs now!"))
    S_nad01_meet = State(_("Nadya has invited me to visit her at the warehouse. I wonder what she wants?"))
    S_nad01_find = State(_("This place has certainly changed... Jab said I'll find Nadya in the office upstairs."))
    S_nad01_lewd = State(_("Gulp! I guess it would be rude to just leave. I should speak to Nadya."))
    S_nad01_done = State()


init python:
    S_nad00_init.add(T_ano28_init, S_nad00_done)
    S_nad00_done.add(T_all_sleep, S_nad01_init,
                     actions=('setdefaultloc', [[L_warehouse_office] * 4]))

    S_nad01_init.add(T_nad01_init, S_nad01_thug,
                     actions=('exec', 'game.lock_sleep()'))
    S_nad01_thug.add(T_nad01_thug, S_nad01_meet,
                     actions=('exec', 'game.unlock_sleep()',
                              'priority', 1))
    S_nad01_meet.add(T_nad01_meet, S_nad01_find)
    S_nad01_find.add(T_nad01_find, S_nad01_lewd)
    S_nad01_lewd.add(T_nad01_lewd, S_nad01_done,
                     actions=('setdefaultloc', [[L_warehouse_depot,
                                                 L_warehouse_depot,
                                                 L_warehouse_office,
                                                 L_NULL]]))


init python:
    M_nadya.add(
        S_nad00_init, S_nad00_done,
        S_nad01_init, S_nad01_thug, S_nad01_meet, S_nad01_find,
            S_nad01_lewd, S_nad01_done)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

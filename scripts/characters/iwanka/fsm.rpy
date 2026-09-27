init -1 python:
    M_iwanka = Machine(
        'iwanka',
        default_loc=[[L_rump_second] * 4],
        pregnancy_chance=.15,
        can_birth_twins=False,
        vars={'number_known': False,
              'sex speed': .3},
        default_pregnancy_schedule={
            '':                LocationSchedule([[L_rump_second, L_boat_bridge, L_rump_second, L_NULL]]),
            '_pregnant_bump':  LocationSchedule([[L_rump_second, L_boat_bridge, L_rump_second, L_NULL]]),
            '_pregnant_belly': LocationSchedule([[L_rump_second, L_boat_bridge, L_rump_second, L_NULL]]),
            '_baby_girl':      LocationSchedule([[L_rump_second] * 4]),
            "_baby_boy":       LocationSchedule([[L_rump_second] * 4])})

    for case in ('first', 'repeat'):
        M_iwanka.pregnancy.add_action(case, 1, ('setdefaultoutfit', [['dressed', 'naked', 'naked', 'naked']]))
        M_iwanka.pregnancy.add_action(case, 5, ('setdefaultoutfit', 'dressed'))
        M_iwanka.pregnancy.add_action(case, 7, ('setdefaultoutfit', [['naked', 'naked', 'swimsuit', 'naked']]))


init -3 python:
    T_iwa00_init = Trigger()

    T_iwa01_init = Trigger()
    T_iwa01_find = Trigger()
    T_iwa01_give = Trigger()
    T_iwa01_wait = Trigger()
    T_iwa01_exit = Trigger()
    T_iwa01_pier = Trigger()

    T_iwa02_init = Trigger()


init python:
    S_iwa00_init = State()
    S_iwa00_done = State()


    S_iwa01_init = State(_("Iwanka knows the code to her dad's office. Maybe I can get her to tell me somehow."))
    S_iwa01_find = State(_("Hopefully, if I help her, I can get the code. Now I just need to find a disguise..."))
    S_iwa01_give = State(_("The guards won't think twice about a maid leaving, this'll be perfect. I should give it to Iwanka."))
    S_iwa01_wait = State(_("Just got to wait for dusk and then I can grab Iwanka and we can make a break for it!"))
    S_iwa01_exit = State(_("We're all set, just need to leave the estate without raising suspicion; cool and calm."))
    S_iwa01_pier = State(_("A boat?! God help me. I guess we're going to the pier."))
    S_iwa01_done = State()


    S_iwa02_init = State(_('I wonder how Iwanka\'s dealing with her father\'s arrest. Maybe I should swing by the estate.'))
    S_iwa02_done = State()


init python:
    S_iwa00_init.add(T_iwa00_init, S_iwa00_done)
    S_iwa00_done.add(T_all_sleep, S_iwa01_init,
                     actions=('priority', 1.9))

    S_iwa01_init.add(T_iwa01_init, S_iwa01_find)
    S_iwa01_find.add(T_iwa01_find, S_iwa01_give)
    S_iwa01_give.add(T_iwa01_give, S_iwa01_wait)
    S_iwa01_wait.add(T_iwa01_wait, S_iwa01_exit,
                     actions=('location', {'place': L_NULL},
                              'force', {'flag': True}))
    S_iwa01_exit.add(T_iwa01_exit, S_iwa01_pier)
    S_iwa01_pier.add(T_iwa01_pier, S_iwa01_done,
                     actions=('priority', 0,
                              'unforce', None,
                              'setdefaultloc', (
                                'iwanka', [[L_rump_second, L_rump_second, L_boat_bridge, L_NULL]]),
                              'setdefaultoutfit', (
                                'iwanka', [['dressed', 'dressed', 'swimsuit', 'dressed']])))

    S_iwa01_done.add(T_ano20_cops, S_iwa02_init,
                     actions=('priority', 1.9,
                              'location', {'place': L_rump_second},
                              'force', {'flag': True}))

    S_iwa02_init.add(T_iwa02_init, S_iwa02_done,
                     actions=('unforce', None))



init python:
    M_iwanka.add(
        S_iwa00_init, S_iwa00_done,
        S_iwa01_init, S_iwa01_find, S_iwa01_give, S_iwa01_wait, S_iwa01_exit,
            S_iwa01_pier, S_iwa01_done,
        S_iwa02_init, S_iwa02_done)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

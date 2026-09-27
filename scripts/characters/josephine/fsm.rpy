init -1 python:
    M_josie = Machine(
        'josie',
        default_loc=[[L_dealership_showroom,
                      L_dealership_lounge,
                      L_dealership_showroom,
                      L_NULL]],
        vars={'jos01_call': False,
              'jos01_kim': False,
              'jos01_sato': False,
              'peeked': False,
              'sex': False,
              'sex speed': .4,
              'scene speed': "slow"},
        pregnancy_chance=0.25,
        can_birth_twins=False)


init -3 python:
    T_jos01_init = Trigger()
    T_jos01_spot = Trigger()
    T_jos01_find = Trigger()

    T_jos02_init = Trigger()


init python:
    S_jos00_init = State()
    S_jos00_done = State()


    S_jos01_init = State(_("I wonder how Josie's doing. I should probably drop by for a visit."))
    S_jos01_spot = State(_("Oooh, I wonder what's going on, and where's Josie? Perhaps I can make out what they're saying."))
    S_jos01_find = State(_("Josie must be here somewhere, there's no way she's managed to get fired yet."))
    S_jos01_done = State(_("Well that was super awkward..."))


    S_jos02_init = State(_("I wonder if Josie finally got fired... I'm tempted to go find out."))
    S_jos02_done = State()


init python:
    S_jos00_init.add(T_ano10_tina, S_jos00_done)
    S_jos00_done.add(T_all_sleep, S_jos01_init,
                     actions=('priority', 2))

    S_jos01_init.add(T_jos01_init, S_jos01_spot,
                     actions=('location', ('jiang', {'place': L_dealership_garage}),
                              'location', ('josie', {'place': L_dealership_office}),
                              'location', ('sato', {'place': L_dealership_showroom}),
                              'force', ('jiang', {'flag': True}),
                              'force', ('josie', {'flag': True}),
                              'force', ('sato', {'flag': True}),
                              'condition', ('M_kim.state is None', (
                                  'location', ('kim', {'place': L_dealership_showroom}),
                                  'force', ('kim', {'flag': True})), (
                                  'location', ('yoyo', {'place': L_dealership_showroom}),
                                  'force', ('yoyo', {'flag': True}))),
                              'condition', ('M_rump.state is None', (
                                  'location', ('rump', {'place': L_dealership_showroom}),
                                  'force', ('rump', {'flag': True})))))
    S_jos01_spot.add(T_jos01_spot, S_jos01_find,
                     actions=('location', ('sato', {'place': L_dealership_showroom}),
                              'condition', ('M_kim.state is None', (
                                  'location', ('kim', {'place': L_dealership_garage})), (
                                  'location', ('yoyo', {'place': L_dealership_lounge}))),
                              'condition', ('M_rump.state is None', (
                                  'location', ('rump', {'place': L_dealership_garage})))))
    S_jos01_find.add(T_jos01_find, S_jos01_done,
                     actions=('unforce', 'jiang',
                              'unforce', 'josie',
                              'unforce', 'sato',
                              'condition', ('M_kim.state is None', (
                                  'unforce', 'kim'), (
                                  'unforce', 'yoyo')),
                              'condition', ('M_rump.state is None', (
                                  'unforce', 'rump'))))
    S_jos01_done.add(T_all_sleep, S_jos02_init,
                     actions=('location', ('josie', {'place': L_dealership_showroom}),
                              'force', ('josie', {'flag': True})))

    S_jos02_init.add(T_jos02_init, S_jos02_done,
                     actions=('unforce', 'josie'))


init python:
    M_josie.add(
        S_jos00_init, S_jos00_done,
        S_jos01_init, S_jos01_spot, S_jos01_find, S_jos01_done,
        S_jos02_init, S_jos02_done)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

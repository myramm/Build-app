init -1 python:
    M_tina = Machine(
        'tina',
        default_loc=[[L_bank_cubicle, L_bank_cubicle, L_tina_lounge, L_NULL]] +
                    [[L_NULL,         L_bank_cubicle, L_tina_lounge, L_NULL]] +
                3 * [[L_bank_cubicle, L_bank_cubicle, L_tina_lounge, L_NULL]] +
                2 * [[L_NULL,         L_NULL,         L_tina_lounge, L_NULL]],
        vars={'becca_crush': False,
              'fertile': False,
              'sexfriend': False,
              'sex': -1,
              'sex speed': .4},
        pregnancy_chance=.02,
        can_birth_twins=True,
        default_pregnancy_schedule={
            '':                LocationSchedule([[L_bank_cubicle, L_bank_cubicle, L_tina_lounge, L_NULL],
                                                 [L_tina_lounge] * 4]),
            '_pregnant_bump':  LocationSchedule([[L_bank_cubicle, L_bank_cubicle, L_tina_lounge, L_NULL],
                                                 [L_tina_lounge] * 4]),
            '_pregnant_belly': LocationSchedule([[L_bank_cubicle, L_bank_cubicle, L_tina_lounge, L_NULL],
                                                 [L_tina_lounge] * 4]),
            '_baby_twins':     LocationSchedule([[L_tina_lounge] * 4]),
            '_baby_boy':       LocationSchedule([[L_tina_lounge] * 4]),
            '_baby_girl':      LocationSchedule([[L_tina_lounge] * 4])})


    for case in ('first', 'repeat'):
        M_tina.pregnancy.add_action(case, 3, ('setdefaultoutfit', [['dressed', 'dressed', 'naked', 'naked'],
                                                                   ['naked'] * 4]))
        M_tina.pregnancy.add_action(case, 5, ('setdefaultoutfit', 'casual'))
        M_tina.pregnancy.add_action(case, 7, ('setdefaultoutfit', [['dressed', 'dressed', 'casual', 'casual'],
                                                                   ['casual'] * 4]))

    M_tina.outfit.set_default_outfit_schedule(
        [['dressed', 'dressed', 'casual', 'casual'], ['casual'] * 4])


init -3 python:
    T_tin01_init = Trigger()

    T_tin02_init = Trigger()
    T_tin02_talk = Trigger()


init python:
    S_tin00_init = State()
    S_tin00_done = State()


    S_tin01_init = State(_("I should visit Tina again, last time was really fun!"))
    S_tin01_done = State(_("We'll have to try and keep this low-key. I guess I'll see her at work."))


    S_tin02_init = State(_("Tina works at the bank during the week, I should try and speak to her there."))
    S_tin02_talk = State(_("Liu said Tina has her own cubicle in the office, I should head back there."))
    S_tin02_done = State()


init python:
    S_tin00_init.add(T_ano10_tina, S_tin00_done)
    S_tin00_done.add(T_all_sleep, S_tin01_init,
                     actions=('priority', 1))

    S_tin01_init.add(T_tin01_init, S_tin01_done)
    S_tin01_done.add(T_all_sleep, S_tin02_init,
                     actions=('setdefaultloc', [[L_bank_cubicle, L_bank_cubicle, L_tina_lounge, L_NULL]] * 1 +
                                               [[L_NULL,         L_bank_cubicle, L_tina_lounge, L_NULL]] * 1 +
                                               [[L_bank_cubicle, L_bank_cubicle, L_tina_lounge, L_NULL]] * 3 +
                                               [[L_NULL, L_NULL, L_tina_lounge, L_NULL], [L_tina_lounge] * 4]))

    S_tin02_init.add(T_tin02_init, S_tin02_talk,
                     actions=('unlocklocation', L_bank_hallway))
    S_tin02_talk.add(T_tin02_talk, S_tin02_done,
                     actions=('setdefaultloc', [[L_bank_lobby,   L_bank_cubicle, L_tina_lounge, L_NULL]] * 1 +
                                               [[L_NULL,         L_bank_cubicle, L_tina_lounge, L_NULL]] * 1 +
                                               [[L_bank_lobby,   L_bank_cubicle, L_tina_lounge, L_NULL]] * 3 +
                                               [[L_NULL, L_NULL, L_tina_lounge, L_NULL], [L_tina_lounge] * 4]))


init python:
    M_tina.add(
        S_tin00_init, S_tin00_done,
        S_tin01_init, S_tin01_done,
        S_tin02_init, S_tin02_talk, S_tin02_done)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

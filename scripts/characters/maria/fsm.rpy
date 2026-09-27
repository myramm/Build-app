init -1 python:
    M_maria = Machine(
        'maria',
        default_loc=[[L_pizzeria_kitchen, L_pizzeria_kitchen, L_pizzeria_storage, L_NULL]] * 5 +
                    [[L_pizzeria_kitchen, L_pizzeria_kitchen, L_maria_lounge,     L_NULL],
                     [L_church,           L_maria_lounge,     L_maria_lounge,     L_NULL]],
        vars={'met': False,
              'overlay sauce': False,
              'sex': False,
              'sex speed': .3},
        pregnancy_chance=0.35,
        default_pregnancy_schedule={
            '':                LocationSchedule([[L_pizzeria_kitchen] * 2 + [L_maria_lounge] * 2] * 6 + [[L_church, L_maria_lounge, L_maria_lounge, L_NULL]]),
            '_pregnant_bump':  LocationSchedule([[L_pizzeria_kitchen] * 2 + [L_maria_lounge] * 2] * 6 + [[L_church, L_maria_lounge, L_maria_lounge, L_NULL]]),
            '_pregnant_belly': LocationSchedule([[L_pizzeria_kitchen] * 2 + [L_maria_lounge] * 2] * 6 + [[L_church, L_maria_lounge, L_maria_lounge, L_NULL]]),
            '_baby_twins':     LocationSchedule([[L_pizzeria_kitchen] * 2 + [L_maria_lounge] * 2] * 6 + [[L_church, L_maria_lounge, L_maria_lounge, L_NULL]]),
            '_baby_boy':       LocationSchedule([[L_pizzeria_kitchen] * 2 + [L_maria_lounge] * 2] * 6 + [[L_church, L_maria_lounge, L_maria_lounge, L_NULL]]),
            '_baby_girl':      LocationSchedule([[L_pizzeria_kitchen] * 2 + [L_maria_lounge] * 2] * 6 + [[L_church, L_maria_lounge, L_maria_lounge, L_NULL]])})

    for case in ('first', 'repeat'):
        M_maria.pregnancy.add_action(case, 3, ('setdefaultoutfit', [['apron', 'apron', 'casual', 'casual']] * 6 +
                                                                   [['casual', 'casual', 'casual', 'casual']]))
        M_maria.pregnancy.add_action(case, 5, ('setdefaultoutfit', [['dressed', 'dressed', 'casual', 'casual']] * 6 +
                                                                   [['casual', 'casual', 'casual', 'casual']]))

    M_maria.pregnancy.add_action('first', 1, ('trigger', T_ano11_done))

    M_maria.outfit.set_default_outfit_schedule(
        [['dressed', 'dressed', 'casual', 'casual']] * 6 +
        [['casual', 'casual', 'casual', 'casual']])


init -3 python:
    T_mar01_init = Trigger()
    T_mar01_help = Trigger()
    T_mar01_tour = Trigger()


init python:
    S_mar00_hook = State()


    S_mar01_init = State()
    S_mar01_help = State(_("Maria's apartment is 302. Shouldn't take long to carry up these bags."))
    S_mar01_tour = State(_("It's getting pretty late, I should leave her to enjoy her evening."))
    S_mar01_done = State()


init python:
    S_mar00_hook.add(T_ano25_plan, S_mar01_done,
                     actions=('unlocklocation', L_maria_lounge)) 

    S_mar00_hook.add(T_tin01_init, S_mar01_init,
                     actions=('location', {'place': L_apt_lobby},
                              'force', {'flag': True}))

    S_mar01_init.add(T_all_tick, S_mar00_hook,
                     actions=('unforce', None)) 
    S_mar01_init.add(T_mar01_init, S_mar01_help,
                     actions=('priority', 3,
                              'location', {'place': L_maria_lounge},
                              'unlocklocation', L_maria_lounge))
    S_mar01_help.add(T_mar01_help, S_mar01_tour)
    S_mar01_tour.add(T_mar01_tour, S_mar01_done,
                     actions=('unforce', None))


init python:
    M_maria.add(
        S_mar00_hook,
        S_mar01_init, S_mar01_help, S_mar01_tour, S_mar01_done)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

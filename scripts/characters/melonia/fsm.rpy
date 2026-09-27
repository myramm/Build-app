init -1 python:
    M_melonia = Machine(
        'melonia',
        default_loc=[[L_rump_back, L_rump_back, L_rump_master, L_NULL]],
        pregnancy_chance=.07,
        can_birth_twins=False,
        vars={'abort_wait': 3,
              'scare': False,
              'sex speed': .3})

    for case in ('first', 'repeat'):
        M_melonia.pregnancy.add_action(case, 1, (
            'setdefaultoutfit', [['dressed', 'swimsuit', 'naked', 'naked']]))
        M_melonia.pregnancy.add_action(case, 5, (
            'setdefaultoutfit', 'naked',
            'set', ('thotbot', '_shadow', 'melonia')))
        M_melonia.pregnancy.add_action(case, 7, (
            'clear', ('thotbot', '_shadow')))


init -3 python:
    T_mel00_init = Trigger()

    T_mel01_init = Trigger()
    T_mel01_hint = Trigger()
    T_mel01_find = Trigger()
    T_mel01_help = Trigger()

    T_mel02_init = Trigger()

    T_mel03_init = Trigger()

    T_mel04_init = Trigger()

    T_mel05_init = Trigger()


init python:
    S_mel00_init = State()
    S_mel00_done = State()


    S_mel01_init = State(_("Better keep Melonia thinking I'm the pool boy. I should speak to her about it."))
    S_mel01_hint = State(_("I have no idea what I'm doing! I hope Ricky can help!"))
    S_mel01_find = State(_("A leaf skimmer, Ricky said it was around here somewhere..."))
    S_mel01_help = State(_("This just looks like a giant flyswatter... I better ask Ricky to show me the ropes."))
    S_mel01_more = State(_("Pool, or rather, hot tub cleaned. That's enough stomach-churning work for today."))
    S_mel01_done = State(_("I better keep cleaning the mayor's hot tub occasionally so no one gets suspicious."))


    S_mel02_init = State(_("The morning would be the best time to clean the hot tub, while no one is using it."))
    S_mel02_done = State(_("This charade had better be worth it. First filthy hot tubs, and now this \"uniform\"..."))


    S_mel03_init = State(_("As much as I hate to think about the state of that hot tub, I should probably clean it again."))
    S_mel03_done = State(_("Aaaand now I dance for money. This is not at all how I saw this going..."))


    S_mel04_init = State(_("That filthy hot tub is going to need my attention again, better get there early."))
    S_mel04_done = State(_("Maybe with her getting so... Comfortable, I can ask her for help next time..."))


    S_mel05_init = State(_("The hot tub awaits. It's no time machine but there's definitely something special about it..."))
    S_mel05_done = State()


init python:
    S_mel00_init.add(T_mel00_init, S_mel00_done)
    S_mel00_done.add(T_all_sleep, S_mel01_init,
                     actions=('priority', 1.9,
                              'location', ('ricky', {'place': L_rump_back}),
                              'force', ('ricky', {'tod': 0})))

    S_mel01_init.add(T_mel01_init, S_mel01_hint,
                     actions=('location', {'place': L_NULL},
                              'force', {'flag': True}))
    S_mel01_hint.add(T_mel01_hint, S_mel01_find)
    S_mel01_find.add(T_mel01_find, S_mel01_help)
    S_mel01_help.add(T_mel01_help, S_mel01_more,
                     actions=('unforce', None))
    S_mel01_more.add(T_all_tick, S_mel01_done)
    S_mel01_done.add(T_all_sleep, S_mel02_init)

    S_mel02_init.add(T_mel02_init, S_mel02_done)
    S_mel02_done.add(T_all_sleep, S_mel03_init)

    S_mel03_init.add(T_mel03_init, S_mel03_done)
    S_mel03_done.add(T_all_sleep, S_mel04_init)

    S_mel04_init.add(T_mel04_init, S_mel04_done)
    S_mel04_done.add(T_all_sleep, S_mel05_init)

    S_mel05_init.add(T_mel05_init, S_mel05_done,
                     actions=('unforce', 'ricky'))


init python:
    M_melonia.add(
        S_mel00_init, S_mel00_done,
        S_mel01_init, S_mel01_hint, S_mel01_find, S_mel01_help,
            S_mel01_more, S_mel01_done,
        S_mel02_init, S_mel02_done,
        S_mel03_init, S_mel03_done,
        S_mel04_init, S_mel04_done,
        S_mel05_init, S_mel05_done)

    M_melonia.outfit.set_default_outfit_schedule(
        [['swimsuit', 'swimsuit', 'dressed', 'dressed']])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

init -1 python:
    M_becca = Machine(
        'becca',
        default_loc=[[L_basketball_court, L_basketball_court,
                      L_tina_bed2, L_tina_bed2],
                     [L_basketball_court, L_basketball_court,
                      L_beach_water, L_tina_bed2]],
        vars={'sex speed': .3,
              'becca beach sex': 0,
              'taken_dick': False})


init -3 python:
    T_becca_beach_sex = Trigger()

    T_bec00_solo = Trigger()

    T_bec01_init = Trigger()
    T_bec01_talk = Trigger()
    T_bec01_done = Trigger()


init python:
    S_bec00_init = State()
    S_bec00_req1 = State()
    S_bec00_req2 = State()
    S_bec00_done = State()


    S_bec01_init = State("I wonder what Becca does at home? Maybe I'll visit her some time.")
    S_bec01_talk = State("Tina says Becca spends a lot of time in her room, do I dare poke my head in?")
    S_bec01_done = State()


init python:
    S_bec00_init.add(T_ano10_tina, S_bec00_req1)
    S_bec00_init.add(T_bec00_solo, S_bec00_req2)
    S_bec00_req1.add(T_bec00_solo, S_bec00_done)
    S_bec00_req2.add(T_ano10_tina, S_bec00_done)
    S_bec00_done.add(T_all_sleep, S_bec01_init,
                     actions=('priority', 1))

    S_bec01_init.add(T_bec01_init, S_bec01_talk)
    S_bec01_talk.add(T_bec01_talk, S_bec01_done)


init python:
    M_becca.add(
        S_bec00_init, S_bec00_req1, S_bec00_req2, S_bec00_done,
        S_bec01_init, S_bec01_talk, S_bec01_done)

    M_becca.add_action(T_becca_beach_sex, ('inc', 'becca beach sex'))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

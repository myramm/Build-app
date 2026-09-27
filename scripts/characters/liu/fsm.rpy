init -1 python:
    M_liu = Machine(
        'liu',
        default_loc=[[L_bank_lobby, L_bank_lobby, L_liu_lounge, L_NULL]] * 6 +
                    [[L_liu_bedroom, L_liu_lounge, L_liu_lounge, L_NULL]],
        vars={'abort_wait': 1},
        pregnancy_chance=0.15,
        can_birth_twins=False,
        default_pregnancy_schedule={
            '_announce':       LocationSchedule(L_liu_lounge),
            '':                LocationSchedule([[L_bank_lobby, L_bank_lobby, L_liu_lounge, L_NULL]] * 6 + [[L_liu_lounge] * 4]),
            '_pregnant_bump':  LocationSchedule([[L_bank_lobby, L_bank_lobby, L_liu_lounge, L_NULL]] * 6 + [[L_liu_lounge] * 4]),
            '_pregnant_belly': LocationSchedule([[L_bank_lobby, L_bank_lobby, L_liu_lounge, L_NULL]] * 6 + [[L_liu_lounge] * 4]),
            '_baby_girl':      LocationSchedule(L_liu_lounge),
            '_baby_boy':       LocationSchedule(L_liu_lounge)})


init -3 python:
    T_liu01_init = Trigger()


init python:

    S_liu01_init = State()
    S_liu01_done = State()


init python:
    S_liu01_init.add(T_liu01_init, S_liu01_done)


init python:
    M_liu.add(S_liu01_init, S_liu01_done)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

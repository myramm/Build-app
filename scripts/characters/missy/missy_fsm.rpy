init -1 python:
    M_missy = Machine(
        'missy',
        default_loc = [[L_basketball_court, L_basketball_court, L_NULL, L_NULL]],
        vars={'sex speed': .3,
              'missy beach sex': 0,
              'taken_dick': False})


init -3 python:

    T_missy_beach_sex = Trigger()

init python:
    M_missy.add_action(T_missy_beach_sex, ["inc", "missy beach sex",])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

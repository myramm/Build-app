init -1 python:
    M_tony = Machine(
        'tony',
        default_loc=[[L_pizzeria_interior, L_pizzeria_interior, L_pizzeria_kitchen, L_NULL]] * 6 +
                    [[L_church, L_maria_lounge, L_maria_lounge, L_NULL]],
        vars={'cooldown': 0,
              'knows': False,
              'watches': None})
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

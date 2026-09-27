init -1 python:
    M_harold = Machine(
        'harold',
        default_loc=[[L_police_office, L_police_office,
                      L_miahouse_entrance, L_miahouse_entrance],
                     [L_church, L_police_office,
                      L_miahouse_entrance, L_miahouse_entrance]],
        vars={'sex speed': .3,
              'topping': renpy.random.choice(['chocolate chips',
                                              'sprinkles',
                                              'vanilla drizzle',
                                              'maple drizzle']),
              'glaze': renpy.random.choice(['chocolate glazed',
                                            'strawberry glazed',
                                            'blueberry glazed',
                                            'vanilla glazed']),
              'lightfingered': None})

init -3 python:

    T_harold_donuts = Trigger()
    T_harold_leaves = Trigger()
    T_harold_missing = Trigger()
    T_harold_photo_clue = Trigger()
    T_harold_found = Trigger()
    T_harold_glasses = Trigger()
    T_harold_grows_a_pair = Trigger()
    T_harold_backup = Trigger()
    T_harold_find_goods = Trigger()
    T_harold_found_goods = Trigger()
    T_harold_promotion = Trigger()
    T_harold_indecisiveness = Trigger()
    T_harold_new_girl = Trigger()

init python:

    S_harold_start = State()
    S_harold_end = State()


    S_harold_start.add(T_harold_donuts, S_harold_end)

    M_harold.add(S_harold_start, S_harold_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

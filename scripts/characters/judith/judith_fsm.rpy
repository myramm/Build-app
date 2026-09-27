init -1 python:
    M_judith = Machine("Judith", default_loc = [[L_school_lefthallway, L_school_lefthallway, L_NULL, L_NULL],
                                                [L_NULL, L_NULL, L_NULL, L_NULL]
                                                ],
                       vars = {
                               "sex speed": .3,
                               "can go in bathroom": False,
                               "in bathroom": False,
                               "sex sequence locked": True,
                       },
    )

init -3 python:
    T_judith_intro = Trigger()
    T_judith_changed = Trigger()
    T_judith_latina_bashed = Trigger()
    T_judith_comfort_her = Trigger()
    T_judith_end = Trigger()

init python:

    S_judith_start = State()
    S_judith_latina_bashing_delay = State()
    S_judith_latina_bashing = State()
    S_judith_in_girls_bathroom = State()
    S_judith_end = State()


    S_judith_start.add(T_judith_changed, S_judith_latina_bashing_delay)
    S_judith_latina_bashing_delay.add(T_all_sleep, S_judith_latina_bashing)
    S_judith_latina_bashing.add(T_judith_latina_bashed, S_judith_in_girls_bathroom,
                                actions = ["set", "in bathroom",
                                           "location", {"place": L_school_stall},
                                           "force", {"tod": [0,1]},
                                           "unlocklocation", L_school_girlsroom,
                                           ],
                                )
    S_judith_in_girls_bathroom.add(T_judith_comfort_her, S_judith_end,
                                   actions = ["set", "can go in bathroom",
                                              "unforce", None,
                                              ]
                                   )


    M_judith.add(S_judith_start, S_judith_latina_bashing_delay, S_judith_latina_bashing,
                 S_judith_in_girls_bathroom, S_judith_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

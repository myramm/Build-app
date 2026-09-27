init -1 python:
    M_bridget = Machine("bridget", default_loc = [[L_school_track, L_school_bridgetoffice, L_NULL, L_NULL],
                                                  [L_NULL, L_NULL, L_NULL, L_NULL]
                                                  ],
                        )

init -3 python:

    T_bridget_workout = Trigger()

init python:

    S_bridget_start = State()
    S_bridget_intro = State(_("MC informs Coach Bridget of his return."))
    S_bridget_end = State()


    S_bridget_start.add(T_mc_lockerroom_change, S_bridget_intro,
                        actions = ["location", ["judith", {"place": L_NULL}],
                                   "force", ["judith", {"tod": [0,1]}],
                                   ],
                        )
    S_bridget_intro.add(T_bridget_workout, S_bridget_end,
                        actions = ["unlocklocation", L_gym_front,
                                   "unlocklocation", L_pool,
                                   "unforce", "judith",
                                   ],
                        )

    M_bridget.add(S_bridget_start, S_bridget_intro, S_bridget_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

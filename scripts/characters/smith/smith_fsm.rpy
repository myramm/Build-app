init -1 python:
    M_smith = Machine("smith", default_loc = [[L_school_smithoffice, L_school_teacherslounge, L_school_smithoffice, L_NULL],
                                              [L_NULL, L_NULL, L_NULL, L_NULL]
                                              ],
                      vars = {"sex speed": .3,
                              "annie trouble": False,
                              "school intro done": False,
                              },
    )

init -3 python:
    T_smith_intro = Trigger()
    T_smith_go_to_locker = Trigger()
    T_smith_unlocked_locker = Trigger()
    T_smith_go_to_athletics = Trigger()
    T_smith_end = Trigger()

init python:

    S_smith_start = State()
    S_smith_intro = State()
    S_smith_go_to_locker = State()
    S_smith_unlocked_locker = State()
    S_smith_go_to_athletics = State()
    S_smith_end = State()


    S_smith_start.add(T_smith_intro, S_smith_intro,
                      actions = ["unlocklocation", L_basketball_court,
                                 "location", ["annie", {"place": L_school_smithoffice}],
                                 "force", ["annie", {"flag": True}],
                                 ],
                      )
    S_smith_intro.add(T_smith_go_to_locker, S_smith_go_to_locker)
    S_smith_go_to_locker.add(T_smith_unlocked_locker, S_smith_unlocked_locker,
                             actions = ["unforce", "annie",],
                             )
    S_smith_unlocked_locker.add(T_smith_go_to_athletics, S_smith_go_to_athletics)
    S_smith_go_to_athletics.add(T_mc_lockerroom_change, S_smith_end,
                                actions = ["set", "school intro done", "exec", "game.unlock_sleep()"],
                                )

    M_smith.add(S_smith_start, S_smith_intro, S_smith_go_to_locker,
                S_smith_unlocked_locker, S_smith_go_to_athletics,
                S_smith_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

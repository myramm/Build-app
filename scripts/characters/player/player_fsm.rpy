init -1 python:
    M_player = Machine("player", default_loc=[[L_NULL, L_NULL, L_NULL, L_NULL]],
                       vars = {"just wokeup": True,
                               "sex speed": .4,
                               "jerk eve": False,
                               "jerk mia": False,
                               "jerk roxxy": False,
                               "jerk mom": False,
                               "jerk diane": False,
                               "jerk jenny": False,
                               "telescope active": True,
                               "telescope selection": None,
                               "found cat": False,
                               "pet cat": False,
                               "first swim": True,
                               "library subscription": False,
                               "wearing swimsuit": False,
                               "pc_fixed": False,
                               "library subscription": False,
                               "drank milk": False,
                               "masturbated tv": False,
                               "mc beach sex": 0,
                               "beach bottle spins": 0,
                               "left of 4some": None,
                               "took pregnax":False,
                               "on_jenny_pc":False,
                               "peep_hole_first": True,
                               "baby_gender":"boy",
                               "pc_know_anon_passwd":False,
                               "pc_know_jenny_passwd":False,
                               "bait": "",
                               "is_virgin": True,
                               "mugged": 0,
                               "deliveries": 0,
                               "ano05_continue": False,
                               "ano07_continue": False,
                              },
    )

init -3 python:

    T_mc_homework = Trigger()
    T_mc_nun_thoughts = Trigger()
    T_mc_mowed_lawn = Trigger()
    T_mc_lockerroom_change = Trigger()
    T_mc_beach_sex = Trigger()

init python:

    S_player_start = State()
    S_player_end = State()


    S_player_start.add(T_all_sleep, S_player_end)

    M_player.add_action(T_all_sleep, ["clear", "took pregnax"])

    M_player.add(S_player_start, S_player_end)
    M_player.add_action(T_mc_beach_sex, ["inc", "mc beach sex",])
    M_player.add_action(T_all_sleep, ["clear", "masturbated tv",
                                      "set", "just wokeup",
                                      ]
                        )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

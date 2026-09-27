init -1 python:
    M_helen = Machine("helen", default_loc = [[L_miahouse_entrance, L_miahouse_helensbedroom, L_miahouse_entrance, L_miahouse_helensbedroom],
                                              [L_church, L_miahouse_helensbedroom, L_miahouse_entrance, L_miahouse_helensbedroom],
                                              ],
                      vars = {"helen route": False,
                              "sex speed": .175,
                              "corset lingerie": False,
                              },
    )

init -3 python:

    T_helen_confessional = Trigger()
    T_helen_convince_fail = Trigger()
    T_helen_convince_change = Trigger()
    T_helen_secret_sacrement = Trigger()
    T_helen_angelica_ritual = Trigger()
    T_helen_caught_masturbating = Trigger()
    T_helen_sexy_lingerie = Trigger()
    T_helen_torture = Trigger()
    T_helen_thanks = Trigger()
    T_helen_master_servant = Trigger()
    T_helen_route = Trigger()
    T_helen_master_servant_sex = Trigger()

init python:

    S_helen_start = State(_("The default state for Helen to start in"))
    S_helen_route_split = State(_("Yikes! That was so kinky. I wonder how Mia and her father feel about this."))
    S_helen_harold_moved_on = State(_("Well Harold seems OK, but I wonder how Mia is doing..."))
    S_helen_mia_breakdown = State(_("Oh no! Mia is devastated. I hope Harold's doing better..."))
    S_helen_master_servant_fun = State(_("Helen suggested I should visit her bedroom in the afternoon."))
    S_helen_aftersex_mia_suspicious = State(_("Uh oh! Mia is suspicious about me visiting her mom's room during the day!"))
    S_helen_end = State(_("The end of Helen's route"))


    S_helen_start.add(T_helen_route, S_helen_route_split,
                      actions=('priority', 1,
                               'clear', ('player', 'is_virgin')))
    S_helen_route_split.add(T_harold_new_girl, S_helen_harold_moved_on)
    S_helen_route_split.add(T_helen_master_servant, S_helen_mia_breakdown)
    S_helen_harold_moved_on.add(T_helen_master_servant, S_helen_master_servant_fun)
    S_helen_mia_breakdown.add(T_harold_new_girl, S_helen_master_servant_fun,
                              actions=["location", {"place": L_miahouse_helensbedroom, "tod":[1, 2]},
                                       "force", {'tod': [1, 2]}])
    S_helen_master_servant_fun.add(T_helen_master_servant_sex, S_helen_aftersex_mia_suspicious,
                            actions=["unforce", None])
    S_helen_aftersex_mia_suspicious.add(T_mia_stay_alone, S_helen_end,
                                        actions=["exec", A_repentance.unlock])

    M_helen.add(S_helen_start, S_helen_route_split, S_helen_mia_breakdown,
                S_helen_harold_moved_on, S_helen_master_servant_fun,
                S_helen_aftersex_mia_suspicious, S_helen_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

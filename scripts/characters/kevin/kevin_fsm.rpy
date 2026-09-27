init -1 python:
    M_kevin = Machine('kevin',
                      default_loc=[[L_school_cafeteria,
                                    L_school_cafeteria,
                                    L_gym,
                                    L_NULL],
                                   [L_gym, L_gym, L_NULL, L_NULL]],
                      default_outfit=[['apron', 'apron', 'apron', 'apron'],
                                      ['gym', 'gym', 'apron', 'apron']])

    def kevin_erik_cafeteria_duty():
        erik = M_erik.get_default_locations()
        for day in erik[0:4]:
            day[1] = L_school_cafeteria
        M_erik.set_default_locations(erik)


init -3 python:
    T_kevin_ambush = Trigger()
    T_kevin_request_spot = Trigger()
    T_kevin_eriks_demand = Trigger()
    T_kevin_bought_seadogs = Trigger()
    T_kevin_bribed_erik = Trigger()
    T_kevin_help_found = Trigger()


init python:
    S_kevin_start = State(_("An unavoidable encounter."))
    S_kevin_on_duty = State(_("He mentioned something about being on cafeteria duty?"))
    S_kevin_convince_erik = State(_("Erik isn't usually busy, maybe I get him to help out with cafeteria duty."))
    S_kevin_get_seadogs = State(_("Erik will accept nothing less than {b}Sea Dogs SAGA{/b} from {b}Cosmic Cumics{/b}."))
    S_kevin_bribe_erik = State(_("Erik should agree to help Kevin once I hand over {b}Sea Dogs SAGA{/b}."))
    S_kevin_erik_agreed = State(_("Help found! I should tell Kevin know the good news!"))
    S_kevin_gym_tomorrow = State(_("Kevin will be at the gym in the morning."))
    S_kevin_gym_rat = State(_("He's at the gym pretty regularly. I could train with him."))


    S_kevin_start.add(T_kevin_ambush, S_kevin_on_duty)
    S_kevin_on_duty.add(T_kevin_request_spot, S_kevin_convince_erik)
    S_kevin_convince_erik.add(T_kevin_eriks_demand, S_kevin_get_seadogs,
        actions=('condition', ('player.has_item("game")',
                               (('trigger', T_kevin_bought_seadogs)), ())))
    S_kevin_get_seadogs.add(T_kevin_bought_seadogs, S_kevin_bribe_erik)
    S_kevin_bribe_erik.add(T_kevin_bribed_erik, S_kevin_erik_agreed)
    S_kevin_erik_agreed.add(T_kevin_help_found, S_kevin_gym_tomorrow,
                            actions=('location', {'place': L_NULL},
                                     'force', {'flag': True}))
    S_kevin_gym_tomorrow.add(T_all_sleep, S_kevin_gym_rat,
        actions=('unforce', None,
                 'setdefaultloc', [[L_gym, L_school_cafeteria, L_gym, L_NULL],
                                   [L_gym, L_gym, L_NULL, L_NULL]],
                 'exec', kevin_erik_cafeteria_duty))


    M_kevin.add(S_kevin_start,
                S_kevin_on_duty,
                S_kevin_convince_erik,
                S_kevin_get_seadogs,
                S_kevin_bribe_erik,
                S_kevin_erik_agreed,
                S_kevin_gym_tomorrow,
                S_kevin_gym_rat)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

init -1 python:
    M_keeves = Machine('keeves',
                       default_loc=[[L_NULL, L_NULL, L_NULL, L_NULL],
                                    [L_church, L_NULL, L_NULL, L_NULL]],
                       vars={})


init -3 python:
    T_kee_intro_homily = Trigger()
    T_kee_intro_met = Trigger()


init python:
    S_kee_intro_ready = State(_("A completely avoidable encounter."))
    S_kee_intro_meet = State(_("That was rather a strange homily, I should speak to the Priest."))
    S_kee_intro_food = State(_("{b}Father Keeves{/b} had the munchies, he'll probably be back tomorrow."))
    S_kee_intro_end = State(_("Woah! {b}Father Keeves{/b} is breathtaking!"))


init python:

    S_kee_intro_ready.add(T_kee_intro_homily, S_kee_intro_meet)
    S_kee_intro_meet.add(T_kee_intro_met, S_kee_intro_food,
                         actions=('location', {'place': L_NULL},
                                  'force', {'tod': 0},
                                  'location', ('angelica', {'place': L_NULL}),
                                  'force', ('angelica', {'tod': 0})))
    S_kee_intro_food.add(T_all_sleep, S_kee_intro_end,
                         actions=('unforce', None,
                                  'unforce', 'angelica',
                                  'setdefaultloc', [[L_church, L_church, L_NULL, L_NULL]]))


init python:
    M_keeves.add(
        S_kee_intro_ready, S_kee_intro_meet, S_kee_intro_food, S_kee_intro_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

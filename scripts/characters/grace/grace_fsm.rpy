init -1 python:
    M_grace = Machine("grace", default_loc=[[L_tattooparlor_interior, L_tattooparlor_interior, L_tattooparlor_interior, L_tattooparlor_bedroom]],
                     vars={'sex speed': .3,
                           'sex_1st_time': True,
                           'massage_sex_1st_time': True,
                           'nude_meditation_first': True,
                           },
                     pregnancy_chance=0.1,
                     can_talk=[True, True, True, False],
                     default_pregnancy_schedule={
                        "": LocationSchedule([[L_tattooparlor_interior, L_tattooparlor_interior, L_tattooparlor_apartment, L_tattooparlor_bedroom]]),
                        "_pregnant_bump": LocationSchedule([[L_tattooparlor_interior, L_tattooparlor_interior, L_tattooparlor_apartment, L_tattooparlor_bedroom]]),
                        "_pregnant_belly": LocationSchedule([[L_tattooparlor_apartment, L_tattooparlor_apartment, (L_tattooparlor_apartment,
                                                                                                                 L_tattooparlor_bathroom), L_tattooparlor_bedroom]]),
                        "_baby_twins": LocationSchedule([[L_tattooparlor_interior, L_tattooparlor_interior, L_tattooparlor_apartment, L_tattooparlor_bedroom]]),
                        "_baby_girl": LocationSchedule([[L_tattooparlor_interior, L_tattooparlor_interior, L_tattooparlor_apartment, L_tattooparlor_bedroom]]),
                        "_baby_boy": LocationSchedule([[L_tattooparlor_interior, L_tattooparlor_interior, L_tattooparlor_apartment, L_tattooparlor_bedroom]]),
                       },
    )

init -3 python:
    T_grace_intro = Trigger()

init python:

    S_grace_start = State()
    S_grace_end = State()


    S_grace_start.add(T_grace_intro, S_grace_end)

    M_grace.add(S_grace_start, S_grace_end)
    M_grace.outfit.set_default_outfit_schedule([["dressed", "dressed", "shirt", "dressed"],["dressed", "shirt", "shirt", "dressed"]])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

init -1 python:
    M_micoe = Machine("micoe", default_loc=[[L_hospital_room, L_hospital_room, L_NULL, L_NULL]],
                     vars={'sex speed': .3,
                           },
    )

init -3 python:
    T_micoe_intro = Trigger()

init python:

    S_micoe_start = State()
    S_micoe_end = State()


    S_micoe_start.add(T_micoe_intro, S_micoe_end)

    M_micoe.add(S_micoe_start, S_micoe_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

init -1 python:
    M_ivy = Machine("ivy", default_loc=[[L_pink, L_pink, L_pink, L_NULL]],
                     vars={'sex speed': .8,
                           'first visit': True,
                           },
    )

init -3 python:
    T_ivy_intro = Trigger()

init python:

    S_ivy_start = State()
    S_ivy_end = State()


    S_ivy_start.add(T_ivy_intro, S_ivy_end)

    M_ivy.add(S_ivy_start, S_ivy_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

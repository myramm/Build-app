init -1 python:
    M_latinas = Machine("latinas", default_loc=[[None, None, None, None]],
                     vars={'sex speed': .3},
    )

init -3 python:
    T_latinas_showers = Trigger()
    T_latinas_annie_trouble = Trigger()

init python:

    S_latinas_start = State()
    S_latinas_caught = State()
    S_latinas_end = State()


    S_latinas_start.add(T_latinas_showers, S_latinas_caught)
    S_latinas_caught.add(T_latinas_annie_trouble, S_latinas_end)

    M_latinas.add(S_latinas_start, S_latinas_caught, S_latinas_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

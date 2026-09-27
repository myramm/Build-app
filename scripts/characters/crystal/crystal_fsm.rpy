init -1 python:
    M_crystal = Machine("crystal", default_loc = [[L_trailer_interior, L_trailer_interior, L_trailer, L_NULL]],
                        vars = {"sex speed": .3,
                                "crystal sex offer": False,
                                "crystal sex offer denied": False,
                                "crystal anal": False,
                                "mood": None,
                                },
    )

init -3 python:
    T_crystal_intro = Trigger()

init python:
    S_crystal_start = State()
    S_crystal_end = State()

    S_crystal_start.add(T_crystal_intro, S_crystal_end)
    M_crystal.add(S_crystal_start, S_crystal_end)

    M_crystal.add_action(T_all_sleep, ('clear', 'mood'))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

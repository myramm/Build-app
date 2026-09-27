init -1 python:
    M_jane = Machine("Jane", default_loc=[[L_library, L_library, L_NULL, L_NULL]],
                    vars={"first book returned": True,
                          "couple_backroom_sex": True})

init -3 python:

    T_jane_library_pass = Trigger()

init python:

    S_jane_start = State()
    S_jane_intro = State()
    S_jane_end = State()


    S_jane_start.add(T_all_school_entrance, S_jane_intro)
    S_jane_intro.add(T_jane_library_pass, S_jane_end)

    M_jane.add(S_jane_start, S_jane_intro, S_jane_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

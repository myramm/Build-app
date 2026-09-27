init -1 python:
    M_dexter = Machine("Dexter", default_loc = [[L_school_track, L_basketball_court, L_NULL, L_NULL],
                                                [L_NULL, L_basketball_court, L_NULL, L_NULL]
                                                ]
                       )

init -3 python:

    T_dex_territory = Trigger()
    T_dex_challenge = Trigger()

init python:

    S_dex_start = State()
    S_dex_flirting = State(_("Dexter is busy flirting on the basket court"))
    S_dex_end = State()


    S_dex_start.add(T_dex_territory, S_dex_flirting)
    S_dex_flirting.add(T_dex_challenge, S_dex_end)

    M_dexter.add(S_dex_start, S_dex_flirting, S_dex_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

init -1 python:
    M_gamsay = Machine('gamsay',
                       default_loc=[[L_rump_kitchen,
                                     L_rump_kitchen,
                                     L_NULL,
                                     L_NULL]],
                       vars={})


init -3 python:
    T_gam_intro_met = Trigger()


init python:
    S_gam_intro_ready = State(_("A completely avoidable encounter."))
    S_gam_intro_end = State(_("I think {b}Chef{/b} might have a bit of a raw nerve..."))


init python:

    S_gam_intro_ready.add(T_gam_intro_met, S_gam_intro_end)


init python:
    M_gamsay.add(
        S_gam_intro_ready, S_gam_intro_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label dealership_dialogue:

    if L_dealership.first_visit:
        call dealership_intro
        $ L_dealership.visited()

    elif M_anon.is_state(S_ano09_brat):
        call ano09_brat_dealership
        $ M_anon.trigger(T_ano09_brat)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

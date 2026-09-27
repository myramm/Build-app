init -1 python:
    M_cassie = Machine("cassie", default_loc=[[L_pool, L_pool, L_pool, L_NULL]],
                     vars={'sex speed': .3,
                           'had sex': False},
    )

init -3 python:
    T_cassie_ban_mc = Trigger()
    T_cassie_lift_ban = Trigger()
    T_cassie_drowning = Trigger()
    T_cassie_end = Trigger()

init python:

    S_cassie_start = State()
    S_cassie_ban_from_pool = State(_("You should go to the pool at night..."))
    S_cassie_caught_skinny_dipping = State(_("Cassie lifted your ban! Go for a swim!"))
    S_cassie_medic_room = State(_("Have fun in the medic room..."))
    S_cassie_end = State()


    S_cassie_start.add(T_cassie_ban_mc, S_cassie_ban_from_pool)
    S_cassie_ban_from_pool.add(T_cassie_lift_ban, S_cassie_caught_skinny_dipping)
    S_cassie_caught_skinny_dipping.add(T_cassie_drowning, S_cassie_medic_room)
    S_cassie_medic_room.add(T_cassie_end, S_cassie_end, actions=["exec", A_drowning_in_pussy.unlock])

    M_cassie.add(S_cassie_start, S_cassie_ban_from_pool,
                 S_cassie_caught_skinny_dipping,
                 S_cassie_medic_room, S_cassie_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

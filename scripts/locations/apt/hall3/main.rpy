label apt_hall3_dialogue:

    if M_anon.is_state(S_ano25_done):
        call ano25_done_apt_hall3
        $ M_anon.trigger(T_ano25_done)

    elif M_maria.is_state(S_mar01_tour):
        call mar01_tour_apt_hall3
        $ M_maria.trigger(T_mar01_tour)
        $ game.timer.tick()

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

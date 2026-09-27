label beach_house_kitchen_dialogue:
    if M_consuela.is_state(S_con03_sing) and L_beachhouse_kitchen.is_here(M_consuela):
        call con03_sing_condo_kitchen
        $ M_consuela.trigger(T_con03_sing)

    elif M_consuela.is_state(S_con03_done) and L_beachhouse_kitchen.is_here(M_consuela):
        call con03_done_condo_kitchen
        python:
            player.go_to(L_beachhouse_bedroom)
            game.timer.tick()
            M_consuela.trigger(T_con03_done)
            persistent.cookie_jar['Consuela']['unlocked'] = True
            persistent.cookie_jar['Consuela']['gallery']['01_unlocked'] = True

    elif M_consuela.is_state(S_con04_hint) and L_beachhouse_kitchen.is_here(M_consuela):
        call con04_hint_condo_kitchen
        python:
            player.go_to(L_beachhouse_entrance)
            game.timer.tick()
            M_consuela.trigger(T_con04_hint)
            persistent.cookie_jar['Consuela']['unlocked'] = True
            persistent.cookie_jar['Consuela']['gallery']['02_unlocked'] = True

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

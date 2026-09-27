label beach_house_bedroom_dialogue:
    $ game.main()

label beach_house_sleeping:
    scene expression L_beachhouse_bedroom.background_blur with None
    call sleep_lock_check

    scene expression "backgrounds/location_beach_house_bedroom_sleep.jpg" with fade
    call popup ('sleep')

    if M_player.is_set("just wokeup"):
        call expression game.dialog_select("player_just_wokeup")

        if M_anon.is_state(S_ano25_init):
            if game.timer.is_date(dow=6):
                call ano25_init_wakeup.wait
            else:
                call ano25_init_wakeup
                $ M_anon.trigger(T_ano25_init)

        elif M_consuela.is_state(S_con03_init) and game.timer.is_weekday():
            call con03_init_condo_bedroom
            $ M_consuela.trigger(T_con03_init)

        elif M_consuela.is_state(S_con04_init) and L_beachhouse_entrance.is_here(M_consuela):
            call con04_init_condo_bedroom
            $ M_consuela.trigger(T_con04_init)

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

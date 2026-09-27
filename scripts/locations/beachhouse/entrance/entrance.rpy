label beach_house_entrance_dialogue:
    if L_beachhouse_entrance.first_visit:
        call expression game.dialog_select("beach_house_first_time")
        $ L_beachhouse_entrance.first_visit = False

    if M_consuela.is_state(S_con03_door):
        call con03_door_condo_lounge
        $ M_consuela.trigger(T_con03_door)

    elif M_consuela.is_state(S_con03_sing) and L_beachhouse_kitchen.is_here(M_consuela):
        call con03_sing_condo_lounge

    elif M_consuela.is_state(S_con04_wake):
        call con04_wake_condo_lounge
        $ player.go_to(L_beachhouse_kitchen)
        $ game.timer.tick()
        $ M_consuela.trigger(T_con04_wake)

    elif L_beachhouse_entrance.is_here(M_consuela) and M_consuela.pregnancy.stage > 4 and not M_consuela.once('stop_cleaning_baby'):
        call beachhouse_entrance_babies

    elif L_beachhouse_entrance.is_here(M_consuela) and M_consuela.is_state(S_con04_done) and player.has_item("mysterious_statue_1") and player.has_item("mysterious_statue_2") and not player.has_item("mysterious_statue_3"):
        call expression game.dialog_select("beach_house_entrance_mysterious_statue_3")
        $ player.get_item("mysterious_statue_3")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

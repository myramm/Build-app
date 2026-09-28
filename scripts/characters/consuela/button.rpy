label consuela_button_dialogue:
    call consuela_button_stage

    if M_anon.is_state(S_ano18_rage, S_ano18_trap):
        call ano18_trap_consuela

    elif L_rump_lobby.is_here(M_consuela) or L_rump_kitchen.is_here(M_consuela):
        call consuela_button_mansion

    elif L_mall_parking_lot.is_here(M_consuela):
        if M_consuela.is_state(S_con02_tell):
            call con02_tell_consuela
        else:
            call consuela_button_mall

    elif M_consuela.pregnancy.stage == 1 and not M_consuela.pregnancy.announced_pregnancy:
        call consuela_button_event_pregnancy

    elif L_hospital_floor2.is_here(M_consuela):
        call consuela_button_hospital

    elif 0 < M_consuela.pregnancy.stage < 5:
        call consuela_button_pregnant

    elif M_consuela.pregnancy.character_bedridden:
        call consuela_button_recovery

    elif M_consuela.pregnancy.stage > 4:
        call consuela_button_baby

    elif L_beachhouse_kitchen.is_here(M_consuela) and M_consuela.is_state(S_con04_done):
        call consuela_button_floor

    elif L_beachhouse_entrance.is_here(M_consuela) or L_beachhouse_kitchen.is_here(M_consuela):
        call consuela_button_beachhouse
    else:

        consuela "Hi."

    $ game.main()
    return

label consuela_button_stage:
    if L_rump_kitchen.is_here(M_consuela):
        scene expression background(512, 408, 3.5)
        show consuela
    elif L_rump_lobby.is_here(M_consuela):
        scene expression background(544, 448, 4.)
        show consuela
    elif L_rump_back.is_here(M_consuela):
        scene expression background(304, 448, 3.)
        show ricky a_shovel at flip
        show consuela
    elif L_mall_parking_lot.is_here(M_consuela):
        scene expression background(256, 400, 5.)
        show consuela b_casual a_sign f_sad at flip
    elif M_consuela.pregnancy.character_bedridden:
        scene expression game.timer.image('location_hospital_baby_bed{}')
        show consuela b_gown_bed f_normal_down
    elif L_hospital_floor2.is_here(M_consuela):
        scene expression background(704, 448, 4.)
        show consuela b_hospital
    elif L_beachhouse_entrance.is_here(M_consuela):
        scene expression background(680, 432, 4.)
        if M_consuela.pregnancy.stage > 4:
            show consuela b_dressed
        elif M_consuela.pregnancy:
            show consuela b_magic
        else:
            if randomizer() < 33:
                show consuela b_magic a_work1
            elif randomizer() < 66:
                show consuela b_magic a_work2
            else:
                show consuela b_magic a_work3
    elif L_beachhouse_kitchen.is_here(M_consuela) and not M_consuela.is_state(S_con04_done):
        scene expression background(232, 472, 3.6) at flip
        show layer master at flip
        show consuela a_work3
    elif L_beachhouse_kitchen.is_here(M_consuela) and renpy.get_mode() == 'screen':
        scene location_beach_house_kitchen_floor
        show consuela b_floor
    elif L_beachhouse_kitchen.is_here(M_consuela):
        scene expression background(576, 440, 3.) as stage at flip
        show layer master at flip
        show consuela b_magic a_cloth
    else:
        scene expression player.location.background_blur
        show consuela
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label nadya_button_dialogue:
    call nadya_button_stage

    if M_anon.is_state(S_ano27_plan):
        call ano27_plan_nadya
        $ player.go_to(L_warehouse_sewer)
        $ M_anon.trigger(T_ano27_plan)

    elif M_nadya.is_state(S_nad01_lewd):
        call nad01_lewd_nadya
        $ game.timer.tick()
        $ player.go_to(L_warehouse)
        $ M_nadya.trigger(T_nad01_lewd)

    elif 0 < M_nadya.pregnancy.stage < 5:
        call nadya_button_pregnant

    elif M_nadya.pregnancy.character_bedridden:
        call nadya_button_recovery

    elif M_nadya.pregnancy.stage > 4:
        call nadya_button_baby

    elif M_khadne.is_state(S_kha01_init) and L_warehouse_depot.is_here(M_nadya):
        call kha01_init_nadya
        $ M_khadne.trigger(T_kha01_init)

    elif M_khadne.is_state(S_kha01_lewd) and L_warehouse_depot.is_here(M_nadya):
        call global_lock_check (L_warehouse)

    elif L_warehouse_depot.is_here(M_nadya):
        call nadya_button_depot
        if _return == 'afterglow':
            $ game.timer.tick()
            $ player.go_to(L_warehouse_furnace)
    else:

        call nadya_button_office
        if _return == 'afterglow':
            $ game.timer.tick()
            $ player.go_to(L_warehouse)

    $ game.main()
    return


label nadya_button_stage:
    if L_warehouse_office.is_here(M_nadya):
        scene expression game.timer.image('location_warehouse_office_couch{}') as stage:
            xoffset -171
        show nadya b_dressed_couch
        if M_nadya.pregnancy.stage > 4:
            show nadya a_baby
        elif M_nadya.pregnancy:
            show nadya b_dressed_couch_magic
    elif L_warehouse_depot.is_here(M_nadya):
        scene expression background(312, 480, 5) as stage
        show svetlana b_dressed:
            xoffset 350
            xzoom -1
        show nadya a_point:
            xoffset 100
        if M_nadya.pregnancy.stage > 4:
            show nadya a_baby
        elif M_nadya.pregnancy:
            show nadya b_dressed_magic
    elif M_nadya.pregnancy.character_bedridden:
        scene expression game.timer.image('location_hospital_baby_bed{}')
        show svetlana a_baby b_dressed f_happy:
            crop (0, 0, 1024, 650)
            xoffset 300
            xzoom -1
            zoom .9
        show nadya b_gown_bed_sleep f_sleep
    else:
        scene expression player.location.background_blur as stage
        show nadya
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

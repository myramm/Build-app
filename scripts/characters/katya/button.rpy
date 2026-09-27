label katya_button_dialogue:
    call katya_button_stage

    if L_warehouse_depot.is_here(M_katya, M_khadne):
        call katya_button_depot
    else:

        call katya_button_office
        if _return == 'afterglow':
            $ game.timer.tick()
            $ player.go_to(L_warehouse_depot)

    $ game.main()
    return


label katya_button_stage:
    if L_warehouse_office.is_here(M_katya):
        scene location_warehouse_office_desk_close as stage
        show katya b_dressed_sit f_normal_down
        show location_warehouse_office_desk_overlay as desk
    else:




        scene expression player.location.background_blur as stage
        show katya
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label khadne_button_dialogue:
    call khadne_button_stage

    if M_khadne.is_state(S_kha01_lewd):
        call kha01_lewd_khadne
        $ game.timer.tick()
        $ player.go_to(L_warehouse_lab)
        $ M_khadne.trigger(T_kha01_lewd)
        $ M_khadne.move(L_warehouse_storage)
    else:

        call khadne_button_lab
        if _return == 'afterglow':
            $ game.timer.tick()
            $ player.go_to(L_warehouse_depot)

    $ game.main()
    return


label khadne_button_stage:
    if L_warehouse_lab.is_here(M_khadne):
        scene location_warehouse_drugs_table_close as stage
        show location_warehouse_drugs_table_stool as stool:
            xoffset 100
        show khadne b_casual_sit f_bored_down:
            xoffset 200
        show location_warehouse_drugs_table_overlay as desk:
            xoffset 200
    else:
        scene expression player.location.background_blur as stage
        show khadne
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

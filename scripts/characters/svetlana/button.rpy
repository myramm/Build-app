label svetlana_button_dialogue:
    call svetlana_button_stage

    if M_nadya.is_state(S_nad01_find):
        call nad01_find_svetlana
        $ player.go_to(L_warehouse_office)
        $ M_nadya.trigger(T_nad01_find)
    else:

        call svetlana_button_depot

    $ game.main()
    return


label svetlana_button_stage:
    if L_warehouse_depot.is_here(M_svetlana):
        scene expression background(480, 272, 7, l=L_warehouse_depot) as stage
        show svetlana b_dressed:
            xoffset -400
    else:
        scene expression player.location.background_blur
        show svetlana
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

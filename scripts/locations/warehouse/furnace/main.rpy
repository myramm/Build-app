label warehouse_furnace_dialogue:
    if L_warehouse_furnace.first_visit:
        call warehouse_furnace_intro
        $ L_warehouse_furnace.visited()

    $ game.main()
    return


label warehouse_furnace_bazooka:
    if M_anon.is_state(S_ano27_peek):
        call ano27_peek_bazooka

    elif M_anon.is_state(S_ano27_yolo):
        call ano27_yolo_bazooka
        $ player.go_to(L_warehouse_depot)
        $ M_anon.trigger(T_ano27_yolo)

    $ game.main()
    return


label warehouse_furnace_pinup:
    call warehouse_furnace_pinup_dialogue

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

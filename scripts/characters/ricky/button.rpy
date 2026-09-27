label ricky_button_dialogue:
    call ricky_button_stage

    if M_melonia.is_state(S_mel01_init) and game.timer.is_day():
        call mel01_init_net

    elif M_melonia.is_state(S_mel01_hint):
        call mel01_hint_ricky
        $ M_melonia.trigger(T_mel01_hint)

    elif M_melonia.is_state(S_mel01_find):
        call mel01_find_ricky

    elif M_melonia.is_state(S_mel01_help):
        call mel01_help_ricky
        $ player.remove_item('leaf_skimmer')
        $ game.timer.tick(1)
        $ M_melonia.trigger(T_mel01_help)

    elif L_rump_back.is_here(M_ricky):
        call ricky_button_garden

    $ game.main()
    return

label ricky_button_stage:
    if L_rump_back.is_here(M_ricky):
        if M_melonia.is_state(S_mel01_find, S_mel01_help):
            scene expression background(768, 368, 4.) as stage
            show location_rump_backyard_jacuzzi_overlay as hottubback:
                yoffset 140
            show location_rump_backyard_jacuzzi_overlay as hottub:
                yoffset 155
            show ricky:
                xoffset 150
        else:
            scene expression background(304, 448, 3.) as stage
            show ricky a_shovel at flip
    else:
        scene expression player.location.background_blur
        show ricky
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

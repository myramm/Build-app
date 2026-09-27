label rump_button_dialogue:
    call rump_button_stage

    if L_mall.is_here(M_rump):
        call rump_button_mall
        $ M_rump.set('seen speech mall', True)

    elif L_rump_back.is_here(M_rump):
        call rump_button_hottub

    elif L_police_basement.is_here(M_rump):
        if not M_rump.once('taunted'):
            call rump_button_jail
        else:
            call rump_button_jail.repeat
        $ player.go_to(L_police_lobby)

    $ game.main()
    return


label rump_button_stage:
    if L_mall.is_here(M_rump):
        scene mall_closeup
        show rump:
            xoffset -300
        show iwanka f_normal_crowd
        show char_xtra_18 as podium:
            align (.5, 1.)
            xoffset -200
    elif L_rump_back.is_here(M_rump):
        scene expression background(840, 368, 4.) as stage
        show location_rump_backyard_jacuzzi_overlay as hottubback:
            yoffset 140
        show rump b_jacuzzi:
            yoffset 155
        show location_rump_backyard_jacuzzi_overlay_evening as hottub:
            yoffset 155
    elif L_police_basement.is_here(M_rump):
        scene location_police_cell at right
        show rump b_jumpsuit a_bars f_angry:
            xoffset -50
            xzoom -1
        show cell_bars at left:
            xoffset -150
        show rump_overlay_jumpsuit_o_hands as hands:
            xoffset -50
            xzoom -1
    else:
        scene expression player.location.background_blur
        show rump
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label sato_button_dialogue:
    call sato_button_stage

    if M_josie.is_state(S_jos01_spot):
        call jos01_spot_sato
        if M_kim.state == 'fled':
            $ M_kim.set('state', 'jailed')
        $ M_josie.trigger(T_jos01_spot)

    elif M_josie.is_state(S_jos01_find):
        if not M_josie.once('jos01_sato'):
            call jos01_find_sato
        else:
            call jos01_find_sato.repeat

    elif L_dealership_office.is_here(M_sato):
        call sato_button_dealership

    elif L_dealership_showroom.is_here(M_sato):
        call sato_button_dealership
    else:

        sato "Oh tidak! Apakah para pengembang juga lupa menghubungkan dialog ini?!"


    if _return == 'josie_phone':
        call popup ('give', 'josie_phone')
        $ player.get_item('josie_phone')
        $ M_anon.trigger(T_ano05_cell)

    $ game.main()
    return


label sato_button_stage:
    if L_dealership_office.is_here(M_sato):
        scene location_dealership_office_desk_closeup
        show sato a_desk_paperwork:
            xoffset -30
            yoffset 86
        show sato_overlay_o_desk as desk
        if M_anon.is_state(S_ano05_cell):
            show sato_overlay_o_desk_phone as phone
    elif L_dealership_showroom.is_here(M_sato):
        if M_josie.is_state(S_jos01_find):
            scene expression background(608, 512, 3.8) as stage
            show sato
            show xtra3 as counter at right
        else:
            scene expression background(856, 464, 4.5) as stage
            show sato
    else:
        scene expression player.location.background_blur as stage
        show sato
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label josie_button_dialogue:
    call josie_button_stage

    if M_anon.is_state(S_ano05_prat):
        call ano05_prat_josie

    elif M_anon.is_state(S_ano05_deal):
        call ano05_deal_josie
        $ M_anon.trigger(T_ano05_deal)

    elif M_anon.is_state(S_ano05_cell):
        call ano05_cell_josie

    elif M_anon.is_state(S_ano05_bait):
        call ano05_bait_josie
        $ player.remove_item('josie_phone')
        $ M_anon.trigger(T_ano05_bait)
        $ M_player.set('ano05_continue', True)

    elif M_anon.is_state(S_ano05_sale) and M_player.ano05_continue:
        call ano05_sale_josie
        $ M_player.set('ano05_continue', False)

    elif M_anon.is_state(S_ano07_perk) and L_dealership_showroom.is_here(M_josie):
        call ano07_perk_josie
        $ M_anon.trigger(T_ano07_perk)
        $ M_player.set('ano07_continue', True)

    elif M_anon.is_state(S_ano07_sale) and M_player.ano07_continue:
        call ano07_sale_josie
        $ M_player.set('ano07_continue', False)

    elif M_anon.is_state(S_ano09_deal):
        call ano09_deal_josie
        $ M_anon.trigger(T_ano09_deal)

    elif M_anon.is_state(S_ano09_vest):
        call ano09_vest_josie

    elif M_yoyo.is_state(S_yoy01_lewd):
        call yoy01_lewd_josie

    elif M_anon.is_state(S_ano09_blow):
        call ano09_blow_josie
        $ M_anon.trigger(T_ano09_blow)
        $ game.timer.tick(3)
        $ player.go_to(L_dealership)

    elif M_josie.is_state(S_jos01_find):
        call jos01_find_josie
        $ M_anon.trigger(T_jos01_find)
        $ game.timer.tick()
        $ player.go_to(L_dealership)

    elif M_josie.sex:
        call josie_button_sex

    elif 0 < M_josie.pregnancy.stage < 5:
        call josie_button_pregnant

    elif M_josie.pregnancy.character_bedridden:
        call josie_button_recovery

    elif M_josie.pregnancy.stage > 4:
        call josie_button_baby

    elif L_dealership_lounge.is_here(M_josie):
        call josie_button_lounge
    else:

        call josie_button_showroom

    if _return == 'scooter_key':
        call popup ('give', 'scooter_key')
        $ player.get_item('scooter_key')
        $ player.transport_level = 2
        $ M_anon.trigger(T_ano05_sale)
        $ game.timer.tick()
        $ player.go_to(L_dealership)
        call ano05_sale_dealership

    elif _return == 'compact_key':
        $ player.remove_item('scooter_key')
        call popup ('give', 'compact_key')
        $ player.get_item('compact_key')
        $ player.transport_level = 3
        $ M_anon.trigger(T_ano07_sale)
        $ game.timer.tick()
        $ player.go_to(L_dealership)
        call ano07_sale_dealership

    elif _return == 'coupe_key':
        $ player.remove_item('compact_key')
        call popup ('give', 'coupe_key')
        $ player.get_item('coupe_key')
        $ player.transport_level = 4
        $ M_anon.trigger(T_ano09_sale)
        $ game.timer.tick()
        $ player.go_to(L_dealership)
        call ano09_sale_dealership

    elif _return == 'blowjob':
        $ game.timer.tick()
        if game.timer.is_night():
            $ player.go_to(L_dealership)

    elif _return == 'sex':
        $ M_josie.set('sex', 'lounge' if game.timer.is_day() else 'office')

    elif _return == 'afterglow':
        $ M_josie.set('sex', False)
        $ game.timer.tick()
        if game.timer.is_night():
            $ player.go_to(L_dealership)
        else:
            $ player.go_to(L_dealership_showroom)

    $ game.main()
    return


label josie_button_stage:
    if L_dealership_showroom.is_here(M_josie):
        scene expression background(608, 512, 3.8) as stage
        show xtra3 as counter at right
        if M_josie.pregnancy:
            if M_josie.pregnancy.stage > 4:
                show josephine a_baby f_normal_down behind counter
            elif M_josie.pregnancy.stage > 2:
                show josephine b_magic f_concerned behind counter
            else:
                show josephine b_magic a_phone f_normal_down behind counter
        elif M_anon.finished_state(S_ano05_bait):
            show josephine b_dressed_bored behind counter
        else:
            show josephine b_dressed_sleeping_no_phone
    elif L_dealership_lounge.is_here(M_josie):
        if M_josie.pregnancy:
            scene expression background(496, 384, 2.75) as stage
            if M_josie.pregnancy.stage > 4:
                show josephine a_baby f_normal_down
            elif M_josie.pregnancy.stage > 2:
                show josephine b_magic f_concerned
            else:
                show josephine b_magic a_phone f_normal_down
        else:
            scene expression background(792, 408, 3.) as stage
            show josephine_overlay_o_couch as couch:
                yoffset 50
            show josephine b_dressed_couch f_normal_down:
                yoffset 50
    elif M_josie.pregnancy.character_bedridden:
        scene expression game.timer.image('location_hospital_baby_bed{}')
        show josephine b_gown_bed f_normal_down
    else:
        scene expression player.location.background_blur
        show josephine
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

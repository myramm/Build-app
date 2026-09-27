screen dealership_showroom():
    add L_dealership_showroom.background

    imagebutton:
        focus_mask True
        pos 443, 269
        idle 'objects/object_door_173.png'
        hover HoverImage('objects/object_door_173.png')
        action MoveTo(L_dealership_office)

    imagebutton:
        focus_mask True
        pos 638, 251
        idle 'objects/object_door_172.png'
        hover HoverImage('objects/object_door_172.png')
        action MoveTo(L_dealership_lounge)

    imagebutton:
        focus_mask True
        pos 705, 423
        idle 'objects/object_door_171.png'
        hover HoverImage('objects/object_door_171.png')
        action MoveTo(L_dealership_garage)

    add 'backgrounds/location_dealership_indoor_car_overlay0[game.showroom_vehicle].png':
        align .5, 1.
        pos 166, 615

    if L_dealership_showroom.is_here(M_josie) and not M_josie.sex:
        imagebutton:
            focus_mask True
            pos 321, 655
            yanchor 1.
            if M_anon.is_state(S_ano05_prat, S_ano05_cell, S_ano05_bait) or M_yoyo.is_state(S_yoy01_lewd):
                idle 'characters/josephine/buttons/character_josephine_03.png'
                hover HoverImage('characters/josephine/buttons/character_josephine_03.png')
            elif M_anon.is_state(S_ano05_deal):
                idle 'characters/josephine/buttons/character_josephine_01b.png'
                hover HoverImage('characters/josephine/buttons/character_josephine_01b.png')
            elif M_josie.pregnancy:
                idle M_josie.get_button_path('showroom', name='josephine', use=('baby', 'belly'))
                hover HoverImage(M_josie.get_button_path('showroom', name='josephine', use=('baby', 'belly')))
            else:
                idle 'characters/josephine/buttons/character_josephine_01.png'
                hover HoverImage('characters/josephine/buttons/character_josephine_01.png')
            action TalkTo(M_josie)

    if L_dealership_showroom.is_here(M_kim) and not M_josie.is_state(S_jos01_spot):
        imagebutton:
            focus_mask True
            if L_dealership_showroom.is_here(M_josie):
                pos 876, 406
                idle 'characters/kim/buttons/character_kim_01.png'
                hover HoverImage('characters/kim/buttons/character_kim_01.png')
            else:
                pos 321, 423
                idle 'characters/kim/buttons/character_kim_02.png'
                hover HoverImage('characters/kim/buttons/character_kim_02.png')
            action TalkTo(M_kim)

    if L_dealership_showroom.is_here(M_yoyo) and not M_josie.is_state(S_jos01_spot):
        imagebutton:
            focus_mask True
            if L_dealership_showroom.is_here(M_josie):
                pos 882, 402
                if M_yoyo.is_state(S_yoy01_hold):
                    idle 'characters/yoyo/buttons/character_yoyo_dealership_lobby_day4.png'
                    hover HoverImage('characters/yoyo/buttons/character_yoyo_dealership_lobby_day4.png')
                else:
                    idle 'characters/yoyo/buttons/character_yoyo_dealership_lobby_day1.png'
                    hover HoverImage('characters/yoyo/buttons/character_yoyo_dealership_lobby_day1.png')
            else:
                pos 321, 426
                if M_yoyo.is_state(S_yoy01_hold):
                    idle 'characters/yoyo/buttons/character_yoyo_dealership_lobby_day3.png'
                    hover HoverImage('characters/yoyo/buttons/character_yoyo_dealership_lobby_day3.png')
                else:
                    idle 'characters/yoyo/buttons/character_yoyo_dealership_lobby_day2.png'
                    hover HoverImage('characters/yoyo/buttons/character_yoyo_dealership_lobby_day2.png')
            action TalkTo(M_yoyo)

    if L_dealership_showroom.is_here(M_sato):
        imagebutton:
            focus_mask True
            if L_dealership_showroom.is_here(M_kim, M_rump) and M_josie.is_state(S_jos01_spot):
                pos 800, 403
                idle 'characters/sato/buttons/character_sato_04.png'
                hover HoverImage('characters/sato/buttons/character_sato_04.png')
            elif L_dealership_showroom.is_here(M_kim) and M_josie.is_state(S_jos01_spot):
                pos 806, 397
                idle 'characters/sato/buttons/character_sato_06.png'
                hover HoverImage('characters/sato/buttons/character_sato_06.png')
            elif L_dealership_showroom.is_here(M_yoyo) and M_josie.is_state(S_jos01_spot):
                pos 806, 397
                idle 'characters/sato/buttons/character_sato_07.png'
                hover HoverImage('characters/sato/buttons/character_sato_07.png')
            elif M_josie.is_state(S_jos01_find):
                pos 321, 409
                idle 'characters/sato/buttons/character_sato_05.png'
                hover HoverImage('characters/sato/buttons/character_sato_05.png')
            else:
                pos 870, 385
                idle 'characters/sato/buttons/character_sato_01.png'
                hover HoverImage('characters/sato/buttons/character_sato_01.png')
            action TalkTo(M_sato)

    if M_josie.is_state(S_jos01_spot) or L_dealership_showroom.is_here(M_josie) and M_josie.sex or not (
        L_dealership_showroom.is_here(M_josie) or L_dealership_showroom.is_here(M_kim) or
        L_dealership_showroom.is_here(M_yoyo) or M_josie.is_state(S_jos01_find)):
        add 'backgrounds/location_dealership_indoor_desk.png':
            pos 322, 499

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action MoveTo(L_dealership)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

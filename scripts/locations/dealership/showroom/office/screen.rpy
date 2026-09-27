screen dealership_office():
    add L_dealership_office.background

    if L_dealership_office.is_here(M_josie) or M_josie.sex == 'office':
        imagebutton:
            focus_mask True
            if M_josie.sex == 'office':
                pos 432, 365
                idle 'characters/josephine/buttons/character_josephine_04.png'
                hover HoverImage('characters/josephine/buttons/character_josephine_04.png')
            else:
                pos 624, 457
                idle 'characters/josephine/buttons/character_josephine_13.png'
                hover HoverImage('characters/josephine/buttons/character_josephine_13.png')
            action TalkTo(M_josie)

    if L_dealership_office.is_here(M_sato):
        imagebutton:
            focus_mask True
            pos 462, 358
            idle 'characters/sato/buttons/character_sato_03.png'
            hover HoverImage('characters/sato/buttons/character_sato_03.png')
            action TalkTo(M_sato)

    if M_anon.is_state(S_ano05_cell):
        imagebutton:
            focus_mask True
            pos 539, 480
            idle 'objects/object_phone_02.png'
            hover HoverImage('objects/object_phone_02.png')
            action HideAll(), Jump('dealership_office_cell')

    if not player.has_picked_up_item('vest'):
        imagebutton:
            focus_mask True
            pos 59, 268
            idle 'objects/object_jacket.png'
            hover HoverImage('objects/object_jacket.png')
            action HideAll(), Jump('dealership_office_vest')

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action MoveTo(L_dealership_showroom)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

screen dealership_lounge():
    add L_dealership_lounge.background

    if L_dealership_lounge.is_here(M_josie) or M_josie.sex == 'lounge':
        imagebutton:
            focus_mask True
            if M_josie.sex == 'lounge':
                pos 353, 323
                idle 'characters/josephine/buttons/character_josephine_05.png'
                hover HoverImage('characters/josephine/buttons/character_josephine_05.png')
            elif M_josie.pregnancy:
                pos 502, 288
                idle M_josie.get_button_path('lounge', name='josephine', use_baby=True)
                hover HoverImage(M_josie.get_button_path('lounge', name='josephine', use_baby=True))
            else:
                pos 744, 433
                idle 'characters/josephine/buttons/character_josephine_02.png'
                hover HoverImage('characters/josephine/buttons/character_josephine_02.png')
            action TalkTo(M_josie)

    if L_dealership_lounge.is_here(M_kim):
        imagebutton:
            focus_mask True
            pos 296, 355
            idle 'characters/kim/buttons/character_kim_03.png'
            hover HoverImage('characters/kim/buttons/character_kim_03.png')
            action TalkTo(M_kim)

    if L_dealership_lounge.is_here(M_yoyo):
        imagebutton:
            focus_mask True
            pos 296, 357
            idle M_yoyo.get_button_path('dealership_lounge')
            hover HoverImage(M_yoyo.get_button_path('dealership_lounge'))
            action TalkTo(M_yoyo)

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action MoveTo(L_dealership_showroom)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

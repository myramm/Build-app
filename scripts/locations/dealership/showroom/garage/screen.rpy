screen dealership_garage():
    add L_dealership_garage.background

    imagebutton:
        focus_mask True
        pos 20, 364
        idle 'objects/object_door_174.png'
        hover HoverImage('objects/object_door_174.png')
        action MoveTo(L_dealership_showroom)

    if L_dealership_garage.is_here(M_kim, M_rump) and not M_josie.jos01_kim:
        imagebutton:
            focus_mask True
            pos 895, 431
            idle 'characters/kim/buttons/character_kim_04.png'
            hover HoverImage('characters/kim/buttons/character_kim_04.png')
            action TalkTo(M_kim)

    if L_dealership_garage.is_here(M_jiang):
        imagebutton:
            focus_mask True
            pos 291, 417
            idle 'characters/jiang/buttons/character_jiang_01.png'
            hover HoverImage('characters/jiang/buttons/character_jiang_01.png')
            action TalkTo(M_jiang)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

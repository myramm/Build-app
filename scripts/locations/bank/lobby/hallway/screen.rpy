screen bank_hallway():
    add L_bank_hallway.background

    imagebutton:
        focus_mask True
        pos 423, 387
        idle 'objects/object_door_192.png'
        hover HoverImage('objects/object_door_192.png')
        action MoveTo(L_bank_basement)

    imagebutton:
        focus_mask True
        pos 681, 190
        idle 'objects/object_door_191.png'
        hover HoverImage('objects/object_door_191.png')
        action MoveTo(L_bank_office)

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action MoveTo(L_bank_lobby)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

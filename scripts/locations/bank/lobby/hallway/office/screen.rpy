screen bank_office():
    add L_bank_office.background

    imagebutton:
        focus_mask True
        pos 771, 292
        idle 'objects/object_door_205.png'
        hover HoverImage('objects/object_door_205.png')
        action MoveTo(L_bank_cubicle)

    imagebutton:
        focus_mask True
        pos 47, 264
        idle 'objects/object_door_193.png'
        hover HoverImage('objects/object_door_193.png')
        action MoveTo(L_bank_hallway)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

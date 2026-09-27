screen bank_basement():
    add L_bank_basement.background

    imagebutton:
        focus_mask True
        pos 905, 245
        idle 'objects/object_door_194.png'
        hover HoverImage('objects/object_door_194.png')
        action MoveTo(L_bank_hallway)

    imagebutton:
        focus_mask True
        if M_anon.is_state(S_ano14_find):
            pos 52, 274
            idle 'objects/object_door_195_open.png'
            hover HoverImage('objects/object_door_195_open.png')
        else:
            pos 50, 323
            idle 'objects/object_door_195.png'
            hover HoverImage('objects/object_door_195.png')
        action MoveTo(L_bank_vault)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

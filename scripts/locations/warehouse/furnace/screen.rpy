screen warehouse_furnace():
    add L_warehouse_furnace.background

    imagebutton:
        focus_mask True
        pos 488, 295
        idle 'objects/object_door_212.png'
        hover HoverImage('objects/object_door_212.png')
        action MoveTo(L_warehouse_cargo)

    imagebutton:
        focus_mask True
        pos 377, 375
        idle 'objects/object_pinup.png'
        hover HoverImage('objects/object_pinup.png')
        action HideAll(), Jump('warehouse_furnace_pinup')

    if M_anon.is_state(S_ano27_peek, S_ano27_yolo):
        imagebutton:
            focus_mask True
            pos 847, 384
            idle 'objects/object_bazooka_furnace.png'
            hover HoverImage('objects/object_bazooka_furnace.png')
            action HideAll(), Jump('warehouse_furnace_bazooka')

    imagebutton:
        focus_mask True
        pos 980, 307
        idle 'objects/object_door_211.png'
        hover HoverImage('objects/object_door_211.png')
        action MoveTo(L_warehouse_depot)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

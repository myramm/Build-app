screen warehouse_cargo():
    add L_warehouse_cargo.background

    if L_warehouse_cargo.is_here(M_jab):
        imagebutton:
            focus_mask True
            pos 292, 298
            idle M_jab.get_button_path('warehouse_leaning')
            hover HoverImage(M_jab.get_button_path('warehouse_leaning'))
            action TalkTo(M_jab)

    imagebutton:
        focus_mask True
        pos 0, 106
        idle 'objects/object_door_213.png'
        hover HoverImage('objects/object_door_213.png')
        action MoveTo(L_warehouse_furnace)

    imagebutton:
        focus_mask True
        pos 283, 596
        idle 'objects/object_ladder_05.png'
        hover HoverImage('objects/object_ladder_05.png')
        action MoveTo(L_warehouse_sewer)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

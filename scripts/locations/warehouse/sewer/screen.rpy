screen warehouse_sewer():
    add L_warehouse_sewer.background

    imagebutton:
        focus_mask True
        pos 396, 35
        idle 'objects/object_ladder_04.png'
        hover HoverImage('objects/object_ladder_04.png')
        action MoveTo(L_warehouse_cargo)

    imagebutton:
        focus_mask True
        pos 0, 417
        idle 'objects/object_pipe_02.png'
        hover HoverImage('objects/object_pipe_02.png')
        action HideAll(), Jump('warehouse_sewer_pipe')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

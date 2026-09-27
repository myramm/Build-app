screen dianes_lobby():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (700,431)
        idle "objects/object_door_56.png"
        hover HoverImage("objects/object_door_56.png")
        action MoveTo(L_diane_yard)

    imagebutton:
        focus_mask True
        pos (26,193)
        idle "objects/object_door_57.png"
        hover HoverImage("objects/object_door_57.png")
        action MoveTo(L_diane_kitchen)

    imagebutton:
        focus_mask True
        pos (369,93)
        idle "objects/object_door_58.png"
        hover HoverImage("objects/object_door_58.png")
        action MoveTo(L_diane_bedroom)

    use mods_screens_hook("dianes_lobby")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

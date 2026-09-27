screen hospital_basement():
    add player.location.background

    imagebutton:
        focus_mask True
        pos 466, 458
        idle "objects/object_elevator_01.png"
        hover HoverImage("objects/object_elevator_01.png")
        action MoveTo(L_hospital_elevator)

    imagebutton:
        focus_mask True
        pos 371, 412
        idle "objects/object_door_136.png"
        hover HoverImage("objects/object_door_136.png")
        action MoveTo(L_hospital_lab)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

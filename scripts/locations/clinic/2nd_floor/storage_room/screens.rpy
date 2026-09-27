screen hospital_storage_room():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (247,282)
        idle "objects/object_door_80.png"
        hover HoverImage("objects/object_door_80.png")
        action MoveTo(L_hospital_storagecabinet)

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_hospital_floor2)

    use mods_screens_hook("hospital_storage_room")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

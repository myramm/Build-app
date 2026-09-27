screen mall_second_floor():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (358,236)
        idle "objects/object_door_21.png"
        hover HoverImage("objects/object_door_21.png")
        action MoveTo(L_pink)

    imagebutton:
        focus_mask True
        pos (45,164)
        idle "objects/object_door_103.png"
        hover HoverImage("objects/object_door_103.png")
        action MoveTo(L_cupid)

    imagebutton:
        focus_mask True
        pos (-2,527)
        idle "objects/object_stairs_07.png"
        hover HoverImage("objects/object_stairs_07.png")
        action MoveTo(L_mall)

    imagebutton:
        focus_mask True
        pos (488,335)
        idle "objects/object_booth_01.png"
        hover HoverImage("objects/object_booth_01.png")
        action MoveTo(L_mall_photobooth)

    use mods_screens_hook("mall_second_floor")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

screen mall():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (612,364)
        idle "objects/object_stairs_06.png"
        hover HoverImage("objects/object_stairs_06.png")
        action MoveTo(L_mall_floor2)

    imagebutton:
        focus_mask True
        pos (761,234)
        idle "objects/object_door_22.png"
        hover HoverImage("objects/object_door_22.png")
        action MoveTo(L_consumr)

    imagebutton:
        focus_mask True
        pos (42,156)
        idle "objects/object_door_23.png"
        hover HoverImage("objects/object_door_23.png")
        action MoveTo(L_movie_theatre)

    if M_jenny.is_state(S_jenny_get_a_mask):
        imagebutton:
            focus_mask True
            pos (439, 321)
            idle "objects/object_door_53b.png"
            hover HoverImage("objects/object_door_53b.png")
            action MoveTo(L_comicstore)
    else:
        imagebutton:
            focus_mask True
            pos (541,321)
            idle "objects/object_door_53.png"
            hover HoverImage("objects/object_door_53.png")
            action MoveTo(L_comicstore)

        if L_mall.is_here(M_rump) and M_rump.get("can see speech mall"):
            imagebutton:
                focus_mask True
                pos (354,308)
                idle "objects/object_podium_01.png"
                hover HoverImage("objects/object_podium_01.png")
                action TalkTo(M_rump)

    imagebutton:
        focus_mask True
        pos (285,317)
        idle "objects/object_door_52.png"
        hover HoverImage("objects/object_door_52.png")
        action MoveTo(L_mall_toilets)

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action ExitLocation()

    use mods_screens_hook("mall")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

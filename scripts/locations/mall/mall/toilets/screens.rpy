screen mall_toilets():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (184,189)
        idle "objects/object_door_54.png"
        hover HoverImage("objects/object_door_54.png")
        action MoveTo(L_mall_toilets_stall)

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_10.png"
        hover HoverImage("boxes/auto_option_10.png")
        action ExitLocation()

    use mods_screens_hook("mall_toilets")


screen mall_toilets_stall():
    add player.location.background

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action ExitLocation()

    use mods_screens_hook("mall_toilets_stall")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

screen donut_shop():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (591,443)
        idle game.timer.image("objects/object_door_91{}.png")
        hover HoverImage(game.timer.image("objects/object_door_91{}.png"))
        action MoveTo(L_donutshop_interior)

    use mods_screens_hook("donut_shop")

screen donut_shop_interior():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (660,325)
        idle "objects/character_beth_01.png"
        hover HoverImage("objects/character_beth_01.png")
        action Hide("donut_shop_interior"), Jump("beth_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action ExitLocation()

    use mods_screens_hook("donut_shop_interior")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

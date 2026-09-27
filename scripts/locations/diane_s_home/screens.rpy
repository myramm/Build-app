screen dianes_front_yard():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (289,382)
        idle game.timer.image("objects/object_door_106{}.png")
        hover HoverImage(game.timer.image("objects/object_door_106{}.png"))
        action MoveTo(L_diane_home)

    imagebutton:
        focus_mask True
        pos (563,482)
        idle game.timer.image("objects/object_door_107{}.png")
        hover HoverImage(game.timer.image("objects/object_door_107{}.png"))
        action MoveTo(L_diane_garden)

    use mods_screens_hook("dianes_front_yard")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

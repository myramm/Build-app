screen church_stairs():
    add player.location.background

    imagebutton:
        focus_mask True
        pos 773, 503
        idle game.timer.image("objects/object_door_72{}.png")
        hover HoverImage(game.timer.image("objects/object_door_72{}.png"))
        action MoveTo(L_church)

    imagebutton:
        focus_mask True
        pos 18, 235
        idle game.timer.image("objects/object_door_73{}.png")
        hover HoverImage(game.timer.image("objects/object_door_73{}.png"))
        action MoveTo(L_church_angelica)

    imagebutton:
        focus_mask True
        pos 316, 210
        idle game.timer.image("objects/object_door_74{}.png")
        hover HoverImage(game.timer.image("objects/object_door_74{}.png"))
        action MoveTo(L_church_bell)

    use mods_screens_hook("church_stairs")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

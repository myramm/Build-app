screen pizzeria_exterior():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (353,465)
        idle game.timer.image("objects/object_door_37{}.png")
        hover HoverImage(game.timer.image("objects/object_door_37{}.png"))
        action MoveTo(L_pizzeria_interior)

    use mods_screens_hook("pizzeria_exterior")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

screen church_cloister_bell():
    add player.location.background

    if M_aqua.is_set("bell search"):
        imagebutton:
            focus_mask True
            pos (322,51)
            idle game.timer.image("objects/object_bell_01{}.png")
            hover HoverImage(game.timer.image("objects/object_bell_01{}.png"))
            action HideAll(), Jump('church_tower_bell')

    imagebutton:
        focus_mask True
        pos (0,305)
        idle game.timer.image("objects/object_door_96{}.png")
        hover HoverImage(game.timer.image("objects/object_door_96{}.png"))
        action MoveTo(L_church_stairs)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

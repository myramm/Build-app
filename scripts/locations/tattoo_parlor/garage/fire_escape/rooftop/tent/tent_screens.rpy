screen tattoo_parlor_tent():
    add player.location.background

    imagebutton:
        focus_mask True
        alt 'Tent Flap'
        pos 832, 168
        idle game.timer.image("objects/object_door_152{}.png")
        hover HoverImage(game.timer.image("objects/object_door_152{}.png"))
        action ExitLocation()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

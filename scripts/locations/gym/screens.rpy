screen gym_front():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (520,259)
        idle game.timer.image("objects/object_door_113{}.png")
        hover HoverImage(game.timer.image("objects/object_door_113{}.png"))
        action MoveTo(L_gym)

    use mods_screens_hook("gym_front")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

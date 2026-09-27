screen beach_house_patio():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (797,194)
        idle game.timer.image("objects/object_door_116{}.png")
        hover HoverImage(game.timer.image("objects/object_door_116{}.png"))
        action MoveTo(L_beachhouse_bedroom)

    use mods_screens_hook("beach_house_patio")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

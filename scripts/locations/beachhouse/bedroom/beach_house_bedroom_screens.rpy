screen beach_house_bedroom():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (0,290)
        idle game.timer.image("objects/object_door_118{}.png")
        hover HoverImage(game.timer.image("objects/object_door_118{}.png"))
        action MoveTo(L_beachhouse_patio)
    imagebutton:
        focus_mask True
        pos (0,690)
        idle game.timer.image("objects/object_stairs_09{}.png")
        hover HoverImage(game.timer.image("objects/object_stairs_09{}.png"))
        action MoveTo(L_beachhouse_entrance)
    imagebutton:
        focus_mask True
        pos (265,475)
        idle game.timer.image("objects/object_bed_12{}.png")
        hover HoverImage(game.timer.image("objects/object_bed_12{}.png"))
        action Hide("beach_house_bedroom"), Jump("beach_house_sleeping")

    use mods_screens_hook("beach_house_bedroom")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

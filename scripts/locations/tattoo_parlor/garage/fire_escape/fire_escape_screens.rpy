screen tattoo_parlor_fire_escape():
    add L_tattooparlor_fire_escape.background

    imagebutton:
        focus_mask True
        pos 239, 211
        idle game.timer.image("objects/object_door_145{}.png")
        hover HoverImage(game.timer.image("objects/object_door_145{}.png"))
        action MoveTo(L_tattooparlor_apartment)

    imagebutton:
        focus_mask True
        pos 481, 517
        idle game.timer.image("objects/object_ladder_03{}.png")
        hover HoverImage(game.timer.image("objects/object_ladder_03{}.png"))
        action MoveTo(L_tattooparlor_garage)

    imagebutton:
        focus_mask True
        pos 699, 0
        idle game.timer.image("objects/object_stairs_11{}.png")
        if not L_tattooparlor_roof.locked:
            hover HoverImage(game.timer.image("objects/object_stairs_11{}.png"))
            action MoveTo(L_tattooparlor_roof)

    use mods_screens_hook("tattoo_parlor_fire_escape")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

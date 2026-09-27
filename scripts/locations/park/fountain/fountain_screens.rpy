screen park_fountain():
    add L_park_fountain.background

    if not player.has_item("weird_coin"):
        imagebutton:
            focus_mask True
            align (0.44,0.81)
            if not game.timer.is_dark():
                idle "objects/object_coin_01.png"
                hover HoverImage("objects/object_coin_01.png")
            else:
                idle Composite((35,37), (0,0), "objects/object_coin_01_night.png", (10,-10), PulseImage(Crop((0,0,30,30), "map/map_sparkle01_alpha.png"), "map/map_sparkle03.png", delay1 = 5, delay2 = 0.2))
                hover HoverImage("objects/object_coin_01_night.png")
            action Hide("park_fountain"), Jump("coin_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("park_fountain"), Jump("park_dialogue")

    use mods_screens_hook("park_fountain")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

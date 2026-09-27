screen garage():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (380,356)
        idle game.timer.image("objects/object_car_01{}.png")
        hover HoverImage(game.timer.image("objects/object_car_01{}.png"))
        action Hide("garage"), Jump("car_dialogue")

    imagebutton:
        focus_mask True
        pos (43,486)
        idle game.timer.image("objects/object_mower_01{}.png")
        hover HoverImage(game.timer.image("objects/object_mower_01{}.png"))
        action Hide("garage"), Jump("lawnmower_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_08.png"
        hover HoverImage("boxes/auto_option_08.png")
        action MoveTo(L_home)

    if not player.has_picked_up_item("shovel"):
        imagebutton:
            focus_mask True
            pos (30,250)
            idle game.timer.image("objects/object_shovel_01{}.png")
            hover HoverImage(game.timer.image("objects/object_shovel_01{}.png"))
            action Hide("garage"), Jump("home_garage_shovel")

    if not player.has_picked_up_item("stool"):
        imagebutton:
            focus_mask True
            pos (257,250)
            idle game.timer.image("objects/object_stool_01{}.png")
            hover HoverImage(game.timer.image("objects/object_stool_01{}.png"))
            action GetItem('stool')

    if not player.has_picked_up_item("drill") and M_dewitt.is_state(S_dewitt_make_new_flute):
        imagebutton:
            focus_mask True
            pos (251,344)
            idle game.timer.image("objects/object_drill_01{}.png")
            hover HoverImage(game.timer.image("objects/object_drill_01{}.png"))
            action Hide("garage"), Jump("garage_dewitt_drill")

    imagebutton:
        focus_mask True
        pos (872,426)
        idle game.timer.image("objects/object_workbench_01{}.png")
        hover HoverImage(game.timer.image("objects/object_workbench_01{}.png"))
        action Hide("garage"), Jump("garage_use_workbench")

    use mods_screens_hook("garage")

screen car_engine():
    add game.timer.image("backgrounds/location_home_garage_car_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (110,97)
        idle game.timer.image("objects/object_engine_01{}.png")
        hover HoverImage(game.timer.image("objects/object_engine_01{}.png"))
        action Hide("car_engine"), Jump("engine_broken")

    use mods_screens_hook("car_engine")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

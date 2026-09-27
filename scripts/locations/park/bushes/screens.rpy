screen park_bushes():
    add game.timer.image("backgrounds/location_park_bushes_day{}.jpg")

    if not player.has_picked_up_item("stolen_goods"):
        imagebutton:
            focus_mask True
            pos (32,508)
            idle game.timer.image("objects/object_bag_02{}.png")
            hover HoverImage(game.timer.image("objects/object_bag_02{}.png"))
            action MoveTo(L_park_bushesbag)

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_park)

    use mods_screens_hook("park_bushes")

screen park_bushes_bag():
    add L_park_bushesbag.background

    if not player.has_item("treasure_key"):
        imagebutton:
            focus_mask True
            pos (540,280)
            idle "objects/object_key_02.png"
            hover HoverImage("objects/object_key_02.png")
            action (Function(player.get_item, "treasure_key"),
                    ShowPopup('give', 'treasure_key'))

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_park_bushes)

    use mods_screens_hook("park_bushes_bag")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

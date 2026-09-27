screen school_third_floor():
    use mods_screens_hook("school_third_floor")

    add game.timer.image("backgrounds/location_school_third_day{}.jpg")

    if M_dewitt.is_state(S_dewitt_paint_trail):
        add "paint_trail_03" at center

    imagebutton:
        focus_mask True
        pos (17,294)
        idle game.timer.image("objects/object_sign_04{}.png")
        hover HoverImage(game.timer.image("objects/object_sign_04{}.png"))
        action MoveTo(L_school_floor2)

    imagebutton:
        focus_mask True
        pos (277,247)
        idle game.timer.image("objects/object_door_98{}.png")
        hover HoverImage(game.timer.image("objects/object_door_98{}.png"))
        action MoveTo(L_school_bissetteoffice)

    imagebutton:
        focus_mask True
        pos (454,301)
        idle game.timer.image("objects/object_door_99{}.png")
        hover HoverImage(game.timer.image("objects/object_door_99{}.png"))
        action MoveTo(L_school_dewittoffice)

    imagebutton:
        focus_mask True
        pos (591,344)
        idle game.timer.image("objects/object_door_100{}.png")
        hover HoverImage(game.timer.image("objects/object_door_100{}.png"))
        action MoveTo(L_school_rossoffice)

    imagebutton:
        focus_mask True
        pos (700,379)
        idle game.timer.image("objects/object_door_101{}.png")
        hover HoverImage(game.timer.image("objects/object_door_101{}.png"))
        action MoveTo(L_school_okitaoffice)

    if (M_okita.is_state(S_okita_get_ingredients) and game.timer.is_afternoon() and not player.has_item("tissue")) and not M_dewitt.is_state([S_dewitt_paint_trail, S_dewitt_check_up]):
        imagebutton:
            focus_mask True
            pos (831,367)
            idle "objects/object_door_13_annie.png"
            hover HoverImage("objects/object_door_13_annie.png")
            action MoveTo(L_school_smithoffice)

    elif L_school_floor3.is_here(M_roxxy):
        imagebutton:
            focus_mask True
            pos (828,367)
            idle "objects/character_roxxy_04.png"
            hover HoverImage("objects/character_roxxy_04.png")
            action Hide("school_third_floor"), Jump("roxxy_third_floor_dialogue")

    else:
        imagebutton:
            focus_mask True
            pos (831,367)
            idle game.timer.image("objects/object_door_13{}.png")
            hover HoverImage(game.timer.image("objects/object_door_13{}.png"))
            action MoveTo(L_school_smithoffice)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

screen school_left_hallway():
    add game.timer.image("backgrounds/location_school_lefthall_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (757,297)
        idle game.timer.image("objects/object_door_14{}.png")
        hover HoverImage(game.timer.image("objects/object_door_14{}.png"))
        action MoveTo(L_school_utilitycloset)

    imagebutton:
        focus_mask True
        pos (661,281)
        if player.location.is_here(M_eve):
            idle "objects/object_door_15_eve.png"
            hover HoverImage("objects/object_door_15_eve.png")
            action TalkTo(M_eve)
        else:
            idle game.timer.image("objects/object_door_15{}.png")
            hover HoverImage(game.timer.image("objects/object_door_15{}.png"))
            action MoveTo(L_school_boysroom)

    imagebutton:
        focus_mask True
        pos (872,172)
        idle game.timer.image("objects/object_door_64{}.png")
        hover HoverImage(game.timer.image("objects/object_door_64{}.png"))
        action MoveTo(L_school_artclassroom)

    imagebutton:
        focus_mask True
        pos (195,281)
        idle game.timer.image("objects/object_door_16{}.png")
        hover HoverImage(game.timer.image("objects/object_door_16{}.png"))
        action MoveTo(L_school_girlsroom)

    if player.location.is_here(M_judith):
        imagebutton:
            focus_mask True
            pos (490,370)
            idle "objects/character_judith_01.png"
            hover HoverImage("objects/character_judith_01.png")
            action TalkTo(M_judith)

    imagebutton:
        focus_mask True
        pos (37,233)
        idle game.timer.image("objects/object_locker_09{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_09{}.png"))
        action MoveTo(L_school_locker_roxxy)

    imagebutton:
        focus_mask True
        pos (133,281)
        idle game.timer.image("objects/object_locker_10{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_10{}.png"))
        action MoveTo(L_school_locker_judith)


    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/door07_option_01.png"
        hover HoverImage("boxes/door07_option_01.png")
        action MoveTo(L_school_hall)

    use mods_screens_hook("school_left_hallway")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

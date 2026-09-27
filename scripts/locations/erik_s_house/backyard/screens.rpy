screen eriks_backyard():
    use mods_screens_hook("eriks_backyard")

    add game.timer.image("backgrounds/location_erik_house_backyard_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (0,395)
        idle game.timer.image("objects/object_door_69{}.png")
        hover HoverImage(game.timer.image("objects/object_door_69{}.png"))
        action MoveTo(L_erikhouse)

    if M_erik.is_state(S_erik_thief_chase):
        imagebutton:
            focus_mask True
            pos (777,394)
            idle "objects/object_door_70_thief_night.png"
            hover HoverImage("objects/object_door_70_thief_night.png")
            action Hide("eriks_backyard"), Jump("erik_thief")
    else:
        imagebutton:
            focus_mask True
            pos (778,393)
            idle game.timer.image("objects/object_door_70{}.png")
            hover HoverImage(game.timer.image("objects/object_door_70{}.png"))
            action MoveTo(L_erikhouse_entrance)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

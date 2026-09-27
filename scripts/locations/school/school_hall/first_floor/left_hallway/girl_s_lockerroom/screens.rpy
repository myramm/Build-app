screen school_girls_lockerroom():
    add game.timer.image("backgrounds/location_school_locker_room_broken{}.jpg")

    imagebutton:
        focus_mask True
        pos (348,314)
        idle game.timer.image("objects/object_door_32{}.png")
        hover HoverImage(game.timer.image("objects/object_door_32{}.png"))
        action Show("door32_options")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_02.png"
        hover HoverImage("boxes/auto_option_02.png")
        action MoveTo(L_school_lefthallway)

    use mods_screens_hook("school_girls_lockerroom")

screen door32_options():
    imagebutton:
        idle "ground.png"
        action Hide("door32_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/door32_option_01.png"
        hover HoverImage("boxes/door32_option_01.png")
        action Hide("door32_options"), MoveTo(L_school_stall)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

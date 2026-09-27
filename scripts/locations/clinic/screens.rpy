screen hospital():
    add L_hospital.background

    imagebutton:
        focus_mask True
        alt "Hospital Lobby Door"

        pos 720, 356
        idle game.timer.image("objects/object_door_155{}.png")
        hover HoverImage(game.timer.image("objects/object_door_155{}.png"))
        action MoveTo(L_hospital_lobby)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

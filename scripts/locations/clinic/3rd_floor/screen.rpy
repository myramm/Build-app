screen hospital_3rd_floor():
    add L_hospital_floor3.background

    imagebutton:
        focus_mask True
        pos 371, 410
        idle game.timer.image('objects/object_door_167{}.png')
        hover HoverImage(game.timer.image('objects/object_door_167{}.png'))
        action MoveTo(L_hospital_recovery1)

    imagebutton:
        focus_mask True
        pos 301, 354
        idle game.timer.image('objects/object_door_168{}.png')
        hover HoverImage(game.timer.image('objects/object_door_168{}.png'))
        action MoveTo(L_hospital_recovery2)

    imagebutton:
        focus_mask True
        pos 195, 269
        idle game.timer.image('objects/object_door_169{}.png')
        hover HoverImage(game.timer.image('objects/object_door_169{}.png'))
        action MoveTo(L_hospital_recovery3)

    imagebutton:
        focus_mask True
        pos 27, 142
        idle game.timer.image('objects/object_door_170{}.png')
        hover HoverImage(game.timer.image('objects/object_door_170{}.png'))
        action MoveTo(L_hospital_recovery4)

    imagebutton:
        focus_mask True
        pos 466, 458
        idle "objects/object_elevator_01.png"
        hover HoverImage("objects/object_elevator_01.png")
        action MoveTo(L_hospital_elevator)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

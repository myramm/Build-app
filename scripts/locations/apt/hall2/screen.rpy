screen apt_hall2():
    add L_apt_hall2.background

    imagebutton:
        focus_mask True
        pos 456, 407
        idle game.timer.image('objects/object_elevator_03{}.png')
        hover HoverImage(game.timer.image('objects/object_elevator_03{}.png'))
        action MoveTo(L_apt_lift)

    imagebutton:
        focus_mask True
        pos 341, 366
        idle game.timer.image('objects/object_door_183{}.png')
        hover HoverImage(game.timer.image('objects/object_door_183{}.png'))
        action MoveTo(L_apt_other)

    imagebutton:
        focus_mask True
        pos 636, 366
        idle game.timer.image('objects/object_door_184{}.png')
        hover HoverImage(game.timer.image('objects/object_door_184{}.png'))
        action MoveTo(L_liu_lounge)

    imagebutton:
        focus_mask True
        pos 123, 203
        idle game.timer.image('objects/object_door_181{}.png')
        hover HoverImage(game.timer.image('objects/object_door_181{}.png'))
        action MoveTo(L_apt_other)

    imagebutton:
        focus_mask True
        pos 796, 203
        idle game.timer.image('objects/object_door_182{}.png')
        hover HoverImage(game.timer.image('objects/object_door_182{}.png'))
        action MoveTo(L_apt_other)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

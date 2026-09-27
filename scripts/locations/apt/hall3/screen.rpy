screen apt_hall3():
    add L_apt_hall3.background

    imagebutton:
        focus_mask True
        pos 456, 407
        idle game.timer.image('objects/object_elevator_04{}.png')
        hover HoverImage(game.timer.image('objects/object_elevator_04{}.png'))
        action MoveTo(L_apt_lift)

    imagebutton:
        focus_mask True
        pos 337, 355
        idle game.timer.image('objects/object_door_187{}.png')
        hover HoverImage(game.timer.image('objects/object_door_187{}.png'))
        action MoveTo(L_apt_other)

    imagebutton:
        focus_mask True
        pos 631, 354
        idle game.timer.image('objects/object_door_188{}.png')
        hover HoverImage(game.timer.image('objects/object_door_188{}.png'))
        action MoveTo(L_apt_other)

    imagebutton:
        focus_mask True
        pos 121, 192
        idle game.timer.image('objects/object_door_185{}.png')
        hover HoverImage(game.timer.image('objects/object_door_185{}.png'))
        action MoveTo(L_tina_lounge)

    imagebutton:
        focus_mask True
        pos 786, 192
        idle game.timer.image('objects/object_door_186{}.png')
        hover HoverImage(game.timer.image('objects/object_door_186{}.png'))
        action MoveTo(L_maria_lounge)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

screen apt_hall1():
    add L_apt_hall1.background

    imagebutton:
        focus_mask True
        pos 341, 366
        idle game.timer.image('objects/object_door_179{}.png')
        hover HoverImage(game.timer.image('objects/object_door_179{}.png'))
        action MoveTo(L_apt_other)

    imagebutton:
        focus_mask True
        pos 636, 366
        idle game.timer.image('objects/object_door_180{}.png')
        hover HoverImage(game.timer.image('objects/object_door_180{}.png'))
        action MoveTo(L_apt_other)

    imagebutton:
        focus_mask True
        pos 123, 203
        idle game.timer.image('objects/object_door_177{}.png')
        hover HoverImage(game.timer.image('objects/object_door_177{}.png'))
        action MoveTo(L_apt_other)

    imagebutton:
        focus_mask True
        pos 796, 203
        idle game.timer.image('objects/object_door_178{}.png')
        hover HoverImage(game.timer.image('objects/object_door_178{}.png'))
        action MoveTo(L_apt_other)

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action MoveTo(L_apt_lobby)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

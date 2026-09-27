screen apt():
    add L_apt.background

    imagebutton:
        focus_mask True
        pos 424, 361
        idle game.timer.image('objects/object_door_175{}.png')
        hover HoverImage(game.timer.image('objects/object_door_175{}.png'))
        action MoveTo(L_apt_lobby)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

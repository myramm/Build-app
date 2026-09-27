screen dealership():
    add L_dealership.background

    imagebutton:
        focus_mask True
        pos 643, 432
        idle game.timer.image('objects/object_door_38{}.png')
        hover HoverImage(game.timer.image('objects/object_door_38{}.png'))
        action MoveTo(L_dealership_showroom)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

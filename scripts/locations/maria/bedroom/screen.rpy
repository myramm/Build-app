screen maria_bedroom():
    add L_maria_bedroom.background

    imagebutton:
        focus_mask True
        pos 722, 306
        idle game.timer.image('objects/object_door_204{}.png')
        hover HoverImage(game.timer.image('objects/object_door_204{}.png'))
        action MoveTo(L_maria_lounge)

    if not player.has_picked_up_item('duffel'):
        imagebutton:
            focus_mask True
            pos 387, 541
            idle game.timer.image('objects/object_duffel{}.png')
            hover HoverImage(game.timer.image('objects/object_duffel{}.png'))
            action HideAll(), Jump('maria_bedroom_duffel')

    if L_maria_bedroom.is_here(M_maria):
        imagebutton:
            focus_mask True
            pos 347, 371
            idle M_maria.get_button_path('bedroom')
            hover HoverImage(M_maria.get_button_path('bedroom'))
            action TalkTo(M_maria)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

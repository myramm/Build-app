screen home_front():
    add L_home.background

    imagebutton:
        if game.mail['player']:
            pos 880, 480
            idle game.timer.image('objects/object_mailbox_home01{}.png')
            hover HoverImage(game.timer.image('objects/object_mailbox_home01{}.png'))
        else:
            pos 880, 500
            idle game.timer.image('objects/object_mailbox_home02{}.png')
            hover HoverImage(game.timer.image('objects/object_mailbox_home02{}.png'))
        action MoveTo(L_home_mailbox)

    imagebutton:
        focus_mask True
        pos 557, 454
        if M_anon.is_state(S_ano27_yumi):
            idle game.timer.image('objects/object_door_34_open{}.png')
            hover HoverImage(game.timer.image('objects/object_door_34_open{}.png'))
        else:
            idle game.timer.image('objects/object_door_34{}.png')
            hover HoverImage(game.timer.image('objects/object_door_34{}.png'))
        action MoveTo(L_home_entrance)

    imagebutton:
        focus_mask True
        pos 172, 403
        idle game.timer.image('objects/object_door_36{}.png')
        hover HoverImage(game.timer.image('objects/object_door_36{}.png'))
        action MoveTo(L_home_garage)

    if M_anon.is_state(S_ano27_yumi, S_ano27_tony):
        imagebutton:
            focus_mask True
            pos 0, 470
            idle game.timer.image('objects/object_car_police_empty{}.png')
            hover HoverImage(game.timer.image('objects/object_car_police_empty{}.png'))
            action HideAll(), Jump('home_main_police_cruiser')

    elif L_home.is_here(M_yumi):
        imagebutton:
            focus_mask True
            pos 0, 470
            idle game.timer.image('objects/object_car_police{}.png')
            hover HoverImage(game.timer.image('objects/object_car_police{}.png'))
            action TalkTo(M_yumi)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

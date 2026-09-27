screen apt_lobby():
    add L_apt_lobby.background

    imagebutton:
        focus_mask True
        pos 456, 407
        idle game.timer.image('objects/object_elevator_02{}.png')
        hover HoverImage(game.timer.image('objects/object_elevator_02{}.png'))
        action MoveTo(L_apt_lift)

    imagebutton:
        focus_mask True
        pos 731, 359
        idle game.timer.image('objects/object_door_176{}.png')
        hover HoverImage(game.timer.image('objects/object_door_176{}.png'))
        action MoveTo(L_apt_hall1)

    imagebutton:
        focus_mask True
        pos 17, 342
        idle game.timer.image('objects/object_mailbox_apartment{}.png')
        hover HoverImage(game.timer.image('objects/object_mailbox_apartment{}.png'))
        action HideAll(), Jump('apt_lobby_mailboxes')

    if L_apt_lobby.is_here(M_sara):
        imagebutton:
            focus_mask True
            pos 951, 401
            idle game.timer.image('characters/sara/buttons/character_sara_01{}.png')
            hover HoverImage(game.timer.image('characters/sara/buttons/character_sara_01{}.png'))
            action TalkTo(M_sara)

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action MoveTo(L_apt)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

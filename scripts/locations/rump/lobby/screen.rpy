screen mayor_rumps_lobby():
    add L_rump_lobby.background

    imagebutton:
        focus_mask True
        pos 203, 49
        idle game.timer.image('objects/object_door_163{}.png')
        hover HoverImage(game.timer.image('objects/object_door_163{}.png'))
        action MoveTo(L_rump_master)

    imagebutton:
        focus_mask True
        pos 587, 179
        idle game.timer.image('objects/object_door_162{}.png')
        hover HoverImage(game.timer.image('objects/object_door_162{}.png'))
        action MoveTo(L_rump_second)

    imagebutton:
        focus_mask True
        pos 889, 342
        idle game.timer.image('objects/object_door_161{}.png')
        hover HoverImage(game.timer.image('objects/object_door_161{}.png'))
        action MoveTo(L_rump_kitchen)

    imagebutton:
        focus_mask True
        pos 360, 337
        idle game.timer.image('objects/object_door_164{}.png')
        hover HoverImage(game.timer.image('objects/object_door_164{}.png'))
        action MoveTo(L_rump_office)

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action MoveTo(L_rump_front)

    if L_rump_lobby.is_here(M_consuela):
        imagebutton:
            focus_mask True
            pos 540, 429
            idle game.timer.image('characters/consuela/buttons/character_consuela_rump_entrance{}.png')
            hover HoverImage(game.timer.image('characters/consuela/buttons/character_consuela_rump_entrance{}.png'))
            action TalkTo(M_consuela)

    if L_rump_lobby.is_here(M_thotbot):
        imagebutton:
            focus_mask True
            pos 580, 382
            idle game.timer.image('characters/thotbot/buttons/character_thotbot_rump{}.png')
            hover HoverImage(game.timer.image('characters/thotbot/buttons/character_thotbot_rump{}.png'))
            action TalkTo(M_thotbot)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

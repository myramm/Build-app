screen mayor_rumps_kitchen():
    add L_rump_kitchen.background

    imagebutton:
        focus_mask True
        pos 12, 240
        idle game.timer.image('objects/object_door_158{}.png')
        hover HoverImage(game.timer.image('objects/object_door_158{}.png'))
        action MoveTo(L_rump_lobby)

    imagebutton:
        focus_mask True
        pos 178, 502
        idle game.timer.image('objects/object_cabinet_05{}.png')
        hover HoverImage(game.timer.image('objects/object_cabinet_05{}.png'))
        action HideAll(), Jump('rump_kitchen_cabinet')

    imagebutton:
        focus_mask True
        pos 268, 355
        idle game.timer.image('objects/object_door_159{}.png')
        hover HoverImage(game.timer.image('objects/object_door_159{}.png'))
        action MoveTo(L_rump_back)

    if L_rump_kitchen.is_here(M_consuela):
        imagebutton:
            focus_mask True
            pos 451, 357
            idle game.timer.image('characters/consuela/buttons/character_consuela_rump_kitchen{}.png')
            hover HoverImage(game.timer.image('characters/consuela/buttons/character_consuela_rump_kitchen{}.png'))
            action TalkTo(M_consuela)

    if L_rump_kitchen.is_here(M_gamsay):
        imagebutton:
            focus_mask True
            pos 766, 322
            idle game.timer.image('characters/gamsay/buttons/character_gamsay_rump_kitchen{}.png')
            hover HoverImage(game.timer.image('characters/gamsay/buttons/character_gamsay_rump_kitchen{}.png'))
            action TalkTo(M_gamsay)


screen rump_kitchen_cabinet():
    sensitive renpy.get_mode() == 'screen'

    add 'location_rump_kitchen_cabinet_closeup'

    if not player.has_picked_up_item('maid_uniform'):
        imagebutton:
            focus_mask True
            pos 92, 26
            idle game.timer.image('objects/object_uniform_02.png')
            hover HoverImage(game.timer.image('objects/object_uniform_02.png'))
            action Return('uniform')

    if renpy.get_mode() == 'screen':
        imagebutton:
            focus_mask True
            align .5, .95
            idle 'boxes/auto_option_generic_01.png'
            hover HoverImage('boxes/auto_option_generic_01.png')
            action Return(True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

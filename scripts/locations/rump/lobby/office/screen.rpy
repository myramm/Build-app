screen mayor_rumps_office():
    add L_rump_office.background

    if M_anon.is_state(S_ano20_find, S_ano20_open):
        imagebutton:
            focus_mask True
            pos 683, 263
            idle game.timer.image('objects/object_shelf_04{}.png')
            hover HoverImage(game.timer.image('objects/object_shelf_04{}.png'))
            action HideAll(), Jump('rump_office_bookcase')

        imagebutton:
            focus_mask True
            pos 520, 195
            idle game.timer.image('objects/object_safe_02{}.png')
            hover HoverImage(game.timer.image('objects/object_safe_02{}.png'))
            action HideAll(), Jump('rump_office_safe')

        imagebutton:
            focus_mask True
            pos 157, 409
            idle game.timer.image('objects/object_documents{}.png')
            hover HoverImage(game.timer.image('objects/object_documents{}.png'))
            action HideAll(), Jump('rump_office_papers')

    imagebutton:
        focus_mask True
        pos 908, 114
        idle game.timer.image('objects/object_door_206{}.png')
        hover HoverImage(game.timer.image('objects/object_door_206{}.png'))
        action MoveTo(L_rump_lobby)


screen rump_office_bookcase():
    sensitive renpy.get_mode() == 'screen'

    add 'location_rump_office_shelf'

    imagebutton:
        focus_mask True
        pos 261, 307
        idle 'objects/object_bobblehead.png'
        hover HoverImage('objects/object_bobblehead.png')
        action HideAll(), Jump('rump_office_bobblehead')

    if renpy.get_mode() == 'screen':
        imagebutton:
            focus_mask True
            align .5, .95
            idle 'boxes/auto_option_generic_01.png'
            hover HoverImage('boxes/auto_option_generic_01.png')
            action Return()


screen rump_office_safe(seen):
    sensitive renpy.get_mode() == 'screen'

    default opts = (('cassette', (722, 274)),
                    ('folder', (319, 191)),
                    ('cash', (144, 414)),
                    ('recorder', (158, 176)),
                    ('passport', (527, 398)))

    add 'minigames/safe/safe_background.png'

    for item, pos in opts:
        imagebutton:
            focus_mask True
            pos pos
            if item in seen:
                idle 'objects/object_' + item + '.png'
                action NullAction()
            else:
                idle 'objects/object_' + item + '_stroke.png'
                hover HoverImage('objects/object_' + item + '_stroke.png')
                action AddToSet(seen, item), Return(item)

    add 'minigames/safe/safe_door_open.png'

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action Return('hint' if len(opts) > len(seen) else False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
